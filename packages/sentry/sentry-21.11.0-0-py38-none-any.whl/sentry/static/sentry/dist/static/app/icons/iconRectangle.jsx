Object.defineProperty(exports, "__esModule", { value: true });
exports.IconRectangle = void 0;
const tslib_1 = require("tslib");
const React = (0, tslib_1.__importStar)(require("react"));
const svgIcon_1 = (0, tslib_1.__importDefault)(require("./svgIcon"));
const IconRectangle = React.forwardRef(function IconRectangle(props, ref) {
    return (<svgIcon_1.default {...props} ref={ref}>
      <rect x="6.38721" y="0.341797" width="9.03286" height="9.03286" rx="1.5" transform="rotate(45 6.38721 0.341797)"/>
    </svgIcon_1.default>);
});
exports.IconRectangle = IconRectangle;
IconRectangle.displayName = 'IconRectangle';
//# sourceMappingURL=iconRectangle.jsx.map