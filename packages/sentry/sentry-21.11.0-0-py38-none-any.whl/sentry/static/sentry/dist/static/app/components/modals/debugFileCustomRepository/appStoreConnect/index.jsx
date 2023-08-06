Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = require("react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const indicator_1 = require("app/actionCreators/indicator");
const alert_1 = (0, tslib_1.__importDefault)(require("app/components/alert"));
const button_1 = (0, tslib_1.__importDefault)(require("app/components/button"));
const buttonBar_1 = (0, tslib_1.__importDefault)(require("app/components/buttonBar"));
const loadingIndicator_1 = (0, tslib_1.__importDefault)(require("app/components/loadingIndicator"));
const icons_1 = require("app/icons");
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const appStoreValidationErrorMessage_1 = require("app/utils/appStoreValidationErrorMessage");
const withApi_1 = (0, tslib_1.__importDefault)(require("app/utils/withApi"));
const stepOne_1 = (0, tslib_1.__importDefault)(require("./stepOne"));
const stepTwo_1 = (0, tslib_1.__importDefault)(require("./stepTwo"));
const utils_1 = require("./utils");
const steps = [(0, locale_1.t)('App Store Connect credentials'), (0, locale_1.t)('Choose an application')];
function AppStoreConnect({ Header, Body, Footer, api, initialData, orgSlug, projectSlug, onSubmit, appStoreConnectStatusData, }) {
    const { credentials } = appStoreConnectStatusData !== null && appStoreConnectStatusData !== void 0 ? appStoreConnectStatusData : {};
    const [isLoading, setIsLoading] = (0, react_1.useState)(false);
    const [activeStep, setActiveStep] = (0, react_1.useState)(0);
    const [appStoreApps, setAppStoreApps] = (0, react_1.useState)([]);
    const [stepOneData, setStepOneData] = (0, react_1.useState)({
        issuer: initialData === null || initialData === void 0 ? void 0 : initialData.appconnectIssuer,
        keyId: initialData === null || initialData === void 0 ? void 0 : initialData.appconnectKey,
        privateKey: typeof (initialData === null || initialData === void 0 ? void 0 : initialData.appconnectPrivateKey) === 'object' ? undefined : '',
        errors: undefined,
    });
    const [stepTwoData, setStepTwoData] = (0, react_1.useState)({
        app: (initialData === null || initialData === void 0 ? void 0 : initialData.appId) && (initialData === null || initialData === void 0 ? void 0 : initialData.appName)
            ? {
                appId: initialData.appId,
                name: initialData.appName,
                bundleId: initialData.bundleId,
            }
            : undefined,
    });
    function checkAppStoreConnectCredentials() {
        var _a;
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            setIsLoading(true);
            try {
                const response = yield api.requestPromise(`/projects/${orgSlug}/${projectSlug}/appstoreconnect/apps/`, {
                    method: 'POST',
                    data: {
                        id: stepOneData.privateKey !== undefined ? undefined : initialData === null || initialData === void 0 ? void 0 : initialData.id,
                        appconnectIssuer: stepOneData.issuer,
                        appconnectKey: stepOneData.keyId,
                        appconnectPrivateKey: stepOneData.privateKey,
                    },
                });
                setAppStoreApps(response.apps);
                if (((_a = stepTwoData.app) === null || _a === void 0 ? void 0 : _a.appId) &&
                    !response.apps.find(app => { var _a; return app.appId === ((_a = stepTwoData.app) === null || _a === void 0 ? void 0 : _a.appId); })) {
                    setStepTwoData({ app: response.apps[0] });
                }
                setIsLoading(false);
                goNext();
            }
            catch (error) {
                setIsLoading(false);
                const appStoreConnnectError = (0, utils_1.getAppStoreErrorMessage)(error);
                if (typeof appStoreConnnectError === 'string') {
                    // app-connect-authentication-error
                    // app-connect-forbidden-error
                    (0, indicator_1.addErrorMessage)(appStoreConnnectError);
                    return;
                }
                setStepOneData(Object.assign(Object.assign({}, stepOneData), { errors: appStoreConnnectError }));
            }
        });
    }
    function persistData() {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            if (!stepTwoData.app) {
                return;
            }
            setIsLoading(true);
            let endpoint = `/projects/${orgSlug}/${projectSlug}/appstoreconnect/`;
            let errorMessage = (0, locale_1.t)('An error occurred while adding the custom repository');
            let successMessage = (0, locale_1.t)('Successfully added custom repository');
            if (!!initialData) {
                endpoint = `${endpoint}${initialData.id}/`;
                errorMessage = (0, locale_1.t)('An error occurred while updating the custom repository');
                successMessage = (0, locale_1.t)('Successfully updated custom repository');
            }
            try {
                yield api.requestPromise(endpoint, {
                    method: 'POST',
                    data: {
                        appconnectIssuer: stepOneData.issuer,
                        appconnectKey: stepOneData.keyId,
                        appconnectPrivateKey: stepOneData.privateKey,
                        appName: stepTwoData.app.name,
                        appId: stepTwoData.app.appId,
                        bundleId: stepTwoData.app.bundleId,
                    },
                });
                (0, indicator_1.addSuccessMessage)(successMessage);
                onSubmit();
            }
            catch (error) {
                setIsLoading(false);
                const appStoreConnnectError = (0, utils_1.getAppStoreErrorMessage)(error);
                if (typeof appStoreConnnectError === 'string') {
                    if (appStoreConnnectError === appStoreValidationErrorMessage_1.unexpectedErrorMessage) {
                        (0, indicator_1.addErrorMessage)(errorMessage);
                        return;
                    }
                    (0, indicator_1.addErrorMessage)(appStoreConnnectError);
                }
            }
        });
    }
    function isFormInvalid() {
        switch (activeStep) {
            case 0:
                return Object.keys(stepOneData).some(key => {
                    var _a;
                    if (key === 'errors') {
                        const errors = (_a = stepOneData[key]) !== null && _a !== void 0 ? _a : {};
                        return Object.keys(errors).some(error => !!errors[error]);
                    }
                    if (key === 'privateKey' && stepOneData[key] === undefined) {
                        return false;
                    }
                    return !stepOneData[key];
                });
            case 1:
                return Object.keys(stepTwoData).some(key => !stepTwoData[key]);
            default:
                return false;
        }
    }
    function goNext() {
        setActiveStep(activeStep + 1);
    }
    function handleGoBack() {
        const newActiveStep = activeStep - 1;
        setActiveStep(newActiveStep);
    }
    function handleGoNext() {
        switch (activeStep) {
            case 0:
                checkAppStoreConnectCredentials();
                break;
            case 1:
                persistData();
                break;
            default:
                break;
        }
    }
    function renderCurrentStep() {
        switch (activeStep) {
            case 0:
                return <stepOne_1.default stepOneData={stepOneData} onSetStepOneData={setStepOneData}/>;
            case 1:
                return (<stepTwo_1.default appStoreApps={appStoreApps} stepTwoData={stepTwoData} onSetStepTwoData={setStepTwoData}/>);
            default:
                return (<alert_1.default type="error" icon={<icons_1.IconWarning />}>
            {(0, locale_1.t)('This step could not be found.')}
          </alert_1.default>);
        }
    }
    function getAlerts() {
        const alerts = [];
        if (activeStep !== 0) {
            return alerts;
        }
        if ((credentials === null || credentials === void 0 ? void 0 : credentials.status) === 'invalid') {
            alerts.push(<StyledAlert type="warning" icon={<icons_1.IconWarning />}>
          {credentials.code === 'app-connect-forbidden-error'
                    ? (0, locale_1.t)('Your App Store Connect credentials have insufficient permissions. To reconnect, update your credentials.')
                    : (0, locale_1.t)('Your App Store Connect credentials are invalid. To reconnect, update your credentials.')}
        </StyledAlert>);
        }
        return alerts;
    }
    function renderBodyContent() {
        const alerts = getAlerts();
        return (<react_1.Fragment>
        {!!alerts.length && (<Alerts>
            {alerts.map((alert, index) => (<react_1.Fragment key={index}>{alert}</react_1.Fragment>))}
          </Alerts>)}
        {renderCurrentStep()}
      </react_1.Fragment>);
    }
    if (initialData && !appStoreConnectStatusData) {
        return <loadingIndicator_1.default />;
    }
    return (<react_1.Fragment>
      <Header closeButton>
        <HeaderContent>
          <NumericSymbol>{activeStep + 1}</NumericSymbol>
          <HeaderContentTitle>{steps[activeStep]}</HeaderContentTitle>
          <StepsOverview>
            {(0, locale_1.tct)('[currentStep] of [totalSteps]', {
            currentStep: activeStep + 1,
            totalSteps: steps.length,
        })}
          </StepsOverview>
        </HeaderContent>
      </Header>
      <Body>{renderBodyContent()}</Body>
      <Footer>
        <buttonBar_1.default gap={1}>
          {activeStep !== 0 && <button_1.default onClick={handleGoBack}>{(0, locale_1.t)('Back')}</button_1.default>}
          <StyledButton priority="primary" onClick={handleGoNext} disabled={isLoading || isFormInvalid()}>
            {isLoading && (<LoadingIndicatorWrapper>
                <loadingIndicator_1.default mini/>
              </LoadingIndicatorWrapper>)}
            {activeStep + 1 === steps.length
            ? initialData
                ? (0, locale_1.t)('Update')
                : (0, locale_1.t)('Save')
            : steps[activeStep + 1]}
          </StyledButton>
        </buttonBar_1.default>
      </Footer>
    </react_1.Fragment>);
}
exports.default = (0, withApi_1.default)(AppStoreConnect);
const HeaderContent = (0, styled_1.default)('div') `
  display: grid;
  grid-template-columns: max-content max-content 1fr;
  align-items: center;
  grid-gap: ${(0, space_1.default)(1)};
`;
const NumericSymbol = (0, styled_1.default)('div') `
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  font-weight: 700;
  font-size: ${p => p.theme.fontSizeMedium};
  background-color: ${p => p.theme.yellow300};
`;
const HeaderContentTitle = (0, styled_1.default)('div') `
  font-weight: 700;
  font-size: ${p => p.theme.fontSizeExtraLarge};
`;
const StepsOverview = (0, styled_1.default)('div') `
  color: ${p => p.theme.gray300};
  display: flex;
  justify-content: flex-end;
`;
const LoadingIndicatorWrapper = (0, styled_1.default)('div') `
  height: 100%;
  position: absolute;
  width: 100%;
  top: 0;
  left: 0;
  display: flex;
  align-items: center;
  justify-content: center;
`;
const StyledButton = (0, styled_1.default)(button_1.default) `
  position: relative;
`;
const Alerts = (0, styled_1.default)('div') `
  display: grid;
  grid-gap: ${(0, space_1.default)(1.5)};
  margin-bottom: ${(0, space_1.default)(3)};
`;
const StyledAlert = (0, styled_1.default)(alert_1.default) `
  margin: 0;
`;
//# sourceMappingURL=index.jsx.map