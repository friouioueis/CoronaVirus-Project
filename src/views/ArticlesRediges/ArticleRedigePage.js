import { makeStyles } from '@material-ui/core/styles';
import clsx from 'clsx';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardMedia from '@material-ui/core/CardMedia';
import CardContent from '@material-ui/core/CardContent';
import CardActions from '@material-ui/core/CardActions';
import Collapse from '@material-ui/core/Collapse';
import Avatar from '@material-ui/core/Avatar';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import { red } from '@material-ui/core/colors';
import FavoriteIcon from '@material-ui/icons/Favorite';
import ShareIcon from '@material-ui/icons/Share';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import MoreVertIcon from '@material-ui/icons/MoreVert';
//import oldmansick from "assets/img/oldmansick.png";
import Container from '@material-ui/core/Container';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';
import React, { Component, useEffect, useState } from 'react';
import Axios from 'axios';



const useStyles = makeStyles(theme => ({
    root: {
        maxWidth: 1000,
        marginBottom: 73,
    },
    media: {
        height: 0,
        paddingTop: '56.25%', // 16:9
    },
    expand: {
        transform: 'rotate(0deg)',
        marginLeft: 'auto',
        transition: theme.transitions.create('transform', {
            duration: theme.transitions.duration.shortest,
        }),
    },
    expandOpen: {
        transform: 'rotate(180deg)',
    },
    avatar: {
        backgroundColor: '#00acc1',
    },
    accbutt: {
        backgroundColor: '#00acc1',
        '&:hover': {
            backgroundColor: '#00acc1',
        },

    },
    refbutt: {
        color: '#00acc1',
        borderColor: "#00acc1",
        '&:hover': {
            color: '#00acc1',
            borderColor: "#00acc1",
            backgroundColor: '#fff'
        },

    }
}));

export default function RecipeReviewCard() {
    const token = localStorage.getItem("token")
    const [articleredigi, setActicleredigi] = useState([])
    const [q, setq] = useState([])
    const classes = useStyles();
    const [expanded, setExpanded] = React.useState(false);


    const handleExpandClick = () => {
        setExpanded(!expanded);
    };


    useEffect(() => {
        get_Articles_redige()
    }, [q])


    const get_Articles_redige = () => {
         alert(token)
        console.log("dada")
        Axios.get('http://localhost:8000/articles/articlesTermines/', 
        { headers: { "Authorization": `Token ${token}` } })
            .then(res => {
                console.log(res.data)
                setActicleredigi(res.data)
            })
    }

    const set_valider_ar = (article_id, id_redacteur, contenu_ar) => {

        console.log("set valider true")
        Axios.put(`http://localhost:8000/articles/articles/${article_id}/`, {
            "contenuAr": contenu_ar,
            "validerAR": true,
            "idRedacteurAr": id_redacteur
        }, { headers: { "Authorization": `Token ${token}` } })
            .then(res => {
                console.log(res)
                get_Articles_redige()
            })
    }


    const set_refuser_ar = (article_id, id_redacteur, contenu_ar) => {

        console.log("set refuser true")
        Axios.put(`http://localhost:8000/articles/articles/${article_id}/`, {
            "contenuAr": contenu_ar,
            "refuserAR": true,
            "idRedacteurAr": id_redacteur
        }, { headers: { "Authorization": `Token ${token}` } })
            .then(res => {
                console.log(res)
                get_Articles_redige()
            })
    }


    return (
        <Container maxWidth="md">
            {articleredigi.map(article => {
                if (article.validerAR === false && article.refuserAR === false) {

                    return (

                        <Card className={classes.root}>
                            <CardHeader
                                avatar={
                                    <Avatar aria-label="recipe" className={classes.avatar}>
                                        RS
                                    </Avatar>
                                }

                                title={article.idRedacteurAr}
                                subheader={article.dateAr}
                            />
                            <CardContent>
                                <Typography variant="body2" color="" component="p">
                                    <div dangerouslySetInnerHTML={{
                                        __html: article.contenuAr
                                    }}>
                                    </div>
                                </Typography>
                            </CardContent>
                            {/* <CardMedia
                                className={classes.media}
                                image={oldmansick}
                                title="Old man sick"
                            /> */}

                            <CardActions disableSpacing>
                                <Grid
                                    container
                                    direction="row"
                                    justify="space-between"
                                    alignItems="center"
                                >
                                    <Button onClick={() => set_valider_ar(article.idArticle, article.idRedacteurAr, article.contenuAr)} variant="contained" color="primary" className={classes.accbutt}>
                                        {/* <FavoriteIcon /> */}
                            Accepter
                        </Button>
                                    <Button onClick={() => set_refuser_ar(article.idArticle, article.idRedacteurAr, article.contenuAr)} variant="outlined" color="primary" className={classes.refbutt}>
                                        {/* <FavoriteIcon /> */}
                            Refuser
                        </Button>
                                </Grid>



                                {/* <IconButton
                                    className={clsx(classes.expand, {
                                        [classes.expandOpen]: expanded,
                                    })}
                                    onClick={handleExpandClick}
                                    aria-expanded={expanded}
                                    aria-label="show more"
                                >
                                    <ExpandMoreIcon />
                                </IconButton> */}
                            </CardActions>
                            <Collapse in={expanded} timeout="auto" unmountOnExit>
                                <CardContent>
                                    {/* <Typography paragraph>La suite:</Typography> */}
                                    <Typography paragraph>

                                    </Typography>
                                </CardContent>
                            </Collapse>
                        </Card>

                    )

                }

            })}

        </Container>
    );
}


