Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const enzyme_1 = require("sentry-test/enzyme");
const initializeOrg_1 = require("sentry-test/initializeOrg");
const eventView_1 = (0, tslib_1.__importDefault)(require("app/utils/discover/eventView"));
const miniGraph_1 = (0, tslib_1.__importDefault)(require("app/views/eventsV2/miniGraph"));
jest.mock('app/components/charts/eventsGeoRequest', () => jest.fn(({ children }) => children({
    errored: false,
    loading: false,
    reloading: false,
    tableData: [
        {
            data: [
                {
                    'geo.country_code': 'PE',
                    count: 9215,
                },
                {
                    'geo.country_code': 'VI',
                    count: 1,
                },
            ],
            meta: {
                'geo.country_code': 'string',
                count: 'integer',
            },
            title: 'Country',
        },
    ],
})));
describe('EventsV2 > MiniGraph', function () {
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
        MockApiClient.clearMockResponses();
        MockApiClient.addMockResponse({
            url: '/organizations/org-slug/events-stats/',
            statusCode: 200,
        });
    });
    it('makes an EventsRequest with all selected multi y axis', function () {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            const yAxis = ['count()', 'failure_count()'];
            const wrapper = (0, enzyme_1.mountWithTheme)(<miniGraph_1.default location={location} eventView={eventView} organization={organization} yAxis={yAxis}/>, initialData.routerContext);
            const eventsRequestProps = wrapper.find('EventsRequest').props();
            expect(eventsRequestProps.yAxis).toEqual(yAxis);
        });
    });
    it('uses low fidelity interval for bar charts', function () {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            const yAxis = ['count()', 'failure_count()'];
            eventView.display = 'bar';
            const wrapper = (0, enzyme_1.mountWithTheme)(<miniGraph_1.default location={location} eventView={eventView} organization={organization} yAxis={yAxis}/>, initialData.routerContext);
            const eventsRequestProps = wrapper.find('EventsRequest').props();
            expect(eventsRequestProps.interval).toEqual('12h');
        });
    });
    it('renders WorldMapChart', function () {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            const yAxis = ['count()', 'failure_count()'];
            eventView.display = 'worldmap';
            const wrapper = (0, enzyme_1.mountWithTheme)(<miniGraph_1.default location={location} eventView={eventView} organization={organization} yAxis={yAxis}/>, initialData.routerContext);
            const worldMapChartProps = wrapper.find('WorldMapChart').props();
            expect(worldMapChartProps.series).toEqual([
                {
                    data: [
                        { name: 'PE', value: 9215 },
                        { name: 'VI', value: 1 },
                    ],
                    seriesName: 'Country',
                },
            ]);
        });
    });
    it('renders error message', function () {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            const errorMessage = 'something went wrong';
            const api = new MockApiClient();
            MockApiClient.clearMockResponses();
            MockApiClient.addMockResponse({
                url: '/organizations/org-slug/events-stats/',
                body: {
                    detail: errorMessage,
                },
                statusCode: 400,
            });
            const wrapper = (0, enzyme_1.mountWithTheme)(<miniGraph_1.default location={location} eventView={eventView} organization={organization} api={api}/>, initialData.routerContext);
            yield tick();
            wrapper.update();
            expect(wrapper.find('MiniGraph').text()).toBe(errorMessage);
        });
    });
});
//# sourceMappingURL=miniGraph.spec.jsx.map