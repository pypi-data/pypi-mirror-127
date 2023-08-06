Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const React = (0, tslib_1.__importStar)(require("react"));
const breadcrumbs_1 = (0, tslib_1.__importDefault)(require("app/components/events/interfaces/breadcrumbs"));
const csp_1 = (0, tslib_1.__importDefault)(require("app/components/events/interfaces/csp"));
const debugMeta_1 = (0, tslib_1.__importDefault)(require("app/components/events/interfaces/debugMeta"));
const debugMeta_v2_1 = (0, tslib_1.__importDefault)(require("app/components/events/interfaces/debugMeta-v2"));
const exception_1 = (0, tslib_1.__importDefault)(require("app/components/events/interfaces/exception"));
const exceptionV2_1 = (0, tslib_1.__importDefault)(require("app/components/events/interfaces/exceptionV2"));
const generic_1 = (0, tslib_1.__importDefault)(require("app/components/events/interfaces/generic"));
const message_1 = (0, tslib_1.__importDefault)(require("app/components/events/interfaces/message"));
const request_1 = (0, tslib_1.__importDefault)(require("app/components/events/interfaces/request"));
const spans_1 = (0, tslib_1.__importDefault)(require("app/components/events/interfaces/spans"));
const stackTrace_1 = (0, tslib_1.__importDefault)(require("app/components/events/interfaces/stackTrace"));
const stackTraceV2_1 = (0, tslib_1.__importDefault)(require("app/components/events/interfaces/stackTraceV2"));
const template_1 = (0, tslib_1.__importDefault)(require("app/components/events/interfaces/template"));
const threads_1 = (0, tslib_1.__importDefault)(require("app/components/events/interfaces/threads"));
const threadsV2_1 = (0, tslib_1.__importDefault)(require("app/components/events/interfaces/threadsV2"));
const event_1 = require("app/types/event");
function EventEntry({ entry, projectSlug, event, organization, group, route, router, }) {
    var _a, _b, _c, _d;
    const hasHierarchicalGrouping = !!((_a = organization.features) === null || _a === void 0 ? void 0 : _a.includes('grouping-stacktrace-ui')) &&
        !!(event.metadata.current_tree_label || event.metadata.finest_tree_label);
    const hasNativeStackTraceV2 = !!((_b = organization.features) === null || _b === void 0 ? void 0 : _b.includes('native-stack-trace-v2'));
    const groupingCurrentLevel = (_c = group === null || group === void 0 ? void 0 : group.metadata) === null || _c === void 0 ? void 0 : _c.current_level;
    switch (entry.type) {
        case event_1.EntryType.EXCEPTION: {
            const { data, type } = entry;
            return hasNativeStackTraceV2 ? (<exceptionV2_1.default type={type} event={event} data={data} projectId={projectSlug} groupingCurrentLevel={groupingCurrentLevel} hasHierarchicalGrouping={hasHierarchicalGrouping}/>) : (<exception_1.default type={type} event={event} data={data} projectId={projectSlug} groupingCurrentLevel={groupingCurrentLevel} hasHierarchicalGrouping={hasHierarchicalGrouping}/>);
        }
        case event_1.EntryType.MESSAGE: {
            const { data } = entry;
            return <message_1.default data={data}/>;
        }
        case event_1.EntryType.REQUEST: {
            const { data, type } = entry;
            return <request_1.default type={type} event={event} data={data}/>;
        }
        case event_1.EntryType.STACKTRACE: {
            const { data, type } = entry;
            return hasNativeStackTraceV2 ? (<stackTraceV2_1.default type={type} event={event} data={data} projectId={projectSlug} groupingCurrentLevel={groupingCurrentLevel} hasHierarchicalGrouping={hasHierarchicalGrouping}/>) : (<stackTrace_1.default type={type} event={event} data={data} projectId={projectSlug} groupingCurrentLevel={groupingCurrentLevel} hasHierarchicalGrouping={hasHierarchicalGrouping}/>);
        }
        case event_1.EntryType.TEMPLATE: {
            const { data, type } = entry;
            return <template_1.default type={type} event={event} data={data}/>;
        }
        case event_1.EntryType.CSP: {
            const { data } = entry;
            return <csp_1.default event={event} data={data}/>;
        }
        case event_1.EntryType.EXPECTCT:
        case event_1.EntryType.EXPECTSTAPLE:
        case event_1.EntryType.HPKP: {
            const { data, type } = entry;
            return <generic_1.default type={type} data={data}/>;
        }
        case event_1.EntryType.BREADCRUMBS: {
            const { data, type } = entry;
            return (<breadcrumbs_1.default type={type} data={data} organization={organization} event={event} router={router} route={route}/>);
        }
        case event_1.EntryType.THREADS: {
            const { data, type } = entry;
            return hasNativeStackTraceV2 ? (<threadsV2_1.default type={type} event={event} data={data} projectId={projectSlug} groupingCurrentLevel={groupingCurrentLevel} hasHierarchicalGrouping={hasHierarchicalGrouping}/>) : (<threads_1.default type={type} event={event} data={data} projectId={projectSlug} groupingCurrentLevel={groupingCurrentLevel} hasHierarchicalGrouping={hasHierarchicalGrouping}/>);
        }
        case event_1.EntryType.DEBUGMETA:
            const { data } = entry;
            const hasImagesLoadedV2Feature = !!((_d = organization.features) === null || _d === void 0 ? void 0 : _d.includes('images-loaded-v2'));
            if (hasImagesLoadedV2Feature) {
                return (<debugMeta_v2_1.default event={event} projectId={projectSlug} groupId={group === null || group === void 0 ? void 0 : group.id} organization={organization} data={data}/>);
            }
            return (<debugMeta_1.default event={event} projectId={projectSlug} organization={organization} data={data}/>);
        case event_1.EntryType.SPANS:
            return (<spans_1.default event={event} organization={organization}/>);
        default:
            // this should not happen
            /* eslint no-console:0 */
            window.console &&
                console.error &&
                console.error('Unregistered interface: ' + entry.type);
            return null;
    }
}
exports.default = EventEntry;
//# sourceMappingURL=eventEntry.jsx.map