import React from 'react'
import { navigate } from '@reach/router'

import './menu.css'

class Menu extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            style : {
                position: 'absolute',
                left: -500,
                opacity: 0,
                transition: 'all 2s ease',
            }
        }

        this.signOut = this.signOut.bind(this)
        this.mountStyle = this.mountStyle.bind(this)
        this.myTradings = this.myTradings.bind(this)
        this.unMountStyle = this.unMountStyle.bind(this)
        this.browseLocalBusinesses = this.browseLocalBusinesses.bind(this)
    }

    componentDidMount(){
        setTimeout(this.mountStyle, 10)
    }

    mountStyle() {
        this.setState({
            style: {
                left: 0,
                opacity: 1,
                transition: 'all 1s ease',
            }
        })
    }

    unMountStyle() {
        this.setState({
            style: {
                left: -500,
                opacity: 0,
                transition: 'all 1s ease',
            }
        })
    }

    browseLocalBusinesses() {
        navigate('/home-client')
        this.props.openCloseMenu()
    }

    myTradings() {
        this.unMountStyle()
        this.props.openCloseMenu()
        // setTimeout(() => {
        navigate('/my-tradings')
        // }, 1000)
    }

    signOut() {
        navigate('/register')
        this.props.openCloseMenu()
    }

    render() {
        return (
            <div className="menu-container" style={this.state.style}>
                <div className="menu">
                    <header>
                        <button
                            className="close"
                            onClick={this.props.openCloseMenu}
                        >
                            x
                        </button>
                        <p className="logo">Logo</p>
                    </header>
                    <div className="nav">
                        <button onClick={this.browseLocalBusinesses}>
                            <div className="neon-green"></div>
                            Browse local businesses
                        </button>
                        <button onClick={this.myTradings}>
                            <div className="neon-orange"></div>
                            My tradings
                        </button>
                        <button onClick={this.myTradings}>
                            <div className="neon-orange"></div>
                            Manage my notifications
                        </button>
                        <button onClick={this.signOut}>
                            <div className="neon-blue"></div>
                            Sign Out
                        </button>
                    </div>
                </div>
            </div>
        )
    }
}

export default Menu;
