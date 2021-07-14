import React from 'react';

import { useTheme } from '@material-ui/core/styles';
import useMediaQuery from '@material-ui/core/useMediaQuery';

import { makeStyles } from '@material-ui/core/styles';
import { Card, Typography, Box, Grid, InputBase, IconButton } from '@material-ui/core';
import SendIcon from '@material-ui/icons/Send';

import Draggable from 'react-draggable';
import { Scrollbars } from 'react-custom-scrollbars';

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
        padding: '1.5vw',
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
        padding: "0.5vw 1vw 0.5vw 2.5vw",
    },
    input: {
        flex: "1 1 auto",
    }
}));

export default function Chat() {

    const theme = useTheme();

    const classes = useStyles();

    return (
        <Draggable bounds="parent"
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
                    className={classes.header}
                    display='flex'
                    flexDirection='row'
                >
                    <img src="logo_musicbot_1.png" className={classes.logo} />
                    <img src="logo_musicbot_2.png" className={classes.logo} />
                </Box>
                <Scrollbars autoHide>
                    <Box
                        className={classes.chatHistory}
                    >
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                        <Typography>Hello</Typography>
                    </Box>
                </Scrollbars>
                <Box
                    className={classes.chat}
                    display="flex"
                    flexDirection="row"
                >
                    <InputBase
                        className={classes.input}
                        inputProps={{style: {fontSize: 20}}}
                        placeholder="Your message here"
                        multiline
                    />
                    <IconButton color="secondary" className={classes.iconButton}>
                        <SendIcon fontSize="large" />
                    </IconButton>
                </Box>
            </Box>
        </Draggable>
    )
}
