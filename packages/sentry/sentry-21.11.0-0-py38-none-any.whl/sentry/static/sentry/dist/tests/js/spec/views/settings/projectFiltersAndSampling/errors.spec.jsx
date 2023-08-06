Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const reactTestingLibrary_1 = require("sentry-test/reactTestingLibrary");
const utils_1 = require("./utils");
describe('Filters and Sampling - Error rule', function () {
    it('edit rule', function () {
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
                                sampleRate: 0.5,
                                type: 'error',
                                condition: {
                                    op: 'and',
                                    inner: [
                                        {
                                            op: 'glob',
                                            name: 'event.release',
                                            value: ['[I3].[0-9]'],
                                        },
                                    ],
                                },
                                id: 44,
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
                url: '/organizations/org-slug/tags/release/values/',
                method: 'GET',
                body: [{ value: '[I3].[0-9]' }],
            });
            (0, utils_1.renderComponent)();
            // Error rules container
            expect(reactTestingLibrary_1.screen.queryByText('There are no error rules to display')).not.toBeInTheDocument();
            expect(reactTestingLibrary_1.screen.getByText('Errors only')).toBeInTheDocument();
            // Transaction traces and individual transactions rules container
            expect(reactTestingLibrary_1.screen.queryByText('There are no transaction rules to display')).not.toBeInTheDocument();
            expect(reactTestingLibrary_1.screen.getByText('Transaction traces')).toBeInTheDocument();
            const editRuleButtons = reactTestingLibrary_1.screen.getAllByLabelText('Edit Rule');
            expect(editRuleButtons).toHaveLength(2);
            // Open rule modal - edit error rule
            yield (0, utils_1.renderModal)(editRuleButtons[0]);
            // Modal content
            expect(reactTestingLibrary_1.screen.getByText('Edit Error Sampling Rule')).toBeInTheDocument();
            expect(reactTestingLibrary_1.screen.queryByText('Tracing')).not.toBeInTheDocument();
            // Release Field
            expect(reactTestingLibrary_1.screen.getByTestId('autocomplete-release')).toBeInTheDocument();
            // Release field is not empty
            const releaseFieldValues = reactTestingLibrary_1.screen.getByTestId('multivalue');
            expect(releaseFieldValues).toBeInTheDocument();
            expect(releaseFieldValues).toHaveTextContent('1*');
            // Button is enabled - meaning the form is valid
            const saveRuleButton = reactTestingLibrary_1.screen.getByLabelText('Save Rule');
            expect(saveRuleButton).toBeInTheDocument();
            expect(saveRuleButton).toBeEnabled();
            // Sample rate field
            const sampleRateField = reactTestingLibrary_1.screen.getByPlaceholderText('\u0025');
            expect(sampleRateField).toBeInTheDocument();
            // Sample rate is not empty
            expect(sampleRateField).toHaveValue(10);
            // Clear release field
            reactTestingLibrary_1.userEvent.clear(reactTestingLibrary_1.screen.getByLabelText('Search or add a release'));
            // Release field is now empty
            expect(reactTestingLibrary_1.screen.queryByTestId('multivalue')).not.toBeInTheDocument();
            expect(reactTestingLibrary_1.screen.getByLabelText('Save Rule')).toBeDisabled();
            // Type into realease field
            reactTestingLibrary_1.userEvent.type(reactTestingLibrary_1.screen.getByLabelText('Search or add a release'), '[I3]');
            // Autocomplete suggests options
            const autocompleteOptions = reactTestingLibrary_1.screen.getByTestId('option');
            expect(autocompleteOptions).toBeInTheDocument();
            expect(autocompleteOptions).toHaveTextContent('[I3].[0-9]');
            // Click on the suggested option
            reactTestingLibrary_1.userEvent.click(autocompleteOptions);
            expect(reactTestingLibrary_1.screen.getByLabelText('Save Rule')).toBeEnabled();
            // Clear sample rate field
            reactTestingLibrary_1.userEvent.clear(sampleRateField);
            expect(reactTestingLibrary_1.screen.getByLabelText('Save Rule')).toBeDisabled();
            // Update sample rate field
            reactTestingLibrary_1.userEvent.type(sampleRateField, '50');
            // Save button is now enabled
            const saveRuleButtonEnabled = reactTestingLibrary_1.screen.getByLabelText('Save Rule');
            expect(saveRuleButtonEnabled).toBeEnabled();
            // Click on save button
            reactTestingLibrary_1.userEvent.click(saveRuleButtonEnabled);
            // Modal will close
            yield (0, reactTestingLibrary_1.waitForElementToBeRemoved)(() => reactTestingLibrary_1.screen.getByText('Edit Error Sampling Rule'));
            // Error rules panel is updated
            expect(reactTestingLibrary_1.screen.getByText('Errors only')).toBeInTheDocument();
            expect(reactTestingLibrary_1.screen.getAllByText('Release')).toHaveLength(2);
            // Old values
            expect(reactTestingLibrary_1.screen.queryByText('1*')).not.toBeInTheDocument();
            expect(reactTestingLibrary_1.screen.queryByText('10%')).not.toBeInTheDocument();
            // New values
            expect(reactTestingLibrary_1.screen.getByText('[I3].[0-9]')).toBeInTheDocument();
            expect(reactTestingLibrary_1.screen.getByText('50%')).toBeInTheDocument();
        });
    });
    it('delete rule', function () {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
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
            (0, utils_1.renderComponent)();
            // Error rules container
            expect(reactTestingLibrary_1.screen.queryByText('There are no error rules to display')).not.toBeInTheDocument();
            expect(reactTestingLibrary_1.screen.getByText('Errors only')).toBeInTheDocument();
            // Transaction traces and individual transactions rules container
            expect(reactTestingLibrary_1.screen.queryByText('There are no transaction rules to display')).not.toBeInTheDocument();
            const transactionTraceRules = reactTestingLibrary_1.screen.getByText('Transaction traces');
            expect(transactionTraceRules).toBeInTheDocument();
            const deleteRuleButtons = reactTestingLibrary_1.screen.getAllByLabelText('Delete Rule');
            expect(deleteRuleButtons).toHaveLength(2);
            // Open deletion confirmation modal - delete error rule
            yield (0, utils_1.renderModal)(deleteRuleButtons[0]);
            expect(reactTestingLibrary_1.screen.getByText('Are you sure you wish to delete this dynamic sampling rule?')).toBeInTheDocument();
            expect(reactTestingLibrary_1.screen.getByText('Confirm')).toBeInTheDocument();
            // Confirm deletion
            reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByText('Confirm'));
            // Confirmation modal will close
            yield (0, reactTestingLibrary_1.waitForElementToBeRemoved)(() => reactTestingLibrary_1.screen.getByText('Are you sure you wish to delete this dynamic sampling rule?'));
            // Error rules panel is updated
            expect(reactTestingLibrary_1.screen.getByText('There are no error rules to display')).toBeInTheDocument();
            // There is still one transaction rule
            expect(transactionTraceRules).toBeInTheDocument();
        });
    });
    describe('modal', function () {
        MockApiClient.addMockResponse({
            url: '/projects/org-slug/project-slug/',
            method: 'GET',
            body: TestStubs.Project(),
        });
        it('renders modal', function () {
            return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                (0, utils_1.renderComponent)();
                // Open Modal
                yield (0, utils_1.renderModal)(reactTestingLibrary_1.screen.getByText('Add error rule'), true);
                // Modal content
                expect(reactTestingLibrary_1.screen.getByText('Add Error Sampling Rule')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.queryByText('Tracing')).not.toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByText('Add Condition')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByText('Apply sampling rate to all errors')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByText('Sampling Rate \u0025')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByPlaceholderText('\u0025')).toHaveValue(null);
                expect(reactTestingLibrary_1.screen.getByLabelText('Cancel')).toBeInTheDocument();
                const saveRuleButton = reactTestingLibrary_1.screen.getByLabelText('Save Rule');
                expect(saveRuleButton).toBeInTheDocument();
                expect(saveRuleButton).toBeDisabled();
                // Close Modal
                reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByLabelText('Close Modal'));
                yield (0, reactTestingLibrary_1.waitForElementToBeRemoved)(() => reactTestingLibrary_1.screen.getByText('Add Error Sampling Rule'));
            });
        });
        it('condition options', function () {
            return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                (0, utils_1.renderComponent)();
                // Open Modal
                yield (0, utils_1.renderModal)(reactTestingLibrary_1.screen.getByText('Add error rule'));
                // Click on 'Add condition'
                reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByText('Add Condition'));
                // Autocomplete
                expect(reactTestingLibrary_1.screen.getByTestId('autocomplete-list')).toBeInTheDocument();
                // Condition Options
                const conditionOptions = reactTestingLibrary_1.screen.getAllByTestId('condition');
                expect(conditionOptions).toHaveLength(utils_1.commonConditionCategories.length);
                for (const conditionOptionIndex in conditionOptions) {
                    expect(conditionOptions[conditionOptionIndex]).toHaveTextContent(utils_1.commonConditionCategories[conditionOptionIndex]);
                }
                // Close Modal
                reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByLabelText('Close Modal'));
                yield (0, reactTestingLibrary_1.waitForElementToBeRemoved)(() => reactTestingLibrary_1.screen.getByText('Add Error Sampling Rule'));
            });
        });
        it('save rule', function () {
            return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                MockApiClient.addMockResponse({
                    url: '/projects/org-slug/project-slug/',
                    method: 'PUT',
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
                (0, utils_1.renderComponent)();
                // Open Modal
                yield (0, utils_1.renderModal)(reactTestingLibrary_1.screen.getByText('Add error rule'));
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
                expect(reactTestingLibrary_1.screen.queryByTestId('multivalue')).not.toBeInTheDocument();
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
                yield (0, reactTestingLibrary_1.waitForElementToBeRemoved)(() => reactTestingLibrary_1.screen.getByText('Add Error Sampling Rule'));
                // Error rules panel is updated
                expect(reactTestingLibrary_1.screen.queryByText('There are no error rules to display')).not.toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByText('Errors only')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByText('Release')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByText('1.2.3')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByText('20%')).toBeInTheDocument();
            });
        });
    });
});
//# sourceMappingURL=errors.spec.jsx.map