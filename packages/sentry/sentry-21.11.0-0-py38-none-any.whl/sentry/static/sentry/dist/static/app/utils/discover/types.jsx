Object.defineProperty(exports, "__esModule", { value: true });
exports.MULTI_Y_AXIS_SUPPORTED_DISPLAY_MODES = exports.CHART_AXIS_OPTIONS = exports.DISPLAY_MODE_FALLBACK_OPTIONS = exports.DISPLAY_MODE_OPTIONS = exports.TOP_EVENT_MODES = exports.DisplayModes = exports.TOP_N = void 0;
const locale_1 = require("app/locale");
exports.TOP_N = 5;
var DisplayModes;
(function (DisplayModes) {
    DisplayModes["DEFAULT"] = "default";
    DisplayModes["PREVIOUS"] = "previous";
    DisplayModes["TOP5"] = "top5";
    DisplayModes["DAILY"] = "daily";
    DisplayModes["DAILYTOP5"] = "dailytop5";
    DisplayModes["WORLDMAP"] = "worldmap";
    DisplayModes["BAR"] = "bar";
})(DisplayModes = exports.DisplayModes || (exports.DisplayModes = {}));
exports.TOP_EVENT_MODES = [DisplayModes.TOP5, DisplayModes.DAILYTOP5];
exports.DISPLAY_MODE_OPTIONS = [
    { value: DisplayModes.DEFAULT, label: (0, locale_1.t)('Total Period') },
    { value: DisplayModes.PREVIOUS, label: (0, locale_1.t)('Previous Period') },
    { value: DisplayModes.TOP5, label: (0, locale_1.t)('Top 5 Period') },
    { value: DisplayModes.DAILY, label: (0, locale_1.t)('Total Daily') },
    { value: DisplayModes.DAILYTOP5, label: (0, locale_1.t)('Top 5 Daily') },
    { value: DisplayModes.WORLDMAP, label: (0, locale_1.t)('World Map') },
    { value: DisplayModes.BAR, label: (0, locale_1.t)('Bar Chart') },
];
/**
 * The chain of fallback display modes to try to use when one is disabled.
 *
 * Make sure that the chain always leads to a display mode that is enabled.
 * There is a fail safe to fall back to the default display mode, but it likely
 * won't be creating results you expect.
 */
exports.DISPLAY_MODE_FALLBACK_OPTIONS = {
    [DisplayModes.DEFAULT]: DisplayModes.DEFAULT,
    [DisplayModes.PREVIOUS]: DisplayModes.DEFAULT,
    [DisplayModes.TOP5]: DisplayModes.DEFAULT,
    [DisplayModes.DAILY]: DisplayModes.DEFAULT,
    [DisplayModes.DAILYTOP5]: DisplayModes.DAILY,
    [DisplayModes.WORLDMAP]: DisplayModes.DEFAULT,
    [DisplayModes.BAR]: DisplayModes.DEFAULT,
};
// default list of yAxis options
exports.CHART_AXIS_OPTIONS = [
    { label: 'count()', value: 'count()' },
    { label: 'count_unique(user)', value: 'count_unique(user)' },
];
exports.MULTI_Y_AXIS_SUPPORTED_DISPLAY_MODES = [
    DisplayModes.DEFAULT,
    DisplayModes.DAILY,
    DisplayModes.PREVIOUS,
    DisplayModes.BAR,
];
//# sourceMappingURL=types.jsx.map