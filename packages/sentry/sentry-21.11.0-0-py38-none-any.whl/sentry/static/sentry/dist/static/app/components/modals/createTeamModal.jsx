Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = require("react");
const teams_1 = require("app/actionCreators/teams");
const createTeamForm_1 = (0, tslib_1.__importDefault)(require("app/components/teams/createTeamForm"));
const locale_1 = require("app/locale");
const useApi_1 = (0, tslib_1.__importDefault)(require("app/utils/useApi"));
function CreateTeamModal(_a) {
    var { Body, Header } = _a, props = (0, tslib_1.__rest)(_a, ["Body", "Header"]);
    const { onClose, closeModal, organization } = props;
    const api = (0, useApi_1.default)();
    function handleSubmit(data, onSuccess, onError) {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            try {
                const team = yield (0, teams_1.createTeam)(api, data, { orgId: organization.slug });
                closeModal();
                onClose === null || onClose === void 0 ? void 0 : onClose(team);
                onSuccess(team);
            }
            catch (err) {
                onError(err);
            }
        });
    }
    return (<react_1.Fragment>
      <Header closeButton>{(0, locale_1.t)('Create Team')}</Header>
      <Body>
        <createTeamForm_1.default {...props} onSubmit={handleSubmit}/>
      </Body>
    </react_1.Fragment>);
}
exports.default = CreateTeamModal;
//# sourceMappingURL=createTeamModal.jsx.map