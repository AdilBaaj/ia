import React, { Component, PropTypes } from 'react';
import Board from './Board';

class Game extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  componentWillMount() {
    this.getInitialBoard()
  }

  getInitialBoard() {

    return fetch('http://localhost:5000/api/square')
    .then((response) => {
      console.log(response)
      return response
    });
  }

  render() {
    return (
      <Board />
    );
  }
}

Board.propTypes = {
  boardWidth: PropTypes.number,
  boardHeight: PropTypes.number
};

export default Game;
