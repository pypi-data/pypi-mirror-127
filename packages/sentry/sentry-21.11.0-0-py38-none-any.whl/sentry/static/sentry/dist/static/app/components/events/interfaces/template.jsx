Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const locale_1 = require("app/locale");
const eventDataSection_1 = (0, tslib_1.__importDefault)(require("../../events/eventDataSection"));
const line_1 = (0, tslib_1.__importDefault)(require("./frame/line"));
const TemplateInterface = ({ type, data, event }) => (<eventDataSection_1.default type={type} title={(0, locale_1.t)('Template')}>
    <div className="traceback no-exception">
      <ul>
        <line_1.default data={data} event={event} registers={{}} components={[]} isExpanded/>
      </ul>
    </div>
  </eventDataSection_1.default>);
exports.default = TemplateInterface;
//# sourceMappingURL=template.jsx.map