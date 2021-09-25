import React from 'react'
import { Router } from '@reach/router'

import Menu from './components/menu/menu'
import Purchase from './components/purchase/purchase'
import Register from './components/register/register'
import MyTradings from './components/my-tradings/my-tradings'
import DashboardClient from './components/dashboard-client/dashboard-client'

import './App.css'

class App extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            menuOpen: false
        }

        this.openCloseMenu = this.openCloseMenu.bind(this)
    }

    openCloseMenu() {
        this.setState({ menuOpen: !this.state.menuOpen })
    }

    render() {
        return (
            <div className="App">
                {this.state.menuOpen && (
                    <Menu
                        openCloseMenu={this.openCloseMenu}
                    />
                )}
                <Router>
                    <Register
                        path="/register"
                        openCloseMenu={this.openCloseMenu}
                    />
                    <DashboardClient
                        path="/home-client"
                        openCloseMenu={this.openCloseMenu}
                    />
                    <Purchase
                        path="/purchase"
                        openCloseMenu={this.openCloseMenu}
                    />
                    <MyTradings
                        path="/my-tradings"
                        openCloseMenu={this.openCloseMenu}
                    />
                </Router>
            </div>
        )
    }
}

export default App;
