import React from 'react';

import { makeStyles } from '@material-ui/core/styles';
import { Card, Typography, Box, Grid } from '@material-ui/core';

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
    },
    header: {
        // width: '100%',
        height: '8%',
        textAlign: 'left',
        padding: '20pt',
        // borderRadius: '2.5vh',
        boxShadow: '0 2px 32px 0 rgba( 31, 38, 135, 0.25 )',
    },
    logo: {
        // width: '100%',
        marginRight: '1vw',
        // borderRadius: '2.5vh',
        // boxShadow: '0 2px 32px 0 rgba( 31, 38, 135, 0.25 )',
    }
}));

export default function Chat() {

    const classes = useStyles();

    return (
        <Draggable bounds="parent">
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
            </Box>
        </Draggable>
    )
}
