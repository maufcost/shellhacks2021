import React from 'react'
import { navigate } from '@reach/router'

import './business.css'

class Business extends React.Component {
    go() {
        navigate('/purchase')
    }

    render() {
        const { imgURL, name, money } = this.props.business

        return (
            <div className="business-container">
                <div className="business">
                    <div className="hug">
                        <img src={imgURL} />
                    </div>
                    <p className="name">{name}</p>
                    <footer>
                        <p>{money}</p>
                        <button onClick={this.go}>Go</button>
                    </footer>
                </div>
            </div>
        )
    }
}

export default Business;
