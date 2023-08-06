Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const reactTestingLibrary_1 = require("sentry-test/reactTestingLibrary");
const eventView_1 = (0, tslib_1.__importDefault)(require("app/utils/discover/eventView"));
const spanOpsQuery_1 = (0, tslib_1.__importDefault)(require("app/utils/performance/suspectSpans/spanOpsQuery"));
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
                url: '/organizations/test-org/events-span-ops/',
                // just asserting that the data is being fetched, no need for actual data here
                body: [],
            });
            (0, reactTestingLibrary_1.mountWithTheme)(<spanOpsQuery_1.default location={location} orgSlug="test-org" eventView={eventView}>
        {() => null}
      </spanOpsQuery_1.default>);
            expect(getMock).toHaveBeenCalledTimes(1);
        });
    });
});
//# sourceMappingURL=spanOpsQuery.spec.jsx.map