import React, { Component, PropTypes } from 'react';
import Board from './Board';
import './Game.css';

class Game extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: []
    };
  }

  getInitialBoard = () => {
    return fetch('http://localhost:5000/api/square')
    .then(response => response.json())
    .then((json) => {
      json.shouldResetValue = true;
      this.setState({ data: json });
      return json;
    });
  }

  render() {
    return (
      <div>
        <div className="buttons">
          <button
            onClick={this.getInitialBoard}
            className="request-data-button"
          >
            {'Request new board state'}
          </button>
          <button
            onClick={this.getInitialBoard}
            className="send-data-button"
          >
            {'Send data'}
          </button>
        </div>
        <Board data={this.state.data} />
      </div>
    );
  }
}

Board.propTypes = {
  boardWidth: PropTypes.number,
  boardHeight: PropTypes.number
};

export default Game;
