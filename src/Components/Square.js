import React, { Component, PropTypes } from 'react';
import * as Constants from './Constants';
import './Square.css';

export default class Square extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: {},
      value: ''
    };
  }

  setValue = (event) => {
    this.setState({
      value: event.target.value
    });

    const squareData = {
      x: this.props.data.x,
      y: this.props.data.y,
      species: this.props.data.species,
      nb: event.target.value
    };
    this.props.sendData(squareData);
  }

  resetValue = () => {
    this.setState({
      value: ''
    });
  }

  render() {
    let backgroundColor = '#52527a';

    if (this.props.data && this.props.data.species) {
      const species = Constants.species[this.props.data.species];
      if (species === 'vampires') {
        backgroundColor = Constants.vampiresColor;
      } else if (species === 'werewolves') {
        backgroundColor = Constants.werewolvesColor;
      } else {
        backgroundColor = Constants.humanColor;
      }
    }

    let defaultValue = '';
    if (this.props.data && this.props.data.nb) {
      defaultValue = this.props.data.nb;
    }

    return (
      <div className="square">
        <input
          placeholder={defaultValue}
          value={this.state.value}
          style={{
            backgroundColor: backgroundColor,
            width: Constants.squareSideLength,
            height: Constants.squareSideLength,
            border: `${Constants.squareBorderWidth}px solid`,
            padding: '0',
            color: 'black',
          }}
          onChange={this.setValue}
        />
      </div>
    );
  }
}

Square.propTypes = {
  data: PropTypes.object,
  shouldResetValue: PropTypes.bool,
  value: PropTypes.string,
  sendData: PropTypes.func
};
