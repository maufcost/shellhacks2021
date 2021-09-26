import React from 'react'

import { SAMPLE_USER } from '../../utils'
import HB from '../../global-assets/hb.svg'

import './header.css'

class Header extends React.Component {
    constructor(props) {
        super(props)
        this.redirect = this.redirect.bind(this)
    }

    redirect() {
        this.props.openCloseMenu()
    }

    render() {
        return (
            <div className="app-header">
                <img
                    className="hamburguer"
                    src={HB}
                    alt="Menu"
                    onClick={this.redirect}
                />
                <p className="logo">bizchain</p>
                {!this.props.noImg && (
                    <img className="user-img" src={SAMPLE_USER} />
                )}
            </div>
        )
    }
}

export default Header;
