Object.defineProperty(exports, "__esModule", { value: true });
exports.getAllByTextContent = exports.getByTextContent = void 0;
const reactTestingLibrary_1 = require("sentry-test/reactTestingLibrary");
// Taken from https://stackoverflow.com/a/56859650/1015027
function findTextWithMarkup(contentNode, textMatch) {
    const hasText = (node) => node.textContent === textMatch;
    const nodeHasText = hasText(contentNode);
    const childrenDontHaveText = Array.from((contentNode === null || contentNode === void 0 ? void 0 : contentNode.children) || []).every(child => !hasText(child));
    return nodeHasText && childrenDontHaveText;
}
/**
 * Search for a text broken up by multiple html elements
 * e.g.: <div>Hello <span>world</span></div>
 */
function getByTextContent(textMatch) {
    return reactTestingLibrary_1.screen.getByText((_, contentNode) => findTextWithMarkup(contentNode, textMatch));
}
exports.getByTextContent = getByTextContent;
/**
 * Search for *all* texts broken up by multiple html elements
 * e.g.: <div><div>Hello <span>world</span></div><div>Hello <span>world</span></div></div>
 */
function getAllByTextContent(textMatch) {
    return reactTestingLibrary_1.screen.getAllByText((_, contentNode) => findTextWithMarkup(contentNode, textMatch));
}
exports.getAllByTextContent = getAllByTextContent;
//# sourceMappingURL=utils.jsx.map