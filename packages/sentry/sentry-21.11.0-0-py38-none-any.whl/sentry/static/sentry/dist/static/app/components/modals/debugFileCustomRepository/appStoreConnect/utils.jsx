Object.defineProperty(exports, "__esModule", { value: true });
exports.getAppStoreErrorMessage = void 0;
const tslib_1 = require("tslib");
const Sentry = (0, tslib_1.__importStar)(require("@sentry/react"));
const locale_1 = require("app/locale");
const appStoreValidationErrorMessage_1 = require("app/utils/appStoreValidationErrorMessage");
// since translations are done on the front-end we need to map  back-end error messages to front-end messages
const fieldErrorMessageMapping = {
    appconnectIssuer: {
        issuer: {
            'Ensure this field has at least 36 characters.': (0, locale_1.t)('This field should be exactly 36 characters.'),
            'Ensure this field has no more than 36 characters.': (0, locale_1.t)('This field should be exactly 36 characters.'),
        },
    },
    appconnectKey: {
        keyId: {
            'Ensure this field has at least 2 characters.': (0, locale_1.t)('This field should be between 2 and 20 characters.'),
            'Ensure this field has no more than 20 characters.': (0, locale_1.t)('This field should be between 2 and 20 characters.'),
        },
    },
};
function getAppStoreErrorMessage(error) {
    var _a;
    if (typeof error === 'string') {
        return error;
    }
    const detailedErrorResponse = (_a = error.responseJSON) === null || _a === void 0 ? void 0 : _a.detail;
    if (detailedErrorResponse) {
        return (0, appStoreValidationErrorMessage_1.getAppStoreValidationErrorMessage)(detailedErrorResponse);
    }
    const errorResponse = error.responseJSON;
    if (!errorResponse) {
        return appStoreValidationErrorMessage_1.unexpectedErrorMessage;
    }
    return Object.keys(errorResponse).reduce((acc, serverSideField) => {
        var _a;
        const fieldErrorMessage = (_a = fieldErrorMessageMapping[serverSideField]) !== null && _a !== void 0 ? _a : {};
        const field = Object.keys(fieldErrorMessage)[0];
        const errorMessages = errorResponse[serverSideField].map(errorMessage => {
            if (fieldErrorMessage[field][errorMessage]) {
                return fieldErrorMessage[field][errorMessage];
            }
            // This will be difficult to happen,
            // but if it happens we will be able to see which message is not being mapped on the fron-tend
            Sentry.withScope(scope => {
                scope.setExtra('serverSideField', serverSideField);
                scope.setExtra('message', errorMessage);
                Sentry.captureException(new Error('App Store Connect - Untranslated error message'));
            });
            return errorMessage;
        });
        // the UI only displays one error message at a time
        return Object.assign(Object.assign({}, acc), { [field]: errorMessages[0] });
    }, {});
}
exports.getAppStoreErrorMessage = getAppStoreErrorMessage;
//# sourceMappingURL=utils.jsx.map