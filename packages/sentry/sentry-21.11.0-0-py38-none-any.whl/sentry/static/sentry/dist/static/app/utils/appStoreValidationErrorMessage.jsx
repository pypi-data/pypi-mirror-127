Object.defineProperty(exports, "__esModule", { value: true });
exports.getAppStoreValidationErrorMessage = exports.unexpectedErrorMessage = void 0;
const tslib_1 = require("tslib");
const Sentry = (0, tslib_1.__importStar)(require("@sentry/react"));
const link_1 = (0, tslib_1.__importDefault)(require("app/components/links/link"));
const locale_1 = require("app/locale");
exports.unexpectedErrorMessage = (0, locale_1.t)('An unexpected error occurred while configuring the App Store Connect integration');
function getAppStoreValidationErrorMessage(error, repo) {
    switch (error.code) {
        case 'app-connect-authentication-error':
            return repo
                ? (0, locale_1.tct)('App Store Connect credentials are invalid or missing. [linkToCustomRepository]', {
                    linkToCustomRepository: (<link_1.default to={repo.link}>
                  {(0, locale_1.tct)("Make sure the credentials of the '[customRepositoryName]' repository are correct and exist.", {
                            customRepositoryName: repo.name,
                        })}
                </link_1.default>),
                })
                : (0, locale_1.t)('The supplied App Store Connect credentials are invalid or missing.');
        case 'app-connect-forbidden-error':
            return (0, locale_1.t)('The supplied API key does not have sufficient permissions.');
        case 'app-connect-multiple-sources-error':
            return (0, locale_1.t)('Only one App Store Connect application is allowed in this project.');
        default: {
            // this shall not happen
            Sentry.captureException(new Error('Unknown app store connect error.'));
            return exports.unexpectedErrorMessage;
        }
    }
}
exports.getAppStoreValidationErrorMessage = getAppStoreValidationErrorMessage;
//# sourceMappingURL=appStoreValidationErrorMessage.jsx.map