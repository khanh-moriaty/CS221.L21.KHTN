import React from 'react';

import { useTheme } from '@material-ui/core/styles';
import useMediaQuery from '@material-ui/core/useMediaQuery';

import { makeStyles } from '@material-ui/core/styles';
import { Card, Typography, Box, Grid, InputBase, IconButton } from '@material-ui/core';
import SendIcon from '@material-ui/icons/Send';

import Draggable from 'react-draggable';
import { Scrollbars } from 'react-custom-scrollbars';

import Message from './Message';
import MessageLoading from './MessageLoading';

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
        height: '8%',
        textAlign: 'left',
        padding: '1.5vw 0 1.5vw 2vw',
        background: '#E8D7FF40',
        boxShadow: '0 2px 32px 0 rgba( 31, 38, 135, 0.25 )',
    },
    logo: {
        marginRight: '1vw',
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

export default function Chat() {

    const theme = useTheme();

    const classes = useStyles();

    const messageRef = React.useRef();
    const messagesEndRef = React.useRef();
    const [isWaiting, setWaiting] = React.useState(false);
    const [messageList, setMessageList] = React.useState([]);

    const submitMessage = e => {
        e.preventDefault();
        if (isWaiting) return;
        console.log(messageRef.current.getElementsByTagName("textarea")[0].value);
        setWaiting(true);
    }

    const handleKeyDown = e => {
        if (e.which === 13) {
            messageRef.current.getElementsByTagName("textarea")[0].style.height = "auto"; //<------resize text area
            submitMessage(e);
        }
    }

    React.useEffect(() => {
        messagesEndRef.current.scrollIntoView({behavior: 'smooth'});
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
                    <img src="logo_musicbot_1.png" className={classes.logo} draggable="false" />
                    <img src="logo_musicbot_2.png" className={classes.logo} draggable="false" />
                </Box>
                <Scrollbars autoHide universal>
                    <Box
                        className={classes.chatHistory}
                    >
                        <Message message="Lorem ipsum dolor sit amet, consectetur adipiscing elit."></Message>
                        <Message user message="Vivamus ultricies neque vitae enim tristique consequat."></Message>
                        <Message message="Proin venenatis odio in ornare mollis."></Message>
                        <Message user message="Phasellus et ligula laoreet, dapibus velit a, consectetur arcu."></Message>
                        <Message user message="Vivamus maximus nulla quis risus elementum, in venenatis massa tempus."></Message>
                        <Message user message="Sed consectetur arcu porttitor tortor vestibulum, eleifend vestibulum eros ornare."></Message>
                        <Message message="Quisque blandit augue a sodales dapibus."></Message>
                        <Message message="Pellentesque at nulla a ligula ultricies sagittis ut sit amet massa."></Message>
                        <Message message="Morbi vel elit a sapien sagittis vestibulum porttitor at odio."></Message>
                        <Message message="Sed nec augue et ex pretium fermentum sed at massa."></Message>
                        <Message user message="Sed maximus magna et pellentesque euismod."></Message>
                        <Message user message="Suspendisse iaculis tortor vitae ligula mattis, nec commodo ligula vestibulum. 
                        Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Vestibulum hendrerit, 
                        nunc ac mattis convallis, nisi felis fermentum massa, et porta neque libero eget tellus. Morbi ultricies purus eu 
                        libero laoreet vulputate. Etiam mollis tempus lectus vel sollicitudin. Nam venenatis ultrices metus, eu pharetra 
                        ex vehicula at. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. 
                        Aliquam iaculis lectus dui, non fermentum dui pellentesque quis. Cras imperdiet viverra massa, sed molestie felis. 
                        Morbi vulputate, ex eu malesuada pulvinar, augue nibh eleifend turpis, id finibus purus nunc sed est. Suspendisse potenti. "></Message>
                        <Message user message="Donec posuere sapien vitae leo porttitor, vehicula eleifend ex imperdiet."></Message>
                        {isWaiting ? <MessageLoading/> : null}
                        <div ref={messagesEndRef}/>
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
