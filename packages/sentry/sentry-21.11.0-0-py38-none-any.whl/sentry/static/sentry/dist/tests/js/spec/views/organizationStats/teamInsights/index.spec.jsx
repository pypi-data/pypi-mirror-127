Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const reactTestingLibrary_1 = require("sentry-test/reactTestingLibrary");
const projectsStore_1 = (0, tslib_1.__importDefault)(require("app/stores/projectsStore"));
const teamInsights_1 = (0, tslib_1.__importDefault)(require("app/views/organizationStats/teamInsights"));
describe('TeamInsightsContainer', () => {
    afterEach(() => {
        projectsStore_1.default.reset();
    });
    it('blocks access if org is missing flag', () => {
        const organization = TestStubs.Organization();
        const context = TestStubs.routerContext([{ organization }]);
        (0, reactTestingLibrary_1.mountWithTheme)(<teamInsights_1.default organization={organization}>
        <div>test</div>
      </teamInsights_1.default>, { context });
        expect(reactTestingLibrary_1.screen.queryByText('test')).not.toBeInTheDocument();
    });
    it('allows access for orgs with flag', () => {
        projectsStore_1.default.loadInitialData([TestStubs.Project()]);
        const organization = TestStubs.Organization({ features: ['team-insights'] });
        const context = TestStubs.routerContext([{ organization }]);
        (0, reactTestingLibrary_1.mountWithTheme)(<teamInsights_1.default organization={organization}>
        <div>test</div>
      </teamInsights_1.default>, { context });
        expect(reactTestingLibrary_1.screen.getByText('test')).toBeInTheDocument();
    });
    it('shows message for users with no teams', () => {
        projectsStore_1.default.loadInitialData([]);
        const organization = TestStubs.Organization({ features: ['team-insights'] });
        const context = TestStubs.routerContext([{ organization }]);
        (0, reactTestingLibrary_1.mountWithTheme)(<teamInsights_1.default organization={organization}/>, { context });
        expect(reactTestingLibrary_1.screen.getByText('You need at least one project to use this view')).toBeInTheDocument();
    });
});
//# sourceMappingURL=index.spec.jsx.map