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
      squares.push(
        <div key={i}>
          <Square
            sendData={this.getUpdatedSquareData}
          />
        </div>
      );
    }
    this.setState({ squares });
    this.getNewBoard();
    this.fetchPlayerTurn();
  }


  getNewBoard = () => {
    this.fetchData().then(() => {
      const squares = [];
      const boardSize = Constants.boardWidth * Constants.boardHeight;
      for (let i = 0; i < boardSize; i++) {
        squares.push(this.renderSquare(i));
      }
      this.setState({ squares });
    });
  }

  getUpdatedSquareData = (squareData) => {
    const index = squareData.x + (squareData.y * 15);
    this.state.currentData[index] = squareData;
  }


  fetchData = () => {
    return fetch('http://localhost:8085/api/square')
    .then((response) => {
      return response.json();
    })
    .then((json) => {
      this.setState({ data: json });
      return json;
    });
  }

  changePlayerTurn = () => {
    return fetch('http://localhost:8085/api/turn', {
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
    return fetch('http://localhost:8085/api/turn')
    .then(response => response.json())
    .then((json) => {
      this.setState({ playerTurn: json.turn } );
      return json;
    });
  }

  renderSquare = (i) => {
    return (<div key={i}>
      <Square
        data={this.state.data[i]}
        sendData={this.getUpdatedSquareData}
      />
    </div>);
  }

  sendAllUpdatedData = () => {
    const component = this;
    const squares = _.filter(this.state.currentData, function (o) { return o !== undefined; });
    return this.fetchPlayerTurn()
    .then((playerPlaying) => {
      const data = {};
      data.species = Constants.speciesToId[playerPlaying.turn];
      data.squares = squares;
      return fetch('http://localhost:8085/api/square', {
        method: 'post',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
    })
    .then(() => {
      component.resetCurrentData()
      return component.changePlayerTurn();
    });
  }

  resetCurrentData = () => {
    const component = this;
    component.state.currentData = new Array(Constants.boardWidth * Constants.boardHeight)
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
