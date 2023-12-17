"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var plugin_react_1 = require("@vitejs/plugin-react");
var vite_1 = require("vite");
var vite_tsconfig_paths_1 = require("vite-tsconfig-paths");
// https://vitejs.dev/config/
exports.default = (0, vite_1.defineConfig)({
    plugins: [(0, plugin_react_1.default)(), (0, vite_tsconfig_paths_1.default)()],
    server: {
        host: true,
        strictPort: true,
        port: 3000,
        hmr: {
            overlay: true,
        },
        proxy: {
            '/api': {
                target: 'http://0.0.0.0:8000',
                changeOrigin: true,
            },
        },
    },
    preview: {
        port: 3001,
        strictPort: true,
    },
    clearScreen: false,
});
