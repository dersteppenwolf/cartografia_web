import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: 'tests/slides',
  use: { baseURL: 'http://127.0.0.1:8011/cartografia_web' },
  webServer: {
    command: 'python -m http.server 8011 --directory .preview',
    port: 8011,
    reuseExistingServer: true,
  },
});
