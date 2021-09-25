import React from 'react'
import Header from '../header/header'
import { v4 as uuidv4 } from 'uuid';
import Slider, { createSliderWithTooltip } from "rc-slider";
import { LineChart, Line, CartesianGrid, XAxis, YAxis } from 'recharts';

import ETHCoin from '../../global-assets/eth.svg'
import BTCCoin from '../../global-assets/btc.svg'
import XRPCoin from '../../global-assets/xrp.svg'
import Bot1 from '../../global-assets/bot1.png'
import Bot2 from '../../global-assets/bot2.png'
import Bot3 from '../../global-assets/bot3.png'

import 'rc-slider/assets/index.css';
import './my-tradings.css'

class MyTradings extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            // bot: 'something',
            bot: null,
            sliderValue: 2,
            transactions: [
                {
                    buy: 123,
                    sell: 456,
                    investment: 87,
                    coin: 'ETH'
                },
                {
                    buy: 123,
                    sell: 456,
                    investment: 87,
                    coin: 'XRP'
                },
                {
                    buy: 123,
                    sell: 456,
                    investment: 87,
                    coin: 'BTC'
                },
                {
                    buy: 123,
                    sell: 456,
                    investment: 87,
                    coin: 'ETH'
                },
            ],
            // FALSE for clients
            // TRUE for businesses
            isBusinessAccount: true,
        }

        this.pickBot = this.pickBot.bind(this)
        this.onSliderChange = this.onSliderChange.bind(this)
    }

    pickBot(bot) {
        this.setState({ bot })
    }

    onSliderChange(sliderValue) {
        this.setState({ sliderValue })
    }

    render() {
        // For the list of transactions
        let transactions = <p>Your bot has not made any transactions yet</p>
        const alreadyChoseABot = this.state.bot !== null && this.state.transactions && this.state.transactions.length > 0
        if (alreadyChoseABot) {
            // Then, we have already chosen a bot!
            transactions = this.state.transactions.map(t => {

                let icon = ETHCoin
                if (t.coin === "ETH") {
                    icon = ETHCoin
                }else if (t.coin === "BTC") {
                    icon = BTCCoin
                }else if (t.coin === "XRP") {
                    icon = XRPCoin
                }

                // return <Trade icon={icon} t={t} key={uuidv4()} />
                return (
                    <div className="transaction" key={uuidv4()}>
                        <img src={icon} />
                        <p className="buy">{t.buy}</p>
                        <p className="sell">{t.sell}</p>
                        <p className="inv">${t.investment}</p>
                    </div>
                )
            })
        }

        // For the graph
        const data = [
            {name: '4 days ago', uv: 400, pv: 2400, amt: 2400},
            {name: '3 days ago', uv: 100, pv: 2400, amt: 2400},
            {name: '2 days ago', uv: 300, pv: 2400, amt: 2400},
            {name: 'yesterday', uv: 200, pv: 2400, amt: 2400},
            {name: 'today', uv: 200, pv: 2400, amt: 2400},
        ];

        return (
            <div className="my-tradings-container">
                <div className="my-tradings auto">
                    <Header openCloseMenu={this.props.openCloseMenu} />
                    {this.state.isBusinessAccount && (
                        <div className="revenue-today">
                            <div className="header">
                                <div className="neon-orange"></div>
                                <h2 className="title">Today's revenue:</h2>
                            </div>
                            <p className="revenue gimme-border">$1,922.12</p>
                            <p className="subtitle">Pick how much of today's revenue you'd like to invest on your portfolio:</p>
                            <div className="slider-area">
                                <Slider
                                    min={2}
                                    max={50}
                                    value={this.state.sliderValue}
                                    onChange={this.onSliderChange}
                                    railStyle={{ height: 2 }}
                                    handleStyle={{
                                        height: 28,
                                        width: 28,
                                        marginLeft: 14,
                                        marginTop: -14,
                                        marginRight: 20,
                                        backgroundColor: "#e58333",
                                        border: 0
                                    }}
                                    trackStyle={{
                                        background: "none"
                                    }}
                                />
                                <p>{this.state.sliderValue} %</p>
                            </div>
                        </div>
                    )}

                    <div className="intro">
                        <div className="top">
                            <div className="neon-orange animate"></div>
                            <h2 className="title">My tradings</h2>
                        </div>
                        <p className="subtitle">Here you can see your crypto profits based on your purchases/sales.</p>
                    </div>

                    <div className="graph">
                        <LineChart width={300} height={200} data={data} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
                            <Line type="monotone" dataKey="uv" stroke="#e58333" />
                            <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
                            <XAxis dataKey="name" />
                            <YAxis />
                        </LineChart>
                    </div>

                    {alreadyChoseABot ? (
                        <div className="transactions">
                            <div className="top">
                                <div className="neon-orange"></div>
                                <h2 className="title">Last transactions</h2>
                            </div>
                            <p className="subtitle">These are your real-time transactions performed by the bot you picked</p>
                            <div className="transactions-header">
                                <p>Coin</p>
                                <p className="b">Buy</p>
                                <p className="s">Sell</p>
                                <p>Invested</p>
                            </div>
                            <div className="list">{transactions}</div>
                        </div>
                    ) : (
                        <div className="pick">
                            <h2 className="pick-title">
                                <div className="neon-orange"></div>
                                Pick your bot
                            </h2>
                            <p className="subtitle">We will automatically trade for you. Feel free to chillax.</p>
                            <div className="bots">
                                <div className="bot">
                                    <img src={Bot1} />
                                    <p className="bot-name">David, The Conqueror I</p>
                                    <p className="bot-desc">Uses a divide and conquer approach with his own grid bot capabilities</p>
                                    <button className="pick-bot" onClick={() => this.pickBot('bot1')}>Pick</button>
                                </div>

                                <div className="bot">
                                    <img src={Bot2} />
                                    <p className="bot-name">Lilian Regrex</p>
                                    <p className="bot-desc">Lilian uses linear regression to predict ETH prices in real time.</p>
                                    <button className="pick-bot" onClick={() => this.pickBot('bot2')}>Pick</button>
                                </div>

                                <div className="bot">
                                    <img src={Bot3} />
                                    <p className="bot-name">Bae Bae</p>
                                    <p className="bot-desc">Bae Bae uses past technical indicators to indicate if a coin is worth buying or selling.</p>
                                    <button className="pick-bot" onClick={() => this.pickBot('bot3')}>Pick</button>
                                </div>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        )
    }
}


export default MyTradings
