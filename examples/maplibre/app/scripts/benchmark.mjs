import { chromium } from "@playwright/test";
import { createServer } from "vite";
import { mkdir, writeFile } from "node:fs/promises";
import { hostname } from "node:os";
import { resolve } from "node:path";

const runs = 5;
const server = await createServer({ server: { host: "localhost", port: 4173 } });
await server.listen();
const browser = await chromium.launch();
const results = {};

try {
  for (const source of ["api", "pmtiles", "cog"]) {
    results[source] = [];
    for (let index = 0; index < runs; index += 1) {
      const page = await browser.newPage();
      const started = performance.now();
      await page.goto("http://localhost:4173/", { waitUntil: "networkidle" });
      if (source !== "api") await page.locator("#fuente").selectOption(source);
      await page.waitForFunction(() => Boolean(window.courseMap?.getSource("referencia")));
      const elapsed = performance.now() - started;
      const resources = await page.evaluate(() => performance.getEntriesByType("resource").map(({ name, duration, transferSize }) => ({ name, duration, transferSize })));
      results[source].push({ milliseconds: Number(elapsed.toFixed(3)), resources });
      await page.close();
    }
  }
} finally {
  await browser.close();
  await server.close();
}

const report = {
  generatedAt: new Date().toISOString(),
  browser: "chromium",
  host: hostname(),
  runs,
  measurement: "Tiempo hasta fuente MapLibre disponible y recursos observados por Performance API.",
  results,
};
const output = resolve(import.meta.dirname, "../../../../.reports/browser-benchmark.json");
await mkdir(resolve(output, ".."), { recursive: true });
await writeFile(output, `${JSON.stringify(report, null, 2)}\n`);
console.log(output);
