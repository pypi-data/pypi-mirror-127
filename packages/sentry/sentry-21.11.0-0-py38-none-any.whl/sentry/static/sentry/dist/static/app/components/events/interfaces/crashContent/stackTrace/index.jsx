Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const errorBoundary_1 = (0, tslib_1.__importDefault)(require("app/components/errorBoundary"));
const stacktrace_1 = require("app/types/stacktrace");
const content_1 = (0, tslib_1.__importDefault)(require("./content"));
const contentV2_1 = (0, tslib_1.__importDefault)(require("./contentV2"));
const contentV3_1 = (0, tslib_1.__importDefault)(require("./contentV3"));
const rawContent_1 = (0, tslib_1.__importDefault)(require("./rawContent"));
function StackTrace({ stackView, stacktrace, event, newestFirst, platform, hasHierarchicalGrouping, groupingCurrentLevel, nativeV2, }) {
    return (<errorBoundary_1.default mini>
      {stackView === stacktrace_1.STACK_VIEW.RAW ? (<pre className="traceback plain">
          {(0, rawContent_1.default)(stacktrace, event.platform)}
        </pre>) : nativeV2 ? (<contentV3_1.default data={stacktrace} className="no-exception" includeSystemFrames={stackView === stacktrace_1.STACK_VIEW.FULL} platform={platform} event={event} newestFirst={newestFirst} groupingCurrentLevel={groupingCurrentLevel}/>) : hasHierarchicalGrouping ? (<contentV2_1.default data={stacktrace} className="no-exception" includeSystemFrames={stackView === stacktrace_1.STACK_VIEW.FULL} platform={platform} event={event} newestFirst={newestFirst} groupingCurrentLevel={groupingCurrentLevel}/>) : (<content_1.default data={stacktrace} className="no-exception" includeSystemFrames={stackView === stacktrace_1.STACK_VIEW.FULL} platform={platform} event={event} newestFirst={newestFirst}/>)}
    </errorBoundary_1.default>);
}
exports.default = StackTrace;
//# sourceMappingURL=index.jsx.map