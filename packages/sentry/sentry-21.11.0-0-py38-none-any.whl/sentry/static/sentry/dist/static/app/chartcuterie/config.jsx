/* global process */
Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
/**
 * This module is used to define the look and feels for charts rendered via the
 * backend chart rendering service Chartcuterie.
 *
 * Be careful what you import into this file, as it will end up being bundled
 * into the configuration file loaded by the service.
 */
const worldMap = (0, tslib_1.__importStar)(require("app/data/world.json"));
const discover_1 = require("./discover");
/**
 * All registered style descriptors
 */
const renderConfig = new Map();
/**
 * Chartcuterie configuration object
 */
const config = {
    version: process.env.COMMIT_SHA,
    init: echarts => {
        echarts.registerMap('sentryWorld', worldMap);
    },
    renderConfig,
};
/**
 * Register a style descriptor
 */
const register = (renderDescriptor) => renderConfig.set(renderDescriptor.key, renderDescriptor);
discover_1.discoverCharts.forEach(register);
exports.default = config;
//# sourceMappingURL=config.jsx.map