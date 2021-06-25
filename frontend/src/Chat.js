import React, { Component } from 'react';
import Message from './Message';
import config from './config';

class Chat extends Component {
  constructor(props) {
    super(props);
    this.form = React.createRef();
    this.state = {
        token: '',
        messages: []
    };
  }

//   componentDidMount() {
//     console.log('Creds in chat: ',this.props.creds);
//     // fetch current messages
//     const url = config.baseUrl + config.api + config.messagesRoute;
//     const reqData = {
//       method: 'GET',
//       headers: {
//         'Content-type': 'application/json',
//         'token': this.props.creds.token
//       },
//       mode: 'cors'
//     }

//     fetch(url, reqData)
//       .then(res => res.json())
//       .then(res => {
//         if (!('error' in res)) {
//           this.setState({messages: res})
//         }
//       })
//       .catch(err => console.log(err));
//   }

  handleSubmit = e => {
    e.preventDefault();

    const payload = {
      token: this.state.token,
      message: this.message.value
    };

    console.log(payload);
    console.log(document.location.host);

    const url = config.baseUrl + config.api + config.messageRoute;
    const reqData = {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(payload),
    };

    this.form.current.reset();

    fetch(url, reqData)
      .then(res => res.json())
      .then(res => {
        console.log(res);
        this.setState(prevState => ({
            messages: [...prevState.messages, ...res.messages]
        }));
      })
      .catch(err => console.log('Error: ', err));
  }

  componentDidUpdate(prevProps) {
    document.querySelector('.message-li:last-child').scrollIntoView();
  }

  render () {
    return (
      <div>
        <h2>Chatbot gợi ý nhạc</h2>
        <ul id="messages">
          {this.state.messages.map(msg =>
            <Message
              username={msg.username}
              timeStamp={msg.timestamp}
              message={msg.message}
            />
          )}
        </ul>
        <form id="chat-message-form" onSubmit={e => e.preventDefault()} ref={this.form} >
          <input id="message-input-field" type="text" placeholder="Soạn câu hỏi cho mình ở đây nhé ^^" ref={input => this.message=input} />
          <button id="send-message-btn" onClick={this.handleSubmit}>Gửi</button>
        </form>
      </div>
    );
  }
}

export default Chat;
