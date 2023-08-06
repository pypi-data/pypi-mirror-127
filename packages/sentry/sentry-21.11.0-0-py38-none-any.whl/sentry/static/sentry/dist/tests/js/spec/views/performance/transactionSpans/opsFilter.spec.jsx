Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const initializeOrg_1 = require("sentry-test/initializeOrg");
const reactTestingLibrary_1 = require("sentry-test/reactTestingLibrary");
const eventView_1 = (0, tslib_1.__importDefault)(require("app/utils/discover/eventView"));
const opsFilter_1 = (0, tslib_1.__importDefault)(require("app/views/performance/transactionSummary/transactionSpans/opsFilter"));
function initializeData({ query } = { query: {} }) {
    const features = ['performance-view', 'performance-suspect-spans-view'];
    const organization = TestStubs.Organization({
        features,
        projects: [TestStubs.Project()],
    });
    const initialData = (0, initializeOrg_1.initializeOrg)({
        organization,
        router: {
            location: {
                query: Object.assign({ transaction: 'Test Transaction', project: '1' }, query),
            },
        },
        project: {},
        projects: [],
    });
    return initialData;
}
function createEventView(location) {
    return eventView_1.default.fromNewQueryWithLocation({
        id: undefined,
        version: 2,
        name: '',
        fields: ['count()'],
        projects: [],
    }, location);
}
describe('Performance > Transaction Spans', function () {
    it('fetches span ops', function () {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            const eventsSpanOpsMock = MockApiClient.addMockResponse({
                url: '/organizations/org-slug/events-span-ops/',
                body: [{ op: 'op1' }, { op: 'op2' }],
            });
            const initialData = initializeData();
            (0, reactTestingLibrary_1.mountWithTheme)(<opsFilter_1.default location={initialData.router.location} eventView={createEventView(initialData.router.location)} organization={initialData.organization} handleOpChange={() => { }} transactionName="Test Transaction"/>, { context: initialData.routerContext });
            expect(eventsSpanOpsMock).toHaveBeenCalledTimes(1);
            expect(yield reactTestingLibrary_1.screen.findByTestId('span-op-filter-header')).toBeInTheDocument();
            const filterItems = yield reactTestingLibrary_1.screen.findAllByTestId('span-op-filter-item');
            expect(filterItems).toHaveLength(2);
            filterItems.forEach(item => expect(item).toBeInTheDocument());
        });
    });
    it('handles op change correctly', function () {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            MockApiClient.addMockResponse({
                url: '/organizations/org-slug/events-span-ops/',
                body: [{ op: 'op1' }, { op: 'op2' }],
            });
            const initialData = initializeData();
            const handleOpChange = jest.fn();
            (0, reactTestingLibrary_1.mountWithTheme)(<opsFilter_1.default location={initialData.router.location} eventView={createEventView(initialData.router.location)} organization={initialData.organization} handleOpChange={handleOpChange} transactionName="Test Transaction"/>, { context: initialData.routerContext });
            expect(handleOpChange).not.toHaveBeenCalled();
            const item = (yield reactTestingLibrary_1.screen.findByText('op1')).closest('li');
            expect(item).toBeInTheDocument();
            reactTestingLibrary_1.userEvent.click(item);
            expect(handleOpChange).toHaveBeenCalledTimes(1);
            expect(handleOpChange).toHaveBeenCalledWith('op1');
        });
    });
});
//# sourceMappingURL=opsFilter.spec.jsx.map