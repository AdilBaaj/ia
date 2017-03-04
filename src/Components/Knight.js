import React, { Component, PropTypes } from 'react';

class Knight extends Component {
  render() {
    return (
      <div style={{
        fontSize: 25,
        fontWeight: 'bold',
        cursor: 'move'
      }}>
        ♘
      </div>
    );
  }
}

Knight.propTypes = {

};

export default Knight;
