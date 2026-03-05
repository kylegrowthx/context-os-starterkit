const fs = require('fs');
const path = require('path');

const PAGE_AUDITS_DIR = __dirname;
const AUDIT_DIR = path.resolve(PAGE_AUDITS_DIR, '..');
const ORGANIC_DIR = path.join(PAGE_AUDITS_DIR, 'url-organic');
const HISTORY_DIR = path.join(PAGE_AUDITS_DIR, 'url-rank-history');
const MANIFEST_PATH = path.join(
  '/Users/marcelsantilli_mac2/.cursor/projects',
  'Users-marcelsantilli-mac2-Dropbox-GrowthX-AI-Projects-growthx-handbook',
  'agent-tools',
  'content-with-traffic.json'
);
const CLASSIFIED_PATH = path.join(AUDIT_DIR, 'classified-pages.md');

function slugify(url) {
  return url
    .replace('https://vercel.com/', '')
    .replace(/\//g, '__')
    .replace(/[^a-zA-Z0-9._-]/g, '_') || 'homepage';
}

function loadManifest() {
  return JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf8'));
}

function loadOrganicJson(slug) {
  const p = path.join(ORGANIC_DIR, `${slug}.json`);
  if (!fs.existsSync(p)) return null;
  try { return JSON.parse(fs.readFileSync(p, 'utf8')); }
  catch { return null; }
}

function loadHistoryJson(slug) {
  const p = path.join(HISTORY_DIR, `${slug}.json`);
  if (!fs.existsSync(p)) return null;
  try { return JSON.parse(fs.readFileSync(p, 'utf8')); }
  catch { return null; }
}

function parseClassifiedSummary() {
  const content = fs.readFileSync(CLASSIFIED_PATH, 'utf8');
  const lines = content.split('\n');
  const rows = [];
  let inTable = false;
  for (const line of lines) {
    if (line.includes('| Type |') && line.includes('| Content |')) {
      inTable = true;
      continue;
    }
    if (inTable && line.startsWith('|---')) continue;
    if (inTable && line.startsWith('|')) {
      const cols = line.split('|').slice(1, -1).map(c => c.trim());
      if (cols[0].startsWith('**Total**')) {
        rows.push({
          type: 'Total',
          content: '—',
          total: parseInt(cols[2].replace(/[*,]/g, '')) || 0,
          withTraffic: parseInt(cols[3].replace(/[*,]/g, '')) || 0,
          curTr: parseInt(cols[4].replace(/[*,]/g, '')) || 0,
          histTr: parseInt(cols[5].replace(/[*,]/g, '')) || 0,
        });
        break;
      }
      rows.push({
        type: cols[0],
        content: cols[1],
        total: parseInt(cols[2].replace(/,/g, '')) || 0,
        withTraffic: parseInt(cols[3].replace(/,/g, '')) || 0,
        curTr: parseInt(cols[4].replace(/,/g, '')) || 0,
        histTr: parseInt(cols[5].replace(/,/g, '')) || 0,
      });
    } else if (inTable && !line.startsWith('|')) {
      break;
    }
  }
  return rows;
}

function parseClassifiedPages() {
  const content = fs.readFileSync(CLASSIFIED_PATH, 'utf8');
  const lines = content.split('\n');
  const pages = [];
  let inTable = false;
  for (const line of lines) {
    if (line.startsWith('| URL |')) {
      inTable = true;
      continue;
    }
    if (inTable && line.startsWith('|---')) continue;
    if (inTable && line.startsWith('|')) {
      const cols = line.split('|').slice(1, -1).map(c => c.trim());
      if (cols.length >= 7) {
        pages.push({
          url: cols[0],
          type: cols[1],
          content: cols[2],
          curKw: parseInt(cols[3].replace(/,/g, '')) || 0,
          curTr: parseInt(cols[4].replace(/,/g, '')) || 0,
          histKw: parseInt(cols[5].replace(/,/g, '')) || 0,
          histTr: parseInt(cols[6].replace(/,/g, '')) || 0,
        });
      }
    } else if (inTable && !line.startsWith('|')) {
      if (pages.length > 0) break;
    }
  }
  return pages;
}

function mdTable(headers, rows) {
  const lines = [
    '| ' + headers.join(' | ') + ' |',
    '| ' + headers.map(() => '---').join(' | ') + ' |',
    ...rows.map(r => '| ' + r.join(' | ') + ' |'),
  ];
  return lines.join('\n');
}

function fmt(n) {
  if (n == null || isNaN(n)) return '0';
  return Math.round(n).toLocaleString('en-US');
}

function fmtPct(cur, hist) {
  if (!hist || hist === 0) {
    if (cur > 0) return 'new';
    return '—';
  }
  const change = ((cur - hist) / hist) * 100;
  const sign = change >= 0 ? '+' : '';
  return `${sign}${change.toFixed(1)}%`;
}

function classifyTrend(history) {
  if (!history || history.length === 0) return 'Dead';

  const sorted = [...history].sort((a, b) => a.Date - b.Date);
  const traffic = sorted.map(h => h['Organic Traffic'] || 0);
  const len = traffic.length;
  const current = traffic[len - 1];
  const maxTraffic = Math.max(...traffic);
  const maxIdx = traffic.lastIndexOf(maxTraffic);

  if (current === 0 && maxTraffic < 10) return 'Dead';

  const sixMoAgo = traffic[Math.max(0, len - 7)] || 0;
  const threeMoAgo = traffic[Math.max(0, len - 4)] || 0;

  const firstNonZeroIdx = traffic.findIndex(t => t > 0);
  if (firstNonZeroIdx >= len - 3 && firstNonZeroIdx > 0) return 'New';

  const sixMoChange = sixMoAgo > 0
    ? (current - sixMoAgo) / sixMoAgo
    : (current > 0 ? 9.99 : 0);
  const threeMoChange = threeMoAgo > 0
    ? (current - threeMoAgo) / threeMoAgo
    : (current > 0 ? 9.99 : 0);

  if (sixMoChange > 0.5 && threeMoChange > 0.2) return 'Accelerating';
  if (sixMoChange > 0.2) return 'Growing';
  if (sixMoChange >= -0.2 && sixMoChange <= 0.2) return 'Stable';
  if (maxIdx > 1 && maxIdx < len - 2 && current < maxTraffic * 0.5) return 'Peaked';
  return 'Declining';
}

function dateToStr(dateInt) {
  const s = String(dateInt);
  return `${s.slice(0, 4)}-${s.slice(4, 6)}`;
}

function getTrafficAtMonth(history, monthsAgo) {
  if (!history || history.length === 0) return 0;
  const sorted = [...history].sort((a, b) => a.Date - b.Date);
  const idx = Math.max(0, sorted.length - 1 - monthsAgo);
  return sorted[idx] ? sorted[idx]['Organic Traffic'] || 0 : 0;
}

function getPeakInfo(history) {
  if (!history || history.length === 0) return { peak: 0, peakDate: '—' };
  const sorted = [...history].sort((a, b) => a.Date - b.Date);
  let peak = 0, peakDate = 0;
  for (const h of sorted) {
    const t = h['Organic Traffic'] || 0;
    if (t >= peak) { peak = t; peakDate = h.Date; }
  }
  return { peak, peakDate: peakDate ? dateToStr(peakDate) : '—' };
}

const CTR_BY_POS = {
  1: 0.28, 2: 0.15, 3: 0.11, 4: 0.08, 5: 0.07,
  6: 0.05, 7: 0.04, 8: 0.03, 9: 0.025, 10: 0.02,
};
function estimatedGain(position, searchVolume) {
  const targetCtr = CTR_BY_POS[3] || 0.11;
  const currentCtr = position <= 10
    ? (CTR_BY_POS[position] || 0.02)
    : position <= 20 ? 0.01 : 0.002;
  return Math.round((targetCtr - currentCtr) * searchVolume);
}

const KEYWORD_THEMES = [
  { name: 'Next.js', test: k => /\bnext\.?js\b|\bnext js\b/i.test(k) },
  { name: 'React', test: k => /\breact\b/i.test(k) && !/next/i.test(k) },
  { name: 'AI / ML', test: k => /\bai\b|\bartificial intelligence\b|\bllm\b|\bchatbot\b|\bgpt\b|\bclaude\b|\bgemini\b|\bmodel\b|\bmachine learning\b/i.test(k) },
  { name: 'v0', test: k => /\bv0\b/i.test(k) },
  { name: 'Deployment', test: k => /\bdeploy\b|\bhosting\b|\bserverless\b|\bedge\b|\bcdn\b/i.test(k) },
  { name: 'Templates', test: k => /\btemplate\b|\bstarter\b|\bboilerplate\b/i.test(k) },
  { name: 'Vercel (Brand)', test: k => /\bvercel\b/i.test(k) },
  { name: 'Performance', test: k => /\bperformance\b|\bspeed\b|\bweb vitals\b|\bcwv\b|\blcp\b/i.test(k) },
  { name: 'E-commerce', test: k => /\bcommerce\b|\becommerce\b|\bshopify\b|\bstripe\b|\bcheckout\b/i.test(k) },
  { name: 'CMS', test: k => /\bcms\b|\bheadless\b|\bsanity\b|\bcontentful\b|\bstrapi\b/i.test(k) },
  { name: 'Database', test: k => /\bdatabase\b|\bpostgres\b|\bredis\b|\bprisma\b|\bsqlite\b|\bblob\b/i.test(k) },
  { name: 'Auth', test: k => /\bauth\b|\blogin\b|\boauth\b|\bsession\b/i.test(k) },
  { name: 'SEO', test: k => /\bseo\b|\bsitemap\b|\bcrawl\b|\bindex/i.test(k) },
  { name: 'Other', test: () => true },
];

function classifyKeywordTheme(keyword) {
  for (const t of KEYWORD_THEMES) {
    if (t.test(keyword)) return t.name;
  }
  return 'Other';
}

module.exports = {
  AUDIT_DIR, PAGE_AUDITS_DIR, ORGANIC_DIR, HISTORY_DIR,
  slugify, loadManifest, loadOrganicJson, loadHistoryJson,
  parseClassifiedSummary, parseClassifiedPages,
  mdTable, fmt, fmtPct, classifyTrend, dateToStr,
  getTrafficAtMonth, getPeakInfo, estimatedGain,
  classifyKeywordTheme, KEYWORD_THEMES,
};
