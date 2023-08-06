Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const locale_1 = require("app/locale");
const stacktrace_1 = require("app/types/stacktrace");
const traceEventDataSection_1 = (0, tslib_1.__importDefault)(require("../traceEventDataSection"));
const displayOptions_1 = require("../traceEventDataSection/displayOptions");
const exception_1 = (0, tslib_1.__importDefault)(require("./crashContent/exception"));
const noStackTraceMessage_1 = (0, tslib_1.__importDefault)(require("./noStackTraceMessage"));
const utils_1 = require("./utils");
function Exception({ event, type, data, projectId, hasHierarchicalGrouping, groupingCurrentLevel, }) {
    var _a, _b, _c, _d, _e, _f, _g;
    const eventHasThreads = !!event.entries.some(entry => entry.type === 'threads');
    /* in case there are threads in the event data, we don't render the
     exception block.  Instead the exception is contained within the
     thread interface. */
    if (eventHasThreads) {
        return null;
    }
    function getPlatform() {
        var _a, _b, _c, _d;
        const dataValue = (_a = data.values) === null || _a === void 0 ? void 0 : _a.find(value => { var _a, _b; return !!((_b = (_a = value.stacktrace) === null || _a === void 0 ? void 0 : _a.frames) === null || _b === void 0 ? void 0 : _b.some(frame => !!frame.platform)); });
        if (dataValue) {
            const framePlatform = (_c = (_b = dataValue.stacktrace) === null || _b === void 0 ? void 0 : _b.frames) === null || _c === void 0 ? void 0 : _c.find(frame => !!frame.platform);
            if (framePlatform === null || framePlatform === void 0 ? void 0 : framePlatform.platform) {
                return framePlatform.platform;
            }
        }
        return (_d = event.platform) !== null && _d !== void 0 ? _d : 'other';
    }
    const stackTraceNotFound = !((_a = data.values) !== null && _a !== void 0 ? _a : []).length;
    const platform = getPlatform();
    return (<traceEventDataSection_1.default title={<Title>{(0, locale_1.t)('Exception')}</Title>} type={type} stackType={stacktrace_1.STACK_TYPE.ORIGINAL} projectId={projectId} eventId={event.id} recentFirst={(0, utils_1.isStacktraceNewestFirst)()} fullStackTrace={!data.hasSystemFrames} platform={platform} hasMinified={!!((_b = data.values) === null || _b === void 0 ? void 0 : _b.some(value => value.rawStacktrace))} hasVerboseFunctionNames={!!((_c = data.values) === null || _c === void 0 ? void 0 : _c.some(value => {
            var _a, _b;
            return !!((_b = (_a = value.stacktrace) === null || _a === void 0 ? void 0 : _a.frames) === null || _b === void 0 ? void 0 : _b.some(frame => !!frame.rawFunction &&
                !!frame.function &&
                frame.rawFunction !== frame.function));
        }))} hasAbsoluteFilePaths={!!((_d = data.values) === null || _d === void 0 ? void 0 : _d.some(value => { var _a, _b; return !!((_b = (_a = value.stacktrace) === null || _a === void 0 ? void 0 : _a.frames) === null || _b === void 0 ? void 0 : _b.some(frame => !!frame.filename)); }))} hasAbsoluteAddresses={!!((_e = data.values) === null || _e === void 0 ? void 0 : _e.some(value => { var _a, _b; return !!((_b = (_a = value.stacktrace) === null || _a === void 0 ? void 0 : _a.frames) === null || _b === void 0 ? void 0 : _b.some(frame => !!frame.instructionAddr)); }))} hasAppOnlyFrames={!!((_f = data.values) === null || _f === void 0 ? void 0 : _f.some(value => { var _a, _b; return !!((_b = (_a = value.stacktrace) === null || _a === void 0 ? void 0 : _a.frames) === null || _b === void 0 ? void 0 : _b.some(frame => frame.inApp !== true)); }))} hasNewestFirst={!!((_g = data.values) === null || _g === void 0 ? void 0 : _g.some(value => { var _a, _b; return ((_b = (_a = value.stacktrace) === null || _a === void 0 ? void 0 : _a.frames) !== null && _b !== void 0 ? _b : []).length > 1; }))} stackTraceNotFound={stackTraceNotFound} showPermalink wrapTitle={false}>
      {({ raw, recentFirst, activeDisplayOptions }) => stackTraceNotFound ? (<noStackTraceMessage_1.default />) : (<exception_1.default stackType={activeDisplayOptions.includes(displayOptions_1.DisplayOption.MINIFIED)
                ? stacktrace_1.STACK_TYPE.MINIFIED
                : stacktrace_1.STACK_TYPE.ORIGINAL} stackView={raw
                ? stacktrace_1.STACK_VIEW.RAW
                : activeDisplayOptions.includes(displayOptions_1.DisplayOption.FULL_STACK_TRACE)
                    ? stacktrace_1.STACK_VIEW.FULL
                    : stacktrace_1.STACK_VIEW.APP} projectId={projectId} newestFirst={recentFirst} event={event} platform={platform} values={data.values} groupingCurrentLevel={groupingCurrentLevel} hasHierarchicalGrouping={hasHierarchicalGrouping}/>)}
    </traceEventDataSection_1.default>);
}
exports.default = Exception;
const Title = (0, styled_1.default)('h3') `
  margin-bottom: 0;
`;
//# sourceMappingURL=exceptionV2.jsx.map