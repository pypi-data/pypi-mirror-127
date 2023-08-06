Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const gridEditable_1 = (0, tslib_1.__importStar)(require("app/components/gridEditable"));
const sortLink_1 = (0, tslib_1.__importDefault)(require("app/components/gridEditable/sortLink"));
const link_1 = (0, tslib_1.__importDefault)(require("app/components/links/link"));
const tooltip_1 = (0, tslib_1.__importDefault)(require("app/components/tooltip"));
const locale_1 = require("app/locale");
const utils_1 = require("app/utils");
const fieldRenderers_1 = require("app/utils/discover/fieldRenderers");
const fields_1 = require("app/utils/discover/fields");
const formatters_1 = require("app/utils/formatters");
const utils_2 = require("../../utils");
const styles_1 = require("./styles");
const types_1 = require("./types");
const utils_3 = require("./utils");
const SPANS_TABLE_COLUMN_ORDER = [
    {
        key: 'id',
        name: 'Example Transaction',
        width: gridEditable_1.COL_WIDTH_UNDEFINED,
    },
    {
        key: 'timestamp',
        name: 'Timestamp',
        width: gridEditable_1.COL_WIDTH_UNDEFINED,
    },
    {
        key: 'spanDuration',
        name: 'Span Duration',
        width: gridEditable_1.COL_WIDTH_UNDEFINED,
    },
    {
        key: 'occurrences',
        name: 'Occurrences',
        width: gridEditable_1.COL_WIDTH_UNDEFINED,
    },
    {
        key: 'cumulativeDuration',
        name: 'Cumulative Duration',
        width: gridEditable_1.COL_WIDTH_UNDEFINED,
    },
];
const SPANS_TABLE_COLUMN_TYPE = {
    id: 'string',
    timestamp: 'date',
    spanDuration: 'duration',
    occurrences: 'integer',
    cumulativeDuration: 'duration',
};
function SuspectSpanEntry(props) {
    const { location, organization, suspectSpan, generateTransactionLink, eventView, totals, } = props;
    const examples = suspectSpan.examples.map(example => ({
        id: example.id,
        project: suspectSpan.project,
        // timestamps are in seconds but want them in milliseconds
        timestamp: example.finishTimestamp * 1000,
        transactionDuration: (example.finishTimestamp - example.startTimestamp) * 1000,
        spanDuration: example.nonOverlappingExclusiveTime,
        occurrences: example.spans.length,
        cumulativeDuration: example.spans.reduce((duration, span) => duration + span.exclusiveTime, 0),
        spans: example.spans,
    }));
    const sort = (0, utils_3.getSuspectSpanSortFromEventView)(eventView);
    return (<div data-test-id="suspect-card">
      <styles_1.UpperPanel data-test-id="suspect-card-upper">
        <styles_1.HeaderItem label={(0, locale_1.t)('Span Operation')} value={<SpanLabel span={suspectSpan}/>} align="left"/>
        <PercentileDuration sort={sort} suspectSpan={suspectSpan} totals={totals}/>
        <SpanCount sort={sort} suspectSpan={suspectSpan} totals={totals}/>
        <TotalCumulativeDuration sort={sort} suspectSpan={suspectSpan} totals={totals}/>
      </styles_1.UpperPanel>
      <styles_1.LowerPanel data-test-id="suspect-card-lower">
        <gridEditable_1.default data={examples} columnOrder={SPANS_TABLE_COLUMN_ORDER} columnSortBy={[]} grid={{
            renderHeadCell,
            renderBodyCell: renderBodyCellWithMeta(location, organization, generateTransactionLink, suspectSpan),
        }} location={location}/>
      </styles_1.LowerPanel>
    </div>);
}
exports.default = SuspectSpanEntry;
const PERCENTILE_LABELS = {
    [types_1.SpanSortPercentiles.P50_EXCLUSIVE_TIME]: (0, locale_1.t)('p50 Duration'),
    [types_1.SpanSortPercentiles.P75_EXCLUSIVE_TIME]: (0, locale_1.t)('p75 Duration'),
    [types_1.SpanSortPercentiles.P95_EXCLUSIVE_TIME]: (0, locale_1.t)('p95 Duration'),
    [types_1.SpanSortPercentiles.P99_EXCLUSIVE_TIME]: (0, locale_1.t)('p99 Duration'),
};
function PercentileDuration(props) {
    const { sort, suspectSpan } = props;
    const sortKey = PERCENTILE_LABELS.hasOwnProperty(sort.field)
        ? sort.field
        : types_1.SpanSortPercentiles.P75_EXCLUSIVE_TIME;
    return (<styles_1.HeaderItem label={PERCENTILE_LABELS[sortKey]} value={<utils_2.PerformanceDuration abbreviation milliseconds={suspectSpan[sortKey]}/>} align="right" isSortKey={sort.field === sortKey}/>);
}
function SpanCount(props) {
    const { sort, suspectSpan, totals } = props;
    if (sort.field === types_1.SpanSortOthers.COUNT) {
        return (<styles_1.HeaderItem label={(0, locale_1.t)('Occurrences')} value={String(suspectSpan.count)} align="right" isSortKey/>);
    }
    // Because the frequency is computed using `count_unique(id)` internally,
    // it is an approximate value. This means that it has the potential to be
    // greater than `totals.count` when it shouldn't. So let's clip the
    // frequency value to make sure we don't see values over 100%.
    const frequency = (0, utils_1.defined)(totals === null || totals === void 0 ? void 0 : totals.count)
        ? Math.min(suspectSpan.frequency, totals.count)
        : suspectSpan.frequency;
    const value = (0, utils_1.defined)(totals === null || totals === void 0 ? void 0 : totals.count) ? (<tooltip_1.default title={(0, locale_1.tct)('[frequency] out of [total] transactions contain this span', {
            frequency,
            total: totals.count,
        })}>
      <span>{(0, formatters_1.formatPercentage)(frequency / totals.count)}</span>
    </tooltip_1.default>) : (String(suspectSpan.count));
    return <styles_1.HeaderItem label={(0, locale_1.t)('Frequency')} value={value} align="right"/>;
}
function TotalCumulativeDuration(props) {
    const { sort, suspectSpan, totals } = props;
    let value = (<utils_2.PerformanceDuration abbreviation milliseconds={suspectSpan.sumExclusiveTime}/>);
    if ((0, utils_1.defined)(totals === null || totals === void 0 ? void 0 : totals.sum_transaction_duration)) {
        value = (<tooltip_1.default title={(0, locale_1.tct)('[percentage] of the total transaction duration of [duration]', {
                percentage: (0, formatters_1.formatPercentage)(suspectSpan.sumExclusiveTime / totals.sum_transaction_duration),
                duration: (<utils_2.PerformanceDuration abbreviation milliseconds={totals.sum_transaction_duration}/>),
            })}>
        {value}
      </tooltip_1.default>);
    }
    return (<styles_1.HeaderItem label={(0, locale_1.t)('Total Cumulative Duration')} value={value} align="right" isSortKey={sort.field === types_1.SpanSortOthers.SUM_EXCLUSIVE_TIME}/>);
}
function renderHeadCell(column, _index) {
    const align = (0, fields_1.fieldAlignment)(column.key, SPANS_TABLE_COLUMN_TYPE[column.key]);
    return (<sortLink_1.default title={column.name} align={align} direction={undefined} canSort={false} generateSortLink={() => undefined}/>);
}
function renderBodyCellWithMeta(location, organization, generateTransactionLink, suspectSpan) {
    return (column, dataRow) => {
        // if the transaction duration is falsey, then just render the span duration on its own
        if (column.key === 'spanDuration' && dataRow.transactionDuration) {
            return (<styles_1.SpanDurationBar spanOp={suspectSpan.op} spanDuration={dataRow.spanDuration} transactionDuration={dataRow.transactionDuration}/>);
        }
        const fieldRenderer = (0, fieldRenderers_1.getFieldRenderer)(column.key, SPANS_TABLE_COLUMN_TYPE);
        let rendered = fieldRenderer(dataRow, { location, organization });
        if (column.key === 'id') {
            const worstSpan = dataRow.spans.length
                ? dataRow.spans.reduce((worst, span) => worst.exclusiveTime >= span.exclusiveTime ? worst : span)
                : null;
            const hash = worstSpan ? `#span-${worstSpan.id}` : undefined;
            const target = generateTransactionLink(organization, dataRow, location.query, hash);
            rendered = <link_1.default to={target}>{rendered}</link_1.default>;
        }
        return rendered;
    };
}
function SpanLabel(props) {
    var _a, _b;
    const { span } = props;
    const example = span.examples.find(ex => (0, utils_1.defined)(ex.description));
    return (<tooltip_1.default title={`${span.op} - ${(_a = example === null || example === void 0 ? void 0 : example.description) !== null && _a !== void 0 ? _a : (0, locale_1.t)('n/a')}`}>
      <styles_1.SpanLabelContainer>
        <span>{span.op}</span> - {(_b = example === null || example === void 0 ? void 0 : example.description) !== null && _b !== void 0 ? _b : styles_1.emptyValue}
      </styles_1.SpanLabelContainer>
    </tooltip_1.default>);
}
//# sourceMappingURL=suspectSpanCard.jsx.map