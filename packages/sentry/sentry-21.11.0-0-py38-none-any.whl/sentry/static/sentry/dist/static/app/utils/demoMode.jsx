Object.defineProperty(exports, "__esModule", { value: true });
exports.urlAttachQueryParams = exports.extraQueryParameterWithEmail = exports.extraQueryParameter = void 0;
const tslib_1 = require("tslib");
const getCookie_1 = (0, tslib_1.__importDefault)(require("app/utils/getCookie"));
function extraQueryParameter() {
    var _a;
    // cookies that have = sign are quotes so extra quotes need to be removed
    const extraQueryString = ((_a = (0, getCookie_1.default)('extra_query_string')) === null || _a === void 0 ? void 0 : _a.replaceAll('"', '')) || '';
    const extraQuery = new URLSearchParams(extraQueryString);
    return extraQuery;
}
exports.extraQueryParameter = extraQueryParameter;
function extraQueryParameterWithEmail() {
    const params = extraQueryParameter();
    const email = localStorage.getItem('email');
    if (email) {
        params.append('email', email);
    }
    return params;
}
exports.extraQueryParameterWithEmail = extraQueryParameterWithEmail;
function urlAttachQueryParams(url, params) {
    const queryString = params.toString();
    if (queryString) {
        return url + '?' + queryString;
    }
    return url;
}
exports.urlAttachQueryParams = urlAttachQueryParams;
//# sourceMappingURL=demoMode.jsx.map