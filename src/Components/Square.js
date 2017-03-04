import React, { Component, PropTypes } from 'react';
import * as Constants from './Constants'

export default class Square extends Component {
  render() {
    const black = this.props.black;
    const fill = black ? 'black' : 'white';

    return (
      <div style={{
        backgroundColor: fill,
        width: Constants.squareSideLength,
        height: Constants.squareSideLength
      }}>
        {this.props.children}
      </div>
    );
  }
}

Square.propTypes = {
  black: PropTypes.bool
};
