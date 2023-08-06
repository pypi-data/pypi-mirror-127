Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = require("react");
const dates_1 = require("app/utils/dates");
const eventView_1 = (0, tslib_1.__importDefault)(require("app/utils/discover/eventView"));
const genericDiscoverQuery_1 = require("app/utils/discover/genericDiscoverQuery");
const EventsGeoRequest = ({ api, organization, yAxis, query, orderby, projects, period, start, end, environments, referrer, children, }) => {
    const eventView = eventView_1.default.fromSavedQuery({
        id: undefined,
        name: '',
        version: 2,
        fields: Array.isArray(yAxis) ? yAxis : [yAxis],
        query,
        orderby: orderby !== null && orderby !== void 0 ? orderby : '',
        projects,
        range: period !== null && period !== void 0 ? period : '',
        start: start ? (0, dates_1.getUtcDateString)(start) : undefined,
        end: end ? (0, dates_1.getUtcDateString)(end) : undefined,
        environment: environments,
    });
    const [results, setResults] = (0, react_1.useState)(undefined);
    const [reloading, setReloading] = (0, react_1.useState)(false);
    const [errored, setErrored] = (0, react_1.useState)(false);
    (0, react_1.useEffect)(() => {
        setErrored(false);
        if (results) {
            setReloading(true);
        }
        (0, genericDiscoverQuery_1.doDiscoverQuery)(api, `/organizations/${organization.slug}/events-geo/`, Object.assign(Object.assign({}, eventView.generateQueryStringObject()), { referrer }))
            .then(discoverQueryResults => {
            setResults([discoverQueryResults[0]]);
            setReloading(false);
        })
            .catch(() => {
            setErrored(true);
            setReloading(false);
        });
    }, [query, yAxis, start, end, period, environments, projects]);
    return children({
        errored,
        loading: !results && !errored,
        reloading,
        tableData: results,
    });
};
exports.default = EventsGeoRequest;
//# sourceMappingURL=eventsGeoRequest.jsx.map