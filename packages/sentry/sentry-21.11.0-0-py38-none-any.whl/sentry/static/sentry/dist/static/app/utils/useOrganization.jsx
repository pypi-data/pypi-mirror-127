Object.defineProperty(exports, "__esModule", { value: true });
const react_1 = require("react");
const organizationContext_1 = require("app/views/organizationContext");
function useOrganization() {
    const organization = (0, react_1.useContext)(organizationContext_1.OrganizationContext);
    if (!organization) {
        throw new Error('useOrganization called but organization is not set.');
    }
    return organization;
}
exports.default = useOrganization;
//# sourceMappingURL=useOrganization.jsx.map