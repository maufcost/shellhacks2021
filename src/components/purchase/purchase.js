import React from 'react'
import { navigate } from '@reach/router'

import Header from '../header/header'

import HBPNG from '../../global-assets/hb_png.png'
import FishPNG from '../../global-assets/fish.png'

import './purchase.css'

class Purchase extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            isBuying: false,
            addr: '',
            loading: false
        }

        this.buying = this.buying.bind(this)
        this.processPurchase = this.processPurchase.bind(this)
    }

    buying() {
        this.setState({ isBuying: !this.state.isBuying });
    }

    processPurchase() {
        window.scrollTo(0, 0);
        this.setState({ loading: true })
        setTimeout(() => {
            navigate('/success')
        }, 4500)
    }

    render() {
        return (
            <div className="purchase-container">
                {this.state.loading && <div className="loading"><span>⌛</span> Loading...</div>}
                <div className="purchase auto">
                    <Header openCloseMenu={this.props.openCloseMenu} />
                    <header>
                        <div className="neon-orange animate"></div>
                        <p>Shopping at Sally's Burger</p>
                    </header>

                    <div className="product">
                        <img src={HBPNG} className="product-image" />
                        <h2>Sally's Peanut Butter Burger</h2>
                        <p className="description">Tasty, delicious, local and has everyone craving more on the first bite.
                        Includes
                        Cheddar cheese, onions with cinnamon, a huge burger, and ketchup.</p>
                        <footer>
                            <div className="owner">
                                <img className="owner-image" src={"https://firebasestorage.googleapis.com/v0/b/test-385af.appspot.com/o/Screen%20Shot%202021-09-24%20at%2022.01.58.png?alt=media&token=f8fede94-0ca2-4fa9-b04d-5993d2049446"} />
                                <p>By Sally's Burger</p>
                            </div>
                            <div className="btn-area">
                                <button onClick={this.buying}>
                                    {this.state.isBuying ? (
                                        <span>x Cancel order</span>
                                    ) : (
                                        <span>Buy for MIA 0.0049</span>
                                    )}
                                </button>
                                <p>Approx. $12.56</p>
                            </div>
                        </footer>
                        {this.state.isBuying && (
                            <div className="is-buying">
                                <p className="t">Hello <span className="rotate">👋</span> Let me help you. What's your wallet address?</p>
                                <p className="s">We will process your order shortly</p>
                                <div className="form">
                                    <input
                                        type="text"
                                        value={this.state.addr}
                                        placeholder="E.g. 2713ybsF1ibs9127bXS"
                                        onChange={(e) => this.setState({ addr: e.target.value })}
                                    />
                                    <button onClick={this.processPurchase}>Buy</button>
                                </div>
                            </div>
                        )}
                    </div>

                    <div className="product">
                        <img src={FishPNG} className="product-image" />
                        <h2>Sally's Salmon Burger</h2>
                        <p className="description">It is juicy, mouthwatering, tasty, and everything you’d ever want to savor. Includes
                        Cheddar cheese, onions with cinnamon, a huge burger, and ketchup.</p>
                        <footer>
                            <div className="owner">
                                <img className="owner-image" src={"https://firebasestorage.googleapis.com/v0/b/test-385af.appspot.com/o/Screen%20Shot%202021-09-24%20at%2022.01.58.png?alt=media&token=f8fede94-0ca2-4fa9-b04d-5993d2049446"} />
                                <p>By Sally's Burger</p>
                            </div>
                            <div className="btn-area">
                                <button onClick={this.buying}>Buy for MIA 0.0012</button>
                                <p>Approx. $19.96</p>
                            </div>
                        </footer>
                    </div>
                </div>
            </div>
        )
    }
}

export default Purchase
