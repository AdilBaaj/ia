import React, { Component, PropTypes } from 'react';
import Square from './Square';
import * as Constants from './Constants';

class Board extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: {}
    };
  }

  renderSquare(i) {
    const black = (i % 2 === 0);
    if (typeof this.props.data.nb === 'number') {
      if (this.props.data.x === (i % 15) && this.props.data.y === Math.floor(i / 15)) {
        console.log(this.props.data)
        return (
          <div key={i}>
            <Square
              black={black}
              data={this.props.data}
            />
          </div>
        );
      }
    }
    return (
      <div key={i}>
        <Square
          black={black}
        />
      </div>
    );
  }

  render() {
    const squares = [];
    const boardSize = Constants.boardWidth * Constants.boardHeight

    for (let i = 0; i < boardSize; i++) {
      squares.push(this.renderSquare(i));
    }
    let boardWidth = Constants.boardWidth * (Constants.squareSideLength + (Constants.squareBorderWidth * 2));
    boardWidth = String(boardWidth) + 'px';
    let boardHeight = Constants.boardHeight * (Constants.squareSideLength + (Constants.squareBorderWidth * 2));
    boardHeight = String(boardWidth) + 'px';
    return (
      <div
        style={{
          width: boardWidth,
          height: boardHeight,
          display: 'flex',
          flexWrap: 'wrap',
          border: 'black'
        }}
      >
        {squares}
      </div>
    );
  }
}

Board.propTypes = {
  boardWidth: PropTypes.number,
  boardHeight: PropTypes.number,
  data: PropTypes.object
};

export default Board;
