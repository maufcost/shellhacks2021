import React from 'react';

import Header from '../header/header'

import './success.css'

class Success extends React.Component {
    render() {
        return (
            <div className="success-container">
                <div className="success auto">
                    <Header openCloseMenu={this.props.openCloseMenu} />
                    <h1>Your order was <span className="gimme-border">successfully</span> processed! <span className="rotate">🎉</span></h1>
                    <p className="s">You just ordered Sally's Peanut Butter Burger from:</p>
                    <div className="owner">
                        <img src={"https://firebasestorage.googleapis.com/v0/b/test-385af.appspot.com/o/Screen%20Shot%202021-09-24%20at%2022.01.58.png?alt=media&token=f8fede94-0ca2-4fa9-b04d-5993d2049446"} />
                        <p className="name">Sally's Brewing Corner</p>
                    </div>
                </div>
            </div>
        )
    }
}

// class Success extends React.Component {
//     render() {
//         return (
//             <div className="success-container">
//                 <div className="success margin">
//                     <Header openCloseMenu={this.openCloseMenu} />
//                     <h1>Your order was successfully processed! 🎉</h1>
//                     <p>You just ordered {this.props.order}</p>
//                     <div className="owner">
//                         <img src={this.props.owner} />
//                         <p className="name">{name}</p>
//                     </div>
//                 </div>
//             </div>
//         )
//     }
// }

export default Success;
