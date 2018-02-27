import React from 'react';
import Square from '../Components/Square';


export function renderSquare(i) {
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
