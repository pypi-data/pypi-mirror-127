Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const enzyme_1 = require("sentry-test/enzyme");
const initializeOrg_1 = require("sentry-test/initializeOrg");
const locale_1 = require("app/locale");
const eventView_1 = (0, tslib_1.__importDefault)(require("app/utils/discover/eventView"));
const types_1 = require("app/utils/discover/types");
const resultsChart_1 = (0, tslib_1.__importDefault)(require("app/views/eventsV2/resultsChart"));
describe('EventsV2 > ResultsChart', function () {
    const features = ['discover-basic', 'connect-discover-and-dashboards'];
    const location = TestStubs.location({
        query: { query: 'tag:value' },
        pathname: '/',
    });
    let organization, eventView, initialData;
    beforeEach(() => {
        organization = TestStubs.Organization({
            features,
            projects: [TestStubs.Project()],
        });
        initialData = (0, initializeOrg_1.initializeOrg)({
            organization,
            router: {
                location,
            },
            project: 1,
            projects: [],
        });
        eventView = eventView_1.default.fromSavedQueryOrLocation(undefined, location);
    });
    it('only allows default, daily, previous period, and bar display modes when multiple y axis are selected', function () {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            const wrapper = (0, enzyme_1.mountWithTheme)(<resultsChart_1.default router={TestStubs.router()} organization={organization} eventView={eventView} location={location} onAxisChange={() => undefined} onDisplayChange={() => undefined} total={1} confirmedQuery yAxis={['count()', 'failure_count()']} onTopEventsChange={() => { }}/>, initialData.routerContext);
            const displayOptions = wrapper.find('ChartFooter').props().displayOptions;
            displayOptions.forEach(({ value, disabled }) => {
                if (![
                    types_1.DisplayModes.DEFAULT,
                    types_1.DisplayModes.DAILY,
                    types_1.DisplayModes.PREVIOUS,
                    types_1.DisplayModes.BAR,
                ].includes(value)) {
                    expect(disabled).toBe(true);
                }
            });
        });
    });
    it('does not display a chart if no y axis is selected', function () {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            const wrapper = (0, enzyme_1.mountWithTheme)(<resultsChart_1.default router={TestStubs.router()} organization={organization} eventView={eventView} location={location} onAxisChange={() => undefined} onDisplayChange={() => undefined} total={1} confirmedQuery yAxis={[]} onTopEventsChange={() => { }}/>, initialData.routerContext);
            expect(wrapper.find('NoChartContainer').children().children().html()).toEqual((0, locale_1.t)('No Y-Axis selected.'));
        });
    });
    it('disables other y-axis options when not in default, daily, previous period, or bar display mode', function () {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            eventView.display = types_1.DisplayModes.WORLDMAP;
            const wrapper = (0, enzyme_1.mountWithTheme)(<resultsChart_1.default router={TestStubs.router()} organization={organization} eventView={eventView} location={location} onAxisChange={() => undefined} onDisplayChange={() => undefined} total={1} confirmedQuery yAxis={['count()']} onTopEventsChange={() => { }}/>, initialData.routerContext);
            const yAxisOptions = wrapper.find('ChartFooter').props().yAxisOptions;
            yAxisOptions.forEach(({ value, disabled }) => {
                if (value !== 'count()') {
                    expect(disabled).toBe(true);
                }
            });
        });
    });
    it('disables equation y-axis options when in World Map display mode', function () {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            eventView.display = types_1.DisplayModes.WORLDMAP;
            eventView.fields = [
                { field: 'count()' },
                { field: 'count_unique(user)' },
                { field: 'equation|count() + 2' },
            ];
            const wrapper = (0, enzyme_1.mountWithTheme)(<resultsChart_1.default router={TestStubs.router()} organization={organization} eventView={eventView} location={location} onAxisChange={() => undefined} onDisplayChange={() => undefined} total={1} confirmedQuery yAxis={['count()']} onTopEventsChange={() => { }}/>, initialData.routerContext);
            const yAxisOptions = wrapper.find('ChartFooter').props().yAxisOptions;
            expect(yAxisOptions.length).toEqual(2);
            expect(yAxisOptions[0].value).toEqual('count()');
            expect(yAxisOptions[1].value).toEqual('count_unique(user)');
        });
    });
});
//# sourceMappingURL=resultsChart.spec.jsx.map