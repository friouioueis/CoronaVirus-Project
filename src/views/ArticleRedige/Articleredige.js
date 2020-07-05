import React, { Component, useEffect, useState } from 'react';
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
import Container from '@material-ui/core/Container';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';
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
    const [user, setUser] = useState([])
    const  [ loading ,setLoading ]= React.useState(false);

    const handleExpandClick = () => {
        setExpanded(!expanded);
    };

    useEffect(() => {
        get_Articles_redige()
    }, [q])

    const get_Articles_redige = () => {

        Axios.get('http://localhost:8000/articles/articlesValides/', { headers: { "Authorization": `Token ${token}` } })
            .then(res => {
                console.log(res.data)
                setActicleredigi(res.data.results)
            }).then(  
                Axios.get(`http://localhost:8000/Utilisateurs/gestionComptes/comptes/`)
                .then(res => {
                    setUser(res.data.results)
                    console.log(res.data.results)
                    setLoading (true)
                })
                   ) 
    }
    function formatDate(string){
        var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: "2-digit", minute:"2-digit"};
        return new Date(string).toLocaleDateString([],options);
      }

    return (
        <Container maxWidth="md">
            {articleredigi.map(article => {
        if (loading) {
                    return (

                        <Card className={classes.root}>
                            <CardHeader
                                avatar={
                                    <Avatar aria-label="recipe" className={classes.avatar}>
                                          {user.find( user => user.id === article.idRedacteurAr).username[0].toUpperCase()} 
                                    </Avatar>
                                }

                                title={user.find( user => user.id === article.idRedacteurAr).username}
                                subheader={formatDate(article.dateAr)}
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