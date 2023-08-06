Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const projectsStore_1 = (0, tslib_1.__importDefault)(require("app/stores/projectsStore"));
const useLegacyStore_1 = require("app/stores/useLegacyStore");
/**
 * Provides projects from the ProjectStore
 */
function useProjects() {
    const { projects, loading } = (0, useLegacyStore_1.useLegacyStore)(projectsStore_1.default);
    return { projects, loadingProjects: loading };
}
exports.default = useProjects;
//# sourceMappingURL=useProjects.jsx.map