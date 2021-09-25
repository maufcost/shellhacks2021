import React from 'react'

import './register.css'

class Register extends React.Component {
    componentDidMount() {
        console.log('register mounted')
    }

    componentWillUnmount() {
        console.log('register UNmounted')
    }

    render() {
        return (
            <div className="register-container">
                <div className="register auto">
                </div>
            </div>
        )
    }
}

export default Register;
