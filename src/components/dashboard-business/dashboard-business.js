import React from 'react'

import '../../dashboard.css'

class DashboardBusiness extends React.Component {
    componentDidMount() {
        console.log('dashboard business mounted')
    }

    componentWillUnmount() {
        console.log('dashboard business UNmounted')
    }

    render() {
        return (
            <div className="dashboard-business-container">
                <div className="dashboard auto">
                </div>
            </div>
        )
    }
}

export default DashboardBusiness;
