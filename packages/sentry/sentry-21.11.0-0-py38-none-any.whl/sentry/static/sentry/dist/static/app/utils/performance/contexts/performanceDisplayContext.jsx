Object.defineProperty(exports, "__esModule", { value: true });
exports.usePerformanceDisplayType = exports.PerformanceDisplayProvider = void 0;
const utils_1 = require("./utils");
const [PerformanceDisplayProvider, _usePerformanceDisplayType] = (0, utils_1.createDefinedContext)({
    name: 'CurrentPerformanceViewContext',
});
exports.PerformanceDisplayProvider = PerformanceDisplayProvider;
function usePerformanceDisplayType() {
    return _usePerformanceDisplayType().performanceType;
}
exports.usePerformanceDisplayType = usePerformanceDisplayType;
//# sourceMappingURL=performanceDisplayContext.jsx.map