Object.defineProperty(exports, "__esModule", { value: true });
exports.transformHistogramQuery = void 0;
function transformHistogramQuery(_, results) {
    const { histograms } = results;
    return Object.assign(Object.assign({}, results), { data: histograms, isLoading: results.isLoading, isErrored: results.error !== null, hasData: !!Object.values(histograms || {}).length });
}
exports.transformHistogramQuery = transformHistogramQuery;
//# sourceMappingURL=transformHistogramQuery.jsx.map