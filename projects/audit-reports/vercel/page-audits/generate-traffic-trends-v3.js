#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const {
  AUDIT_DIR, slugify, loadManifest, loadHistoryJson,
  mdTable, fmt, fmtPct, classifyTrend, dateToStr,
  getTrafficAtMonth, getPeakInfo,
} = require('./audit-utils');

function main() {
  console.log('Generating content-traffic-trends-v3.md...');

  const manifest = loadManifest();

  // Load history data and classify each page
  const pages = [];
  for (const page of manifest) {
    const slug = slugify(page.url);
    const history = loadHistoryJson(slug);
    const trend = classifyTrend(history);
    const { peak, peakDate } = getPeakInfo(history);
    const curTraffic = getTrafficAtMonth(history, 0);
    const sixMoTraffic = getTrafficAtMonth(history, 6);
    const twelveMoTraffic = getTrafficAtMonth(history, 12);

    let monthsToFirstTraffic = null;
    let monthsFromFirstToPeak = null;
    if (history && history.length > 0) {
      const sorted = [...history].sort((a, b) => a.Date - b.Date);
      const firstIdx = sorted.findIndex(h => (h['Organic Traffic'] || 0) > 0);
      const peakIdx = sorted.findIndex(h => (h['Organic Traffic'] || 0) === peak);
      if (firstIdx >= 0 && peakIdx >= 0) {
        monthsFromFirstToPeak = peakIdx - firstIdx;
      }
    }

    pages.push({
      url: page.url,
      shortUrl: page.url.replace('https://vercel.com', ''),
      type: page.type,
      curKw: page.curKw,
      curTraffic,
      sixMoTraffic,
      twelveMoTraffic,
      peak,
      peakDate,
      trend,
      monthsFromFirstToPeak,
      historyLen: history ? history.length : 0,
    });
  }

  // --- Section 1: Summary Table ---
  const CONTENT_TYPES = [...new Set(manifest.map(p => p.type))].sort();
  const trendCategories = ['Accelerating', 'Growing', 'Stable', 'Peaked', 'Declining', 'New', 'Dead'];

  const summaryRows = CONTENT_TYPES.map(type => {
    const typePages = pages.filter(p => p.type === type);
    const counts = {};
    for (const cat of trendCategories) counts[cat] = typePages.filter(p => p.trend === cat).length;
    const totalTraffic = typePages.reduce((s, p) => s + p.curTraffic, 0);
    const totalHistTraffic = typePages.reduce((s, p) => s + p.sixMoTraffic, 0);
    return [
      type,
      String(typePages.length),
      String(counts.Accelerating + counts.Growing),
      String(counts.Stable),
      String(counts.Peaked + counts.Declining),
      String(counts.Dead + counts.New),
      fmt(totalTraffic),
      fmtPct(totalTraffic, totalHistTraffic),
    ];
  });

  const allGrowing = pages.filter(p => p.trend === 'Accelerating' || p.trend === 'Growing').length;
  const allStable = pages.filter(p => p.trend === 'Stable').length;
  const allDeclining = pages.filter(p => p.trend === 'Peaked' || p.trend === 'Declining').length;
  const allDead = pages.filter(p => p.trend === 'Dead' || p.trend === 'New').length;
  const totalCurTraffic = pages.reduce((s, p) => s + p.curTraffic, 0);
  const totalSixMoTraffic = pages.reduce((s, p) => s + p.sixMoTraffic, 0);

  summaryRows.push([
    '**Total**',
    `**${pages.length}**`,
    `**${allGrowing}**`,
    `**${allStable}**`,
    `**${allDeclining}**`,
    `**${allDead}**`,
    `**${fmt(totalCurTraffic)}**`,
    `**${fmtPct(totalCurTraffic, totalSixMoTraffic)}**`,
  ]);

  const sec1 = [
    '## 1. Summary by content type',
    '',
    mdTable(
      ['Type', 'Pages', 'Growing', 'Stable', 'Declining', 'Dead/New', 'Traffic', '6mo Change'],
      summaryRows
    ),
    '',
    `Of ${pages.length} content pages with traffic, ${allGrowing} are growing (accelerating or trending up), ${allStable} are stable, ${allDeclining} are declining or peaked, and ${allDead} are dead or too new to classify.`,
  ].join('\n');

  // --- Section 2: Trajectory Classification ---
  const trendCounts = {};
  for (const cat of trendCategories) {
    const cp = pages.filter(p => p.trend === cat);
    trendCounts[cat] = {
      count: cp.length,
      traffic: cp.reduce((s, p) => s + p.curTraffic, 0),
    };
  }

  const trendRows = trendCategories.map(cat => [
    `**${cat}**`,
    String(trendCounts[cat].count),
    fmt(trendCounts[cat].traffic),
    pages.length > 0 ? ((trendCounts[cat].count / pages.length) * 100).toFixed(1) + '%' : '—',
  ]);

  const sec2 = [
    '## 2. Trajectory classification',
    '',
    '| Trend | Definition |',
    '| --- | --- |',
    '| **Accelerating** | Traffic increasing AND rate of increase is growing (6mo > +50%, 3mo > +20%) |',
    '| **Growing** | Consistent upward trend (6mo > +20%) |',
    '| **Stable** | Traffic within +/-20% over last 6 months |',
    '| **Peaked** | Hit a historical maximum, now below 50% of peak |',
    '| **Declining** | Consistent downward trend (6mo < -20%) |',
    '| **New** | First appeared with traffic in the last 3 months |',
    '| **Dead** | Zero or near-zero traffic throughout history |',
    '',
    mdTable(
      ['Trend', 'Pages', 'Current Traffic', '% of Pages'],
      trendRows
    ),
    '',
    `Accelerating (${trendCounts.Accelerating.count}) and Growing (${trendCounts.Growing.count}) pages account for ${fmt(trendCounts.Accelerating.traffic + trendCounts.Growing.traffic)} monthly traffic. Declining (${trendCounts.Declining.count}) and Peaked (${trendCounts.Peaked.count}) pages hold ${fmt(trendCounts.Declining.traffic + trendCounts.Peaked.traffic)} traffic at risk.`,
  ].join('\n');

  // --- Section 3: Top Movers — Gainers ---
  const gainers = pages
    .map(p => ({ ...p, gain: p.curTraffic - p.sixMoTraffic }))
    .filter(p => p.gain > 0)
    .sort((a, b) => b.gain - a.gain)
    .slice(0, 20);

  const sec3 = [
    '## 3. Top movers — biggest gainers',
    '',
    mdTable(
      ['URL', 'Type', 'Traffic Now', '6mo Ago', 'Gain', 'Peak', 'Peak Month'],
      gainers.map(p => [
        p.shortUrl, p.type, fmt(p.curTraffic), fmt(p.sixMoTraffic),
        '+' + fmt(p.gain), fmt(p.peak), p.peakDate,
      ])
    ),
  ].join('\n');

  // --- Section 4: Top Movers — Losers ---
  const losers = pages
    .map(p => ({ ...p, loss: p.sixMoTraffic - p.curTraffic }))
    .filter(p => p.loss > 0)
    .sort((a, b) => b.loss - a.loss)
    .slice(0, 20);

  const sec4 = [
    '## 4. Top movers — biggest losers',
    '',
    mdTable(
      ['URL', 'Type', 'Traffic Now', '6mo Ago', 'Loss', 'Peak', 'Peak Month'],
      losers.map(p => [
        p.shortUrl, p.type, fmt(p.curTraffic), fmt(p.sixMoTraffic),
        '-' + fmt(p.loss), fmt(p.peak), p.peakDate,
      ])
    ),
  ].join('\n');

  // --- Section 5: Content Lifecycle Analysis ---
  const lifecycleByType = {};
  for (const page of pages) {
    if (!lifecycleByType[page.type]) {
      lifecycleByType[page.type] = { peaks: [], peakMonths: [], currents: [] };
    }
    lifecycleByType[page.type].peaks.push(page.peak);
    if (page.monthsFromFirstToPeak != null && page.monthsFromFirstToPeak > 0) {
      lifecycleByType[page.type].peakMonths.push(page.monthsFromFirstToPeak);
    }
    lifecycleByType[page.type].currents.push(page.curTraffic);
  }

  const avg = arr => arr.length > 0 ? arr.reduce((s, v) => s + v, 0) / arr.length : 0;

  const lcRows = Object.entries(lifecycleByType).map(([type, data]) => {
    const avgPeak = avg(data.peaks);
    const avgCurrent = avg(data.currents);
    const avgMonths = data.peakMonths.length > 0 ? avg(data.peakMonths).toFixed(1) : '—';
    const decayRate = avgPeak > 0 ? ((1 - avgCurrent / avgPeak) * 100).toFixed(1) + '%' : '—';
    return [
      type,
      String(data.peaks.length),
      avgMonths,
      fmt(Math.round(avgPeak)),
      fmt(Math.round(avgCurrent)),
      decayRate,
    ];
  });

  const sec5 = [
    '## 5. Content lifecycle analysis',
    '',
    'For pages with a clear trajectory from first traffic to peak, how quickly do different content types mature and decay?',
    '',
    mdTable(
      ['Type', 'Pages', 'Avg Months to Peak', 'Avg Peak Traffic', 'Avg Current Traffic', 'Decay from Peak'],
      lcRows
    ),
  ].join('\n');

  // --- Section 6: Page-by-Page Full Table ---
  const sortedPages = [...pages].sort((a, b) => b.curTraffic - a.curTraffic);

  const fullRows = sortedPages.map(p => [
    p.shortUrl,
    p.type,
    fmt(p.curKw),
    fmt(p.curTraffic),
    fmt(p.sixMoTraffic),
    fmt(p.twelveMoTraffic),
    fmt(p.peak),
    p.peakDate,
    p.trend,
  ]);

  const sec6 = [
    '## 6. Page-by-page data (all content pages with traffic)',
    '',
    `${pages.length} pages sorted by current traffic.`,
    '',
    mdTable(
      ['URL', 'Type', 'Cur KW', 'Cur Traffic', '6mo Traffic', '12mo Traffic', 'Peak', 'Peak Month', 'Trend'],
      fullRows
    ),
  ].join('\n');

  // --- Assemble ---
  const output = [
    '# Content Traffic Trends — vercel.com (v3)',
    '',
    `**Date:** ${new Date().toISOString().slice(0, 10)}`,
    '**Source:** SEMRush `url_rank_history` (US database) — 15 monthly snapshots per page',
    `**Scope:** ${pages.length} content pages with traffic (current or historical)`,
    '',
    '---',
    '',
    sec1, '', '---', '',
    sec2, '', '---', '',
    sec3, '', '---', '',
    sec4, '', '---', '',
    sec5, '', '---', '',
    sec6, '',
    '---',
    '',
    `*Data provenance: SEMRush US database. \`url_rank_history\` pulled for ${pages.length} content pages with traffic. Each file contains up to 170 monthly snapshots. Trend classification uses the most recent 6-month window. v3 uses per-page time series data; v2 used only two-point comparison (current vs. Aug 2025).*`,
  ].join('\n');

  const outPath = path.join(AUDIT_DIR, 'content-traffic-trends-v3.md');
  fs.writeFileSync(outPath, output);
  console.log(`  Written: ${outPath} (${sortedPages.length} pages)`);
  console.log('Done!');
}

main();
