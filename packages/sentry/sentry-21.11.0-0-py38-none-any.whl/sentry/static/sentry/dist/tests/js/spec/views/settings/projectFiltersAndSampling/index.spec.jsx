Object.defineProperty(exports, "__esModule", { value: true });
const reactTestingLibrary_1 = require("sentry-test/reactTestingLibrary");
const utils_1 = require("sentry-test/utils");
const utils_2 = require("app/views/settings/project/filtersAndSampling/utils");
const utils_3 = require("./utils");
describe('Filters and Sampling', function () {
    MockApiClient.addMockResponse({
        url: '/projects/org-slug/project-slug/',
        method: 'GET',
        body: TestStubs.Project(),
    });
    describe('renders', function () {
        it('empty', function () {
            const { container } = (0, utils_3.renderComponent)(false);
            // Title
            expect(reactTestingLibrary_1.screen.getByText('Filters & Sampling')).toBeInTheDocument();
            // Error rules container
            expect((0, utils_1.getByTextContent)('Manage the inbound data you want to store. To change the sampling rate or rate limits, update your SDK configuration. The rules added below will apply on top of your SDK configuration. Any new rule may take a few minutes to propagate.')).toBeTruthy();
            expect(reactTestingLibrary_1.screen.getByRole('link', {
                name: 'update your SDK configuration',
            })).toHaveAttribute('href', utils_2.DYNAMIC_SAMPLING_DOC_LINK);
            expect(reactTestingLibrary_1.screen.getByText('There are no error rules to display')).toBeInTheDocument();
            expect(reactTestingLibrary_1.screen.getByText('Add error rule')).toBeInTheDocument();
            // Transaction traces and individual transactions rules container
            expect(reactTestingLibrary_1.screen.getByText('Rules for traces should precede rules for individual transactions.')).toBeInTheDocument();
            expect(reactTestingLibrary_1.screen.getByText('There are no transaction rules to display')).toBeInTheDocument();
            expect(reactTestingLibrary_1.screen.getByText('Add transaction rule')).toBeInTheDocument();
            const readDocsButtonLinks = reactTestingLibrary_1.screen.getAllByRole('button', {
                name: 'Read the docs',
            });
            expect(readDocsButtonLinks).toHaveLength(2);
            for (const readDocsButtonLink of readDocsButtonLinks) {
                expect(readDocsButtonLink).toHaveAttribute('href', utils_2.DYNAMIC_SAMPLING_DOC_LINK);
            }
            expect(reactTestingLibrary_1.screen.getAllByText('Type')).toHaveLength(2);
            expect(reactTestingLibrary_1.screen.getAllByText('Conditions')).toHaveLength(2);
            expect(reactTestingLibrary_1.screen.getAllByText('Rate')).toHaveLength(2);
            expect(container).toSnapshot();
        });
        it('with rules', function () {
            MockApiClient.addMockResponse({
                url: '/projects/org-slug/project-slug/',
                method: 'GET',
                body: TestStubs.Project({
                    dynamicSampling: {
                        rules: [
                            {
                                sampleRate: 0.2,
                                type: 'error',
                                condition: {
                                    op: 'and',
                                    inner: [
                                        {
                                            op: 'glob',
                                            name: 'event.release',
                                            value: ['1.2.3'],
                                        },
                                    ],
                                },
                                id: 39,
                            },
                            {
                                sampleRate: 0.2,
                                type: 'trace',
                                condition: {
                                    op: 'and',
                                    inner: [
                                        {
                                            op: 'glob',
                                            name: 'trace.release',
                                            value: ['1.2.3'],
                                        },
                                    ],
                                },
                                id: 40,
                            },
                            {
                                sampleRate: 0.2,
                                type: 'transaction',
                                condition: {
                                    op: 'and',
                                    inner: [
                                        {
                                            op: 'custom',
                                            name: 'event.legacy_browser',
                                            value: [
                                                'ie_pre_9',
                                                'ie9',
                                                'ie10',
                                                'ie11',
                                                'safari_pre_6',
                                                'opera_pre_15',
                                                'opera_mini_pre_8',
                                                'android_pre_4',
                                            ],
                                        },
                                    ],
                                },
                                id: 42,
                            },
                        ],
                        next_id: 43,
                    },
                }),
            });
            const { container } = (0, utils_3.renderComponent)(false);
            // Title
            expect(reactTestingLibrary_1.screen.getByText('Filters & Sampling')).toBeInTheDocument();
            // Error rules container
            expect((0, utils_1.getByTextContent)('Manage the inbound data you want to store. To change the sampling rate or rate limits, update your SDK configuration. The rules added below will apply on top of your SDK configuration. Any new rule may take a few minutes to propagate.')).toBeTruthy();
            expect(reactTestingLibrary_1.screen.getByRole('link', {
                name: 'update your SDK configuration',
            })).toHaveAttribute('href', utils_2.DYNAMIC_SAMPLING_DOC_LINK);
            expect(reactTestingLibrary_1.screen.queryByText('There are no error rules to display')).not.toBeInTheDocument();
            expect(reactTestingLibrary_1.screen.getByText('Errors only')).toBeInTheDocument();
            expect(reactTestingLibrary_1.screen.getByText('Add error rule')).toBeInTheDocument();
            // Transaction traces and individual transactions rules container
            expect(reactTestingLibrary_1.screen.getByText('Rules for traces should precede rules for individual transactions.')).toBeInTheDocument();
            expect(reactTestingLibrary_1.screen.queryByText('There are no transaction rules to display')).not.toBeInTheDocument();
            const transactionTraceRules = reactTestingLibrary_1.screen.getByText('Transaction traces');
            expect(transactionTraceRules).toBeInTheDocument();
            const individualTransactionRules = reactTestingLibrary_1.screen.getByText('Individual transactions');
            expect(individualTransactionRules).toBeInTheDocument();
            expect(reactTestingLibrary_1.screen.getByText('Add transaction rule')).toBeInTheDocument();
            const readDocsButtonLinks = reactTestingLibrary_1.screen.getAllByRole('button', {
                name: 'Read the docs',
            });
            expect(readDocsButtonLinks).toHaveLength(2);
            for (const readDocsButtonLink of readDocsButtonLinks) {
                expect(readDocsButtonLink).toHaveAttribute('href', utils_2.DYNAMIC_SAMPLING_DOC_LINK);
            }
            expect(reactTestingLibrary_1.screen.getAllByText('Type')).toHaveLength(2);
            expect(reactTestingLibrary_1.screen.getAllByText('Conditions')).toHaveLength(2);
            expect(reactTestingLibrary_1.screen.getAllByText('Rate')).toHaveLength(2);
            expect(container).toSnapshot();
        });
    });
});
//# sourceMappingURL=index.spec.jsx.map