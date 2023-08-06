Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const enzyme_1 = require("sentry-test/enzyme");
const initializeOrg_1 = require("sentry-test/initializeOrg");
const widgetQueryFields_1 = (0, tslib_1.__importDefault)(require("app/components/dashboards/widgetQueryFields"));
const types_1 = require("app/views/dashboardsV2/types");
const types_2 = require("app/views/eventsV2/table/types");
describe('BaseChart', function () {
    const { routerContext } = (0, initializeOrg_1.initializeOrg)();
    const organization = TestStubs.Organization();
    let wrapper;
    beforeEach(() => {
        wrapper = (0, enzyme_1.mountWithTheme)(<widgetQueryFields_1.default displayType={types_1.DisplayType.TOP_N} fieldOptions={{
                'function:count': {
                    label: 'count()',
                    value: {
                        kind: types_2.FieldValueKind.FUNCTION,
                        meta: {
                            name: 'count',
                            parameters: [],
                        },
                    },
                },
                'field:title': {
                    label: 'title',
                    value: {
                        kind: types_2.FieldValueKind.FIELD,
                        meta: {
                            name: 'title',
                            dataType: 'string',
                        },
                    },
                },
                'function:p95': {
                    label: 'p95(…)',
                    value: {
                        kind: types_2.FieldValueKind.FUNCTION,
                        meta: {
                            name: 'p95',
                            parameters: [],
                        },
                    },
                },
            }} fields={[
                {
                    kind: 'field',
                    field: 'title',
                },
                {
                    kind: 'function',
                    function: ['count', '', undefined, undefined],
                },
                {
                    kind: 'function',
                    function: ['p95', 'transaction.duration', undefined, undefined],
                },
            ]} organization={organization} onChange={() => undefined}/>, routerContext);
    });
    it('renders with grey dotted previous period when using only a single series', function () {
        const columns = wrapper.find('StyledColumnEditCollection').find('QueryField');
        expect(columns.length).toEqual(2);
        expect(columns.at(0).props().fieldValue).toEqual({
            kind: 'field',
            field: 'title',
        });
        expect(columns.at(1).props().fieldValue).toEqual({
            kind: 'function',
            function: ['count', '', undefined, undefined],
        });
        expect(wrapper.find('QueryFieldWrapper').find('QueryField').props().fieldValue).toEqual({
            function: ['p95', 'transaction.duration', undefined, undefined],
            kind: 'function',
        });
    });
});
//# sourceMappingURL=widgetQueryFields.spec.jsx.map