Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const omit_1 = (0, tslib_1.__importDefault)(require("lodash/omit"));
const genericDiscoverQuery_1 = (0, tslib_1.__importDefault)(require("app/utils/discover/genericDiscoverQuery"));
const withApi_1 = (0, tslib_1.__importDefault)(require("app/utils/withApi"));
function SpanOpsQuery(props) {
    return (<genericDiscoverQuery_1.default route="events-span-ops" limit={20} {...(0, omit_1.default)(props, 'children')}>
      {(_a) => {
            var { tableData } = _a, rest = (0, tslib_1.__rest)(_a, ["tableData"]);
            return props.children(Object.assign({ spanOps: tableData }, rest));
        }}
    </genericDiscoverQuery_1.default>);
}
exports.default = (0, withApi_1.default)(SpanOpsQuery);
//# sourceMappingURL=spanOpsQuery.jsx.map