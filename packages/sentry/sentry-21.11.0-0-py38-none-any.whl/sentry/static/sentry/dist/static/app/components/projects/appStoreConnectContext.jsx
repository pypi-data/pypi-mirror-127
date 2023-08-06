Object.defineProperty(exports, "__esModule", { value: true });
exports.Provider = void 0;
const tslib_1 = require("tslib");
const react_1 = require("react");
const appStoreValidationErrorMessage_1 = require("app/utils/appStoreValidationErrorMessage");
const useApi_1 = (0, tslib_1.__importDefault)(require("app/utils/useApi"));
const AppStoreConnectContext = (0, react_1.createContext)(undefined);
const Provider = ({ children, project, organization }) => {
    const api = (0, useApi_1.default)();
    const [projectDetails, setProjectDetails] = (0, react_1.useState)();
    const [appStoreConnectStatusData, setAppStoreConnectStatusData] = (0, react_1.useState)(undefined);
    const orgSlug = organization.slug;
    const appStoreConnectSymbolSources = ((projectDetails === null || projectDetails === void 0 ? void 0 : projectDetails.symbolSources) ? JSON.parse(projectDetails.symbolSources) : []).reduce((acc, _a) => {
        var { type, id } = _a, symbolSource = (0, tslib_1.__rest)(_a, ["type", "id"]);
        if (type.toLowerCase() === 'appstoreconnect') {
            acc[id] = Object.assign({ type }, symbolSource);
        }
        return acc;
    }, {});
    (0, react_1.useEffect)(() => {
        fetchProjectDetails();
    }, [project]);
    (0, react_1.useEffect)(() => {
        fetchAppStoreConnectStatusData();
    }, [projectDetails]);
    function fetchProjectDetails() {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            if (!project || projectDetails) {
                return;
            }
            if (project.symbolSources) {
                setProjectDetails(project);
                return;
            }
            try {
                const response = yield api.requestPromise(`/projects/${orgSlug}/${project.slug}/`);
                setProjectDetails(response);
            }
            catch (_a) {
                // do nothing
            }
        });
    }
    function fetchAppStoreConnectStatusData() {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            if (!projectDetails) {
                return;
            }
            if (!Object.keys(appStoreConnectSymbolSources).length) {
                return;
            }
            try {
                const response = yield api.requestPromise(`/projects/${orgSlug}/${projectDetails.slug}/appstoreconnect/status/`);
                setAppStoreConnectStatusData(response);
            }
            catch (_a) {
                // do nothing
            }
        });
    }
    function getUpdateAlertMessage(respository, credentials) {
        if ((credentials === null || credentials === void 0 ? void 0 : credentials.status) === 'valid') {
            return undefined;
        }
        return (0, appStoreValidationErrorMessage_1.getAppStoreValidationErrorMessage)(credentials, respository);
    }
    return (<AppStoreConnectContext.Provider value={appStoreConnectStatusData && project
            ? Object.keys(appStoreConnectStatusData).reduce((acc, key) => {
                const appStoreConnect = appStoreConnectStatusData[key];
                return Object.assign(Object.assign({}, acc), { [key]: Object.assign(Object.assign({}, appStoreConnect), { updateAlertMessage: getUpdateAlertMessage({
                            name: appStoreConnectSymbolSources[key].name,
                            link: `/settings/${organization.slug}/projects/${project.slug}/debug-symbols/?customRepository=${key}`,
                        }, appStoreConnect.credentials) }) });
            }, {})
            : undefined}>
      {children}
    </AppStoreConnectContext.Provider>);
};
exports.Provider = Provider;
exports.default = AppStoreConnectContext;
//# sourceMappingURL=appStoreConnectContext.jsx.map