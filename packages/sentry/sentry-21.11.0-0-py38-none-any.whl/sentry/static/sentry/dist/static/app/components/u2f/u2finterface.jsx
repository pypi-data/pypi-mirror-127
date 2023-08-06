Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const React = (0, tslib_1.__importStar)(require("react"));
const Sentry = (0, tslib_1.__importStar)(require("@sentry/react"));
const u2f_api_1 = (0, tslib_1.__importDefault)(require("u2f-api"));
const locale_1 = require("app/locale");
const configStore_1 = (0, tslib_1.__importDefault)(require("app/stores/configStore"));
class U2fInterface extends React.Component {
    constructor() {
        super(...arguments);
        this.state = {
            isSupported: null,
            formElement: null,
            challengeElement: null,
            hasBeenTapped: false,
            deviceFailure: null,
            responseElement: null,
        };
        this.onTryAgain = () => {
            this.setState({ hasBeenTapped: false, deviceFailure: null }, () => void this.invokeU2fFlow());
        };
        this.bindChallengeElement = ref => {
            this.setState({
                challengeElement: ref,
                formElement: ref && ref.form,
            });
            if (ref) {
                ref.value = JSON.stringify(this.props.challengeData);
            }
        };
        this.bindResponseElement = ref => this.setState({ responseElement: ref });
        this.renderFailure = () => {
            const { deviceFailure } = this.state;
            const supportMail = configStore_1.default.get('supportEmail');
            const support = supportMail ? (<a href={'mailto:' + supportMail}>{supportMail}</a>) : (<span>{(0, locale_1.t)('Support')}</span>);
            return (<div className="failure-message">
        <div>
          <strong>{(0, locale_1.t)('Error: ')}</strong>{' '}
          {{
                    UNKNOWN_ERROR: (0, locale_1.t)('There was an unknown problem, please try again'),
                    DEVICE_ERROR: (0, locale_1.t)('Your U2F device reported an error.'),
                    DUPLICATE_DEVICE: (0, locale_1.t)('This device is already registered with Sentry.'),
                    UNKNOWN_DEVICE: (0, locale_1.t)('The device you used for sign-in is unknown.'),
                    BAD_APPID: (0, locale_1.tct)('[p1:The Sentry server administrator modified the ' +
                        'device registrations.]' +
                        '[p2:You need to remove and re-add the device to continue ' +
                        'using your U2F device. Use a different sign-in method or ' +
                        'contact [support] for assistance.]', {
                        p1: <p />,
                        p2: <p />,
                        support,
                    }),
                }[deviceFailure || '']}
        </div>
        {this.canTryAgain && (<div style={{ marginTop: 18 }}>
            <a onClick={this.onTryAgain} className="btn btn-primary">
              {(0, locale_1.t)('Try Again')}
            </a>
          </div>)}
      </div>);
        };
    }
    componentDidMount() {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            const supported = yield u2f_api_1.default.isSupported();
            // eslint-disable-next-line react/no-did-mount-set-state
            this.setState({ isSupported: supported });
            if (supported) {
                this.invokeU2fFlow();
            }
        });
    }
    submitU2fResponse(promise) {
        promise
            .then(data => {
            this.setState({
                hasBeenTapped: true,
            }, () => {
                var _a;
                const u2fResponse = JSON.stringify(data);
                const challenge = JSON.stringify(this.props.challengeData);
                if (this.state.responseElement) {
                    // eslint-disable-next-line react/no-direct-mutation-state
                    this.state.responseElement.value = u2fResponse;
                }
                if (!this.props.onTap) {
                    (_a = this.state.formElement) === null || _a === void 0 ? void 0 : _a.submit();
                    return;
                }
                this.props
                    .onTap({
                    response: u2fResponse,
                    challenge,
                })
                    .catch(() => {
                    // This is kind of gross but I want to limit the amount of changes to this component
                    this.setState({
                        deviceFailure: 'UNKNOWN_ERROR',
                        hasBeenTapped: false,
                    });
                });
            });
        })
            .catch(err => {
            let failure = 'DEVICE_ERROR';
            // in some rare cases there is no metadata on the error which
            // causes this to blow up badly.
            if (err.metaData) {
                if (err.metaData.type === 'DEVICE_INELIGIBLE') {
                    if (this.props.flowMode === 'enroll') {
                        failure = 'DUPLICATE_DEVICE';
                    }
                    else {
                        failure = 'UNKNOWN_DEVICE';
                    }
                }
                else if (err.metaData.type === 'BAD_REQUEST') {
                    failure = 'BAD_APPID';
                }
            }
            // we want to know what is happening here.  There are some indicators
            // that users are getting errors that should not happen through the
            // regular u2f flow.
            Sentry.captureException(err);
            this.setState({
                deviceFailure: failure,
                hasBeenTapped: false,
            });
        });
    }
    invokeU2fFlow() {
        let promise;
        if (this.props.flowMode === 'sign') {
            promise = u2f_api_1.default.sign(this.props.challengeData.authenticateRequests);
        }
        else if (this.props.flowMode === 'enroll') {
            const { registerRequests, registeredKeys } = this.props.challengeData;
            promise = u2f_api_1.default.register(registerRequests, registeredKeys);
        }
        else {
            throw new Error(`Unsupported flow mode '${this.props.flowMode}'`);
        }
        this.submitU2fResponse(promise);
    }
    renderUnsupported() {
        return this.props.silentIfUnsupported ? null : (<div className="u2f-box">
        <div className="inner">
          <p className="error">
            {(0, locale_1.t)(`
             Unfortunately your browser does not support U2F. You need to use
             a different two-factor method or switch to a browser that supports
             it (Google Chrome or Microsoft Edge).`)}
          </p>
        </div>
      </div>);
    }
    get canTryAgain() {
        return this.state.deviceFailure !== 'BAD_APPID';
    }
    renderBody() {
        return this.state.deviceFailure ? this.renderFailure() : this.props.children;
    }
    renderPrompt() {
        const { style } = this.props;
        return (<div style={style} className={'u2f-box' +
                (this.state.hasBeenTapped ? ' tapped' : '') +
                (this.state.deviceFailure ? ' device-failure' : '')}>
        <div className="device-animation-frame">
          <div className="device-failed"/>
          <div className="device-animation"/>
          <div className="loading-dots">
            <span className="dot"/>
            <span className="dot"/>
            <span className="dot"/>
          </div>
        </div>
        <input type="hidden" name="challenge" ref={this.bindChallengeElement}/>
        <input type="hidden" name="response" ref={this.bindResponseElement}/>
        <div className="inner">{this.renderBody()}</div>
      </div>);
    }
    render() {
        const { isSupported } = this.state;
        // if we are still waiting for the browser to tell us if we can do u2f this
        // will be null.
        if (isSupported === null) {
            return null;
        }
        if (!isSupported) {
            return this.renderUnsupported();
        }
        return this.renderPrompt();
    }
}
exports.default = U2fInterface;
//# sourceMappingURL=u2finterface.jsx.map