Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const reactTestingLibrary_1 = require("sentry-test/reactTestingLibrary");
const alertBadge_1 = (0, tslib_1.__importDefault)(require("app/views/alerts/alertBadge"));
const types_1 = require("app/views/alerts/types");
describe('AlertBadge', () => {
    it('displays status', () => {
        (0, reactTestingLibrary_1.mountWithTheme)(<alertBadge_1.default status={types_1.IncidentStatus.CLOSED}/>);
        expect(reactTestingLibrary_1.screen.getByText('Resolved')).toBeInTheDocument();
    });
    it('hides status text', () => {
        (0, reactTestingLibrary_1.mountWithTheme)(<alertBadge_1.default hideText status={types_1.IncidentStatus.CLOSED}/>);
        expect(reactTestingLibrary_1.screen.queryByText('Resolved')).not.toBeInTheDocument();
    });
    it('can be an issue badge', () => {
        (0, reactTestingLibrary_1.mountWithTheme)(<alertBadge_1.default isIssue/>);
        expect(reactTestingLibrary_1.screen.getByText('Issue')).toBeInTheDocument();
    });
});
//# sourceMappingURL=alertBadge.spec.jsx.map