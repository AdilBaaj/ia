import React, { Component, PropTypes } from 'react';
import * as Constants from './Constants'
import './Square.css';

export default class Square extends Component {
  render() {
    const vampiresColor = '#0052cc'
    const humanColor = '#ce9613'
    const werewolvesColor = '#00802b'
    let backgroundColor = '#52527a'

    if(this.props.species === 'vampires') {
      backgroundColor = vampiresColor
    } else if (this.props.species === 'werewolves') {
      backgroundColor = werewolvesColor
    } else if (this.props.species === 'human') {
      backgroundColor = humanColor
    }

    return (
      <div className='square'>
        <input style={{
          backgroundColor: backgroundColor,
          width: Constants.squareSideLength,
          height: Constants.squareSideLength,
          border: `${Constants.squareBorderWidth}px solid`,
          padding: '0',
          color: 'black'
        }} />
      </div>
    );
  }
}

Square.propTypes = {
  species: PropTypes.string
};
