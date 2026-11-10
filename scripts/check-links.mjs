import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { posix } from 'node:path';

const DIST = 'dist';
const walk = (dir) =>
  readdirSync(dir, { withFileTypes: true }).flatMap((e) => {
    const p = posix.join(dir, e.name);
    return e.isDirectory() ? walk(p) : p.endsWith('.html') ? [p] : [];
  });

const exists = (urlPath) => {
  const p = posix.join(DIST, decodeURI(urlPath));
  if (!existsSync(p)) return false;
  return statSync(p).isFile() || existsSync(posix.join(p, 'index.html'));
};

const broken = [];
for (const file of walk(DIST)) {
  const pageUrl = '/' + posix.relative(DIST, file).replace(/index\.html$/, '');
  for (const [, , target] of readFileSync(file, 'utf8').matchAll(/\b(href|src)="([^"]+)"/g)) {
    if (/^([a-z][a-z0-9+.-]*:|#|\/\/)/i.test(target)) continue;
    const path = target.split(/[?#]/)[0];
    if (!path) continue;
    const abs = path.startsWith('/') ? path : posix.join(pageUrl, path);
    if (!exists(abs)) broken.push(`${pageUrl} -> ${target}`);
  }
}

console.log(`${broken.length} broken internal links`);
if (broken.length) {
  console.log([...new Set(broken)].join('\n'));
  process.exit(1);
}
