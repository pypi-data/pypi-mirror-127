Object.defineProperty(exports, "__esModule", { value: true });
exports.Client = exports.initApiClientErrorHandling = exports.Request = void 0;
const tslib_1 = require("tslib");
const isEqual_1 = (0, tslib_1.__importDefault)(require("lodash/isEqual"));
const RealApi = jest.requireActual('app/api');
class Request {
}
exports.Request = Request;
exports.initApiClientErrorHandling = RealApi.initApiClientErrorHandling;
const respond = (isAsync, fn, ...args) => {
    if (!fn) {
        return;
    }
    if (isAsync) {
        setTimeout(() => fn(...args), 1);
        return;
    }
    fn(...args);
};
/**
 * Compare two records. `want` is all the entries we want to have the same value in `check`
 */
function compareRecord(want, check) {
    for (const entry of Object.entries(want)) {
        const [key, value] = entry;
        if (!(0, isEqual_1.default)(check[key], value)) {
            return false;
        }
    }
    return true;
}
class Client {
    constructor() {
        this.activeRequests = {};
        this.baseUrl = '';
        this.handleRequestError = RealApi.Client.prototype.handleRequestError;
    }
    static clearMockResponses() {
        Client.mockResponses = [];
    }
    /**
     * Create a query string match callable.
     *
     * Only keys/values defined in `query` are checked.
     */
    static matchQuery(query) {
        const queryMatcher = (_url, options) => {
            var _a;
            return compareRecord(query, (_a = options.query) !== null && _a !== void 0 ? _a : {});
        };
        return queryMatcher;
    }
    /**
     * Create a data match callable.
     *
     * Only keys/values defined in `data` are checked.
     */
    static matchData(data) {
        const dataMatcher = (_url, options) => {
            var _a;
            return compareRecord(data, (_a = options.data) !== null && _a !== void 0 ? _a : {});
        };
        return dataMatcher;
    }
    // Returns a jest mock that represents Client.request calls
    static addMockResponse(response, options) {
        var _a;
        const mock = jest.fn();
        // Convert predicate into a matcher for backwards compatibility
        if (options === null || options === void 0 ? void 0 : options.predicate) {
            if (!response.match) {
                response.match = [];
            }
            response.match.push(options.predicate);
        }
        Client.mockResponses.unshift([
            Object.assign(Object.assign({ url: '', status: 200, statusCode: 200, statusText: 'OK', responseText: '', responseJSON: '', body: '', method: 'GET', callCount: 0, match: [] }, response), { headers: (_a = response.headers) !== null && _a !== void 0 ? _a : {}, getResponseHeader: (key) => { var _a, _b; return (_b = (_a = response.headers) === null || _a === void 0 ? void 0 : _a[key]) !== null && _b !== void 0 ? _b : null; } }),
            mock,
        ]);
        return mock;
    }
    static findMockResponse(url, options) {
        return Client.mockResponses.find(([response]) => {
            if (url !== response.url) {
                return false;
            }
            if ((options.method || 'GET') !== response.method) {
                return false;
            }
            return response.match.every(matcher => matcher(url, options));
        });
    }
    uniqueId() {
        return '123';
    }
    /**
     * In the real client, this clears in-flight responses. It's NOT
     * clearMockResponses. You probably don't want to call this from a test.
     */
    clear() { }
    wrapCallback(_id, func, _cleanup = false) {
        return (...args) => {
            // @ts-expect-error
            if (RealApi.hasProjectBeenRenamed(...args)) {
                return;
            }
            respond(Client.mockAsync, func, ...args);
        };
    }
    requestPromise(path, _a = {}) {
        var { includeAllArgs } = _a, options = (0, tslib_1.__rest)(_a, ["includeAllArgs"]);
        return new Promise((resolve, reject) => {
            this.request(path, Object.assign(Object.assign({}, options), { success: (data, ...args) => {
                    includeAllArgs ? resolve([data, ...args]) : resolve(data);
                }, error: (error, ..._args) => {
                    reject(error);
                } }));
        });
    }
    // XXX(ts): We type the return type for requestPromise and request as `any`. Typically these woul
    request(url, options = {}) {
        var _a, _b;
        const [response, mock] = Client.findMockResponse(url, options) || [
            undefined,
            undefined,
        ];
        if (!response || !mock) {
            // Endpoints need to be mocked
            const err = new Error(`No mocked response found for request: ${options.method || 'GET'} ${url}`);
            // Mutate stack to drop frames since test file so that we know where in the test
            // this needs to be mocked
            const lines = (_a = err.stack) === null || _a === void 0 ? void 0 : _a.split('\n');
            const startIndex = lines === null || lines === void 0 ? void 0 : lines.findIndex(line => line.includes('tests/js/spec'));
            err.stack = ['\n', lines === null || lines === void 0 ? void 0 : lines[0], ...((_b = lines === null || lines === void 0 ? void 0 : lines.slice(startIndex)) !== null && _b !== void 0 ? _b : [])].join('\n');
            // Throwing an error here does not do what we want it to do....
            // Because we are mocking an API client, we generally catch errors to show
            // user-friendly error messages, this means in tests this error gets gobbled
            // up and developer frustration ensues. Use `setTimeout` to get around this
            setTimeout(() => {
                throw err;
            });
        }
        else {
            // has mocked response
            // mock gets returned when we add a mock response, will represent calls to api.request
            mock(url, options);
            const body = typeof response.body === 'function' ? response.body(url, options) : response.body;
            if (![200, 202].includes(response.statusCode)) {
                response.callCount++;
                const errorResponse = Object.assign({
                    status: response.statusCode,
                    responseText: JSON.stringify(body),
                    responseJSON: body,
                }, {
                    overrideMimeType: () => { },
                    abort: () => { },
                    then: () => { },
                    error: () => { },
                }, new XMLHttpRequest());
                this.handleRequestError({
                    id: '1234',
                    path: url,
                    requestOptions: options,
                }, errorResponse, 'error', 'error');
            }
            else {
                response.callCount++;
                respond(Client.mockAsync, options.success, body, {}, {
                    getResponseHeader: (key) => response.headers[key],
                    statusCode: response.statusCode,
                    status: response.statusCode,
                });
            }
        }
        respond(Client.mockAsync, options.complete);
    }
}
exports.Client = Client;
Client.mockResponses = [];
Client.mockAsync = false;
//# sourceMappingURL=api.jsx.map