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

import AddIcon from '@material-ui/icons/Add';
import Fab from '@material-ui/core/Fab';
import DeleteIcon from '@material-ui/icons/Close';
import Tooltip from '@material-ui/core/Tooltip';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

const useStyles = makeStyles(theme => ({
    root: {
        maxWidth: 1000,
        marginBottom: 50,
        padding : "10px 30px"
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

    },
    icon: {
        color: "#757575",
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
    const  [ open ,setOpen ]= React.useState(false);
    const  [ id ,setId ]= React.useState(0);
    const handleExpandClick = () => {
        setExpanded(!expanded);
    };
    const handleClickOpen =  (id) => {
        setOpen(true)
        setId(id)
        //setValider(val)
      };
   
     const handleClose = () => {
        setOpen(false)
      };
    useEffect(() => {
        get_Articles_redige()
    }, [q])

    const get_Articles_redige = () => {

        console.log("dada")
        Axios.get('http://localhost:8000/articles/articlesTermines/', { headers: { "Authorization": `Token ${token}` } })
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

    const delete_article = () => {
        handleClose()
        Axios.delete(`http://localhost:8000/articles/articles/${id}/`, { headers: { "Authorization": `Token ${token}` } })
            .then(res => {
                console.log(res)
                window.location.reload(false);
                alert("Article rejeter avec success!")
            }).catch(error =>alert(error));
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
                            <Grid
                                container
                                direction="row"
                                justify="space-between"
                                alignItems="center"
                            >
                                <CardHeader
                                    avatar={
                                        <Avatar aria-label="recipe" className={classes.avatar}>
                                           {user.find( user => user.id === article.idRedacteurAr).username[0].toUpperCase()}
                                      </Avatar>
                                    }

                                    title={user.find( user => user.id === article.idRedacteurAr).username}
                                    subheader={formatDate(article.dateAr)}
                                />
                                <Tooltip title="Rejeter l'article">
                                    <IconButton aria-label="delete">
                                        <DeleteIcon onClick={() => handleClickOpen(article.idArticle)} className={classes.icon} />
                                    </IconButton>
                                </Tooltip>
                            </Grid>
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
                            {/* </CardActions> */}
                            <Collapse in={expanded} timeout="auto" unmountOnExit>
                                <CardContent>
                                    {/* <Typography paragraph>La suite:</Typography> */}
                                    <Typography paragraph>

                                    </Typography>
                                </CardContent>
                            </Collapse>
                            
<Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title">
   <DialogTitle id="form-dialog-title">Confirmation</DialogTitle>
   <DialogContent>
     <p className={classes.text}>
     Etes vous sure de vouloir Rejeter cet article ?
         </p>
   </DialogContent>
   <DialogActions>
   <Button  color="primary" onClick={() => delete_article()}  type = "submit">
      Confirmer
     </Button>
     <Button onClick={handleClose} color="primary">
       Annuler
     </Button>
   </DialogActions>
 </Dialog>
                        </Card>

                    )}
            })}

        </Container>
    );
}
