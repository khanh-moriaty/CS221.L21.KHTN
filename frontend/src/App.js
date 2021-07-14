import React from 'react';
import '@fontsource/roboto';
import './App.css';

import { makeStyles } from '@material-ui/core/styles';
import Box from '@material-ui/core/Box';

import { ThemeProvider, createTheme, responsiveFontSizes } from '@material-ui/core/styles';

import Chat from './chat/Chat';

const theme = responsiveFontSizes(createTheme({
    typography: {
        fontFamily: [
            'Baloo 2',
        ].join(','),
    },
    palette: {
        primary: {
            main: '#ED6A5A',
        },
        secondary: {
            main: '#000000',
        },
    }
}));

const useStyles = makeStyles(theme => ({
    root: {
        height: '100vh',
        width: '100vw',
        padding: '1vh',
        boxSizing: 'border-box',
        backgroundImage: 'url("bg_musicbot.jpg")',
        backgroundPosition: 'center',
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat',
    }
}));

export default function App() {

    const classes = useStyles();

    return (
        <div className="App">
            <ThemeProvider theme={theme}>
                <Box
                    className={classes.root}
                    // display="flex"
                    // flexDirection="column"
                >
                    <Chat />
                </Box>
            </ThemeProvider>
        </div>
    );
}