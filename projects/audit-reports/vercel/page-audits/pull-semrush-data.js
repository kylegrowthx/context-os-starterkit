#!/usr/bin/env node

const https = require('https');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.SEMRUSH_API_KEY;
if (!API_KEY) {
  console.error('Set SEMRUSH_API_KEY env var');
  process.exit(1);
}

const DB = 'us';
const DISPLAY_LIMIT = 2000;
const DELAY_MS = 300;

const AUDIT_DIR = __dirname;
const ORGANIC_DIR = path.join(AUDIT_DIR, 'url-organic');
const HISTORY_DIR = path.join(AUDIT_DIR, 'url-rank-history');

function csvToJson(csvText) {
  const lines = csvText.replace(/\r/g, '').trim().split('\n').filter(Boolean);
  if (lines.length < 2) return [];
  const headers = lines[0].split(';');
  return lines.slice(1).map((line) => {
    const vals = line.split(';');
    const obj = {};
    headers.forEach((h, i) => {
      const v = (vals[i] || '').trim();
      obj[h] = /^\d+(\.\d+)?$/.test(v) ? Number(v) : v;
    });
    return obj;
  });
}
const MANIFEST = path.join(
  '/Users/marcelsantilli_mac2/.cursor/projects',
  'Users-marcelsantilli-mac2-Dropbox-GrowthX-AI-Projects-growthx-handbook',
  'agent-tools',
  'content-with-traffic.json'
);

function slugify(url) {
  return url
    .replace('https://vercel.com/', '')
    .replace(/\//g, '__')
    .replace(/[^a-zA-Z0-9._-]/g, '_') || 'homepage';
}

function fetch(url) {
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';
      res.on('data', (chunk) => (data += chunk));
      res.on('end', () => resolve({ status: res.statusCode, body: data }));
    }).on('error', reject);
  });
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

async function pullUrlOrganic(pageUrl) {
  const params = new URLSearchParams({
    type: 'url_organic',
    key: API_KEY,
    url: pageUrl,
    database: DB,
    display_limit: DISPLAY_LIMIT,
  });
  return fetch(`https://api.semrush.com/?${params}`);
}

async function pullUrlRankHistory(pageUrl) {
  const params = new URLSearchParams({
    type: 'url_rank_history',
    key: API_KEY,
    url: pageUrl,
    database: DB,
  });
  return fetch(`https://api.semrush.com/?${params}`);
}

async function main() {
  const startIdx = parseInt(process.argv[2] || '0', 10);
  const endIdx = process.argv[3] ? parseInt(process.argv[3], 10) : undefined;

  const pages = JSON.parse(fs.readFileSync(MANIFEST, 'utf8'));
  const slice = endIdx ? pages.slice(startIdx, endIdx) : pages.slice(startIdx);

  fs.mkdirSync(ORGANIC_DIR, { recursive: true });
  fs.mkdirSync(HISTORY_DIR, { recursive: true });

  console.log(`Pulling ${slice.length} pages (index ${startIdx} to ${startIdx + slice.length - 1})`);
  console.log(`Output: ${AUDIT_DIR}\n`);

  let successOrganic = 0;
  let successHistory = 0;
  let errors = [];

  for (let i = 0; i < slice.length; i++) {
    const page = slice[i];
    const globalIdx = startIdx + i;
    const slug = slugify(page.url);
    const organicCsv = path.join(ORGANIC_DIR, `${slug}.csv`);
    const organicJson = path.join(ORGANIC_DIR, `${slug}.json`);
    const historyCsv = path.join(HISTORY_DIR, `${slug}.csv`);
    const historyJson = path.join(HISTORY_DIR, `${slug}.json`);

    if (fs.existsSync(organicCsv) && fs.existsSync(historyCsv)) {
      console.log(`[${globalIdx}] SKIP (exists) ${page.url}`);
      successOrganic++;
      successHistory++;
      continue;
    }

    try {
      if (!fs.existsSync(organicCsv)) {
        const organic = await pullUrlOrganic(page.url);
        if (organic.status === 200 && !organic.body.startsWith('ERROR')) {
          fs.writeFileSync(organicCsv, organic.body);
          fs.writeFileSync(organicJson, JSON.stringify(csvToJson(organic.body), null, 2));
          successOrganic++;
        } else {
          errors.push({ url: page.url, report: 'url_organic', error: organic.body.slice(0, 200) });
          console.log(`[${globalIdx}] ERR organic: ${organic.body.slice(0, 80)}`);
        }
        await sleep(DELAY_MS);
      } else {
        successOrganic++;
      }

      if (!fs.existsSync(historyCsv)) {
        const history = await pullUrlRankHistory(page.url);
        if (history.status === 200 && !history.body.startsWith('ERROR')) {
          fs.writeFileSync(historyCsv, history.body);
          fs.writeFileSync(historyJson, JSON.stringify(csvToJson(history.body), null, 2));
          successHistory++;
        } else {
          errors.push({ url: page.url, report: 'url_rank_history', error: history.body.slice(0, 200) });
          console.log(`[${globalIdx}] ERR history: ${history.body.slice(0, 80)}`);
        }
        await sleep(DELAY_MS);
      } else {
        successHistory++;
      }

      const oSize = fs.existsSync(organicCsv) ? (fs.statSync(organicCsv).size / 1024).toFixed(1) + 'kb' : 'ERR';
      const hSize = fs.existsSync(historyCsv) ? (fs.statSync(historyCsv).size / 1024).toFixed(1) + 'kb' : 'ERR';
      console.log(`[${globalIdx}/${pages.length - 1}] ${slug}  organic=${oSize}  history=${hSize}`);
    } catch (err) {
      errors.push({ url: page.url, report: 'both', error: err.message });
      console.log(`[${globalIdx}] FATAL: ${err.message}`);
    }
  }

  console.log(`\n--- Done ---`);
  console.log(`url_organic:      ${successOrganic}/${slice.length} saved to ${ORGANIC_DIR}`);
  console.log(`url_rank_history: ${successHistory}/${slice.length} saved to ${HISTORY_DIR}`);

  if (errors.length) {
    const errFile = path.join(AUDIT_DIR, 'pull-errors.json');
    fs.writeFileSync(errFile, JSON.stringify(errors, null, 2));
    console.log(`${errors.length} errors logged to ${errFile}`);
  }
}

main().catch((err) => {
  console.error('Fatal:', err);
  process.exit(1);
});
