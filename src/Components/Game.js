import React, { Component, PropTypes } from 'react';
import Board from './Board';

class Game extends Component {

  submit() {
    return $.getJSON('http://localhost.me/api/')
      .then((data) => {
        this.setState({ person: data.results });
      });
  }

  render() {
    return (
      <div>
        <button
        onClick =
        >
        </button>
        <Board />
      </div>

    );
  }
}

Board.propTypes = {
  boardWidth: PropTypes.number,
  boardHeight: PropTypes.number
};

export default Game;
