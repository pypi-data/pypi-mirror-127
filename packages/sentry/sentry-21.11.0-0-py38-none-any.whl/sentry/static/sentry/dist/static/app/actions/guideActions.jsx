Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const reflux_1 = (0, tslib_1.__importDefault)(require("reflux"));
const GuideActions = reflux_1.default.createActions([
    'closeGuide',
    'fetchSucceeded',
    'nextStep',
    'toStep',
    'registerAnchor',
    'unregisterAnchor',
]);
exports.default = GuideActions;
//# sourceMappingURL=guideActions.jsx.map