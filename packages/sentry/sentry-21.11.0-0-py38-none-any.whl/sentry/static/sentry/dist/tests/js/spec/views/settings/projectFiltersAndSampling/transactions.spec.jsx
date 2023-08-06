Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const reactTestingLibrary_1 = require("sentry-test/reactTestingLibrary");
const utils_1 = require("sentry-test/utils");
const utils_2 = require("app/views/settings/project/filtersAndSampling/utils");
const utils_3 = require("./utils");
describe('Filters and Sampling - Transaction rule', function () {
    describe('transaction rule', function () {
        it('renders', function () {
            return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                MockApiClient.addMockResponse({
                    url: '/projects/org-slug/project-slug/',
                    method: 'GET',
                    body: TestStubs.Project({
                        dynamicSampling: {
                            rules: [
                                {
                                    sampleRate: 0.1,
                                    type: 'error',
                                    condition: {
                                        op: 'and',
                                        inner: [
                                            {
                                                op: 'glob',
                                                name: 'event.release',
                                                value: ['1*'],
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
                            ],
                            next_id: 43,
                        },
                    }),
                });
                MockApiClient.addMockResponse({
                    url: '/projects/org-slug/project-slug/',
                    method: 'PUT',
                    body: TestStubs.Project({
                        dynamicSampling: {
                            rules: [
                                {
                                    sampleRate: 0.1,
                                    type: 'error',
                                    condition: {
                                        op: 'and',
                                        inner: [
                                            {
                                                op: 'glob',
                                                name: 'event.release',
                                                value: ['1*'],
                                            },
                                        ],
                                    },
                                    id: 44,
                                },
                                {
                                    sampleRate: 0.6,
                                    type: 'trace',
                                    condition: {
                                        op: 'and',
                                        inner: [
                                            {
                                                op: 'glob',
                                                name: 'trace.release',
                                                value: ['[0-9]'],
                                            },
                                        ],
                                    },
                                    id: 45,
                                },
                            ],
                            next_id: 43,
                        },
                    }),
                });
                MockApiClient.addMockResponse({
                    url: '/organizations/org-slug/tags/release/values/',
                    method: 'GET',
                    body: [{ value: '[0-9]' }],
                });
                (0, utils_3.renderComponent)();
                // Error rules container
                expect(reactTestingLibrary_1.screen.queryByText('There are no error rules to display')).not.toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByText('Errors only')).toBeInTheDocument();
                // Transaction traces and individual transactions rules container
                expect(reactTestingLibrary_1.screen.queryByText('There are no transaction rules to display')).not.toBeInTheDocument();
                const transactionTraceRules = reactTestingLibrary_1.screen.getByText('Transaction traces');
                expect(transactionTraceRules).toBeInTheDocument();
                const editRuleButtons = reactTestingLibrary_1.screen.getAllByLabelText('Edit Rule');
                expect(editRuleButtons).toHaveLength(2);
                // Open rule modal - edit transaction rule
                yield (0, utils_3.renderModal)(editRuleButtons[1]);
                // Modal content
                expect(reactTestingLibrary_1.screen.getByText('Edit Transaction Sampling Rule')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByText('Tracing')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByRole('checkbox')).toBeChecked();
                // Release Field
                expect(reactTestingLibrary_1.screen.getByTestId('autocomplete-release')).toBeInTheDocument();
                // Release field is not empty
                const releaseFieldValues = reactTestingLibrary_1.screen.getByTestId('multivalue');
                expect(releaseFieldValues).toBeInTheDocument();
                expect(releaseFieldValues).toHaveTextContent('1.2.3');
                // Button is enabled - meaning the form is valid
                const saveRuleButton = reactTestingLibrary_1.screen.getByLabelText('Save Rule');
                expect(saveRuleButton).toBeInTheDocument();
                expect(saveRuleButton).toBeEnabled();
                // Sample rate field
                const sampleRateField = reactTestingLibrary_1.screen.getByPlaceholderText('\u0025');
                expect(sampleRateField).toBeInTheDocument();
                // Sample rate is not empty
                expect(sampleRateField).toHaveValue(20);
                // Clear release field
                reactTestingLibrary_1.userEvent.clear(reactTestingLibrary_1.screen.getByLabelText('Search or add a release'));
                // Release field is now empty
                const newReleaseFieldValues = reactTestingLibrary_1.screen.queryByTestId('multivalue');
                expect(newReleaseFieldValues).not.toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByLabelText('Save Rule')).toBeDisabled();
                // Type into realease field
                reactTestingLibrary_1.userEvent.type(reactTestingLibrary_1.screen.getByLabelText('Search or add a release'), '[0-9]');
                // Autocomplete suggests options
                const autocompleteOptions = reactTestingLibrary_1.screen.getByTestId('option');
                expect(autocompleteOptions).toBeInTheDocument();
                expect(autocompleteOptions).toHaveTextContent('[0-9]');
                // Click on the suggested option
                reactTestingLibrary_1.userEvent.click(autocompleteOptions);
                expect(reactTestingLibrary_1.screen.getByLabelText('Save Rule')).toBeEnabled();
                // Clear sample rate field
                reactTestingLibrary_1.userEvent.clear(sampleRateField);
                expect(reactTestingLibrary_1.screen.getByLabelText('Save Rule')).toBeDisabled();
                // Update sample rate field
                reactTestingLibrary_1.userEvent.type(sampleRateField, '60');
                // Save button is now enabled
                const saveRuleButtonEnabled = reactTestingLibrary_1.screen.getByLabelText('Save Rule');
                expect(saveRuleButtonEnabled).toBeEnabled();
                // Click on save button
                reactTestingLibrary_1.userEvent.click(saveRuleButtonEnabled);
                // Modal will close
                yield (0, reactTestingLibrary_1.waitForElementToBeRemoved)(() => reactTestingLibrary_1.screen.getByText('Edit Transaction Sampling Rule'));
                // Error rules panel is updated
                expect(reactTestingLibrary_1.screen.getByText('Errors only')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByText('Transaction traces')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getAllByText('Release')).toHaveLength(2);
                // Old values
                expect(reactTestingLibrary_1.screen.queryByText('1.2.3')).not.toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.queryByText('20%')).not.toBeInTheDocument();
                // New values
                expect(reactTestingLibrary_1.screen.getByText('[0-9]')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByText('60%')).toBeInTheDocument();
            });
        });
        describe('modal', function () {
            MockApiClient.addMockResponse({
                url: '/projects/org-slug/project-slug/',
                method: 'GET',
                body: TestStubs.Project(),
            });
            const conditionTracingCategories = [
                'Release',
                'Environment',
                'User Id',
                'User Segment',
                'Transaction',
            ];
            it('renders modal', function () {
                return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                    (0, utils_3.renderComponent)();
                    // Open Modal
                    yield (0, utils_3.renderModal)(reactTestingLibrary_1.screen.getByText('Add transaction rule'), true);
                    // Modal content
                    expect(reactTestingLibrary_1.screen.getByText('Add Transaction Sampling Rule')).toBeInTheDocument();
                    expect(reactTestingLibrary_1.screen.getByText('Tracing')).toBeInTheDocument();
                    expect(reactTestingLibrary_1.screen.getByRole('checkbox')).toBeChecked();
                    expect((0, utils_1.getByTextContent)('Include all related transactions by trace ID. This can span across multiple projects. All related errors will remain. Learn more about tracing.')).toBeTruthy();
                    expect(reactTestingLibrary_1.screen.getByRole('link', {
                        name: 'Learn more about tracing',
                    })).toHaveAttribute('href', utils_2.DYNAMIC_SAMPLING_DOC_LINK);
                    expect(reactTestingLibrary_1.screen.getByText('Add Condition')).toBeInTheDocument();
                    expect(reactTestingLibrary_1.screen.getByText('Apply sampling rate to all transactions')).toBeInTheDocument();
                    expect(reactTestingLibrary_1.screen.getByText('Sampling Rate \u0025')).toBeInTheDocument();
                    expect(reactTestingLibrary_1.screen.getByPlaceholderText('\u0025')).toHaveValue(null);
                    expect(reactTestingLibrary_1.screen.getByLabelText('Cancel')).toBeInTheDocument();
                    const saveRuleButton = reactTestingLibrary_1.screen.getByLabelText('Save Rule');
                    expect(saveRuleButton).toBeInTheDocument();
                    expect(saveRuleButton).toBeDisabled();
                    // Close Modal
                    reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByLabelText('Close Modal'));
                    yield (0, reactTestingLibrary_1.waitForElementToBeRemoved)(() => reactTestingLibrary_1.screen.getByText('Add Transaction Sampling Rule'));
                });
            });
            it('condition options', function () {
                return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                    (0, utils_3.renderComponent)();
                    // Open Modal
                    yield (0, utils_3.renderModal)(reactTestingLibrary_1.screen.getByText('Add transaction rule'));
                    // Click on 'Add condition'
                    reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByText('Add Condition'));
                    // Autocomplete
                    expect(reactTestingLibrary_1.screen.getByTestId('autocomplete-list')).toBeInTheDocument();
                    // Trancing Condition Options
                    const conditionTracingOptions = reactTestingLibrary_1.screen.getAllByTestId('condition');
                    expect(conditionTracingOptions).toHaveLength(conditionTracingCategories.length);
                    for (const conditionTracingOptionIndex in conditionTracingOptions) {
                        expect(conditionTracingOptions[conditionTracingOptionIndex]).toHaveTextContent(conditionTracingCategories[conditionTracingOptionIndex]);
                    }
                    // Unchecked tracing checkbox
                    reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByRole('checkbox'));
                    // Click on 'Add condition'
                    reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByText('Add Condition'));
                    // No Tracing Condition Options
                    const conditionOptions = reactTestingLibrary_1.screen.getAllByTestId('condition');
                    expect(conditionOptions).toHaveLength(utils_3.commonConditionCategories.length);
                    for (const conditionOptionIndex in conditionOptions) {
                        expect(conditionOptions[conditionOptionIndex]).toHaveTextContent(utils_3.commonConditionCategories[conditionOptionIndex]);
                    }
                    // Close Modal
                    reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByLabelText('Close Modal'));
                    yield (0, reactTestingLibrary_1.waitForElementToBeRemoved)(() => reactTestingLibrary_1.screen.getByText('Add Transaction Sampling Rule'));
                });
            });
            describe('save rule', function () {
                it('transaction trace', function () {
                    return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                        MockApiClient.addMockResponse({
                            url: '/projects/org-slug/project-slug/',
                            method: 'PUT',
                            body: TestStubs.Project({
                                dynamicSampling: {
                                    rules: [
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
                                    ],
                                    next_id: 40,
                                },
                            }),
                        });
                        MockApiClient.addMockResponse({
                            url: '/organizations/org-slug/tags/release/values/',
                            method: 'GET',
                            body: [{ value: '1.2.3' }],
                        });
                        (0, utils_3.renderComponent)();
                        // Open Modal
                        yield (0, utils_3.renderModal)(reactTestingLibrary_1.screen.getByText('Add transaction rule'));
                        // Checked tracing checkbox
                        expect(reactTestingLibrary_1.screen.getByRole('checkbox')).toBeChecked();
                        // Click on 'Add condition'
                        reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByText('Add Condition'));
                        // Autocomplete
                        expect(reactTestingLibrary_1.screen.getByTestId('autocomplete-list')).toBeInTheDocument();
                        // Condition Options
                        const conditionOptions = reactTestingLibrary_1.screen.getAllByTestId('condition');
                        // Click on the first condition option
                        reactTestingLibrary_1.userEvent.click(conditionOptions[0]);
                        // Release Field
                        expect(reactTestingLibrary_1.screen.getByTestId('autocomplete-release')).toBeInTheDocument();
                        // Release field is empty
                        const releaseFieldValues = reactTestingLibrary_1.screen.queryByTestId('multivalue');
                        expect(releaseFieldValues).not.toBeInTheDocument();
                        // Type into realease field
                        reactTestingLibrary_1.userEvent.type(reactTestingLibrary_1.screen.getByLabelText('Search or add a release'), '1.2.3');
                        // Autocomplete suggests options
                        const autocompleteOptions = reactTestingLibrary_1.screen.getByTestId('option');
                        expect(autocompleteOptions).toBeInTheDocument();
                        expect(autocompleteOptions).toHaveTextContent('1.2.3');
                        // Click on the suggested option
                        reactTestingLibrary_1.userEvent.click(autocompleteOptions);
                        // Button is still disabled
                        const saveRuleButton = reactTestingLibrary_1.screen.getByLabelText('Save Rule');
                        expect(saveRuleButton).toBeInTheDocument();
                        expect(saveRuleButton).toBeDisabled();
                        // Fill sample rate field
                        const sampleRateField = reactTestingLibrary_1.screen.getByPlaceholderText('\u0025');
                        expect(sampleRateField).toBeInTheDocument();
                        reactTestingLibrary_1.userEvent.type(sampleRateField, '20');
                        // Save button is now enabled
                        const saveRuleButtonEnabled = reactTestingLibrary_1.screen.getByLabelText('Save Rule');
                        expect(saveRuleButtonEnabled).toBeEnabled();
                        // Click on save button
                        reactTestingLibrary_1.userEvent.click(saveRuleButtonEnabled);
                        // Modal will close
                        yield (0, reactTestingLibrary_1.waitForElementToBeRemoved)(() => reactTestingLibrary_1.screen.getByText('Add Transaction Sampling Rule'));
                        // Transaction rules panel is updated
                        expect(reactTestingLibrary_1.screen.queryByText('There are no transaction rules to display')).not.toBeInTheDocument();
                        const transactionTraceRules = reactTestingLibrary_1.screen.getByText('Transaction traces');
                        expect(transactionTraceRules).toBeInTheDocument();
                        expect(reactTestingLibrary_1.screen.getByText('Release')).toBeInTheDocument();
                        expect(reactTestingLibrary_1.screen.getByText('1.2.3')).toBeInTheDocument();
                        expect(reactTestingLibrary_1.screen.getByText('20%')).toBeInTheDocument();
                    });
                });
                describe('individual transaction', function () {
                    it('release', function () {
                        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                            MockApiClient.addMockResponse({
                                url: '/projects/org-slug/project-slug/',
                                method: 'PUT',
                                body: TestStubs.Project({
                                    dynamicSampling: {
                                        rules: [
                                            {
                                                sampleRate: 0.2,
                                                type: 'transaction',
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
                                                id: 41,
                                            },
                                        ],
                                        next_id: 40,
                                    },
                                }),
                            });
                            MockApiClient.addMockResponse({
                                url: '/organizations/org-slug/tags/release/values/',
                                method: 'GET',
                                body: [{ value: '1.2.3' }],
                            });
                            (0, utils_3.renderComponent)();
                            // Open Modal
                            yield (0, utils_3.renderModal)(reactTestingLibrary_1.screen.getByText('Add transaction rule'));
                            // Unchecked tracing checkbox
                            reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByRole('checkbox'));
                            // Click on 'Add condition'
                            reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByText('Add Condition'));
                            // Condition Options
                            const conditionOptions = reactTestingLibrary_1.screen.getAllByTestId('condition');
                            // Click on the first condition option
                            reactTestingLibrary_1.userEvent.click(conditionOptions[0]);
                            // Release Field
                            expect(reactTestingLibrary_1.screen.getByTestId('autocomplete-release')).toBeInTheDocument();
                            // Release field is empty
                            const releaseFieldValues = reactTestingLibrary_1.screen.queryByTestId('multivalue');
                            expect(releaseFieldValues).not.toBeInTheDocument();
                            // Type into realease field
                            reactTestingLibrary_1.userEvent.type(reactTestingLibrary_1.screen.getByLabelText('Search or add a release'), '1.2.3');
                            // Autocomplete suggests options
                            const autocompleteOptions = reactTestingLibrary_1.screen.getByTestId('option');
                            expect(autocompleteOptions).toBeInTheDocument();
                            expect(autocompleteOptions).toHaveTextContent('1.2.3');
                            // Click on the suggested option
                            reactTestingLibrary_1.userEvent.click(autocompleteOptions);
                            // Button is still disabled
                            const saveRuleButton = reactTestingLibrary_1.screen.getByLabelText('Save Rule');
                            expect(saveRuleButton).toBeInTheDocument();
                            expect(saveRuleButton).toBeDisabled();
                            // Fill sample rate field
                            const sampleRateField = reactTestingLibrary_1.screen.getByPlaceholderText('\u0025');
                            expect(sampleRateField).toBeInTheDocument();
                            reactTestingLibrary_1.userEvent.type(sampleRateField, '20');
                            // Save button is now enabled
                            const saveRuleButtonEnabled = reactTestingLibrary_1.screen.getByLabelText('Save Rule');
                            expect(saveRuleButtonEnabled).toBeEnabled();
                            // Click on save button
                            reactTestingLibrary_1.userEvent.click(saveRuleButtonEnabled);
                            // Modal will close
                            yield (0, reactTestingLibrary_1.waitForElementToBeRemoved)(() => reactTestingLibrary_1.screen.getByText('Add Transaction Sampling Rule'));
                            // Transaction rules panel is updated
                            expect(reactTestingLibrary_1.screen.queryByText('There are no transaction rules to display')).not.toBeInTheDocument();
                            const individualTransactionRules = reactTestingLibrary_1.screen.getByText('Individual transactions');
                            expect(individualTransactionRules).toBeInTheDocument();
                            expect(reactTestingLibrary_1.screen.getByText('Release')).toBeInTheDocument();
                            expect(reactTestingLibrary_1.screen.getByText('1.2.3')).toBeInTheDocument();
                            expect(reactTestingLibrary_1.screen.getByText('20%')).toBeInTheDocument();
                        });
                    });
                    it('legacy browser', function () {
                        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                            MockApiClient.addMockResponse({
                                url: '/projects/org-slug/project-slug/',
                                method: 'PUT',
                                body: TestStubs.Project({
                                    dynamicSampling: {
                                        rules: [
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
                                        next_id: 40,
                                    },
                                }),
                            });
                            (0, utils_3.renderComponent)();
                            // Open Modal
                            yield (0, utils_3.renderModal)(reactTestingLibrary_1.screen.getByText('Add transaction rule'));
                            const checkedCheckbox = reactTestingLibrary_1.screen.getByRole('checkbox');
                            // Checked tracing checkbox
                            expect(checkedCheckbox).toBeChecked();
                            // Uncheck tracing checkbox
                            reactTestingLibrary_1.userEvent.click(checkedCheckbox);
                            // Unched tracing checkbox
                            expect(checkedCheckbox).not.toBeChecked();
                            // Click on 'Add condition'
                            reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByText('Add Condition'));
                            // Condition Options
                            const conditionOptions = reactTestingLibrary_1.screen.getAllByTestId('condition');
                            // Click on the seventh condition option
                            reactTestingLibrary_1.userEvent.click(conditionOptions[6]);
                            // Legacy Browsers
                            expect(reactTestingLibrary_1.screen.getByText('All browsers')).toBeInTheDocument();
                            const legacyBrowsers = Object.keys(utils_2.LEGACY_BROWSER_LIST);
                            for (const legacyBrowser of legacyBrowsers) {
                                const { icon, title } = utils_2.LEGACY_BROWSER_LIST[legacyBrowser];
                                expect(reactTestingLibrary_1.screen.getByText(title)).toBeInTheDocument();
                                expect(reactTestingLibrary_1.screen.getAllByTestId(`icon-${icon}`)[0]).toBeInTheDocument();
                            }
                            expect(reactTestingLibrary_1.screen.getAllByTestId('icon-internet-explorer')).toHaveLength(4);
                            expect(reactTestingLibrary_1.screen.getAllByTestId('icon-opera')).toHaveLength(2);
                            expect(reactTestingLibrary_1.screen.getByTestId('icon-safari')).toBeInTheDocument();
                            expect(reactTestingLibrary_1.screen.getByTestId('icon-android')).toBeInTheDocument();
                            const switchButtons = reactTestingLibrary_1.screen.getAllByTestId('switch');
                            expect(switchButtons).toHaveLength(legacyBrowsers.length + 1);
                            // All browsers are unchecked
                            for (const switchButton of switchButtons) {
                                expect(switchButton).not.toBeChecked();
                            }
                            // Click on the switch of 'All browsers' option
                            reactTestingLibrary_1.userEvent.click(switchButtons[0]);
                            // All browsers are now checked
                            for (const switchButton of switchButtons) {
                                expect(switchButton).toBeChecked();
                            }
                            // Button is still disabled
                            const saveRuleButton = reactTestingLibrary_1.screen.getByLabelText('Save Rule');
                            expect(saveRuleButton).toBeInTheDocument();
                            expect(saveRuleButton).toBeDisabled();
                            // Fill sample rate field
                            const sampleRateField = reactTestingLibrary_1.screen.getByPlaceholderText('\u0025');
                            expect(sampleRateField).toBeInTheDocument();
                            reactTestingLibrary_1.userEvent.type(sampleRateField, '20');
                            // Save button is now enabled
                            const saveRuleButtonEnabled = reactTestingLibrary_1.screen.getByLabelText('Save Rule');
                            expect(saveRuleButtonEnabled).toBeEnabled();
                            // Click on save button
                            reactTestingLibrary_1.userEvent.click(saveRuleButtonEnabled);
                            // Modal will close
                            yield (0, reactTestingLibrary_1.waitForElementToBeRemoved)(() => reactTestingLibrary_1.screen.getByText('Add Transaction Sampling Rule'));
                            // Transaction rules panel is updated
                            expect(reactTestingLibrary_1.screen.queryByText('There are no transaction rules to display')).not.toBeInTheDocument();
                            const individualTransactionRules = reactTestingLibrary_1.screen.getByText('Individual transactions');
                            expect(individualTransactionRules).toBeInTheDocument();
                            expect(reactTestingLibrary_1.screen.getByText('Legacy Browser')).toBeInTheDocument();
                            for (const legacyBrowser of legacyBrowsers) {
                                const { title } = utils_2.LEGACY_BROWSER_LIST[legacyBrowser];
                                expect(reactTestingLibrary_1.screen.getByText(title)).toBeInTheDocument();
                            }
                            expect(reactTestingLibrary_1.screen.getByText('20%')).toBeInTheDocument();
                        });
                    });
                });
            });
        });
    });
    describe('individual transaction rule', function () {
        it('renders', function () {
            return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                MockApiClient.addMockResponse({
                    url: '/projects/org-slug/project-slug/',
                    method: 'GET',
                    body: TestStubs.Project({
                        dynamicSampling: {
                            rules: [
                                {
                                    sampleRate: 0.1,
                                    type: 'error',
                                    condition: {
                                        op: 'and',
                                        inner: [
                                            {
                                                op: 'glob',
                                                name: 'event.release',
                                                value: ['1*'],
                                            },
                                        ],
                                    },
                                    id: 39,
                                },
                                {
                                    sampleRate: 0.2,
                                    type: 'transaction',
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
                                    id: 40,
                                },
                            ],
                            next_id: 43,
                        },
                    }),
                });
                MockApiClient.addMockResponse({
                    url: '/projects/org-slug/project-slug/',
                    method: 'PUT',
                    body: TestStubs.Project({
                        dynamicSampling: {
                            rules: [
                                {
                                    sampleRate: 0.1,
                                    type: 'error',
                                    condition: {
                                        op: 'and',
                                        inner: [
                                            {
                                                op: 'glob',
                                                name: 'event.release',
                                                value: ['1*'],
                                            },
                                        ],
                                    },
                                    id: 44,
                                },
                                {
                                    sampleRate: 0.6,
                                    type: 'transaction',
                                    condition: {
                                        op: 'and',
                                        inner: [
                                            {
                                                op: 'glob',
                                                name: 'event.release',
                                                value: ['[0-9]'],
                                            },
                                        ],
                                    },
                                    id: 45,
                                },
                            ],
                            next_id: 43,
                        },
                    }),
                });
                MockApiClient.addMockResponse({
                    url: '/organizations/org-slug/tags/release/values/',
                    method: 'GET',
                    body: [{ value: '[0-9]' }],
                });
                (0, utils_3.renderComponent)();
                // Error rules container
                expect(reactTestingLibrary_1.screen.queryByText('There are no error rules to display')).not.toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByText('Errors only')).toBeInTheDocument();
                // Transaction traces and individual transactions rules container
                expect(reactTestingLibrary_1.screen.queryByText('There are no transaction rules to display')).not.toBeInTheDocument();
                const transactionTraceRules = reactTestingLibrary_1.screen.getByText('Individual transactions');
                expect(transactionTraceRules).toBeInTheDocument();
                const editRuleButtons = reactTestingLibrary_1.screen.getAllByLabelText('Edit Rule');
                expect(editRuleButtons).toHaveLength(2);
                // Open rule modal - edit transaction rule
                yield (0, utils_3.renderModal)(editRuleButtons[1]);
                // Modal content
                expect(reactTestingLibrary_1.screen.getByText('Edit Transaction Sampling Rule')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByText('Tracing')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByRole('checkbox')).not.toBeChecked();
                // Release Field
                expect(reactTestingLibrary_1.screen.getByTestId('autocomplete-release')).toBeInTheDocument();
                // Release field is not empty
                expect(reactTestingLibrary_1.screen.getByTestId('multivalue')).toBeInTheDocument();
                // Button is enabled - meaning the form is valid
                const saveRuleButton = reactTestingLibrary_1.screen.getByLabelText('Save Rule');
                expect(saveRuleButton).toBeInTheDocument();
                expect(saveRuleButton).toBeEnabled();
                // Sample rate field
                const sampleRateField = reactTestingLibrary_1.screen.getByPlaceholderText('\u0025');
                expect(sampleRateField).toBeInTheDocument();
                // Sample rate is not empty
                expect(sampleRateField).toHaveValue(20);
                // Clear release field
                reactTestingLibrary_1.userEvent.clear(reactTestingLibrary_1.screen.getByLabelText('Search or add a release'));
                // Release field is now empty
                const newReleaseFieldValues = reactTestingLibrary_1.screen.queryByTestId('multivalue');
                expect(newReleaseFieldValues).not.toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByLabelText('Save Rule')).toBeDisabled();
                // Type into realease field
                reactTestingLibrary_1.userEvent.type(reactTestingLibrary_1.screen.getByLabelText('Search or add a release'), '[0-9]');
                // Autocomplete suggests options
                const autocompleteOptions = reactTestingLibrary_1.screen.getByTestId('option');
                expect(autocompleteOptions).toBeInTheDocument();
                expect(autocompleteOptions).toHaveTextContent('[0-9]');
                // Click on the suggested option
                reactTestingLibrary_1.userEvent.click(autocompleteOptions);
                expect(reactTestingLibrary_1.screen.getByLabelText('Save Rule')).toBeEnabled();
                // Clear sample rate field
                reactTestingLibrary_1.userEvent.clear(sampleRateField);
                expect(reactTestingLibrary_1.screen.getByLabelText('Save Rule')).toBeDisabled();
                // Update sample rate field
                reactTestingLibrary_1.userEvent.type(sampleRateField, '60');
                // Save button is now enabled
                const saveRuleButtonEnabled = reactTestingLibrary_1.screen.getByLabelText('Save Rule');
                expect(saveRuleButtonEnabled).toBeEnabled();
                // Click on save button
                reactTestingLibrary_1.userEvent.click(saveRuleButtonEnabled);
                // Modal will close
                yield (0, reactTestingLibrary_1.waitForElementToBeRemoved)(() => reactTestingLibrary_1.screen.getByText('Edit Transaction Sampling Rule'));
                // Error rules panel is updated
                expect(reactTestingLibrary_1.screen.getByText('Errors only')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByText('Individual transactions')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getAllByText('Release')).toHaveLength(2);
                // Old values
                expect(reactTestingLibrary_1.screen.queryByText('1.2.3')).not.toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.queryByText('20%')).not.toBeInTheDocument();
                // New values
                expect(reactTestingLibrary_1.screen.getByText('[0-9]')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByText('60%')).toBeInTheDocument();
            });
        });
    });
});
//# sourceMappingURL=transactions.spec.jsx.map