Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = require("react");
const test_utils_1 = require("react-dom/test-utils");
const reactTestingLibrary_1 = require("sentry-test/reactTestingLibrary");
const eventsGeoRequest_1 = (0, tslib_1.__importDefault)(require("app/components/charts/eventsGeoRequest"));
const genericDiscoverQuery = (0, tslib_1.__importStar)(require("app/utils/discover/genericDiscoverQuery"));
describe('EventsRequest', function () {
    const project = TestStubs.Project();
    const organization = TestStubs.Organization();
    const mock = jest.fn(() => <react_1.Fragment />);
    const DEFAULTS = {
        api: new MockApiClient(),
        organization,
        yAxis: ['count()'],
        query: 'event.type:transaction',
        projects: [parseInt(project.id, 10)],
        period: '24h',
        start: new Date(),
        end: new Date(),
        environments: [],
    };
    let wrapper;
    describe('with props changes', function () {
        beforeEach(function () {
            return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                mock.mockClear();
                jest
                    .spyOn(genericDiscoverQuery, 'doDiscoverQuery')
                    .mockImplementation(() => Promise.resolve([{ data: 'test' }, undefined, undefined]));
                yield (0, test_utils_1.act)(() => (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                    wrapper = (0, reactTestingLibrary_1.mountWithTheme)(<eventsGeoRequest_1.default {...DEFAULTS}>{mock}</eventsGeoRequest_1.default>);
                    return wrapper;
                }));
            });
        });
        it('renders with loading state', function () {
            return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                expect(mock).toHaveBeenNthCalledWith(1, expect.objectContaining({
                    errored: false,
                    loading: true,
                    reloading: false,
                    tableData: undefined,
                }));
            });
        });
        it('makes requests', function () {
            return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                expect(mock).toHaveBeenLastCalledWith(expect.objectContaining({
                    errored: false,
                    loading: false,
                    reloading: false,
                    tableData: [{ data: 'test' }],
                }));
            });
        });
        it('renders with error if request errors', function () {
            return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                jest.spyOn(genericDiscoverQuery, 'doDiscoverQuery').mockImplementation(() => {
                    return Promise.reject();
                });
                yield (0, test_utils_1.act)(() => (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                    wrapper = (0, reactTestingLibrary_1.mountWithTheme)(<eventsGeoRequest_1.default {...DEFAULTS}>{mock}</eventsGeoRequest_1.default>);
                    return wrapper;
                }));
                expect(mock).toHaveBeenLastCalledWith(expect.objectContaining({
                    errored: true,
                    loading: false,
                    reloading: false,
                    tableData: undefined,
                }));
            });
        });
        it('makes a new request if query prop changes', function () {
            return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                yield (0, test_utils_1.act)(() => (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                    wrapper.rerender(<eventsGeoRequest_1.default {...DEFAULTS} query="event.type:error">
            {mock}
          </eventsGeoRequest_1.default>);
                }));
                expect(mock).toHaveBeenLastCalledWith(expect.objectContaining({
                    errored: false,
                    loading: false,
                    reloading: false,
                    tableData: [{ data: 'test' }],
                }));
                expect(genericDiscoverQuery.doDiscoverQuery).toHaveBeenCalledWith(expect.anything(), expect.anything(), expect.objectContaining({
                    query: 'event.type:error',
                }));
            });
        });
        it('makes a new request if yAxis prop changes', function () {
            return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                yield (0, test_utils_1.act)(() => (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                    wrapper.rerender(<eventsGeoRequest_1.default {...DEFAULTS} yAxis={['failure_count()']}>
            {mock}
          </eventsGeoRequest_1.default>);
                }));
                expect(mock).toHaveBeenLastCalledWith(expect.objectContaining({
                    errored: false,
                    loading: false,
                    reloading: false,
                    tableData: [{ data: 'test' }],
                }));
                expect(genericDiscoverQuery.doDiscoverQuery).toHaveBeenCalledWith(expect.anything(), expect.anything(), expect.objectContaining({
                    yAxis: 'failure_count()',
                }));
            });
        });
        it('makes a new request if period prop changes', function () {
            return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                yield (0, test_utils_1.act)(() => (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                    wrapper.rerender(<eventsGeoRequest_1.default {...DEFAULTS} period="12h">
            {mock}
          </eventsGeoRequest_1.default>);
                }));
                expect(mock).toHaveBeenLastCalledWith(expect.objectContaining({
                    errored: false,
                    loading: false,
                    reloading: false,
                    tableData: [{ data: 'test' }],
                }));
                expect(genericDiscoverQuery.doDiscoverQuery).toHaveBeenCalledWith(expect.anything(), expect.anything(), expect.objectContaining({
                    statsPeriod: '12h',
                }));
            });
        });
    });
});
//# sourceMappingURL=eventsGeoRequest.spec.jsx.map