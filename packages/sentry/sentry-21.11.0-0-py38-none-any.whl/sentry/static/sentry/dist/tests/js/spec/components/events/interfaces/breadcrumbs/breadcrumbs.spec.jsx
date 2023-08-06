Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const initializeOrg_1 = require("sentry-test/initializeOrg");
const reactTestingLibrary_1 = require("sentry-test/reactTestingLibrary");
const utils_1 = require("sentry-test/utils");
const breadcrumbs_1 = (0, tslib_1.__importDefault)(require("app/components/events/interfaces/breadcrumbs"));
const breadcrumbs_2 = require("app/types/breadcrumbs");
const event_1 = require("app/types/event");
describe('Breadcrumbs', () => {
    let props;
    const { router } = (0, initializeOrg_1.initializeOrg)();
    beforeEach(() => {
        props = {
            route: {},
            router,
            organization: TestStubs.Organization(),
            event: TestStubs.Event({ entries: [] }),
            type: event_1.EntryType.BREADCRUMBS,
            data: {
                values: [
                    {
                        message: 'sup',
                        category: 'default',
                        level: breadcrumbs_2.BreadcrumbLevelType.WARNING,
                        type: breadcrumbs_2.BreadcrumbType.INFO,
                    },
                    {
                        message: 'hey',
                        category: 'error',
                        level: breadcrumbs_2.BreadcrumbLevelType.INFO,
                        type: breadcrumbs_2.BreadcrumbType.INFO,
                    },
                    {
                        message: 'hello',
                        category: 'default',
                        level: breadcrumbs_2.BreadcrumbLevelType.WARNING,
                        type: breadcrumbs_2.BreadcrumbType.INFO,
                    },
                    {
                        message: 'bye',
                        category: 'default',
                        level: breadcrumbs_2.BreadcrumbLevelType.WARNING,
                        type: breadcrumbs_2.BreadcrumbType.INFO,
                    },
                    {
                        message: 'ok',
                        category: 'error',
                        level: breadcrumbs_2.BreadcrumbLevelType.WARNING,
                        type: breadcrumbs_2.BreadcrumbType.INFO,
                    },
                    {
                        message: 'sup',
                        category: 'default',
                        level: breadcrumbs_2.BreadcrumbLevelType.WARNING,
                        type: breadcrumbs_2.BreadcrumbType.INFO,
                    },
                    {
                        message: 'sup',
                        category: 'default',
                        level: breadcrumbs_2.BreadcrumbLevelType.INFO,
                        type: breadcrumbs_2.BreadcrumbType.INFO,
                    },
                ],
            },
        };
    });
    describe('filterCrumbs', function () {
        it('should filter crumbs based on crumb message', function () {
            return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                (0, reactTestingLibrary_1.mountWithTheme)(<breadcrumbs_1.default {...props}/>);
                reactTestingLibrary_1.userEvent.type(reactTestingLibrary_1.screen.getByPlaceholderText('Search breadcrumbs'), 'hi');
                expect(yield reactTestingLibrary_1.screen.findByText('Sorry, no breadcrumbs match your search query')).toBeInTheDocument();
                reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByLabelText('Clear'));
                reactTestingLibrary_1.userEvent.type(reactTestingLibrary_1.screen.getByPlaceholderText('Search breadcrumbs'), 'up');
                expect(reactTestingLibrary_1.screen.queryByText('Sorry, no breadcrumbs match your search query')).not.toBeInTheDocument();
                expect((0, utils_1.getAllByTextContent)('sup')).toHaveLength(3);
            });
        });
        it('should filter crumbs based on crumb level', function () {
            (0, reactTestingLibrary_1.mountWithTheme)(<breadcrumbs_1.default {...props}/>);
            reactTestingLibrary_1.userEvent.type(reactTestingLibrary_1.screen.getByPlaceholderText('Search breadcrumbs'), 'war');
            // breadcrumbs + filter item
            // TODO(Priscila): Filter should not render in the dom if not open
            expect((0, utils_1.getAllByTextContent)('Warning')).toHaveLength(6);
        });
        it('should filter crumbs based on crumb category', function () {
            (0, reactTestingLibrary_1.mountWithTheme)(<breadcrumbs_1.default {...props}/>);
            reactTestingLibrary_1.userEvent.type(reactTestingLibrary_1.screen.getByPlaceholderText('Search breadcrumbs'), 'error');
            expect((0, utils_1.getAllByTextContent)('error')).toHaveLength(2);
        });
    });
    describe('render', function () {
        it('should display the correct number of crumbs with no filter', function () {
            props.data.values = props.data.values.slice(0, 4);
            (0, reactTestingLibrary_1.mountWithTheme)(<breadcrumbs_1.default {...props}/>);
            // data.values + virtual crumb
            expect(reactTestingLibrary_1.screen.getAllByTestId('crumb')).toHaveLength(4);
            expect(reactTestingLibrary_1.screen.getByTestId('last-crumb')).toBeInTheDocument();
        });
        it('should display the correct number of crumbs with a filter', function () {
            props.data.values = props.data.values.slice(0, 4);
            (0, reactTestingLibrary_1.mountWithTheme)(<breadcrumbs_1.default {...props}/>);
            const searchInput = reactTestingLibrary_1.screen.getByPlaceholderText('Search breadcrumbs');
            reactTestingLibrary_1.userEvent.type(searchInput, 'sup');
            expect(reactTestingLibrary_1.screen.queryByTestId('crumb')).not.toBeInTheDocument();
            expect(reactTestingLibrary_1.screen.getByTestId('last-crumb')).toBeInTheDocument();
        });
        it('should not crash if data contains a toString attribute', function () {
            // Regression test: A "toString" property in data should not falsely be
            // used to coerce breadcrumb data to string. This would cause a TypeError.
            const data = { nested: { toString: 'hello' } };
            props.data.values = [
                {
                    message: 'sup',
                    category: 'default',
                    level: breadcrumbs_2.BreadcrumbLevelType.INFO,
                    type: breadcrumbs_2.BreadcrumbType.INFO,
                    data,
                },
            ];
            (0, reactTestingLibrary_1.mountWithTheme)(<breadcrumbs_1.default {...props}/>);
            // data.values + virtual crumb
            expect(reactTestingLibrary_1.screen.getByTestId('crumb')).toBeInTheDocument();
            expect(reactTestingLibrary_1.screen.getByTestId('last-crumb')).toBeInTheDocument();
        });
    });
});
//# sourceMappingURL=breadcrumbs.spec.jsx.map