Object.defineProperty(exports, "__esModule", { value: true });
exports.makeSuspectSpan = void 0;
const tslib_1 = require("tslib");
const initializeOrg_1 = require("sentry-test/initializeOrg");
const reactTestingLibrary_1 = require("sentry-test/reactTestingLibrary");
const projectsStore_1 = (0, tslib_1.__importDefault)(require("app/stores/projectsStore"));
const events_1 = require("app/utils/events");
const transactionSpans_1 = (0, tslib_1.__importDefault)(require("app/views/performance/transactionSummary/transactionSpans"));
const types_1 = require("app/views/performance/transactionSummary/transactionSpans/types");
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
    });
    (0, reactTestingLibrary_1.act)(() => void projectsStore_1.default.loadInitialData(initialData.organization.projects));
    return initialData;
}
function makeSpan(opt) {
    const { id } = opt;
    return {
        id,
        startTimestamp: 10100,
        finishTimestamp: 10200,
        exclusiveTime: 100,
    };
}
function makeExample(opt) {
    const { id, description, spans } = opt;
    return {
        id,
        description,
        startTimestamp: 10000,
        finishTimestamp: 12000,
        nonOverlappingExclusiveTime: 2000,
        spans: spans.map(makeSpan),
    };
}
function makeSuspectSpan(opt) {
    const { op, group, examples } = opt;
    return {
        projectId: 1,
        project: 'bar',
        transaction: 'transaction-1',
        op,
        group,
        frequency: 1,
        count: 1,
        sumExclusiveTime: 1,
        p50ExclusiveTime: 1,
        p75ExclusiveTime: 1,
        p95ExclusiveTime: 1,
        p99ExclusiveTime: 1,
        examples: examples.map(makeExample),
    };
}
exports.makeSuspectSpan = makeSuspectSpan;
const spans = [
    {
        op: 'op1',
        group: 'aaaaaaaaaaaaaaaa',
        examples: [
            {
                id: 'abababababababab',
                description: 'span-1',
                spans: [{ id: 'ababab11' }, { id: 'ababab22' }],
            },
            {
                id: 'acacacacacacacac',
                description: 'span-2',
                spans: [{ id: 'acacac11' }, { id: 'acacac22' }],
            },
        ],
    },
    {
        op: 'op2',
        group: 'bbbbbbbbbbbbbbbb',
        examples: [
            {
                id: 'bcbcbcbcbcbcbcbc',
                description: 'span-3',
                spans: [{ id: 'bcbcbc11' }, { id: 'bcbcbc11' }],
            },
            {
                id: 'bdbdbdbdbdbdbdbd',
                description: 'span-4',
                spans: [{ id: 'bdbdbd11' }, { id: 'bdbdbd22' }],
            },
        ],
    },
];
describe('Performance > Transaction Spans', function () {
    let eventsV2Mock;
    let eventsSpanOpsMock;
    let eventsSpansPerformanceMock;
    beforeEach(function () {
        MockApiClient.addMockResponse({
            url: '/organizations/org-slug/projects/',
            body: [],
        });
        MockApiClient.addMockResponse({
            url: '/prompts-activity/',
            body: {},
        });
        MockApiClient.addMockResponse({
            url: '/organizations/org-slug/sdk-updates/',
            body: [],
        });
        MockApiClient.addMockResponse({
            url: '/organizations/org-slug/events-has-measurements/',
            body: { measurements: false },
        });
        eventsV2Mock = MockApiClient.addMockResponse({
            url: '/organizations/org-slug/eventsv2/',
            body: 100,
        });
        eventsSpanOpsMock = MockApiClient.addMockResponse({
            url: '/organizations/org-slug/events-span-ops/',
            body: [],
        });
    });
    afterEach(function () {
        MockApiClient.clearMockResponses();
        projectsStore_1.default.reset();
    });
    describe('Without Span Data', function () {
        beforeEach(function () {
            eventsSpansPerformanceMock = MockApiClient.addMockResponse({
                url: '/organizations/org-slug/events-spans-performance/',
                body: [],
            });
        });
        it('renders empty state', function () {
            return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                const initialData = initializeData({
                    query: { sort: types_1.SpanSortOthers.SUM_EXCLUSIVE_TIME },
                });
                (0, reactTestingLibrary_1.mountWithTheme)(<transactionSpans_1.default organization={initialData.organization} location={initialData.router.location}/>, { context: initialData.routerContext });
                expect(yield reactTestingLibrary_1.screen.findByText('No span data found')).toBeInTheDocument();
            });
        });
    });
    describe('With Span Data', function () {
        beforeEach(function () {
            eventsSpansPerformanceMock = MockApiClient.addMockResponse({
                url: '/organizations/org-slug/events-spans-performance/',
                body: spans.map(makeSuspectSpan),
            });
        });
        it('renders basic UI elements', function () {
            return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                const initialData = initializeData({
                    query: { sort: types_1.SpanSortOthers.SUM_EXCLUSIVE_TIME },
                });
                (0, reactTestingLibrary_1.mountWithTheme)(<transactionSpans_1.default organization={initialData.organization} location={initialData.router.location}/>, { context: initialData.routerContext });
                const cards = yield reactTestingLibrary_1.screen.findAllByTestId('suspect-card');
                expect(cards).toHaveLength(2);
                for (let i = 0; i < cards.length; i++) {
                    const card = cards[i];
                    // these headers should be present by default
                    expect(yield (0, reactTestingLibrary_1.within)(card).findByText('Span Operation')).toBeInTheDocument();
                    expect(yield (0, reactTestingLibrary_1.within)(card).findByText('p75 Duration')).toBeInTheDocument();
                    expect(yield (0, reactTestingLibrary_1.within)(card).findByText('Frequency')).toBeInTheDocument();
                    expect(yield (0, reactTestingLibrary_1.within)(card).findByText('Total Cumulative Duration')).toBeInTheDocument();
                    for (const example of spans[i].examples) {
                        expect(yield (0, reactTestingLibrary_1.within)(card).findByText((0, events_1.getShortEventId)(example.id))).toBeInTheDocument();
                    }
                }
                expect(eventsV2Mock).toHaveBeenCalledTimes(1);
                expect(eventsSpanOpsMock).toHaveBeenCalledTimes(1);
                expect(eventsSpansPerformanceMock).toHaveBeenCalledTimes(1);
            });
        });
        [
            { sort: types_1.SpanSortPercentiles.P50_EXCLUSIVE_TIME, label: 'p50 Duration' },
            { sort: types_1.SpanSortPercentiles.P75_EXCLUSIVE_TIME, label: 'p75 Duration' },
            { sort: types_1.SpanSortPercentiles.P95_EXCLUSIVE_TIME, label: 'p95 Duration' },
            { sort: types_1.SpanSortPercentiles.P99_EXCLUSIVE_TIME, label: 'p99 Duration' },
        ].forEach(({ sort, label }) => {
            it('renders the right percentile header', function () {
                return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                    const initialData = initializeData({ query: { sort } });
                    (0, reactTestingLibrary_1.mountWithTheme)(<transactionSpans_1.default organization={initialData.organization} location={initialData.router.location}/>, { context: initialData.routerContext });
                    const cards = yield reactTestingLibrary_1.screen.findAllByTestId('suspect-card');
                    expect(cards).toHaveLength(2);
                    for (let i = 0; i < cards.length; i++) {
                        const card = cards[i];
                        // these headers should be present by default
                        expect(yield (0, reactTestingLibrary_1.within)(card).findByText('Span Operation')).toBeInTheDocument();
                        expect(yield (0, reactTestingLibrary_1.within)(card).findByText(label)).toBeInTheDocument();
                        expect(yield (0, reactTestingLibrary_1.within)(card).findByText('Frequency')).toBeInTheDocument();
                        expect(yield (0, reactTestingLibrary_1.within)(card).findByText('Total Cumulative Duration')).toBeInTheDocument();
                        const arrow = yield (0, reactTestingLibrary_1.within)(card).findByTestId('span-sort-arrow');
                        expect(arrow).toBeInTheDocument();
                        expect(yield (0, reactTestingLibrary_1.within)(arrow.closest('div')).findByText(label)).toBeInTheDocument();
                    }
                });
            });
        });
        it('renders the right count header', function () {
            return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                const initialData = initializeData({ query: { sort: types_1.SpanSortOthers.COUNT } });
                (0, reactTestingLibrary_1.mountWithTheme)(<transactionSpans_1.default organization={initialData.organization} location={initialData.router.location}/>, { context: initialData.routerContext });
                const cards = yield reactTestingLibrary_1.screen.findAllByTestId('suspect-card');
                expect(cards).toHaveLength(2);
                for (let i = 0; i < cards.length; i++) {
                    const card = cards[i];
                    // need to narrow the search to the upper half of the card because `Occurrences` appears in the table header as well
                    const upper = yield (0, reactTestingLibrary_1.within)(card).findByTestId('suspect-card-upper');
                    // these headers should be present by default
                    expect(yield (0, reactTestingLibrary_1.within)(upper).findByText('Span Operation')).toBeInTheDocument();
                    expect(yield (0, reactTestingLibrary_1.within)(upper).findByText('p75 Duration')).toBeInTheDocument();
                    expect(yield (0, reactTestingLibrary_1.within)(upper).findByText('Occurrences')).toBeInTheDocument();
                    expect(yield (0, reactTestingLibrary_1.within)(upper).findByText('Total Cumulative Duration')).toBeInTheDocument();
                    const arrow = yield (0, reactTestingLibrary_1.within)(upper).findByTestId('span-sort-arrow');
                    expect(arrow).toBeInTheDocument();
                    expect(yield (0, reactTestingLibrary_1.within)(arrow.closest('div')).findByText('Occurrences')).toBeInTheDocument();
                }
            });
        });
        it('renders the right table headers', function () {
            return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                const initialData = initializeData();
                (0, reactTestingLibrary_1.mountWithTheme)(<transactionSpans_1.default organization={initialData.organization} location={initialData.router.location}/>, { context: initialData.routerContext });
                const cards = yield reactTestingLibrary_1.screen.findAllByTestId('suspect-card');
                expect(cards).toHaveLength(2);
                for (let i = 0; i < cards.length; i++) {
                    const card = cards[i];
                    const lower = yield (0, reactTestingLibrary_1.within)(card).findByTestId('suspect-card-lower');
                    expect(yield (0, reactTestingLibrary_1.within)(lower).findByText('Example Transaction')).toBeInTheDocument();
                    expect(yield (0, reactTestingLibrary_1.within)(lower).findByText('Timestamp')).toBeInTheDocument();
                    expect(yield (0, reactTestingLibrary_1.within)(lower).findByText('Span Duration')).toBeInTheDocument();
                    expect(yield (0, reactTestingLibrary_1.within)(lower).findByText('Occurrences')).toBeInTheDocument();
                    expect(yield (0, reactTestingLibrary_1.within)(lower).findByText('Cumulative Duration')).toBeInTheDocument();
                }
            });
        });
    });
});
//# sourceMappingURL=index.spec.jsx.map