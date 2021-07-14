import React from 'react';

import { makeStyles } from '@material-ui/core/styles';
import { Card, Typography, Box } from '@material-ui/core';

import Draggable from 'react-draggable';

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
    }
}));

export default function Chat() {

    const classes = useStyles();

    return (
        <Draggable bounds="parent">
            <Box
                className={classes.root}
            >
            </Box>
        </Draggable>
    )
}
