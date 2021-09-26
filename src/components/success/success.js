import React from 'react';

import Header from '../header/header'

import './success.css'

class Success extends React.Component {
    render() {
        return (
            <div className="success-container">
                <div className="success margin">
                    <Header openCloseMenu={this.openCloseMenu} />
                    <h1>Your order was successfully processed! 🎉</h1>
                    <p>You just ordered {this.props.order}</p>
                    <div className="owner">
                        <img src={this.props.owner} />
                        <p className="name">{name}</p>
                    </div>
                </div>
            </div>
        )
    }
}

export default Success;
