import React, { Component, PropTypes } from 'react';
import * as _ from 'lodash';
import Square from './Square';
import * as Constants from './Constants';
import './Board.css';

class Board extends Component {
  constructor(props) {
    super(props);
    this.state = {
      squares: [],
      data: [],
      currentData: new Array(Constants.boardWidth * Constants.boardHeight),
      turn: ''
    };
  }

  componentWillMount() {
    const squares = [];
    const boardSize = Constants.boardWidth * Constants.boardHeight;
    for (let i = 0; i < boardSize; i++) {
      squares.push(this.renderSquare(i));
    }
    this.setState({ squares });
    this.getNewBoard();
    this.fetchPlayerTurn();
  }


  getNewBoard = () => {
    return this.fetchData().then(() => {
      const squares = [];
      const boardSize = Constants.boardWidth * Constants.boardHeight;
      for (let i = 0; i < boardSize; i++) {
        squares.push(this.renderSquare(i));
      }
      this.setState({ squares });
      return 'OK';
    });
  }

  getUpdatedSquareData = (squareData) => {
    const index = squareData.x + (squareData.y * 15);
    this.state.currentData[index] = squareData;
  }

  sleep = (ms) => {
    return new Promise((resolve) => {
      setTimeout(resolve, ms);
    });
  }

  fetchData = () => {
    return fetch('http://localhost:5000/api/square')
    .then((response) => {
      return response.json();
    })
    .then((json) => {
      this.setState({ data: json });
      return json;
    });
  }

  changePlayerTurn = () => {
    return fetch('http://localhost:5000/api/turn', {
      method: 'put',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json'
      },
      body: {}
    })
    .then(response => response.json())
    .then((json) => {
      this.setState({ turn: json.turn });
      return this.state.turn;
    });
  }

  fetchPlayerTurn = () => {
    return fetch('http://localhost:5000/api/turn')
    .then(response => response.json())
    .then((json) => {
      this.setState({ playerTurn: json.turn });
      return json;
    });
  }

  renderSquare(i) {
    const black = (i % 2 === 0);
    const squares = this.state.data;
    for (let j = 0; j < squares.length; j++) {
      const square = squares[j];
      if (square !== undefined && square.x === (i % 15) && square.y === Math.floor(i / 15)) {
        return (
          <div key={i}>
            <Square
              black={black}
              data={square}
              sendData={this.getUpdatedSquareData}
            />
          </div>
        );
      }
    }
    return (
      <div key={i}>
        <Square
          black={black}
          sendData={this.getUpdatedSquareData}
        />
      </div>
    );
  }

  sendUpdatedData = (data) => {
    // const myHeaders = new Headers();
    return this.fetchPlayerTurn()
    .then((playerPlaying) => {
      data.species = Constants.revertDictSpecies[playerPlaying.turn];
      return fetch('http://localhost:5000/api/square', {
        method: 'post',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
    });
  }

  sendAllUpdatedData = () => {
    const component = this
    const dataToSend = _.filter(this.state.currentData, function (o) { return o !== undefined; });
    return Promise.all(_.forEach(dataToSend, function (data) {
      return component.sendUpdatedData(data);
    }))
    .then(() => {
      // return this.getNewBoard()
      return this.changePlayerTurn();
    });
  }

  render() {
    let boardWidth = Constants.boardWidth * (Constants.squareSideLength + (Constants.squareBorderWidth * 2));
    boardWidth = String(boardWidth) + 'px';
    let boardHeight = Constants.boardHeight * (Constants.squareSideLength + (Constants.squareBorderWidth * 2));
    boardHeight = String(boardWidth) + 'px';
    return (
      <div>
        <div className="buttons">
          <button
            onClick={this.getNewBoard}
            className="request-data-button"
          >
            {'Request new board state'}
          </button>
          <button
            onClick={this.sendAllUpdatedData}
            className="send-data-button"
          >
            {'Send data'}
          </button>
        </div>
        <div
          style={{
            width: boardWidth,
            height: boardHeight,
            display: 'flex',
            flexWrap: 'wrap',
            border: 'black'
          }}
        >
          {this.state.squares}
        </div>
      </div>
    );
  }
}

Board.propTypes = {
  boardWidth: PropTypes.number,
  boardHeight: PropTypes.number,
};

export default Board;
