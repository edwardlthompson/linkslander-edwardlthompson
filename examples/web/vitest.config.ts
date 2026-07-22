import { defineConfig } from "vitest/config";
import viteConfig from "./vite.config";

const nodeMajor = Number.parseInt(process.versions.node.split(".")[0] ?? "0", 10);
// Node 25+ enables a broken native Web Storage stub that blocks jsdom localStorage.
const execArgv = nodeMajor >= 25 ? ["--no-webstorage"] : [];

export default defineConfig({
  ...viteConfig,
  test: {
    environment: "jsdom",
    execArgv,
    exclude: ["e2e/**", "node_modules/**"],
    coverage: {
      provider: "v8",
      include: [
        "src/about/updateChecker.ts",
        "src/about/aboutSession.ts",
        "src/about/donations.ts",
        "src/settings/preferences.ts",
        "src/appBootstrap.ts",
        "src/greet.ts",
      ],
      thresholds: {
        lines: 90,
        functions: 90,
        branches: 85,
        statements: 90,
      },
    },
  },
});
