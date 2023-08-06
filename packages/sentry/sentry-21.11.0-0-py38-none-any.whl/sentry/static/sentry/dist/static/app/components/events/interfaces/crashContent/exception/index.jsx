Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const errorBoundary_1 = (0, tslib_1.__importDefault)(require("app/components/errorBoundary"));
const stacktrace_1 = require("app/types/stacktrace");
const content_1 = (0, tslib_1.__importDefault)(require("./content"));
const rawContent_1 = (0, tslib_1.__importDefault)(require("./rawContent"));
function Exception({ stackView, stackType, projectId, values, event, newestFirst, hasHierarchicalGrouping, groupingCurrentLevel, platform = 'other', }) {
    return (<errorBoundary_1.default mini>
      {stackView === stacktrace_1.STACK_VIEW.RAW ? (<rawContent_1.default eventId={event.id} projectId={projectId} type={stackType} values={values} platform={platform}/>) : (<content_1.default type={stackType} stackView={stackView} values={values} platform={platform} newestFirst={newestFirst} event={event} hasHierarchicalGrouping={hasHierarchicalGrouping} groupingCurrentLevel={groupingCurrentLevel}/>)}
    </errorBoundary_1.default>);
}
exports.default = Exception;
//# sourceMappingURL=index.jsx.map