import React from 'react';
import timeStamp2str from './utils';

const Message = ({username, timeStamp, message}) => {

  return (
    <li className="message-li">
      <div className="username">{username}</div>
      <div className="timeStamp">{timeStamp2str(timeStamp)}</div>
      <div className="message-text">{message}</div>
    </li>
  );
}

export default Message;
