Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = require("react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const isNil_1 = (0, tslib_1.__importDefault)(require("lodash/isNil"));
const pill_1 = (0, tslib_1.__importDefault)(require("app/components/pill"));
const pills_1 = (0, tslib_1.__importDefault)(require("app/components/pills"));
const locale_1 = require("app/locale");
const stacktrace_1 = require("app/types/stacktrace");
const traceEventDataSection_1 = (0, tslib_1.__importDefault)(require("../traceEventDataSection"));
const displayOptions_1 = require("../traceEventDataSection/displayOptions");
const exception_1 = (0, tslib_1.__importDefault)(require("./crashContent/exception"));
const stackTrace_1 = (0, tslib_1.__importDefault)(require("./crashContent/stackTrace"));
const threadSelector_1 = (0, tslib_1.__importDefault)(require("./threads/threadSelector"));
const findBestThread_1 = (0, tslib_1.__importDefault)(require("./threads/threadSelector/findBestThread"));
const getThreadException_1 = (0, tslib_1.__importDefault)(require("./threads/threadSelector/getThreadException"));
const getThreadStacktrace_1 = (0, tslib_1.__importDefault)(require("./threads/threadSelector/getThreadStacktrace"));
const noStackTraceMessage_1 = (0, tslib_1.__importDefault)(require("./noStackTraceMessage"));
const utils_1 = require("./utils");
function getIntendedStackView(thread, event) {
    const exception = (0, getThreadException_1.default)(event, thread);
    if (exception) {
        return !!exception.values.find(value => { var _a; return !!((_a = value.stacktrace) === null || _a === void 0 ? void 0 : _a.hasSystemFrames); })
            ? stacktrace_1.STACK_VIEW.APP
            : stacktrace_1.STACK_VIEW.FULL;
    }
    const stacktrace = (0, getThreadStacktrace_1.default)(false, thread);
    return (stacktrace === null || stacktrace === void 0 ? void 0 : stacktrace.hasSystemFrames) ? stacktrace_1.STACK_VIEW.APP : stacktrace_1.STACK_VIEW.FULL;
}
function Threads({ data, event, projectId, type, hasHierarchicalGrouping, groupingCurrentLevel, }) {
    var _a, _b, _c, _d, _e, _f, _g, _h, _j, _k, _l, _m, _o, _p, _q, _r, _s;
    const threads = (_a = data.values) !== null && _a !== void 0 ? _a : [];
    const [state, setState] = (0, react_1.useState)(() => {
        const thread = !!threads.length ? (0, findBestThread_1.default)(threads) : undefined;
        return { activeThread: thread };
    });
    const stackTraceNotFound = !threads.length;
    const { activeThread } = state;
    const hasMoreThanOneThread = threads.length > 1;
    const exception = (0, getThreadException_1.default)(event, activeThread);
    const stackView = activeThread ? getIntendedStackView(activeThread, event) : undefined;
    function getPlatform() {
        var _a, _b, _c, _d, _e, _f;
        let exceptionFramePlatform = undefined;
        for (const value of (_a = exception === null || exception === void 0 ? void 0 : exception.values) !== null && _a !== void 0 ? _a : []) {
            exceptionFramePlatform = (_c = (_b = value.stacktrace) === null || _b === void 0 ? void 0 : _b.frames) === null || _c === void 0 ? void 0 : _c.find(frame => !!frame.platform);
            if (exceptionFramePlatform) {
                break;
            }
        }
        if (exceptionFramePlatform === null || exceptionFramePlatform === void 0 ? void 0 : exceptionFramePlatform.platform) {
            return exceptionFramePlatform.platform;
        }
        const threadFramePlatform = (_e = (_d = activeThread === null || activeThread === void 0 ? void 0 : activeThread.stacktrace) === null || _d === void 0 ? void 0 : _d.frames) === null || _e === void 0 ? void 0 : _e.find(frame => !!frame.platform);
        if (threadFramePlatform === null || threadFramePlatform === void 0 ? void 0 : threadFramePlatform.platform) {
            return threadFramePlatform.platform;
        }
        return (_f = event.platform) !== null && _f !== void 0 ? _f : 'other';
    }
    function renderPills() {
        const { id, name, current, crashed } = activeThread !== null && activeThread !== void 0 ? activeThread : {};
        if ((0, isNil_1.default)(id) || !name) {
            return null;
        }
        return (<pills_1.default>
        {!(0, isNil_1.default)(id) && <pill_1.default name={(0, locale_1.t)('id')} value={String(id)}/>}
        {!!(name === null || name === void 0 ? void 0 : name.trim()) && <pill_1.default name={(0, locale_1.t)('name')} value={name}/>}
        {current !== undefined && <pill_1.default name={(0, locale_1.t)('was active')} value={current}/>}
        {crashed !== undefined && (<pill_1.default name={(0, locale_1.t)('errored')} className={crashed ? 'false' : 'true'}>
            {crashed ? (0, locale_1.t)('yes') : (0, locale_1.t)('no')}
          </pill_1.default>)}
      </pills_1.default>);
    }
    function renderContent({ recentFirst, raw, activeDisplayOptions, }) {
        const stackType = activeDisplayOptions.includes(displayOptions_1.DisplayOption.MINIFIED)
            ? stacktrace_1.STACK_TYPE.MINIFIED
            : stacktrace_1.STACK_TYPE.ORIGINAL;
        if (exception) {
            return (<exception_1.default stackType={stackType} stackView={raw
                    ? stacktrace_1.STACK_VIEW.RAW
                    : activeDisplayOptions.includes(displayOptions_1.DisplayOption.FULL_STACK_TRACE)
                        ? stacktrace_1.STACK_VIEW.FULL
                        : stacktrace_1.STACK_VIEW.APP} projectId={projectId} newestFirst={recentFirst} event={event} platform={platform} values={exception.values} groupingCurrentLevel={groupingCurrentLevel} hasHierarchicalGrouping={hasHierarchicalGrouping}/>);
        }
        const stackTrace = (0, getThreadStacktrace_1.default)(stackType !== stacktrace_1.STACK_TYPE.ORIGINAL, activeThread);
        if (stackTrace) {
            return (<stackTrace_1.default stacktrace={stackTrace} stackView={raw
                    ? stacktrace_1.STACK_VIEW.RAW
                    : activeDisplayOptions.includes(displayOptions_1.DisplayOption.FULL_STACK_TRACE)
                        ? stacktrace_1.STACK_VIEW.FULL
                        : stacktrace_1.STACK_VIEW.APP} newestFirst={recentFirst} event={event} platform={platform} groupingCurrentLevel={groupingCurrentLevel} hasHierarchicalGrouping={hasHierarchicalGrouping} nativeV2/>);
        }
        return (<noStackTraceMessage_1.default message={(activeThread === null || activeThread === void 0 ? void 0 : activeThread.crashed) ? (0, locale_1.t)('Thread Errored') : undefined}/>);
    }
    function getTitle() {
        if (hasMoreThanOneThread && activeThread) {
            return (<threadSelector_1.default threads={threads} activeThread={activeThread} event={event} onChange={thread => {
                    setState(Object.assign(Object.assign({}, state), { activeThread: thread }));
                }} exception={exception} fullWidth/>);
        }
        return <Title>{(0, locale_1.t)('Stack Trace')}</Title>;
    }
    const platform = getPlatform();
    return (<traceEventDataSection_1.default type={type} stackType={stacktrace_1.STACK_TYPE.ORIGINAL} projectId={projectId} eventId={event.id} recentFirst={(0, utils_1.isStacktraceNewestFirst)()} fullStackTrace={stackView === stacktrace_1.STACK_VIEW.FULL} title={getTitle()} platform={platform} showPermalink={!hasMoreThanOneThread} hasMinified={!!((_b = exception === null || exception === void 0 ? void 0 : exception.values) === null || _b === void 0 ? void 0 : _b.find(value => value.rawStacktrace)) ||
            !!(activeThread === null || activeThread === void 0 ? void 0 : activeThread.rawStacktrace)} hasVerboseFunctionNames={!!((_c = exception === null || exception === void 0 ? void 0 : exception.values) === null || _c === void 0 ? void 0 : _c.some(value => {
            var _a, _b;
            return !!((_b = (_a = value.stacktrace) === null || _a === void 0 ? void 0 : _a.frames) === null || _b === void 0 ? void 0 : _b.some(frame => !!frame.rawFunction &&
                !!frame.function &&
                frame.rawFunction !== frame.function));
        })) ||
            !!((_e = (_d = activeThread === null || activeThread === void 0 ? void 0 : activeThread.stacktrace) === null || _d === void 0 ? void 0 : _d.frames) === null || _e === void 0 ? void 0 : _e.some(frame => !!frame.rawFunction &&
                !!frame.function &&
                frame.rawFunction !== frame.function))} hasAbsoluteFilePaths={!!((_f = exception === null || exception === void 0 ? void 0 : exception.values) === null || _f === void 0 ? void 0 : _f.some(value => { var _a, _b; return !!((_b = (_a = value.stacktrace) === null || _a === void 0 ? void 0 : _a.frames) === null || _b === void 0 ? void 0 : _b.some(frame => !!frame.filename)); })) || !!((_h = (_g = activeThread === null || activeThread === void 0 ? void 0 : activeThread.stacktrace) === null || _g === void 0 ? void 0 : _g.frames) === null || _h === void 0 ? void 0 : _h.some(frame => !!frame.filename))} hasAbsoluteAddresses={!!((_j = exception === null || exception === void 0 ? void 0 : exception.values) === null || _j === void 0 ? void 0 : _j.some(value => { var _a, _b; return !!((_b = (_a = value.stacktrace) === null || _a === void 0 ? void 0 : _a.frames) === null || _b === void 0 ? void 0 : _b.some(frame => !!frame.instructionAddr)); })) || !!((_l = (_k = activeThread === null || activeThread === void 0 ? void 0 : activeThread.stacktrace) === null || _k === void 0 ? void 0 : _k.frames) === null || _l === void 0 ? void 0 : _l.some(frame => !!frame.instructionAddr))} hasAppOnlyFrames={!!((_m = exception === null || exception === void 0 ? void 0 : exception.values) === null || _m === void 0 ? void 0 : _m.some(value => { var _a, _b; return !!((_b = (_a = value.stacktrace) === null || _a === void 0 ? void 0 : _a.frames) === null || _b === void 0 ? void 0 : _b.some(frame => frame.inApp !== true)); })) || !!((_p = (_o = activeThread === null || activeThread === void 0 ? void 0 : activeThread.stacktrace) === null || _o === void 0 ? void 0 : _o.frames) === null || _p === void 0 ? void 0 : _p.some(frame => frame.inApp !== true))} hasNewestFirst={!!((_q = exception === null || exception === void 0 ? void 0 : exception.values) === null || _q === void 0 ? void 0 : _q.some(value => { var _a, _b; return ((_b = (_a = value.stacktrace) === null || _a === void 0 ? void 0 : _a.frames) !== null && _b !== void 0 ? _b : []).length > 1; })) ||
            ((_s = (_r = activeThread === null || activeThread === void 0 ? void 0 : activeThread.stacktrace) === null || _r === void 0 ? void 0 : _r.frames) !== null && _s !== void 0 ? _s : []).length > 1} stackTraceNotFound={stackTraceNotFound} wrapTitle={false}>
      {childrenProps => (<react_1.Fragment>
          {renderPills()}
          {renderContent(childrenProps)}
        </react_1.Fragment>)}
    </traceEventDataSection_1.default>);
}
exports.default = Threads;
const Title = (0, styled_1.default)('h3') `
  margin-bottom: 0;
`;
//# sourceMappingURL=threadsV2.jsx.map