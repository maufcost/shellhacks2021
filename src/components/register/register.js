import React from 'react'
import Header from '../header/header'

import './register.css'

class Register extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            email: '',
            pwd: '',
            cpwd: ''
        }

        this.register = this.register.bind(this)
    }

    register() {

    }

    render() {
        return (
            <div className="register-container">
                <div className="register auto">
                    <Header openCloseMenu={this.props.openCloseMenu} noImg />

                    <h1>Welcome to XX!</h1>
                    <p className="s">Let's create an account for you 😊</p>

                    <div className="divider">
                        <label>Enter your email address</label>
                        <p>All your transactions, sales, or purchases will be sent to this email</p>
                        <input
                            type="text"
                            value={this.state.email}
                            placeholder="E.g. michaelscott@dundermifflin.com"
                            onChange={(e) => this.setState({ email: e.target.value })}
                        />
                    </div>

                    <div className="divider">
                        <label>Enter a secure password</label>
                        <p>Make sure to choose a safe password</p>
                        <input
                            type="password"
                            value={this.state.pwd}
                            placeholder="E.g. myduckhas3feet"
                            onChange={(e) => this.setState({ pwd: e.target.value })}
                        />
                    </div>

                    <div className="divider">
                        <label>Let's confirm your password</label>
                        <p>This should be the same password as above</p>
                        <input
                            type="password"
                            value={this.state.cpwd}
                            placeholder="E.g. myduckhas3feet"
                            onChange={(e) => this.setState({ cpwd: e.target.value })}
                        />
                    </div>

                    <div className="divider">
                        <label>Are you a business owner or a client?</label>
                        <div className="option">
                            <input type="checkbox" />
                            <span>I am a <span className="gimme-border">business owner</span></span>
                        </div>
                        <div className="option">
                            <input type="checkbox" />
                            <span>I am a <span className="gimme-border">client</span></span>
                        </div>
                    </div>

                    <button onClick={this.register}>Create account</button>
                </div>
            </div>
        )
    }
}

export default Register;
