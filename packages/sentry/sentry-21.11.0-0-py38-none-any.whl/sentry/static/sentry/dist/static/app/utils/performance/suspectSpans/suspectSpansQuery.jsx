Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const omit_1 = (0, tslib_1.__importDefault)(require("lodash/omit"));
const genericDiscoverQuery_1 = (0, tslib_1.__importDefault)(require("app/utils/discover/genericDiscoverQuery"));
const withApi_1 = (0, tslib_1.__importDefault)(require("app/utils/withApi"));
function getSuspectSpanPayload(props) {
    const payload = { spanOp: props.spanOps };
    const additionalPayload = (0, omit_1.default)(props.eventView.getEventsAPIPayload(props.location), [
        'field',
    ]);
    return Object.assign(payload, additionalPayload);
}
function SuspectSpansQuery(props) {
    return (<genericDiscoverQuery_1.default route="events-spans-performance" getRequestPayload={getSuspectSpanPayload} limit={4} {...(0, omit_1.default)(props, 'children')}>
      {(_a) => {
            var { tableData } = _a, rest = (0, tslib_1.__rest)(_a, ["tableData"]);
            return props.children(Object.assign({ suspectSpans: tableData }, rest));
        }}
    </genericDiscoverQuery_1.default>);
}
exports.default = (0, withApi_1.default)(SuspectSpansQuery);
//# sourceMappingURL=suspectSpansQuery.jsx.map