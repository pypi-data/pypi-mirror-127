Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const reactTestingLibrary_1 = require("sentry-test/reactTestingLibrary");
const eventView_1 = (0, tslib_1.__importDefault)(require("app/utils/discover/eventView"));
const suspectSpansQuery_1 = (0, tslib_1.__importDefault)(require("app/utils/performance/suspectSpans/suspectSpansQuery"));
const types_1 = require("app/views/performance/transactionSummary/transactionSpans/types");
describe('SuspectSpansQuery', function () {
    let eventView, location;
    beforeEach(function () {
        eventView = eventView_1.default.fromSavedQuery({
            id: '',
            name: '',
            version: 2,
            fields: [...Object.values(types_1.SpanSortOthers), ...Object.values(types_1.SpanSortPercentiles)],
            projects: [],
            environment: [],
        });
        location = {
            pathname: '/',
            query: {},
        };
    });
    it('fetches data on mount', function () {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            const getMock = MockApiClient.addMockResponse({
                url: '/organizations/test-org/events-spans-performance/',
                // just asserting that the data is being fetched, no need for actual data here
                body: [],
            });
            (0, reactTestingLibrary_1.mountWithTheme)(<suspectSpansQuery_1.default location={location} orgSlug="test-org" eventView={eventView} spanOps={[]}>
        {() => null}
      </suspectSpansQuery_1.default>);
            expect(getMock).toHaveBeenCalledTimes(1);
        });
    });
    it('fetches data with the right ops filter', function () {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            const getMock = MockApiClient.addMockResponse({
                url: '/organizations/test-org/events-spans-performance/',
                // just asserting that the data is being fetched, no need for actual data here
                body: [],
                match: [MockApiClient.matchQuery({ spanOp: ['op1'] })],
            });
            (0, reactTestingLibrary_1.mountWithTheme)(<suspectSpansQuery_1.default location={location} orgSlug="test-org" eventView={eventView} spanOps={['op1']}>
        {() => null}
      </suspectSpansQuery_1.default>);
            expect(getMock).toHaveBeenCalledTimes(1);
        });
    });
});
//# sourceMappingURL=suspectSpansQuery.spec.jsx.map