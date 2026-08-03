import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: 'tests/a11y',
  use: { baseURL: 'http://127.0.0.1:8000' },
  webServer: {
    command: 'python -m http.server 8000',
    port: 8000,
    reuseExistingServer: true,
  },
});
