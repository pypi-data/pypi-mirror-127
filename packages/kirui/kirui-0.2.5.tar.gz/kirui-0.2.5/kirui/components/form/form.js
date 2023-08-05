import { Component } from "/kirui/core/component";
import { registry } from "/kirui/core/registry";
import { h } from 'preact';
import { evaluate } from '/kirui/core/element';
import $ from "jquery";


class Form extends Component {
    constructor(props) {
        super(props);

        this.state = {
            'csrfmiddlewaretoken': this.props.csrfmiddlewaretoken
        }

        this.handleInputChange = this.handleInputChange.bind(this);
        this.bubbleSubmit = this.bubbleSubmit.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.bubbleStateChange = this.bubbleStateChange.bind(this);
    }

    handleInputChange(event) {
        const target = event.target;

        let name, value;
        if (event instanceof CustomEvent) {
            name = event.target.getAttribute('name');
            value = event.detail.data;
        } else if (event instanceof Event) {
            // console.log(event);
            name = target.name;
            value = target.type === 'checkbox' ? target.checked : target.value;
        } else {
            // console.log(event);
            name = target.name;
            value = target.value.toString();  // TODO: megnézni, hogy ez így jó lesz-e. Minden value-t string-é konvertálunk, különben a default 0 értékbőll null lesz
        }

        this.setState({[name]: value});
        $.extend(this.state, {[name]: value});
    }

    bubbleStateChange(orig_event) {
        let params = {bubbles: true, detail: {'data': this.state, 'src': null}}
        if (orig_event !== undefined) {
            orig_event.preventDefault();
            orig_event.stopPropagation();

            if (orig_event.target.tagName === 'INPUT') {
                params.detail.src = orig_event.target.name || "";
            }

            params.detail.forceUpdate = true;
        } else {
            params.detail.forceUpdate = false;
        }

        let event = new CustomEvent('StateChange', params);
        this.base.dispatchEvent(event);
    }

    bubbleSubmit(ev) {
        ev.preventDefault();
        ev.stopPropagation();
        let params = {bubbles: true, detail: {'data': this.state}};

        if (ev.target.tagName === 'INPUT') {
            params.detail.src = ev.target.name || "";
        }

        params.detail.forceUpdate = true;
        let event = new CustomEvent('StateChange', params);
        this.base.dispatchEvent(event);
    }

    handleSubmit(event) {
        event.preventDefault();

        if (event.submitter.name) {
            console.log(event.submitter.name);
            this.state[event.submitter.name] = ''
        }

        let e = new CustomEvent('AjaxLoading', {'bubbles': true, 'detail': {'loading': true}});
        this.base.dispatchEvent(e);

        $.post({
            url: this.props.action || window.location,
            data: $.param(this.state, true),
            statusCode: {
                340: function (resp) {
                    window.location.replace(resp.getResponseHeader('location'));
                }
            }
        }).done((resp, status, xhr) => {
            let dom = resp;
            this.dataToCreateElement([dom]);
            this.props.children = dom[2];
            this.forceUpdate();

            let e = new CustomEvent('AjaxLoading', {'bubbles': true, 'detail': {'loading': false}});
            this.base.dispatchEvent(e);
        }).fail((resp) => {
            if (resp.status === 403) {
                let d = evaluate(resp.responseText);
                this.props.children = d.props.children;
                this.forceUpdate();

                let e = new CustomEvent('AjaxLoading', {'bubbles': true, 'detail': {'loading': false}});
                this.base.dispatchEvent(e);
            } else if (resp.status === 302) {
                console.log(resp)
            }
        });
    }

    doRender() {
        return <form {...this.props} onHandleInputChange={this.handleInputChange}>
            {this.props.children}
        </form>
    }

    componentDidMount() {
        if (this.props.didMountCallback) {
            this.bubbleStateChange();
        }
    }
}

registry.register('kr-form', Form);
export { Form }