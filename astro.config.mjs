// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://kylewagner4.github.io',
  trailingSlash: 'ignore',
  build: {
    // Small stylesheets are inlined to avoid a render-blocking request.
    inlineStylesheets: 'auto',
  },
});
