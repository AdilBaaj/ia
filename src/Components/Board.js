import React, { Component, PropTypes } from 'react';
import * as _ from 'lodash';
import Square from './Square';
import * as Constants from './Constants';
import './Board.css';


class Board extends Component {
  constructor(props) {
    super(props);
    this.state = {
      squares: new Array(Constants.boardWidth * Constants.boardHeight),
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
    return this.fetchBoardState().then((listSquareData) => {
      listSquareData = listSquareData.sort(this.compareSquareOrder)
      const squares = []
      for (var i=0; i <  listSquareData.length; i++) {
        squares.push(this.renderSquare(listSquareData[i]));
      }
      this.setState({ squares: squares.sort(this.compareSquareOrder) });
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
  fetchBoardState = () => {
    return fetch('http://localhost:8085/api/square')
    .then((response) => {
      return response.json();
    })
  }


  // TODO : put in utils
  computeIndexFromCoordinates = (x, y) => {
    return (x * Constants.boardHeight) + y;
  }


  // TODO : put in utils
  compareSquareOrder = (a, b) => {
    return this.computeIndexFromCoordinates(a.x, a.y) - this.computeIndexFromCoordinates(b.x, b.y)
  }


  updateSquare = (index, updatedSquare) => {
    let square = this.state.squares[index]
    square.nb = updatedSquare.nb
    square.species = updatedSquare.species // data not defined
  }


  updateSquares = (listUpdatedSquares) => {
    let squares = this.state.squares
    for(let i = 0; i < listUpdatedSquares.length; i++){ 
      const updatedSquare = listUpdatedSquares[i]
      const index = this.computeIndexFromCoordinates(updatedSquare.x, updatedSquare.y)
      squares[index] = this.updateSquare(index, updatedSquare)
    }
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


  renderSquare = (squareData) => {
    const squareIndex = this.computeIndexFromCoordinates(squareData.x, squareData.y)
    return (<div key={squareIndex}>
      <Square
        data={squareData}
        sendData={this.getUpdatedSquareData}
      />
    </div>);
  }

  computeAndDisplayNewBoard = () => {
    const component = this;
    const data = {};
    data.squares = this.state.modifiedSquares;
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
