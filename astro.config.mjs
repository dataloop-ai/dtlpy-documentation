import { readFileSync } from 'node:fs';
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import YAML from 'yaml';
import { pageUrl } from './scripts/urls.mjs';
import redirects from './redirects.json' with { type: 'json' };

const toSidebar = (n) => {
  if (n.items) {
    const items = n.items.map(toSidebar);
    const landing = n.page ? pageUrl(n.page) : n.href;
    if (landing && !items.some((i) => i.link === landing)) items.unshift({ label: 'Overview', link: landing });
    return { label: n.group, collapsed: n.expanded === false, items };
  }
  return { label: n.label ?? n.group, link: n.href ?? pageUrl(n.page) };
};

const sidebar = YAML.parse(readFileSync('./sidebars.yaml', 'utf8')).map(toSidebar);

export default defineConfig({
  site: 'https://developers.dataloop.ai',
  trailingSlash: 'always',
  redirects,
  integrations: [
    starlight({
      title: 'DDOE Developers',
      description:
        'Developer documentation for the Dell Data Orchestration Engine (DDOE): SDK, REST API, tutorials and notebooks for data management, annotation, automation pipelines and model management.',
      logo: { src: './assets/site/dell-logo.svg', alt: 'Dell' },
      favicon: '/favicon.svg',
      social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/dataloop-ai/dtlpy-documentation' }],
      customCss: ['./src/styles/custom.css'],
      sidebar,
    }),
  ],
});
