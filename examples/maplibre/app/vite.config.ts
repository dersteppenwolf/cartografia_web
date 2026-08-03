import { defineConfig } from "vitest/config";

export default defineConfig({
  base: "./",
  test: {
    exclude: ["tests/**/*.spec.ts"],
  },
});
