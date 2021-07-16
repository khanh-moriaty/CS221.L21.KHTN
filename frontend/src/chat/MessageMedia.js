import React from 'react';

import { useTheme } from '@material-ui/core/styles';
import useMediaQuery from '@material-ui/core/useMediaQuery';
import { makeStyles } from '@material-ui/core/styles';
import { Box } from '@material-ui/core';

import './MessageMedia.css';

const useStyles = makeStyles(theme => ({
    root: {
        margin: "6pt 12pt 6pt 12pt",
    },
    ytWrap: {
        background: '#E8D7FFd0',
        borderRadius: '8pt',
        width: '400pt',
        height: '240pt',
        [theme.breakpoints.down('xs')]: {
            width: '200pt',
            height: '120pt',
        },
    },
    zingWrap: {
        background: '#E8D7FFd0',
        borderRadius: '8pt',
        width: '400pt',
        height: '180pt',
        [theme.breakpoints.down('xs')]: {
            width: '200pt',
            height: '90pt',
        },
    },
    nctWrap: {
        borderRadius: '8pt',
        width: '376pt',
        height: '174pt',
        [theme.breakpoints.down('sm')]: {
            width: '200pt',
            height: '93pt',
        },
        overflow: "hidden",
    },
}));

export default function MessageMedia(props) {

    const theme = useTheme();
    const classes = useStyles();
    const smallMedia = useMediaQuery(theme.breakpoints.down('sm'));

    const getMedia = url => {
        if (url.match(/youtube/))
            return getYoutube(url.match(/v=.*/)[0].substring(2))
        if (url.match(/zingmp3/))
            return getZing(url.match(/[A-Z0-9]*.html/)[0].match(/[A-Z0-9]*/))
        if (url.match(/nhaccuatui/))
            return getNCT(url.match(/[A-Za-z0-9]*.html/)[0].match(/[A-Za-z0-9]*/))
    }

    const getYoutube = id => (
        <iframe
            className={classes.ytWrap}
            title={id}
            src={"https://www.youtube-nocookie.com/embed/" + id}
            frameborder="0"
            allow="autoplay; clipboard-write; encrypted-media"
        />
    )

    const getZing = id => (
        <iframe
            className={classes.zingWrap}
            title={id}
            src={"https://zingmp3.vn/embed/song/" + id + "?start=false"}
            frameborder="0"
        />
    )

    const getNCT = id => (
        <div className={classes.nctWrap}>
            <iframe
                className={smallMedia ? "nct-media-small" : "nct-media"}
                width='210pt'
                height='191pt'
                title={id}
                src={"https://www.nhaccuatui.com/mh/normal/" + id}
                frameborder="0"
                allow="autoplay; clipboard-write; encrypted-media"
            />
        </div>
    )

    return (
        <Box
            className={classes.root}
            display="flex"
            flexDirection="row"
            justifyContent="flex-start"
        >
            {getMedia(props.url)}
        </Box>
    );

}