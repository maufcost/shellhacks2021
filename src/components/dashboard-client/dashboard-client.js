import React from 'react'
import { v4 as uuidv4 } from 'uuid';
import { SAMPLE_USER } from '../../utils'

import Business from '../business/business'

import HB from '../../global-assets/hb.svg'

import '../../dashboard.css'

class DashboardClient extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            search: '',
            // @TODO: transfer to firebase (we should be retrieving these link
            // and business names)
            // businesses: [],
            businesses: [
                {
                    imgURL: "https://firebasestorage.googleapis.com/v0/b/test-385af.appspot.com/o/Screen%20Shot%202021-09-24%20at%2022.01.58.png?alt=media&token=f8fede94-0ca2-4fa9-b04d-5993d2049446",
                    name: "Sally's Brewing Corner",
                    money: "$$$"
                },
                {
                    imgURL: "https://firebasestorage.googleapis.com/v0/b/test-385af.appspot.com/o/Screen%20Shot%202021-09-24%20at%2022.02.28.png?alt=media&token=c493c0db-15f9-4b65-bf60-34be2ef8f26c",
                    name: "Burger Ger Ger",
                    money: "$$"
                },
                {
                    imgURL: "https://firebasestorage.googleapis.com/v0/b/test-385af.appspot.com/o/Screen%20Shot%202021-09-24%20at%2022.04.00.png?alt=media&token=98bea15b-f9c2-4574-8402-b1e97e29c556",
                    name: "Sensei Power Temakis",
                    money: "$"
                },
                {
                    imgURL: "https://firebasestorage.googleapis.com/v0/b/test-385af.appspot.com/o/Screen%20Shot%202021-09-24%20at%2022.02.42.png?alt=media&token=ad02a579-bd94-4c89-a64b-6cd2531a83ee",
                    name: "Pastries du Moi",
                    money: "$$$"
                },
                {
                    imgURL: "https://firebasestorage.googleapis.com/v0/b/test-385af.appspot.com/o/Screen%20Shot%202021-09-24%20at%2022.02.11.png?alt=media&token=f9838b34-667e-41b2-a69e-1de2aa071a0e",
                    name: "Alfred's Afternoon Coffee",
                    money: "$$"
                },
                {
                    imgURL: "https://firebasestorage.googleapis.com/v0/b/test-385af.appspot.com/o/Screen%20Shot%202021-09-24%20at%2022.10.22.png?alt=media&token=709ccdfa-149a-4cba-80cc-0f4c1872bccf",
                    name: "Cat Library by Ashley",
                    money: "$"
                },
                {
                    imgURL: "https://firebasestorage.googleapis.com/v0/b/test-385af.appspot.com/o/Screen%20Shot%202021-09-24%20at%2022.03.06.png?alt=media&token=8b1d8763-9f15-4a03-a4a0-061e7ccf6c5d",
                    name: "Sun Moon Sushi",
                    money: "$$$"
                }
            ]
        }

        this.onChangeSearch = this.onChangeSearch.bind(this)
    }

    onChangeSearch(e) {
        const search = e.target.value
        this.setState({ search })
    }

    render() {
        // Getting businesses currently registered on the app
        let businessList = <p>Loading...</p>
        const bs = this.state.businesses
        if (bs && bs.length > 0) {
            businessList = bs.map(b => {
                return (
                    <Business key={uuidv4()} business={b}/>
                )
            })
        }

        return (
            <div className="dashboard-client-container">
                <div className="dashboard auto">
                    <div className="nav">
                        <img
                            className="hamburguer"
                            src={HB}
                            alt="Menu"
                            onClick={this.props.openCloseMenu}
                        />
                        <p>logo</p>
                        <img className="user-img" src={SAMPLE_USER} />
                    </div>
                    <header>
                        <h1>The best combination: <span className="gimme-border">local business shopping</span> and <span className="gimme-border">crypto</span></h1>
                        <input
                            className="search-input"
                            type="text"
                            placeholder="Search businesses near you"
                            value={this.state.search}
                            onChange={this.onChangeSearch}
                        />
                    </header>
                    <h2 className="subtitle">Browse local businesses</h2>
                    <div className="businesses">
                        {businessList}
                    </div>
                </div>
            </div>
        )
    }
}

export default DashboardClient;
