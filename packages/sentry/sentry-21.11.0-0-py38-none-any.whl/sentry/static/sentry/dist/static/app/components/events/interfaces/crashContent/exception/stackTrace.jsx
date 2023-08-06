Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const panels_1 = require("app/components/panels");
const icons_1 = require("app/icons");
const locale_1 = require("app/locale");
const stacktrace_1 = require("app/types/stacktrace");
const utils_1 = require("app/utils");
const useOrganization_1 = (0, tslib_1.__importDefault)(require("app/utils/useOrganization"));
const emptyMessage_1 = (0, tslib_1.__importDefault)(require("app/views/settings/components/emptyMessage"));
const content_1 = (0, tslib_1.__importDefault)(require("../stackTrace/content"));
const contentV2_1 = (0, tslib_1.__importDefault)(require("../stackTrace/contentV2"));
const contentV3_1 = (0, tslib_1.__importDefault)(require("../stackTrace/contentV3"));
function StackTrace({ stackView, stacktrace, chainedException, platform, newestFirst, groupingCurrentLevel, hasHierarchicalGrouping, data, expandFirstFrame, event, }) {
    var _a, _b, _c;
    let organization = null;
    try {
        organization = (0, useOrganization_1.default)();
    }
    catch (_d) {
        // Organization context may be unavailable for the shared event view. We
        // don't need to do anything if it's unavailable.
    }
    if (!(0, utils_1.defined)(stacktrace)) {
        return null;
    }
    if (stackView === stacktrace_1.STACK_VIEW.APP &&
        ((_a = stacktrace.frames) !== null && _a !== void 0 ? _a : []).filter(frame => frame.inApp).length === 0 &&
        !chainedException) {
        return (<panels_1.Panel dashedBorder>
        <emptyMessage_1.default icon={<icons_1.IconWarning size="xs"/>} title={hasHierarchicalGrouping
                ? (0, locale_1.t)('No relevant stack trace has been found!')
                : (0, locale_1.t)('No app only stack trace has been found!')}/>
      </panels_1.Panel>);
    }
    if (!data) {
        return null;
    }
    const includeSystemFrames = stackView === stacktrace_1.STACK_VIEW.FULL ||
        (chainedException && ((_b = data.frames) === null || _b === void 0 ? void 0 : _b.every(frame => !frame.inApp)));
    /**
     * Armin, Markus:
     * If all frames are in app, then no frame is in app.
     * This normally does not matter for the UI but when chained exceptions
     * are used this causes weird behavior where one exception appears to not have a stack trace.
     *
     * It is easier to fix the UI logic to show a non-empty stack trace for chained exceptions
     */
    if (!!((_c = organization === null || organization === void 0 ? void 0 : organization.features) === null || _c === void 0 ? void 0 : _c.includes('native-stack-trace-v2'))) {
        return (<contentV3_1.default data={data} expandFirstFrame={expandFirstFrame} includeSystemFrames={includeSystemFrames} groupingCurrentLevel={groupingCurrentLevel} platform={platform} newestFirst={newestFirst} event={event}/>);
    }
    if (hasHierarchicalGrouping) {
        return (<contentV2_1.default data={data} expandFirstFrame={expandFirstFrame} includeSystemFrames={includeSystemFrames} groupingCurrentLevel={groupingCurrentLevel} platform={platform} newestFirst={newestFirst} event={event}/>);
    }
    return (<content_1.default data={data} expandFirstFrame={expandFirstFrame} includeSystemFrames={includeSystemFrames} platform={platform} newestFirst={newestFirst} event={event}/>);
}
exports.default = StackTrace;
//# sourceMappingURL=stackTrace.jsx.map