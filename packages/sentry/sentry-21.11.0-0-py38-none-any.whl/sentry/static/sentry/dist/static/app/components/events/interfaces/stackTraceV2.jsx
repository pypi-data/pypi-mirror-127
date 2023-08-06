Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const locale_1 = require("app/locale");
const stacktrace_1 = require("app/types/stacktrace");
const traceEventDataSection_1 = (0, tslib_1.__importDefault)(require("../traceEventDataSection"));
const displayOptions_1 = require("../traceEventDataSection/displayOptions");
const stackTrace_1 = (0, tslib_1.__importDefault)(require("./crashContent/stackTrace"));
const noStackTraceMessage_1 = (0, tslib_1.__importDefault)(require("./noStackTraceMessage"));
const utils_1 = require("./utils");
function StackTrace({ projectId, event, data, type, hasHierarchicalGrouping, groupingCurrentLevel, }) {
    var _a, _b, _c, _d, _e, _f;
    function getPlatform() {
        var _a, _b, _c;
        const framePlatform = (_a = data.frames) === null || _a === void 0 ? void 0 : _a.find(frame => !!frame.platform);
        return (_c = (_b = framePlatform === null || framePlatform === void 0 ? void 0 : framePlatform.platform) !== null && _b !== void 0 ? _b : event.platform) !== null && _c !== void 0 ? _c : 'other';
    }
    const platform = getPlatform();
    const stackTraceNotFound = !((_a = data.frames) !== null && _a !== void 0 ? _a : []).length;
    return (<traceEventDataSection_1.default type={type} stackType={stacktrace_1.STACK_TYPE.ORIGINAL} projectId={projectId} eventId={event.id} platform={platform} stackTraceNotFound={stackTraceNotFound} recentFirst={(0, utils_1.isStacktraceNewestFirst)()} fullStackTrace={!data.hasSystemFrames} title={<Title>{(0, locale_1.t)('Stack Trace')}</Title>} wrapTitle={false} hasMinified={false} hasVerboseFunctionNames={!!((_b = data.frames) === null || _b === void 0 ? void 0 : _b.some(frame => !!frame.rawFunction &&
            !!frame.function &&
            frame.rawFunction !== frame.function))} hasAbsoluteFilePaths={!!((_c = data.frames) === null || _c === void 0 ? void 0 : _c.some(frame => !!frame.filename))} hasAbsoluteAddresses={!!((_d = data.frames) === null || _d === void 0 ? void 0 : _d.some(frame => !!frame.instructionAddr))} hasAppOnlyFrames={!!((_e = data.frames) === null || _e === void 0 ? void 0 : _e.some(frame => frame.inApp !== true))} hasNewestFirst={((_f = data.frames) !== null && _f !== void 0 ? _f : []).length > 1} showPermalink>
      {({ raw, recentFirst, activeDisplayOptions }) => stackTraceNotFound ? (<noStackTraceMessage_1.default />) : (<stackTrace_1.default event={event} platform={platform} stackView={raw
                ? stacktrace_1.STACK_VIEW.RAW
                : activeDisplayOptions.includes(displayOptions_1.DisplayOption.FULL_STACK_TRACE)
                    ? stacktrace_1.STACK_VIEW.FULL
                    : stacktrace_1.STACK_VIEW.APP} newestFirst={recentFirst} stacktrace={data} groupingCurrentLevel={groupingCurrentLevel} hasHierarchicalGrouping={hasHierarchicalGrouping} nativeV2/>)}
    </traceEventDataSection_1.default>);
}
exports.default = StackTrace;
const Title = (0, styled_1.default)('h3') `
  margin-bottom: 0;
`;
//# sourceMappingURL=stackTraceV2.jsx.map