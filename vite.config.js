import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';
import tailwindcss from 'tailwindcss';
import autoprefixer from 'autoprefixer';
import { resolve } from 'path';
import vitePrerender from 'vite-plugin-prerender';

const Renderer = vitePrerender.PuppeteerRenderer;

export default defineConfig({
  plugins: [
    svelte(),
    vitePrerender({
      staticDir: resolve(__dirname, 'dist'),
      routes: ['/', '/about', '/akce', '/cenik', '/kontakt', '/ochrana-udaju'],
      renderer: new Renderer({
        headless: true,
        renderAfterTime: 2000,
      }),
    }),
  ],
  css: {
    postcss: {
      plugins: [
        tailwindcss(),
        autoprefixer()
      ]
    }
  }
});
