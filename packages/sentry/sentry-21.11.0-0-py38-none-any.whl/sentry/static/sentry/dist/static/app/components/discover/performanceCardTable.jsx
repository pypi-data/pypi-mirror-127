Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = require("react");
const React = (0, tslib_1.__importStar)(require("react"));
const react_router_1 = require("react-router");
const react_2 = require("@emotion/react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const alert_1 = (0, tslib_1.__importDefault)(require("app/components/alert"));
const loadingIndicator_1 = (0, tslib_1.__importDefault)(require("app/components/loadingIndicator"));
const notAvailable_1 = (0, tslib_1.__importDefault)(require("app/components/notAvailable"));
const panels_1 = require("app/components/panels");
const panelTable_1 = (0, tslib_1.__importDefault)(require("app/components/panels/panelTable"));
const icons_1 = require("app/icons");
const locale_1 = require("app/locale");
const overflowEllipsis_1 = (0, tslib_1.__importDefault)(require("app/styles/overflowEllipsis"));
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const discoverQuery_1 = (0, tslib_1.__importDefault)(require("app/utils/discover/discoverQuery"));
const fieldRenderers_1 = require("app/utils/discover/fieldRenderers");
const fields_1 = require("app/utils/discover/fields");
const constants_1 = require("app/utils/performance/vitals/constants");
const utils_1 = require("app/views/performance/utils");
function PerformanceCardTable({ organization, location, project, releaseEventView, allReleasesTableData, thisReleaseTableData, performanceType, isLoading, }) {
    const miseryRenderer = (allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.meta) &&
        (0, fieldRenderers_1.getFieldRenderer)('user_misery', allReleasesTableData.meta);
    function renderChange(allReleasesScore, thisReleaseScore, meta) {
        if (allReleasesScore === undefined || thisReleaseScore === undefined) {
            return <StyledNotAvailable />;
        }
        const trend = allReleasesScore - thisReleaseScore;
        const trendSeconds = trend >= 1000 ? trend / 1000 : trend;
        const trendPercentage = (allReleasesScore - thisReleaseScore) * 100;
        const valPercentage = Math.round(Math.abs(trendPercentage));
        const val = Math.abs(trendSeconds).toFixed(2);
        if (trend === 0) {
            return <SubText>{`0${meta === 'duration' ? 'ms' : '%'}`}</SubText>;
        }
        return (<TrendText color={trend >= 0 ? 'success' : 'error'}>
        {`${meta === 'duration' ? val : valPercentage}${meta === 'duration' ? (trend >= 1000 ? 's' : 'ms') : '%'}`}
        <StyledIconArrow color={trend >= 0 ? 'success' : 'error'} direction={trend >= 0 ? 'down' : 'up'} size="xs"/>
      </TrendText>);
    }
    function userMiseryTrend() {
        var _a, _b, _c, _d;
        const allReleasesUserMisery = (_b = (_a = allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.data) === null || _a === void 0 ? void 0 : _a[0]) === null || _b === void 0 ? void 0 : _b.user_misery;
        const thisReleaseUserMisery = (_d = (_c = thisReleaseTableData === null || thisReleaseTableData === void 0 ? void 0 : thisReleaseTableData.data) === null || _c === void 0 ? void 0 : _c[0]) === null || _d === void 0 ? void 0 : _d.user_misery;
        return (<StyledPanelItem>
        {renderChange(allReleasesUserMisery, thisReleaseUserMisery, 'number')}
      </StyledPanelItem>);
    }
    function renderFrontendPerformance() {
        const webVitals = [
            { title: fields_1.WebVital.FCP, field: 'p75_measurements_fcp' },
            { title: fields_1.WebVital.FID, field: 'p75_measurements_fid' },
            { title: fields_1.WebVital.LCP, field: 'p75_measurements_lcp' },
            { title: fields_1.WebVital.CLS, field: 'p75_measurements_cls' },
        ];
        const spans = [
            { title: 'HTTP', column: 'p75(spans.http)', field: 'p75_spans_http' },
            { title: 'Browser', column: 'p75(spans.browser)', field: 'p75_spans_browser' },
            { title: 'Resource', column: 'p75(spans.resource)', field: 'p75_spans_resource' },
        ];
        const webVitalTitles = webVitals.map((vital, idx) => {
            const newView = releaseEventView.withColumns([
                { kind: 'field', field: `p75(${vital.title})` },
            ]);
            return (<SubTitle key={idx}>
          <react_router_1.Link to={newView.getResultsViewUrlTarget(organization.slug)}>
            {constants_1.WEB_VITAL_DETAILS[vital.title].name} (
            {constants_1.WEB_VITAL_DETAILS[vital.title].acronym})
          </react_router_1.Link>
        </SubTitle>);
        });
        const spanTitles = spans.map((span, idx) => {
            const newView = releaseEventView.withColumns([
                { kind: 'field', field: `${span.column}` },
            ]);
            return (<SubTitle key={idx}>
          <react_router_1.Link to={newView.getResultsViewUrlTarget(organization.slug)}>
            {(0, locale_1.t)(span.title)}
          </react_router_1.Link>
        </SubTitle>);
        });
        const webVitalsRenderer = webVitals.map(vital => (allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.meta) &&
            (0, fieldRenderers_1.getFieldRenderer)(vital.field, allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.meta));
        const spansRenderer = spans.map(span => (allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.meta) &&
            (0, fieldRenderers_1.getFieldRenderer)(span.field, allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.meta));
        const webReleaseTrend = webVitals.map(vital => {
            var _a, _b, _c, _d, _e, _f;
            return {
                allReleasesRow: {
                    data: (_b = (_a = allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.data) === null || _a === void 0 ? void 0 : _a[0]) === null || _b === void 0 ? void 0 : _b[vital.field],
                    meta: (_c = allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.meta) === null || _c === void 0 ? void 0 : _c[vital.field],
                },
                thisReleaseRow: {
                    data: (_e = (_d = thisReleaseTableData === null || thisReleaseTableData === void 0 ? void 0 : thisReleaseTableData.data) === null || _d === void 0 ? void 0 : _d[0]) === null || _e === void 0 ? void 0 : _e[vital.field],
                    meta: (_f = thisReleaseTableData === null || thisReleaseTableData === void 0 ? void 0 : thisReleaseTableData.meta) === null || _f === void 0 ? void 0 : _f[vital.field],
                },
            };
        });
        const spansReleaseTrend = spans.map(span => {
            var _a, _b, _c, _d, _e, _f;
            return {
                allReleasesRow: {
                    data: (_b = (_a = allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.data) === null || _a === void 0 ? void 0 : _a[0]) === null || _b === void 0 ? void 0 : _b[span.field],
                    meta: (_c = allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.meta) === null || _c === void 0 ? void 0 : _c[span.field],
                },
                thisReleaseRow: {
                    data: (_e = (_d = thisReleaseTableData === null || thisReleaseTableData === void 0 ? void 0 : thisReleaseTableData.data) === null || _d === void 0 ? void 0 : _d[0]) === null || _e === void 0 ? void 0 : _e[span.field],
                    meta: (_f = thisReleaseTableData === null || thisReleaseTableData === void 0 ? void 0 : thisReleaseTableData.meta) === null || _f === void 0 ? void 0 : _f[span.field],
                },
            };
        });
        const emptyColumn = (<div>
        <SingleEmptySubText>
          <StyledNotAvailable tooltip={(0, locale_1.t)('No results found')}/>
        </SingleEmptySubText>
        <StyledPanelItem>
          <TitleSpace />
          {webVitals.map((vital, index) => (<MultipleEmptySubText key={vital[index]}>
              {<StyledNotAvailable tooltip={(0, locale_1.t)('No results found')}/>}
            </MultipleEmptySubText>))}
        </StyledPanelItem>
        <StyledPanelItem>
          <TitleSpace />
          {spans.map((span, index) => (<MultipleEmptySubText key={span[index]}>
              {<StyledNotAvailable tooltip={(0, locale_1.t)('No results found')}/>}
            </MultipleEmptySubText>))}
        </StyledPanelItem>
      </div>);
        return (<react_1.Fragment>
        <div>
          <panels_1.PanelItem>{(0, locale_1.t)('User Misery')}</panels_1.PanelItem>
          <StyledPanelItem>
            <div>{(0, locale_1.t)('Web Vitals')}</div>
            {webVitalTitles}
          </StyledPanelItem>
          <StyledPanelItem>
            <div>{(0, locale_1.t)('Span Operations')}</div>
            {spanTitles}
          </StyledPanelItem>
        </div>
        {(allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.data.length) === 0
                ? emptyColumn
                : allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.data.map((dataRow, idx) => {
                    const allReleasesMisery = miseryRenderer === null || miseryRenderer === void 0 ? void 0 : miseryRenderer(dataRow, {
                        organization,
                        location,
                    });
                    const allReleasesWebVitals = webVitalsRenderer === null || webVitalsRenderer === void 0 ? void 0 : webVitalsRenderer.map(renderer => renderer === null || renderer === void 0 ? void 0 : renderer(dataRow, { organization, location }));
                    const allReleasesSpans = spansRenderer === null || spansRenderer === void 0 ? void 0 : spansRenderer.map(renderer => renderer === null || renderer === void 0 ? void 0 : renderer(dataRow, { organization, location }));
                    return (<div key={idx}>
                  <UserMiseryPanelItem>{allReleasesMisery}</UserMiseryPanelItem>
                  <StyledPanelItem>
                    <TitleSpace />
                    {allReleasesWebVitals.map(webVital => webVital)}
                  </StyledPanelItem>
                  <StyledPanelItem>
                    <TitleSpace />
                    {allReleasesSpans.map(span => span)}
                  </StyledPanelItem>
                </div>);
                })}
        {(thisReleaseTableData === null || thisReleaseTableData === void 0 ? void 0 : thisReleaseTableData.data.length) === 0
                ? emptyColumn
                : thisReleaseTableData === null || thisReleaseTableData === void 0 ? void 0 : thisReleaseTableData.data.map((dataRow, idx) => {
                    const thisReleasesMisery = miseryRenderer === null || miseryRenderer === void 0 ? void 0 : miseryRenderer(dataRow, {
                        organization,
                        location,
                    });
                    const thisReleasesWebVitals = webVitalsRenderer === null || webVitalsRenderer === void 0 ? void 0 : webVitalsRenderer.map(renderer => renderer === null || renderer === void 0 ? void 0 : renderer(dataRow, { organization, location }));
                    const thisReleasesSpans = spansRenderer === null || spansRenderer === void 0 ? void 0 : spansRenderer.map(renderer => renderer === null || renderer === void 0 ? void 0 : renderer(dataRow, { organization, location }));
                    return (<div key={idx}>
                  <div>
                    <UserMiseryPanelItem>{thisReleasesMisery}</UserMiseryPanelItem>
                    <StyledPanelItem>
                      <TitleSpace />
                      {thisReleasesWebVitals.map(webVital => webVital)}
                    </StyledPanelItem>
                    <StyledPanelItem>
                      <TitleSpace />
                      {thisReleasesSpans.map(span => span)}
                    </StyledPanelItem>
                  </div>
                </div>);
                })}
        <div>
          {userMiseryTrend()}
          <StyledPanelItem>
            <TitleSpace />
            {webReleaseTrend === null || webReleaseTrend === void 0 ? void 0 : webReleaseTrend.map(row => {
                var _a, _b, _c;
                return renderChange((_a = row.allReleasesRow) === null || _a === void 0 ? void 0 : _a.data, (_b = row.thisReleaseRow) === null || _b === void 0 ? void 0 : _b.data, (_c = row.allReleasesRow) === null || _c === void 0 ? void 0 : _c.meta);
            })}
          </StyledPanelItem>
          <StyledPanelItem>
            <TitleSpace />
            {spansReleaseTrend === null || spansReleaseTrend === void 0 ? void 0 : spansReleaseTrend.map(row => {
                var _a, _b, _c;
                return renderChange((_a = row.allReleasesRow) === null || _a === void 0 ? void 0 : _a.data, (_b = row.thisReleaseRow) === null || _b === void 0 ? void 0 : _b.data, (_c = row.allReleasesRow) === null || _c === void 0 ? void 0 : _c.meta);
            })}
          </StyledPanelItem>
        </div>
      </react_1.Fragment>);
    }
    function renderBackendPerformance() {
        const spans = [
            { title: 'HTTP', column: 'p75(spans.http)', field: 'p75_spans_http' },
            { title: 'DB', column: 'p75(spans.db)', field: 'p75_spans_db' },
        ];
        const spanTitles = spans.map((span, idx) => {
            const newView = releaseEventView.withColumns([
                { kind: 'field', field: `${span.column}` },
            ]);
            return (<SubTitle key={idx}>
          <react_router_1.Link to={newView.getResultsViewUrlTarget(organization.slug)}>
            {(0, locale_1.t)(span.title)}
          </react_router_1.Link>
        </SubTitle>);
        });
        const apdexRenderer = (allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.meta) && (0, fieldRenderers_1.getFieldRenderer)('apdex', allReleasesTableData.meta);
        const spansRenderer = spans.map(span => (allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.meta) &&
            (0, fieldRenderers_1.getFieldRenderer)(span.field, allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.meta));
        const spansReleaseTrend = spans.map(span => {
            var _a, _b, _c, _d, _e, _f;
            return {
                allReleasesRow: {
                    data: (_b = (_a = allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.data) === null || _a === void 0 ? void 0 : _a[0]) === null || _b === void 0 ? void 0 : _b[span.field],
                    meta: (_c = allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.meta) === null || _c === void 0 ? void 0 : _c[span.field],
                },
                thisReleaseRow: {
                    data: (_e = (_d = thisReleaseTableData === null || thisReleaseTableData === void 0 ? void 0 : thisReleaseTableData.data) === null || _d === void 0 ? void 0 : _d[0]) === null || _e === void 0 ? void 0 : _e[span.field],
                    meta: (_f = thisReleaseTableData === null || thisReleaseTableData === void 0 ? void 0 : thisReleaseTableData.meta) === null || _f === void 0 ? void 0 : _f[span.field],
                },
            };
        });
        function apdexTrend() {
            var _a, _b, _c, _d;
            const allReleasesApdex = (_b = (_a = allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.data) === null || _a === void 0 ? void 0 : _a[0]) === null || _b === void 0 ? void 0 : _b.apdex;
            const thisReleaseApdex = (_d = (_c = thisReleaseTableData === null || thisReleaseTableData === void 0 ? void 0 : thisReleaseTableData.data) === null || _c === void 0 ? void 0 : _c[0]) === null || _d === void 0 ? void 0 : _d.apdex;
            return (<StyledPanelItem>
          {renderChange(allReleasesApdex, thisReleaseApdex, 'string')}
        </StyledPanelItem>);
        }
        const emptyColumn = (<div>
        <SingleEmptySubText>
          <StyledNotAvailable tooltip={(0, locale_1.t)('No results found')}/>
        </SingleEmptySubText>
        <SingleEmptySubText>
          <StyledNotAvailable tooltip={(0, locale_1.t)('No results found')}/>
        </SingleEmptySubText>
        <StyledPanelItem>
          <TitleSpace />
          {spans.map((span, index) => (<MultipleEmptySubText key={span[index]}>
              {<StyledNotAvailable tooltip={(0, locale_1.t)('No results found')}/>}
            </MultipleEmptySubText>))}
        </StyledPanelItem>
      </div>);
        return (<react_1.Fragment>
        <div>
          <panels_1.PanelItem>{(0, locale_1.t)('User Misery')}</panels_1.PanelItem>
          <StyledPanelItem>
            <div>{(0, locale_1.t)('Apdex')}</div>
          </StyledPanelItem>
          <StyledPanelItem>
            <div>{(0, locale_1.t)('Span Operations')}</div>
            {spanTitles}
          </StyledPanelItem>
        </div>
        {(allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.data.length) === 0
                ? emptyColumn
                : allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.data.map((dataRow, idx) => {
                    const allReleasesMisery = miseryRenderer === null || miseryRenderer === void 0 ? void 0 : miseryRenderer(dataRow, {
                        organization,
                        location,
                    });
                    const allReleasesApdex = apdexRenderer === null || apdexRenderer === void 0 ? void 0 : apdexRenderer(dataRow, { organization, location });
                    const allReleasesSpans = spansRenderer === null || spansRenderer === void 0 ? void 0 : spansRenderer.map(renderer => renderer === null || renderer === void 0 ? void 0 : renderer(dataRow, { organization, location }));
                    return (<div key={idx}>
                  <UserMiseryPanelItem>{allReleasesMisery}</UserMiseryPanelItem>
                  <ApdexPanelItem>{allReleasesApdex}</ApdexPanelItem>
                  <StyledPanelItem>
                    <TitleSpace />
                    {allReleasesSpans.map(span => span)}
                  </StyledPanelItem>
                </div>);
                })}
        {(thisReleaseTableData === null || thisReleaseTableData === void 0 ? void 0 : thisReleaseTableData.data.length) === 0
                ? emptyColumn
                : thisReleaseTableData === null || thisReleaseTableData === void 0 ? void 0 : thisReleaseTableData.data.map((dataRow, idx) => {
                    const thisReleasesMisery = miseryRenderer === null || miseryRenderer === void 0 ? void 0 : miseryRenderer(dataRow, {
                        organization,
                        location,
                    });
                    const thisReleasesApdex = apdexRenderer === null || apdexRenderer === void 0 ? void 0 : apdexRenderer(dataRow, {
                        organization,
                        location,
                    });
                    const thisReleasesSpans = spansRenderer === null || spansRenderer === void 0 ? void 0 : spansRenderer.map(renderer => renderer === null || renderer === void 0 ? void 0 : renderer(dataRow, { organization, location }));
                    return (<div key={idx}>
                  <UserMiseryPanelItem>{thisReleasesMisery}</UserMiseryPanelItem>
                  <ApdexPanelItem>{thisReleasesApdex}</ApdexPanelItem>
                  <StyledPanelItem>
                    <TitleSpace />
                    {thisReleasesSpans.map(span => span)}
                  </StyledPanelItem>
                </div>);
                })}
        <div>
          {userMiseryTrend()}
          {apdexTrend()}
          <StyledPanelItem>
            <TitleSpace />
            {spansReleaseTrend === null || spansReleaseTrend === void 0 ? void 0 : spansReleaseTrend.map(row => {
                var _a, _b, _c;
                return renderChange((_a = row.allReleasesRow) === null || _a === void 0 ? void 0 : _a.data, (_b = row.thisReleaseRow) === null || _b === void 0 ? void 0 : _b.data, (_c = row.allReleasesRow) === null || _c === void 0 ? void 0 : _c.meta);
            })}
          </StyledPanelItem>
        </div>
      </react_1.Fragment>);
    }
    function renderMobilePerformance() {
        const mobileVitals = [
            fields_1.MobileVital.AppStartCold,
            fields_1.MobileVital.AppStartWarm,
            fields_1.MobileVital.FramesSlow,
            fields_1.MobileVital.FramesFrozen,
        ];
        const mobileVitalTitles = mobileVitals.map(mobileVital => {
            return (<panels_1.PanelItem key={mobileVital}>{constants_1.MOBILE_VITAL_DETAILS[mobileVital].name}</panels_1.PanelItem>);
        });
        const mobileVitalFields = [
            'p75_measurements_app_start_cold',
            'p75_measurements_app_start_warm',
            'p75_measurements_frames_slow',
            'p75_measurements_frames_frozen',
        ];
        const mobileVitalsRenderer = mobileVitalFields.map(field => (allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.meta) && (0, fieldRenderers_1.getFieldRenderer)(field, allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.meta));
        const mobileReleaseTrend = mobileVitalFields.map(field => {
            var _a, _b, _c, _d, _e, _f;
            return {
                allReleasesRow: {
                    data: (_b = (_a = allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.data) === null || _a === void 0 ? void 0 : _a[0]) === null || _b === void 0 ? void 0 : _b[field],
                    meta: (_c = allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.meta) === null || _c === void 0 ? void 0 : _c[field],
                },
                thisReleaseRow: {
                    data: (_e = (_d = thisReleaseTableData === null || thisReleaseTableData === void 0 ? void 0 : thisReleaseTableData.data) === null || _d === void 0 ? void 0 : _d[0]) === null || _e === void 0 ? void 0 : _e[field],
                    meta: (_f = thisReleaseTableData === null || thisReleaseTableData === void 0 ? void 0 : thisReleaseTableData.meta) === null || _f === void 0 ? void 0 : _f[field],
                },
            };
        });
        const emptyColumn = (<div>
        <SingleEmptySubText>
          <StyledNotAvailable tooltip={(0, locale_1.t)('No results found')}/>
        </SingleEmptySubText>
        {mobileVitalFields.map((vital, index) => (<SingleEmptySubText key={vital[index]}>
            <StyledNotAvailable tooltip={(0, locale_1.t)('No results found')}/>
          </SingleEmptySubText>))}
      </div>);
        return (<react_1.Fragment>
        <div>
          <panels_1.PanelItem>{(0, locale_1.t)('User Misery')}</panels_1.PanelItem>
          {mobileVitalTitles}
        </div>
        {(allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.data.length) === 0
                ? emptyColumn
                : allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.data.map((dataRow, idx) => {
                    const allReleasesMisery = miseryRenderer === null || miseryRenderer === void 0 ? void 0 : miseryRenderer(dataRow, {
                        organization,
                        location,
                    });
                    const allReleasesMobile = mobileVitalsRenderer === null || mobileVitalsRenderer === void 0 ? void 0 : mobileVitalsRenderer.map(renderer => renderer === null || renderer === void 0 ? void 0 : renderer(dataRow, { organization, location }));
                    return (<div key={idx}>
                  <UserMiseryPanelItem>{allReleasesMisery}</UserMiseryPanelItem>
                  {allReleasesMobile.map((mobileVital, i) => (<StyledPanelItem key={i}>{mobileVital}</StyledPanelItem>))}
                </div>);
                })}
        {(thisReleaseTableData === null || thisReleaseTableData === void 0 ? void 0 : thisReleaseTableData.data.length) === 0
                ? emptyColumn
                : thisReleaseTableData === null || thisReleaseTableData === void 0 ? void 0 : thisReleaseTableData.data.map((dataRow, idx) => {
                    const thisReleasesMisery = miseryRenderer === null || miseryRenderer === void 0 ? void 0 : miseryRenderer(dataRow, {
                        organization,
                        location,
                    });
                    const thisReleasesMobile = mobileVitalsRenderer === null || mobileVitalsRenderer === void 0 ? void 0 : mobileVitalsRenderer.map(renderer => renderer === null || renderer === void 0 ? void 0 : renderer(dataRow, { organization, location }));
                    return (<div key={idx}>
                  <UserMiseryPanelItem>{thisReleasesMisery}</UserMiseryPanelItem>
                  {thisReleasesMobile.map((mobileVital, i) => (<StyledPanelItem key={i}>{mobileVital}</StyledPanelItem>))}
                </div>);
                })}
        <div>
          {userMiseryTrend()}
          {mobileReleaseTrend === null || mobileReleaseTrend === void 0 ? void 0 : mobileReleaseTrend.map((row, idx) => {
                var _a, _b, _c;
                return (<StyledPanelItem key={idx}>
              {renderChange((_a = row.allReleasesRow) === null || _a === void 0 ? void 0 : _a.data, (_b = row.thisReleaseRow) === null || _b === void 0 ? void 0 : _b.data, (_c = row.allReleasesRow) === null || _c === void 0 ? void 0 : _c.meta)}
            </StyledPanelItem>);
            })}
        </div>
      </react_1.Fragment>);
    }
    function renderUnknownPerformance() {
        const emptyColumn = (<div>
        <SingleEmptySubText>
          <StyledNotAvailable tooltip={(0, locale_1.t)('No results found')}/>
        </SingleEmptySubText>
      </div>);
        return (<react_1.Fragment>
        <div>
          <panels_1.PanelItem>{(0, locale_1.t)('User Misery')}</panels_1.PanelItem>
        </div>
        {(allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.data.length) === 0
                ? emptyColumn
                : allReleasesTableData === null || allReleasesTableData === void 0 ? void 0 : allReleasesTableData.data.map((dataRow, idx) => {
                    const allReleasesMisery = miseryRenderer === null || miseryRenderer === void 0 ? void 0 : miseryRenderer(dataRow, {
                        organization,
                        location,
                    });
                    return (<div key={idx}>
                  <UserMiseryPanelItem>{allReleasesMisery}</UserMiseryPanelItem>
                </div>);
                })}
        {(thisReleaseTableData === null || thisReleaseTableData === void 0 ? void 0 : thisReleaseTableData.data.length) === 0
                ? emptyColumn
                : thisReleaseTableData === null || thisReleaseTableData === void 0 ? void 0 : thisReleaseTableData.data.map((dataRow, idx) => {
                    const thisReleasesMisery = miseryRenderer === null || miseryRenderer === void 0 ? void 0 : miseryRenderer(dataRow, {
                        organization,
                        location,
                    });
                    return (<div key={idx}>
                  <UserMiseryPanelItem>{thisReleasesMisery}</UserMiseryPanelItem>
                </div>);
                })}
        <div>{userMiseryTrend()}</div>
      </react_1.Fragment>);
    }
    const loader = <StyledLoadingIndicator />;
    const platformPerformanceRender = {
        [utils_1.PROJECT_PERFORMANCE_TYPE.FRONTEND]: {
            title: (0, locale_1.t)('Frontend Performance'),
            section: renderFrontendPerformance(),
        },
        [utils_1.PROJECT_PERFORMANCE_TYPE.BACKEND]: {
            title: (0, locale_1.t)('Backend Performance'),
            section: renderBackendPerformance(),
        },
        [utils_1.PROJECT_PERFORMANCE_TYPE.MOBILE]: {
            title: (0, locale_1.t)('Mobile Performance'),
            section: renderMobilePerformance(),
        },
        [utils_1.PROJECT_PERFORMANCE_TYPE.ANY]: {
            title: (0, locale_1.t)('[Unknown] Performance'),
            section: renderUnknownPerformance(),
        },
    };
    const isUnknownPlatform = performanceType === utils_1.PROJECT_PERFORMANCE_TYPE.ANY;
    return (<react_1.Fragment>
      <HeadCellContainer>
        {platformPerformanceRender[performanceType].title}
      </HeadCellContainer>
      {isUnknownPlatform && (<StyledAlert type="warning" icon={<icons_1.IconWarning size="md"/>} system>
          {(0, locale_1.tct)('For more performance metrics, specify which platform this project is using in [link]', {
                link: (<react_router_1.Link to={`/settings/${organization.slug}/projects/${project.slug}/`}>
                  {(0, locale_1.t)('project settings.')}
                </react_router_1.Link>),
            })}
        </StyledAlert>)}
      <StyledPanelTable isLoading={isLoading} headers={[
            <Cell key="description" align="left">
            {(0, locale_1.t)('Description')}
          </Cell>,
            <Cell key="releases" align="right">
            {(0, locale_1.t)('All Releases')}
          </Cell>,
            <Cell key="release" align="right">
            {(0, locale_1.t)('This Release')}
          </Cell>,
            <Cell key="change" align="right">
            {(0, locale_1.t)('Change')}
          </Cell>,
        ]} disablePadding loader={loader} disableTopBorder={isUnknownPlatform}>
        {platformPerformanceRender[performanceType].section}
      </StyledPanelTable>
    </react_1.Fragment>);
}
function PerformanceCardTableWrapper({ organization, project, allReleasesEventView, releaseEventView, performanceType, location, }) {
    return (<discoverQuery_1.default eventView={allReleasesEventView} orgSlug={organization.slug} location={location}>
      {({ isLoading, tableData: allReleasesTableData }) => (<discoverQuery_1.default eventView={releaseEventView} orgSlug={organization.slug} location={location}>
          {({ isLoading: isReleaseLoading, tableData: thisReleaseTableData }) => (<PerformanceCardTable isLoading={isLoading || isReleaseLoading} organization={organization} location={location} project={project} allReleasesEventView={allReleasesEventView} releaseEventView={releaseEventView} allReleasesTableData={allReleasesTableData} thisReleaseTableData={thisReleaseTableData} performanceType={performanceType}/>)}
        </discoverQuery_1.default>)}
    </discoverQuery_1.default>);
}
exports.default = PerformanceCardTableWrapper;
const emptyFieldCss = p => (0, react_2.css) `
  color: ${p.theme.chartOther};
  text-align: right;
`;
const StyledLoadingIndicator = (0, styled_1.default)(loadingIndicator_1.default) `
  margin: 70px auto;
`;
const HeadCellContainer = (0, styled_1.default)('div') `
  font-size: ${p => p.theme.fontSizeExtraLarge};
  padding: ${(0, space_1.default)(2)};
  border-top: 1px solid ${p => p.theme.border};
  border-left: 1px solid ${p => p.theme.border};
  border-right: 1px solid ${p => p.theme.border};
  border-top-left-radius: ${p => p.theme.borderRadius};
  border-top-right-radius: ${p => p.theme.borderRadius};
`;
const StyledPanelTable = (0, styled_1.default)(panelTable_1.default) `
  border-top-left-radius: 0;
  border-top-right-radius: 0;
  border-top: ${p => (p.disableTopBorder ? 'none' : `1px solid ${p.theme.border}`)};
  @media (max-width: ${p => p.theme.breakpoints[2]}) {
    grid-template-columns: min-content 1fr 1fr 1fr;
  }
`;
const StyledPanelItem = (0, styled_1.default)(panels_1.PanelItem) `
  display: block;
  white-space: nowrap;
  width: 100%;
`;
const SubTitle = (0, styled_1.default)('div') `
  margin-left: ${(0, space_1.default)(3)};
`;
const TitleSpace = (0, styled_1.default)('div') `
  height: 24px;
`;
const UserMiseryPanelItem = (0, styled_1.default)(panels_1.PanelItem) `
  justify-content: flex-end;
`;
const ApdexPanelItem = (0, styled_1.default)(panels_1.PanelItem) `
  text-align: right;
`;
const SingleEmptySubText = (0, styled_1.default)(panels_1.PanelItem) `
  display: block;
  ${emptyFieldCss}
`;
const MultipleEmptySubText = (0, styled_1.default)('div') `
  ${emptyFieldCss}
`;
const Cell = (0, styled_1.default)('div') `
  text-align: ${p => p.align};
  margin-left: ${p => p.align === 'left' && (0, space_1.default)(2)};
  padding-right: ${p => p.align === 'right' && (0, space_1.default)(2)};
  ${overflowEllipsis_1.default}
`;
const StyledAlert = (0, styled_1.default)(alert_1.default) `
  border-top: 1px solid ${p => p.theme.border};
  border-right: 1px solid ${p => p.theme.border};
  border-left: 1px solid ${p => p.theme.border};
  margin-bottom: 0;
`;
const StyledNotAvailable = (0, styled_1.default)(notAvailable_1.default) `
  text-align: right;
`;
const SubText = (0, styled_1.default)('div') `
  color: ${p => p.theme.subText};
  text-align: right;
`;
const TrendText = (0, styled_1.default)('div') `
  color: ${p => p.theme[p.color]};
  text-align: right;
`;
const StyledIconArrow = (0, styled_1.default)(icons_1.IconArrow) `
  color: ${p => p.theme[p.color]};
  margin-left: ${(0, space_1.default)(0.5)};
`;
//# sourceMappingURL=performanceCardTable.jsx.map