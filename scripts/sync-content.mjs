import { cpSync, existsSync, mkdirSync, readFileSync, readdirSync, rmSync, statSync, writeFileSync } from 'node:fs';
import { posix } from 'node:path';
import YAML from 'yaml';
import { pageUrl } from './urls.mjs';

const SOURCES = ['onboarding', 'tutorials', 'notebooks', 'resources/dtljs'];
const OUT = 'src/content/docs';
const FILES_OUT = 'public/files';
const REPO_EDIT = 'https://github.com/dataloop-ai/dtlpy-documentation/edit/main';
const TEMPLATES = 'docs_build/tutorials_templates';

const walk = (dir) =>
  readdirSync(dir, { withFileTypes: true }).flatMap((e) => {
    const p = posix.join(dir, e.name);
    return e.isDirectory() ? walk(p) : p.endsWith('.md') ? [p] : [];
  });

const isFile = (p) => existsSync(p) && statSync(p).isFile();

const redirects = JSON.parse(readFileSync('redirects.json', 'utf8'));
const allPages = SOURCES.flatMap(walk);
const sources = allPages.filter((f) => !(pageUrl(f) in redirects));
const known = new Set(allPages);
const GENERATED = 'resources/dtljs/';
const warnings = [];
const generatedBroken = [];
const copied = new Set();

const resolveLink = (target, fromFile) => {
  if (/^([a-z][a-z0-9+.-]*:|#|\/\/)/i.test(target)) return target;
  const [, rawPath, suffix = ''] = target.match(/^([^?#]*)([?#].*)?$/);
  if (!rawPath) return target;
  const path = decodeURI(rawPath);
  const dir = posix.dirname(fromFile);
  const candidates = path.startsWith('/')
    ? [path.slice(1)]
    : [posix.join(dir, path), posix.normalize(path)];
  for (const c of candidates) {
    if (known.has(c)) return (redirects[pageUrl(c)] ?? pageUrl(c)) + suffix;
    if (c.endsWith('.md') || !isFile(c)) continue;
    if (c.startsWith('assets/')) return encodeURI(`/${c}`) + suffix;
    if (!copied.has(c)) {
      mkdirSync(posix.dirname(posix.join(FILES_OUT, c)), { recursive: true });
      cpSync(c, posix.join(FILES_OUT, c));
      copied.add(c);
    }
    return encodeURI(`/files/${c}`) + suffix;
  }
  (fromFile.startsWith(GENERATED) ? generatedBroken : warnings).push(`${fromFile}: unresolved link ${target}`);
  return null;
};

const rewriteLinks = (body, file) => {
  let fenced = false;
  return body
    .split('\n')
    .map((line) => {
      if (/^\s*(```|~~~)/.test(line)) fenced = !fenced;
      if (fenced) return line;
      return line
        .replace(/(!?)\[([^\]]*)\]\(([^)\s]+)((?:\s+"[^"]*")?)\)/g, (all, bang, text, t, title) => {
          const url = resolveLink(t, file);
          if (url) return `${bang}[${text}](${url}${title})`;
          return bang || !file.startsWith(GENERATED) ? all : text;
        })
        .replace(/\b(href|src)="([^"]+)"/g, (all, a, t) => `${a}="${resolveLink(t, file) ?? t}"`);
    })
    .join('\n');
};

const plainTitle = (s) =>
  s
    .replace(/!\[[^\]]*\]\([^)]*\)/g, '')
    .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')
    .replace(/[`*_]/g, '')
    .trim();

const convert = (file) => {
  let body = readFileSync(file, 'utf8').replace(/^\uFEFF/, '').replace(/\r\n/g, '\n');
  let fm = {};
  const m = body.match(/^---\n([\s\S]*?)\n---\n?/);
  if (m) {
    fm = YAML.parse(m[1]) ?? {};
    body = body.slice(m[0].length);
  }
  const h1 = body.match(/^\s*# (.+)\n?/);
  if (h1) {
    fm.title = plainTitle(h1[1]);
    body = body.slice(h1[0].length);
  }
  if (/^tutorials\/[^/]+\.md$/.test(file)) {
    const h2 = body.match(/^\s*## (.+)\n?/);
    if (h2) {
      fm.title = plainTitle(h2[1]);
      body = body.slice(h2[0].length);
    }
  }
  fm.title ||= posix.basename(file, '.md');
  const template = file.startsWith('tutorials/') && posix.join(TEMPLATES, file.slice('tutorials/'.length));
  fm.editUrl = `${REPO_EDIT}/${template && existsSync(template) ? template : file}`;
  return `---\n${YAML.stringify(fm)}---\n\n${rewriteLinks(body, file)}`;
};

for (const dir of SOURCES) if (existsSync(posix.join(OUT, dir))) walk(posix.join(OUT, dir)).forEach((f) => rmSync(f));
rmSync(FILES_OUT, { recursive: true, force: true });
rmSync('public/assets', { recursive: true, force: true });

for (const file of sources) {
  const dest = posix.join(OUT, file);
  mkdirSync(posix.dirname(dest), { recursive: true });
  writeFileSync(dest, convert(file));
}
cpSync('assets', 'public/assets', { recursive: true });

console.log(`synced ${sources.length} pages, ${copied.size} extra files`);
if (generatedBroken.length) console.log(`${generatedBroken.length} broken links in generated ${GENERATED} converted to plain text`);
if (warnings.length) {
  console.warn(`${warnings.length} unresolved links:\n${warnings.join('\n')}`);
  if (process.env.STRICT_LINKS) process.exit(1);
}
