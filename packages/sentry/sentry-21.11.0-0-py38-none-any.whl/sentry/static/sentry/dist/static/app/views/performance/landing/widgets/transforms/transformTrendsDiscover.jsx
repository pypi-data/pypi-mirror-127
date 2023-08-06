Object.defineProperty(exports, "__esModule", { value: true });
exports.transformTrendsDiscover = void 0;
const utils_1 = require("app/views/performance/trends/utils");
function transformTrendsDiscover(_, props) {
    var _a;
    const { trendsData } = props;
    const events = trendsData
        ? (0, utils_1.normalizeTrends)((trendsData && trendsData.events && trendsData.events.data) || [])
        : [];
    return Object.assign(Object.assign({}, props), { data: trendsData, hasData: !!((_a = trendsData === null || trendsData === void 0 ? void 0 : trendsData.events) === null || _a === void 0 ? void 0 : _a.data.length), loading: props.isLoading, isLoading: props.isLoading, isErrored: !!props.error, errored: props.error, statsData: trendsData ? trendsData.stats : {}, transactionsList: events && events.slice ? events.slice(0, 3) : [], events });
}
exports.transformTrendsDiscover = transformTrendsDiscover;
//# sourceMappingURL=transformTrendsDiscover.jsx.map