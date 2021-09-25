import React from 'react'
import { Router } from '@reach/router'

import Menu from './components/menu/menu'
import Register from './components/register/register'
import DashboardClient from './components/dashboard-client/dashboard-client'
import DashboardBusiness from './components/dashboard-business/dashboard-business'

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
                    />
                    <DashboardClient
                        path="/home-client"
                        openCloseMenu={this.openCloseMenu}
                    />
                    <DashboardBusiness
                        path="/home-business"
                    />
                </Router>
            </div>
        )
    }
}

export default App;
