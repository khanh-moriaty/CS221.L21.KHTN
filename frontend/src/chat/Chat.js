import React from 'react';

import { makeStyles } from '@material-ui/core/styles';
import { Box, InputBase, IconButton } from '@material-ui/core';
import SendIcon from '@material-ui/icons/Send';

import Draggable from 'react-draggable';
import { Scrollbars } from 'react-custom-scrollbars';

import Message from './Message';
import MessageLoading from './MessageLoading';
import MessageMedia from './MessageMedia';

const useStyles = makeStyles(theme => ({
    root: {
        width: '60vw',
        height: '80vh',
        [theme.breakpoints.down("xs")]: {
            width: '100%',
            height: '90vh',
        },
        background: '#E8D7FFa0',
        boxShadow: '0 8px 32px 0 rgba( 31, 38, 135, 0.37 )',
        backdropFilter: 'blur( 12.0pt )',
        borderRadius: '2.5vh',
        border: '1px solid #E8D7FF32'
    },
    header: {
        height: '64pt',
        textAlign: 'left',
        padding: '1.5% 0 1.5% 2.5%',
        background: '#E8D7FF40',
        boxShadow: '0 2px 32px 0 rgba( 31, 38, 135, 0.25 )',
    },
    logo: {
        marginRight: '1vw',
        height: '100%',
    },
    chatHistory: {
        overflowX: 'hidden',
        overflowY: 'auto',
        flex: '1 1 auto',
    },
    chat: {
        boxShadow: '0 -2px 32px 0 rgba( 31, 38, 135, 0.25 )',
        padding: "8pt 20pt 8pt 24pt",
    },
    input: {
        flex: "1 1 auto",
    }
}));

// const url = 'https://aiclub.uit.edu.vn/music-chatbot/api/frontend/message';
const url = document.location.href + '/api/frontend/message';

export default function Chat() {

    const classes = useStyles();

    const messageRef = React.useRef();
    const messagesEndRef = React.useRef();
    const [isWaiting, setWaiting] = React.useState(false);
    const [messageList, setMessageList] = React.useState([]);
    const [token, setToken] = React.useState('');

    const processResponse = res => {
        console.log(res);
        const tmp = [];
        res.messages.forEach(element => {
            if (element.username === 'CHATBOT')
                tmp.push(element);
        });
        setMessageList([...messageList, ...tmp]);
        setToken(res.token);
        setWaiting(false);
    }

    // On mount: fetch welcome message
    React.useEffect(() => {
        setWaiting(true);
        const reqData = {
            method: 'GET',
        }

        fetch(url, reqData)
            .then(res => res.json())
            .then(processResponse)
            .catch(err => console.log(err));
        // eslint-disable-next-line
    }, [])

    // On user input
    React.useEffect(() => {
        if (messageList.length > 0 && messageList[messageList.length - 1].username !== 'CHATBOT') {
            setWaiting(true);
            const payload = {
                token: token,
                message: messageList[messageList.length - 1].message
            };
            const reqData = {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload),
            };

            fetch(url, reqData)
                .then(res => res.json())
                .then(processResponse)
                .catch(err => console.log('Error: ', err));
        }
        // eslint-disable-next-line
    }, [messageList])

    const submitMessage = e => {
        e.preventDefault();
        if (isWaiting) return;

        const message = messageRef.current.getElementsByTagName("textarea")[0].value.trim();
        messageRef.current.getElementsByTagName("textarea")[0].value = '';
        if (message) {
            setMessageList([...messageList, { message: message }]);
        }
    }

    const handleKeyDown = e => {
        if (e.which === 13) {
            // messageRef.current.getElementsByTagName("textarea")[0].style.height = "auto"; //<------resize text area
            submitMessage(e);
        }
    }

    React.useEffect(() => {
        messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }, [isWaiting])

    return (
        <Draggable bounds="parent" handle=".chat-header"
        // defaultPosition={useMediaQuery(theme.breakpoints.down('sm')) ? { x: 0, y: 0 } : { x: 200, y: 80 }}
        >
            <Box
                className={classes.root}
                display='flex'
                flexDirection='column'
            >
                {/* <Grid container
                    style={{ height: '5%'}}
                >
                    <Grid item
                        className={classes.header}
                    >
                        <img src="logo_musicbot.png" style={{ maxWidth: '100%', maxHeight: '100%' }} />
                    </Grid>
                </Grid> */}
                <Box
                    className={`${classes.header} chat-header`}
                    display='flex'
                    flexDirection='row'
                >
                    <img src="logo_musicbot_1.png" alt="logo1" className={classes.logo} draggable="false" />
                    <img src="logo_musicbot_2.png" alt="logo2" className={classes.logo} draggable="false" />
                </Box>
                <Scrollbars autoHide universal>
                    <Box
                        className={classes.chatHistory}
                    >
                        <div style={{ height: "16pt" }} />
                        {messageList.map(msg => (
                            <div>
                                <Message
                                    user={msg.username !== 'CHATBOT'}
                                    message={msg.message}
                                />
                                {msg.url ? <MessageMedia url={msg.url}/> : null}
                            </div>
                        ))}
                        {isWaiting ? <MessageLoading /> : null}
                        <div ref={messagesEndRef} />
                    </Box>
                </Scrollbars>
                <form onSubmit={submitMessage}>
                    <Box
                        className={`${classes.chat} chat-footer`}
                        display="flex"
                        flexDirection="row"
                    >
                        <InputBase
                            ref={messageRef}
                            className={classes.input}
                            inputProps={{ style: { fontSize: 20 } }}
                            onKeyDown={handleKeyDown}
                            placeholder="Nhập tin nhắn..."
                            multiline
                        />
                        <IconButton color="secondary" type="submit" className={classes.iconButton}>
                            <SendIcon fontSize="large" />
                        </IconButton>
                    </Box>
                </form>
            </Box>
        </Draggable>
    )
}
