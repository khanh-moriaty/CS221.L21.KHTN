import React from 'react';

import { makeStyles } from '@material-ui/core/styles';
import { Box, Typography } from '@material-ui/core';

const useStyles = makeStyles(theme => ({
    root: {
        margin: "6pt 12pt 6pt 12pt",
    },
    messageUser: {
        background: '#ed6a5ad0',
        borderRadius: '12pt',
        color: "#fff",
        maxWidth: '80%',
        padding: '1vh 2vh 1vh 2vh',
    },
    messageBot: {
        background: '#E8D7FFd0',
        borderRadius: '2vh',
        color: "#000",
        maxWidth: '80%',
        padding: '1vh 2vh 1vh 2vh',
    }
}));

function Message(props) {

    const classes = useStyles();

    return (
        <Box
            className={classes.root}
            display="flex"
            flexDirection="row"
            justifyContent={props.user ? "flex-end" : "flex-start"}
        >
            <Typography
                className={props.user ? classes.messageUser : classes.messageBot}
                style={props.user ? { color: "#fff" } : { color: "#000" }}
                align="left"
            >
                {props.message}
            </Typography>
        </Box>
    );

}

Message.defaultProps = {
    user: false,
}

export default Message;