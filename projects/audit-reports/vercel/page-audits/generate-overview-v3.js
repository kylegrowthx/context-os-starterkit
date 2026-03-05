#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const {
  AUDIT_DIR, slugify, loadManifest, loadOrganicJson,
  parseClassifiedSummary, parseClassifiedPages,
  mdTable, fmt, fmtPct, estimatedGain,
} = require('./audit-utils');

function main() {
  console.log('Generating seo-overview-v3.md...');

  const manifest = loadManifest();
  const summary = parseClassifiedSummary();
  const totals = summary.find(r => r.type === 'Total');
  const types = summary.filter(r => r.type !== 'Total');

  // --- Section 1: Core Metrics ---
  const domainRaw = fs.readFileSync(path.join(AUDIT_DIR, 'raw-domain-overview.md'), 'utf8');
  const histRaw = fs.readFileSync(path.join(AUDIT_DIR, 'raw-domain-history.md'), 'utf8');

  const contentTypes = types.filter(t => t.content === 'Yes');
  const contentTraffic = contentTypes.reduce((s, t) => s + t.curTr, 0);
  const contentPages = contentTypes.reduce((s, t) => s + t.total, 0);
  const contentWithTraffic = contentTypes.reduce((s, t) => s + t.withTraffic, 0);
  const contentTrafficShare = ((contentTraffic / totals.curTr) * 100).toFixed(1);

  const sec1 = [
    '## 1. Core metrics snapshot',
    '',
    '| Metric | Value |',
    '| --- | --- |',
    `| SEMRush Rank | ${fmt(13550)} |`,
    `| Organic Keywords | ${fmt(76267)} |`,
    `| Organic Traffic | ${fmt(168294)} /mo |`,
    `| Organic Traffic Value | $${fmt(677038)} /mo |`,
    `| Total Indexed Pages | ${fmt(totals.total)} |`,
    `| Pages with Traffic | ${fmt(totals.withTraffic)} (${((totals.withTraffic / totals.total) * 100).toFixed(1)}%) |`,
    `| Content Pages (total) | ${fmt(contentPages)} |`,
    `| Content Pages with Traffic | ${fmt(contentWithTraffic)} |`,
    `| Content Traffic Share | ${contentTrafficShare}% of domain total |`,
    '',
    `Traffic up 32.4% over 6 months (${fmt(127079)} to ${fmt(168294)}) with essentially flat keywords (+0.7%). Content pages (${contentTrafficShare}% of traffic) span ${fmt(contentPages)} pages across ${contentTypes.length} content types. The remaining traffic is driven by brand pages, docs, and transactional pages.`,
  ].join('\n');

  // --- Section 2: 15-Month Domain Trend ---
  const histLines = histRaw.split('\n');
  const histTableStart = histLines.findIndex(l => l.startsWith('| Date |'));
  const histTableEnd = histLines.findIndex((l, i) => i > histTableStart + 1 && !l.startsWith('|'));
  const histTable = histLines.slice(histTableStart, histTableEnd > 0 ? histTableEnd : undefined).join('\n');

  const sec2 = [
    '## 2. 15-month domain trend',
    '',
    histTable,
    '',
    'Consistent upward trajectory since Feb 2025. Traffic up 83% year-over-year. Keyword count fluctuated between 47K and 79K but traffic grew steadily, indicating position improvements on high-value terms rather than tail keyword growth.',
  ].join('\n');

  // --- Section 3: Content Type Breakdown ---
  const typeRows = types.map(t => {
    const sixMo = fmtPct(t.curTr, t.histTr);
    const perPage = t.withTraffic > 0 ? fmt(Math.round(t.curTr / t.withTraffic)) : '—';
    return [
      t.content === 'Yes' ? `**${t.type}**` : t.type,
      t.content,
      fmt(t.total),
      fmt(t.withTraffic),
      fmt(t.curTr),
      fmt(t.histTr),
      sixMo,
      perPage,
    ];
  });

  const sec3 = [
    '## 3. Content type breakdown',
    '',
    mdTable(
      ['Type', 'Content', 'Pages', 'With Traffic', 'Cur Traffic', 'Hist Traffic', '6mo Change', 'Traffic/Page'],
      typeRows
    ),
    '',
    `Brand pages (${fmt(types.find(t => t.type === 'Brand').curTr)} traffic) dominate due to homepage concentration. Among content types, Templates leads with ${fmt(contentTypes[0]?.curTr)} traffic across ${fmt(contentTypes[0]?.withTraffic)} pages, followed by Blog (${fmt(types.find(t => t.type === 'Blog').curTr)}). AI Gateway is the fastest-growing section (${fmtPct(types.find(t => t.type === 'AI Gateway').curTr, types.find(t => t.type === 'AI Gateway').histTr)}).`,
  ].join('\n');

  // --- Section 4: Content vs. Non-Content ---
  const nonContentTraffic = totals.curTr - contentTraffic;
  const nonContentPages = totals.total - contentPages;
  const nonContentWithTraffic = totals.withTraffic - contentWithTraffic;

  const sec4 = [
    '## 4. Content vs. non-content split',
    '',
    mdTable(
      ['Segment', 'Pages', 'With Traffic', 'Traffic', 'Traffic/Page', '% of Domain'],
      [
        ['Content', fmt(contentPages), fmt(contentWithTraffic), fmt(contentTraffic),
          contentWithTraffic > 0 ? fmt(Math.round(contentTraffic / contentWithTraffic)) : '—',
          contentTrafficShare + '%'],
        ['Non-Content', fmt(nonContentPages), fmt(nonContentWithTraffic), fmt(nonContentTraffic),
          nonContentWithTraffic > 0 ? fmt(Math.round(nonContentTraffic / nonContentWithTraffic)) : '—',
          ((nonContentTraffic / totals.curTr) * 100).toFixed(1) + '%'],
        ['**Total**', `**${fmt(totals.total)}**`, `**${fmt(totals.withTraffic)}**`, `**${fmt(totals.curTr)}**`, '', '100%'],
      ]
    ),
    '',
    `Content pages represent ${contentTrafficShare}% of organic traffic despite being ${((contentPages / totals.total) * 100).toFixed(1)}% of indexed pages. Non-content pages (primarily brand, docs, and transactional) generate ${((nonContentTraffic / totals.curTr) * 100).toFixed(1)}% of traffic — heavily concentrated in the homepage.`,
  ].join('\n');

  // --- Section 5: Index Efficiency ---
  const effRows = types.map(t => {
    const zeroRate = t.total > 0 ? ((1 - t.withTraffic / t.total) * 100).toFixed(1) + '%' : '—';
    return [t.type, fmt(t.total), fmt(t.withTraffic), zeroRate];
  });

  const sec5 = [
    '## 5. Index efficiency',
    '',
    mdTable(['Type', 'Indexed Pages', 'With Traffic', 'Zero-Traffic Rate'], effRows),
    '',
    `Overall index efficiency: ${((totals.withTraffic / totals.total) * 100).toFixed(1)}% of pages generate traffic. Community (${types.find(t => t.type === 'Community')?.total || 0} pages, ${((1 - (types.find(t => t.type === 'Community')?.withTraffic || 0) / (types.find(t => t.type === 'Community')?.total || 1)) * 100).toFixed(1)}% dead) is the largest bloat contributor.`,
  ].join('\n');

  // --- Section 6: Keyword Position Distribution ---
  console.log('  Loading url-organic JSONs for position distribution...');
  const posBuckets = { '1': { count: 0, vol: 0 }, '2-3': { count: 0, vol: 0 }, '4-10': { count: 0, vol: 0 }, '11-20': { count: 0, vol: 0 }, '21-50': { count: 0, vol: 0 }, '51-100': { count: 0, vol: 0 } };
  let totalKw = 0;

  for (const page of manifest) {
    const slug = slugify(page.url);
    const data = loadOrganicJson(slug);
    if (!data) continue;
    for (const kw of data) {
      const pos = kw.Position;
      const vol = kw['Search Volume'] || 0;
      totalKw++;
      if (pos === 1) { posBuckets['1'].count++; posBuckets['1'].vol += vol; }
      else if (pos <= 3) { posBuckets['2-3'].count++; posBuckets['2-3'].vol += vol; }
      else if (pos <= 10) { posBuckets['4-10'].count++; posBuckets['4-10'].vol += vol; }
      else if (pos <= 20) { posBuckets['11-20'].count++; posBuckets['11-20'].vol += vol; }
      else if (pos <= 50) { posBuckets['21-50'].count++; posBuckets['21-50'].vol += vol; }
      else { posBuckets['51-100'].count++; posBuckets['51-100'].vol += vol; }
    }
  }

  const posRows = Object.entries(posBuckets).map(([bucket, d]) => [
    'Position ' + bucket,
    fmt(d.count),
    totalKw > 0 ? ((d.count / totalKw) * 100).toFixed(1) + '%' : '—',
    fmt(d.vol),
  ]);
  posRows.push(['**Total**', `**${fmt(totalKw)}**`, '**100%**', `**${fmt(Object.values(posBuckets).reduce((s, d) => s + d.vol, 0))}**`]);

  const sec6 = [
    '## 6. Keyword position distribution (content pages)',
    '',
    mdTable(['Position Bucket', 'Keywords', '% of Total', 'Total Search Volume'], posRows),
    '',
    `Across ${fmt(totalKw)} keyword-URL pairs on content pages, ${((posBuckets['1'].count + posBuckets['2-3'].count + posBuckets['4-10'].count) / totalKw * 100).toFixed(1)}% sit in the top 10. The remaining ${((1 - (posBuckets['1'].count + posBuckets['2-3'].count + posBuckets['4-10'].count) / totalKw) * 100).toFixed(1)}% (positions 11+) represent untapped inventory with ${fmt(posBuckets['11-20'].vol + posBuckets['21-50'].vol + posBuckets['51-100'].vol)} combined monthly search volume.`,
  ].join('\n');

  // --- Section 7: Quick Wins ---
  console.log('  Finding quick-win keywords...');
  const quickWins = [];
  for (const page of manifest) {
    const slug = slugify(page.url);
    const data = loadOrganicJson(slug);
    if (!data) continue;
    for (const kw of data) {
      if (kw.Position >= 4 && kw.Position <= 20 && (kw['Search Volume'] || 0) >= 100) {
        quickWins.push({
          keyword: kw.Keyword,
          url: page.url.replace('https://vercel.com', ''),
          position: kw.Position,
          volume: kw['Search Volume'],
          cpc: kw.CPC || 0,
          gain: estimatedGain(kw.Position, kw['Search Volume']),
        });
      }
    }
  }
  quickWins.sort((a, b) => b.volume - a.volume);
  const top20 = quickWins.slice(0, 20);

  const sec7 = [
    '## 7. Quick wins — top keywords by volume (position 4-20)',
    '',
    `${fmt(quickWins.length)} keywords on content pages rank position 4-20 with search volume >= 100. Moving these to top 3 would capture significant incremental traffic.`,
    '',
    mdTable(
      ['Keyword', 'URL', 'Pos', 'Search Vol', 'CPC', 'Est. Gain (top 3)'],
      top20.map(w => [
        w.keyword, w.url, String(w.position), fmt(w.volume),
        '$' + w.cpc.toFixed(2), '+' + fmt(w.gain) + '/mo',
      ])
    ),
  ].join('\n');

  // --- Section 8: Raw Data Index ---
  const sec8 = [
    '## 8. Raw data files',
    '',
    '| File | Contents |',
    '| --- | --- |',
    '| `raw-domain-overview.md` | SEMRush `domain_rank` snapshot (Feb 2026) |',
    '| `raw-domain-history.md` | SEMRush `domain_rank_history` — 15 monthly snapshots |',
    '| `raw-pages-current.md` | `domain_organic_unique` — all pages, Feb 2026 |',
    '| `raw-pages-historical.md` | `domain_organic_unique` — all pages, Aug 2025 |',
    '| `classified-pages.md` | All 6,548 pages classified by type with traffic data |',
    '| `page-audits/url-organic/` | 523 JSON+CSV files — keywords per content page |',
    '| `page-audits/url-rank-history/` | 548 JSON+CSV files — 15-month traffic history per content page |',
  ].join('\n');

  // --- Assemble ---
  const output = [
    '# SEO Overview: vercel.com (v3)',
    '',
    `**Date:** ${new Date().toISOString().slice(0, 10)}`,
    '**Source:** SEMRush (US database) — `domain_rank`, `domain_organic_unique`, `url_organic`, `url_rank_history`',
    '**Domain:** vercel.com',
    `**Scope:** ${fmt(totals.total)} indexed pages, ${fmt(contentPages)} content pages, ${fmt(totalKw)} content keyword-URL pairs`,
    '',
    '---',
    '',
    sec1, '', '---', '',
    sec2, '', '---', '',
    sec3, '', '---', '',
    sec4, '', '---', '',
    sec5, '', '---', '',
    sec6, '', '---', '',
    sec7, '', '---', '',
    sec8, '',
    '---',
    '',
    `*Data provenance: SEMRush US database. Domain-level data from Feb 2026. Page-level data from \`domain_organic_unique\` (Feb 2026 + Aug 2025, ${fmt(totals.total)} pages). Keyword-level data from \`url_organic\` (${fmt(totalKw)} keyword-URL pairs across 523 content pages, display_limit=2000). Traffic history from \`url_rank_history\` (548 content pages, 15 monthly snapshots). v3 supersedes v2 which was based on \`domain_organic\` keyword-URL pair sampling.*`,
  ].join('\n');

  const outPath = path.join(AUDIT_DIR, 'seo-overview-v3.md');
  fs.writeFileSync(outPath, output);
  console.log(`  Written: ${outPath}`);
  console.log(`  Total keywords processed: ${fmt(totalKw)}`);
  console.log('Done!');
}

main();
