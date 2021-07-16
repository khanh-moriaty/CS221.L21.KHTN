import React from 'react';

import { makeStyles } from '@material-ui/core/styles';
import { Box } from '@material-ui/core';

import './MessageLoading.css';

const useStyles = makeStyles(theme => ({
    root: {
        margin: "6pt 12pt 6pt 12pt",
    },
    message: {
        background: '#E8D7FFd0',
        borderRadius: '2vh',
        color: "#000",
        maxWidth: '80%',
        padding: '1.3vh 2vh 1.3vh 2vh',
    }
}));

export default function MessageLoading() {

    const classes = useStyles();

    return (
        <Box
            className={classes.root}
            display="flex"
            flexDirection="row"
            justifyContent="flex-start"
        >
            <div className={`${classes.message} loading`}>
                <div className="loading1"></div>
                <div className="loading2"></div>
                <div className="loading3"></div>
            </div>
        </Box>
    );

}