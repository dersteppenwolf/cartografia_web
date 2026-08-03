import { defineConfig } from "@playwright/test";

export default defineConfig({
  testDir: "tests",
  use: { baseURL: "http://localhost:4173" },
  webServer: {
    command: "npm run dev -- --port 4173 --strictPort",
    port: 4173,
    reuseExistingServer: true,
  },
});
