// Entry program for the make.fun bounty "Post a GTA 6 meme on X"
// (gta6-meme-x-01). Node 22, standard library only.
//
// The post on X is the entry: the house reads the post itself — its first
// picture, then its text — and hands that to the judge. This program does
// one job: it carries the post's address from POST.json at the repository
// root into the output directory, where the gate picks it up.
//
// Run it the way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const raw = readFileSync(join(BOT_DIR, 'POST.json'), 'utf8');
const post: unknown = JSON.parse(raw);
if (
  typeof post !== 'object' ||
  post === null ||
  typeof (post as { url?: unknown }).url !== 'string'
) {
  throw new Error('POST.json must be a JSON object with a string "url"');
}

// The gate only accepts an X post address (x.com or twitter.com, with the
// post id digits). Warn early when the address is not one, so a placeholder
// or a typo is caught before submission — the copy below still goes ahead,
// because the house, not this program, is the one that refuses a bad post.
const url = (post as { url: string }).url;
const looksLikeXPost =
  /^https:\/\/(www\.|mobile\.)?(x\.com|twitter\.com)\/[^/]+\/(status|statuses|i\/web\/status)\/\d+/.test(
    url,
  );
if (!looksLikeXPost) {
  console.error(
    `warning: POST.json url does not look like an X post address: ${url}`,
  );
}

mkdirSync(OUTPUT_DIR, { recursive: true });
writeFileSync(join(OUTPUT_DIR, 'POST.json'), raw, 'utf8');
