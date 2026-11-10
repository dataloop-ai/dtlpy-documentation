export const pageUrl = (src) => {
  const p = src.replace(/^\/+/, '').replace(/\.mdx?$/, '').replace(/(^|\/)index$/, '');
  return `/${p}${p ? '/' : ''}`.toLowerCase();
};
