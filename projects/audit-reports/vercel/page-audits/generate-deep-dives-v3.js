#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const {
  AUDIT_DIR, slugify, loadManifest, loadOrganicJson, loadHistoryJson,
  parseClassifiedPages, mdTable, fmt, fmtPct, classifyTrend,
  dateToStr, getTrafficAtMonth, getPeakInfo, estimatedGain,
  classifyKeywordTheme,
} = require('./audit-utils');

const DEEP_DIVE_TYPES = ['Templates', 'Blog', 'AI Gateway', 'Knowledge Base', 'Fonts'];

function buildDeepDive(typeName, manifestPages, allClassifiedPages) {
  console.log(`  Building deep dive: ${typeName}...`);

  const typePages = manifestPages.filter(p => p.type === typeName);
  const allTypePages = allClassifiedPages.filter(p => p.type === typeName);
  const deadPages = allTypePages.filter(p => p.curTr === 0 && p.histTr === 0);
  const lostPages = allTypePages.filter(p => p.curTr === 0 && p.histTr > 0);

  const enriched = [];
  const allKeywords = [];
  const monthlyAgg = {};

  for (const page of typePages) {
    const slug = slugify(page.url);
    const history = loadHistoryJson(slug);
    const organic = loadOrganicJson(slug);
    const trend = classifyTrend(history);
    const { peak, peakDate } = getPeakInfo(history);
    const curTraffic = getTrafficAtMonth(history, 0);
    const sixMoTraffic = getTrafficAtMonth(history, 6);

    enriched.push({
      url: page.url,
      shortUrl: page.url.replace('https://vercel.com', ''),
      curKw: page.curKw,
      curTraffic,
      sixMoTraffic,
      peak,
      peakDate,
      trend,
    });

    if (organic) {
      for (const kw of organic) {
        allKeywords.push({
          keyword: kw.Keyword,
          url: page.url.replace('https://vercel.com', ''),
          position: kw.Position,
          volume: kw['Search Volume'] || 0,
          cpc: kw.CPC || 0,
          trafficPct: kw['Traffic (%)'] || 0,
        });
      }
    }

    if (history) {
      const sorted = [...history].sort((a, b) => a.Date - b.Date);
      for (const h of sorted) {
        const d = dateToStr(h.Date);
        if (!monthlyAgg[d]) monthlyAgg[d] = { pages: 0, kw: 0, traffic: 0 };
        const tr = h['Organic Traffic'] || 0;
        const kw = h['Organic Keywords'] || 0;
        if (tr > 0 || kw > 0) monthlyAgg[d].pages++;
        monthlyAgg[d].kw += kw;
        monthlyAgg[d].traffic += tr;
      }
    }
  }

  const totalCurTraffic = enriched.reduce((s, p) => s + p.curTraffic, 0);
  const totalSixMoTraffic = enriched.reduce((s, p) => s + p.sixMoTraffic, 0);
  const perPage = enriched.length > 0 ? Math.round(totalCurTraffic / enriched.length) : 0;

  // --- Section 1: Overview ---
  const sec1 = [
    '## 1. Section overview',
    '',
    mdTable(
      ['Metric', 'Value'],
      [
        ['Total indexed pages', fmt(allTypePages.length)],
        ['Pages with traffic', fmt(typePages.length)],
        ['Dead pages (never had traffic)', fmt(deadPages.length)],
        ['Lost pages (had traffic, now zero)', fmt(lostPages.length)],
        ['Current traffic', fmt(totalCurTraffic) + '/mo'],
        ['6mo change', fmtPct(totalCurTraffic, totalSixMoTraffic)],
        ['Traffic per page', fmt(perPage)],
        ['Total keywords tracked', fmt(allKeywords.length)],
      ]
    ),
  ].join('\n');

  // --- Section 2: Monthly Traffic Trend ---
  const months = Object.keys(monthlyAgg).sort();
  const recentMonths = months.slice(-15);
  const trendRows = recentMonths.map(m => [
    m,
    fmt(monthlyAgg[m].pages),
    fmt(monthlyAgg[m].kw),
    fmt(monthlyAgg[m].traffic),
  ]);

  const sec2 = [
    '## 2. Traffic trend (section-level)',
    '',
    mdTable(
      ['Month', 'Pages Ranking', 'Total Keywords', 'Total Traffic'],
      trendRows
    ),
  ].join('\n');

  // --- Section 3: Top 25 Pages ---
  const top25 = [...enriched].sort((a, b) => b.curTraffic - a.curTraffic).slice(0, 25);
  const sec3 = [
    '## 3. Top 25 pages',
    '',
    mdTable(
      ['URL', 'Keywords', 'Traffic', '6mo Traffic', 'Peak', 'Peak Month', 'Trend'],
      top25.map(p => [
        p.shortUrl, fmt(p.curKw), fmt(p.curTraffic), fmt(p.sixMoTraffic),
        fmt(p.peak), p.peakDate, p.trend,
      ])
    ),
  ].join('\n');

  // --- Section 4: Top Keywords ---
  const kwMap = {};
  for (const kw of allKeywords) {
    const key = kw.keyword.toLowerCase();
    if (!kwMap[key] || kw.position < kwMap[key].position) {
      kwMap[key] = { ...kw, keyword: kw.keyword };
    }
  }
  const topKw = Object.values(kwMap)
    .sort((a, b) => b.trafficPct - a.trafficPct)
    .slice(0, 30);

  const sec4 = [
    '## 4. Top keywords driving traffic',
    '',
    mdTable(
      ['Keyword', 'Best URL', 'Pos', 'Search Vol', 'CPC', 'Traffic %'],
      topKw.map(k => [
        k.keyword, k.url, String(k.position), fmt(k.volume),
        '$' + k.cpc.toFixed(2), k.trafficPct.toFixed(2) + '%',
      ])
    ),
  ].join('\n');

  // --- Section 5: Position Opportunities ---
  const opportunities = allKeywords
    .filter(k => k.position >= 4 && k.position <= 20 && k.volume >= 100)
    .sort((a, b) => b.volume - a.volume);
  const dedupedOpps = [];
  const seenKw = new Set();
  for (const o of opportunities) {
    if (!seenKw.has(o.keyword.toLowerCase())) {
      seenKw.add(o.keyword.toLowerCase());
      dedupedOpps.push(o);
    }
    if (dedupedOpps.length >= 20) break;
  }

  const sec5 = [
    '## 5. Position opportunities (pos 4-20, volume >= 100)',
    '',
    `${opportunities.length} keyword-URL pairs qualify. Top 20 by search volume:`,
    '',
    mdTable(
      ['Keyword', 'URL', 'Pos', 'Search Vol', 'CPC', 'Est. Gain (top 3)'],
      dedupedOpps.map(k => [
        k.keyword, k.url, String(k.position), fmt(k.volume),
        '$' + k.cpc.toFixed(2), '+' + fmt(estimatedGain(k.position, k.volume)) + '/mo',
      ])
    ),
  ].join('\n');

  // --- Section 6: Dead Pages ---
  const deadList = [...lostPages].sort((a, b) => b.histTr - a.histTr);
  const deadDisplay = deadList.length <= 50 ? deadList : deadList.slice(0, 20);
  const sec6Lines = [
    '## 6. Dead and lost pages',
    '',
    `**${fmt(deadPages.length)}** pages have never had traffic. **${fmt(lostPages.length)}** pages had traffic historically but now have zero.`,
  ];
  if (lostPages.length > 0) {
    sec6Lines.push('');
    sec6Lines.push(lostPages.length > 50
      ? `Top ${deadDisplay.length} lost pages by historical traffic:`
      : 'Lost pages (had traffic, now zero):');
    sec6Lines.push('');
    sec6Lines.push(mdTable(
      ['URL', 'Hist Keywords', 'Hist Traffic'],
      deadDisplay.map(p => [p.url, fmt(p.histKw), fmt(p.histTr)])
    ));
  }
  const sec6 = sec6Lines.join('\n');

  // --- Section 7: Keyword Theme Clusters ---
  const themes = {};
  for (const kw of allKeywords) {
    const theme = classifyKeywordTheme(kw.keyword);
    if (!themes[theme]) themes[theme] = { keywords: 0, pages: new Set(), traffic: 0, positions: [] };
    themes[theme].keywords++;
    themes[theme].pages.add(kw.url);
    themes[theme].traffic += kw.trafficPct;
    themes[theme].positions.push(kw.position);
  }

  const themeRows = Object.entries(themes)
    .sort((a, b) => b[1].keywords - a[1].keywords)
    .filter(([, d]) => d.keywords >= 3)
    .map(([name, d]) => {
      const avgPos = (d.positions.reduce((s, p) => s + p, 0) / d.positions.length).toFixed(1);
      return [name, fmt(d.keywords), String(d.pages.size), d.traffic.toFixed(1) + '%', avgPos];
    });

  const sec7 = [
    '## 7. Keyword theme clusters',
    '',
    mdTable(
      ['Theme', 'Keywords', 'Pages', 'Traffic Share', 'Avg Position'],
      themeRows
    ),
  ].join('\n');

  // --- Assemble ---
  const fileSlug = typeName.toLowerCase().replace(/\s+/g, '-');
  const output = [
    `# Deep Dive: ${typeName} — vercel.com (v3)`,
    '',
    `**Date:** ${new Date().toISOString().slice(0, 10)}`,
    `**Source:** SEMRush \`url_organic\` + \`url_rank_history\` (US database)`,
    `**Scope:** ${fmt(allTypePages.length)} total ${typeName} pages, ${fmt(typePages.length)} with traffic, ${fmt(allKeywords.length)} keyword-URL pairs`,
    '',
    '---',
    '',
    sec1, '', '---', '',
    sec2, '', '---', '',
    sec3, '', '---', '',
    sec4, '', '---', '',
    sec5, '', '---', '',
    sec6, '', '---', '',
    sec7, '',
    '---',
    '',
    `*Data provenance: SEMRush US database. Keyword data from \`url_organic\` (display_limit=2000). Traffic history from \`url_rank_history\` (up to 170 monthly snapshots). Page classification from \`domain_organic_unique\` with v3 type rules.*`,
  ].join('\n');

  const outPath = path.join(AUDIT_DIR, `deep-dive-${fileSlug}-v3.md`);
  fs.writeFileSync(outPath, output);
  console.log(`    Written: ${outPath}`);
  return outPath;
}

function main() {
  console.log('Generating deep dive reports...');

  const manifest = loadManifest();
  const allClassified = parseClassifiedPages();

  for (const typeName of DEEP_DIVE_TYPES) {
    buildDeepDive(typeName, manifest, allClassified);
  }

  console.log('Done! Generated 5 deep dive reports.');
}

main();
