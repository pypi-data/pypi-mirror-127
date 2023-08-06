Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const React = (0, tslib_1.__importStar)(require("react"));
const getDisplayName_1 = (0, tslib_1.__importDefault)(require("app/utils/getDisplayName"));
const useProjects_1 = (0, tslib_1.__importDefault)(require("app/utils/useProjects"));
/**
 * Higher order component that uses ProjectsStore and provides a list of projects
 */
function withProjects(WrappedComponent) {
    const Wrapper = props => {
        const { projects, loadingProjects } = (0, useProjects_1.default)();
        return <WrappedComponent {...props} {...{ projects, loadingProjects }}/>;
    };
    Wrapper.displayName = `withProjects(${(0, getDisplayName_1.default)(WrappedComponent)})`;
    return Wrapper;
}
exports.default = withProjects;
//# sourceMappingURL=withProjects.jsx.map