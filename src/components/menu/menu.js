import React from 'react'

import './menu.css'

class Menu extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            style : {
                position: 'absolute',
                top: -500,
                opacity: 0,
                transition: 'all 2s ease',
            }
        }

        this.mountStyle = this.mountStyle.bind(this)
        this.unMountStyle = this.unMountStyle.bind(this)
    }

    componentDidMount(){
        setTimeout(this.mountStyle, 10)
    }

    mountStyle() {
        this.setState({
            style: {
                top: 0,
                opacity: 1,
                transition: 'all 1s ease',
            }
        })
    }

    unMountStyle() {
        this.setState({
            style: {
                opacity: 0,
                transition: 'all 1s ease',
            }
        })
    }

    render() {
        return (
            <div className="menu-container" style={this.state.style}>
                <div className="menu">
                    <button onClick={this.props.openCloseMenu}>close</button>
                    <p>test</p>
                </div>
            </div>
        )
    }
}

export default Menu;
