import React, { Component } from 'react';
import './App.css';

import Chat from './Chat';

class App extends Component {

  constructor() {
    super();
    this.state = {};
  }

  render() {
    return (
      <div className="App">
          <div className="container">
              <Chat/>
          </div>
      </div>
    );
  }
}

export default App;