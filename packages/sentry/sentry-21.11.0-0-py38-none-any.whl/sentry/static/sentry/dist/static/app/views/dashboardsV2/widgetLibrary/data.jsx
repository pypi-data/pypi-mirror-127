Object.defineProperty(exports, "__esModule", { value: true });
exports.DEFAULT_WIDGETS = void 0;
const locale_1 = require("app/locale");
const types_1 = require("../types");
exports.DEFAULT_WIDGETS = [
    {
        id: undefined,
        title: (0, locale_1.t)('Total Errors'),
        displayType: types_1.DisplayType.BIG_NUMBER,
        interval: '5m',
        queries: [
            {
                name: '',
                conditions: '!event.type:transaction',
                fields: ['count()'],
                orderby: '',
            },
        ],
    },
    {
        id: undefined,
        title: (0, locale_1.t)('All Events'),
        displayType: types_1.DisplayType.AREA,
        interval: '5m',
        queries: [
            {
                name: '',
                conditions: '!event.type:transaction',
                fields: ['count()'],
                orderby: '',
            },
        ],
    },
    {
        id: undefined,
        title: (0, locale_1.t)('Affected Users'),
        displayType: types_1.DisplayType.LINE,
        interval: '5m',
        queries: [
            {
                name: 'Known Users',
                conditions: 'has:user.email !event.type:transaction',
                fields: ['count_unique(user)'],
                orderby: '',
            },
            {
                name: 'Anonymous Users',
                conditions: '!has:user.email !event.type:transaction',
                fields: ['count_unique(user)'],
                orderby: '',
            },
        ],
    },
    {
        id: undefined,
        title: (0, locale_1.t)('Handled vs. Unhandled'),
        displayType: types_1.DisplayType.LINE,
        interval: '5m',
        queries: [
            {
                name: 'Handled',
                conditions: 'error.handled:true',
                fields: ['count()'],
                orderby: '',
            },
            {
                name: 'Unhandled',
                conditions: 'error.handled:false',
                fields: ['count()'],
                orderby: '',
            },
        ],
    },
    {
        id: undefined,
        title: (0, locale_1.t)('Errors by Country'),
        displayType: types_1.DisplayType.WORLD_MAP,
        interval: '5m',
        queries: [
            {
                name: 'Error counts',
                conditions: '!event.type:transaction has:geo.country_code',
                fields: ['count()'],
                orderby: '',
            },
        ],
    },
    {
        id: undefined,
        title: (0, locale_1.t)('Errors by Browser'),
        displayType: types_1.DisplayType.TABLE,
        interval: '5m',
        queries: [
            {
                name: '',
                conditions: '!event.type:transaction has:browser.name',
                fields: ['browser.name', 'count()'],
                orderby: '-count',
            },
        ],
    },
];
//# sourceMappingURL=data.jsx.map