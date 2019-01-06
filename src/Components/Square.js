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
    let backgroundColor;

    if (this.props.data && this.props.data.species) {
      const species = this.props.data.species;
      if (species === Constants.species.VAMPIRE) {
        backgroundColor = Constants.vampiresColor;
      } else if (species === Constants.species.WEREWOLF) {
        backgroundColor = Constants.werewolvesColor;
      } else if (species === Constants.species.HUMAN) {
        backgroundColor = Constants.humanColor;
      } else {
        backgroundColor = Constants.emptyColor;
      }
    }

    let defaultValue = '';
    if (this.props.data && this.props.data.nb) {
      defaultValue = this.props.data.nb;
    }

    let style = {
      backgroundColor,
      width: Constants.squareSideLength,
      height: Constants.squareSideLength,
      border: `${Constants.squareBorderWidth}px solid`,
      padding: '0',
      color: 'black'
    }

    return (
      <div className="square">
        <input
          placeholder={defaultValue}
          value={this.state.value}
          style={style}
          onChange={this.setValue}
        />
      </div>
    );
  }
}

Square.propTypes = {
  data: PropTypes.object,
  sendData: PropTypes.func
};
