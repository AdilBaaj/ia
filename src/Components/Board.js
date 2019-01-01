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
      modifiedSquares: [],
      turn: undefined
    };
  }


  componentWillMount() {
    const squares = [];
    const boardSize = Constants.boardWidth * Constants.boardHeight;

    // Querying data from api
    this.displayInitialBoard().then(() => {
      this.fetchPlayerTurn();
    })
  }


  displayInitialBoard = () => {
    return this.fetchInitialBoardState().then(() => {
      const squares = [];
      const boardSize = Constants.boardWidth * Constants.boardHeight;
      for (let i = 0; i < boardSize; i++) {
        squares.push(this.renderSquare(i));
      }
      this.setState({ squares });
    })
  }


  getUpdatedSquareData = (squareData) => {
    if (squareData && squareData.nb) {
      this.setState({
        modifiedSquares : this.state.modifiedSquares.concat(squareData)
      });
    }
  }


  // TODO : put within a saga
  fetchInitialBoardState = () => {
    return fetch('http://localhost:8085/api/square')
    .then((response) => {
      return response.json();
    })
    .then((updatedSquares) => {
      squares = this.state.squares
      for (square in updatedSquares) {
        const index = computeIndexFromCoordinates(square.x, square.y)
        squares[index] = square
      }
      this.setState({ squares });
    });
  }


  // TODO : put in utils
  computeIndexFromCoordinates = (x, y) => {
    return squareData.x + (squareData.y * Constants.boardWidth);
  }


  updateSquare = (index, updatedSquare) => {
    square = this.state.squares[index]
    square.nb = updatedSquare.nb
    square.species = data.species
    return square
  }


  updateSquares = (listUpdatedSquares) => {
    squares = this.state.squares
    for(updatedSquare in listUpdatedSquares){
      index = this.computeIndexFromCoordinates(updatedSquare.x, updatedSquare.y)
      squares[index] = this.updateSquare(index, v)
    }
    this.setState({ squares });
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


  renderSquare = (squareIndex) => {
    return (<div key={squareIndex}>
      <Square
        data={this.state.data[squareIndex]}
        sendData={this.getUpdatedSquareData}
      />
    </div>);
  }

  computeAndDisplayNewBoard = () => {
    const component = this;
    const data = {};
    data.squares = squares;
    fetch('http://localhost:8085/api/square', {
      method: 'post',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    }).then((listOfUpdatedSquares) => {
      component.updateSquares(listOfUpdatedSquares)
      component.setState({ modifiedSquares: [] })
      component.changePlayerTurn();
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
            onClick={this.computeAndDisplayNewBoard}
            className="send-data-button"
          >
            {'Compute new board state'}
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
