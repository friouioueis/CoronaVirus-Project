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
import DeleteIcon from '@material-ui/icons/Close';
import EditIcon from '@material-ui/icons/Edit';
import Tooltip from '@material-ui/core/Tooltip';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import moment from "moment";
const useStyles = makeStyles(theme => ({
    root: {
        maxWidth: 1000,
        marginBottom: 73,
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
    const  [ open1 ,setOpen1 ]= React.useState(false);
    const  [ open2 ,setOpen2 ]= React.useState(false);
    const  [ id ,setId ]= React.useState(0);

    const handleClickOpen1 =  (id) => {
        setOpen1(true)
        //setValider(val)
        setId(id)
      };
   
     const handleClose1 = () => {
        setOpen1(false)
      };
      const handleClickOpen2 =  (id) => {
        setOpen2(true)
        setId(id)
        //setValider(val)
      };
   
     const handleClose2 = () => {
        setOpen2(false)
      };
    const handleExpandClick = () => {
        setExpanded(!expanded);
    };

    useEffect(() => {
        get_Articles_redige()
    }, [q])

    const set_terminer = (valider,contenu) => {
      //  alert(contenu)
       // alert(valider)
       // alert(id)
        handleClose1()
        console.log("set valider true")
        Axios.put(`http://localhost:8000/articles/articles/${id}/`, {
            "dateAr": moment().format("YYYY-MM-DD[T]HH:mm:ss"),
            "contenuAr": contenu,
            "terminerAR": valider,
         }, { headers: { "Authorization": `Token ${token}` } })
            .then(res => {
                console.log(res)
                window.location.reload(false);
            })
    }

    const delete_article = () => {
      //  alert(id)
        handleClose2()
        Axios.delete(`http://localhost:8000/articles/articles/${id}/`, { headers: { "Authorization": `Token ${token}` } })
            .then(res => {
                console.log(res)
                window.location.reload(false);
                alert("Article rejeter avec success!")
            }).catch(error =>alert(error));
    }


    const get_Articles_redige = () => {

        Axios.get('http://localhost:8000/articles/articlesNonTermines/', { headers: { "Authorization": `Token ${token}` } })
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
                            const url = '/redacteur/nonTermines/editer'+article.idArticle
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
                               <div >
                              <Tooltip title="Modifier l'article">
                                    <IconButton aria-label="modifier">
                                    <a href={url} style={{color : "#00acc1"}}>
                                        <EditIcon  className={classes.icon} />
                                        </a>
                                    </IconButton>
                                </Tooltip>
                                
                                <Tooltip title="Rejeter l'article">
                                    <IconButton aria-label="delete">
                                       
                                      <DeleteIcon  onClick={() => handleClickOpen2(article.idArticle) } className={classes.icon} />
                                     
                                    </IconButton>
                                </Tooltip>
                                </div>
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

                            
                            <CardActions disableSpacing>
                                    <Button  variant="contained" color="primary" className={classes.accbutt} onClick={() => handleClickOpen1(article.idArticle) }>
                                        {/* <FavoriteIcon /> */}
                                    Terminer
                                    </Button>
                            </CardActions>

                            <Collapse in={expanded} timeout="auto" unmountOnExit>
                                <CardContent>
                                    {/* <Typography paragraph>La suite:</Typography> */}
                                    <Typography paragraph>

                                    </Typography>
                                </CardContent>
                            </Collapse>
                                                       
<Dialog open={open1} onClose={handleClose1} aria-labelledby="form-dialog-title">
   <DialogTitle id="form-dialog-title">Confirmation</DialogTitle>
   <DialogContent>
     <p className={classes.text}>
     Etes vous sure que vous avez terminer cet article ?
         </p>
   </DialogContent>
   <DialogActions>
   <Button  color="primary" onClick={() => set_terminer(true,article.contenuAr) }  type = "submit">
      Confirmer
     </Button>
     <Button onClick={handleClose1} color="primary">
       Annuler
     </Button>
   </DialogActions>
 </Dialog>
 <Dialog open={open2} onClose={handleClose2} aria-labelledby="form-dialog-title">
   <DialogTitle id="form-dialog-title">Confirmation</DialogTitle>
   <DialogContent>
     <p className={classes.text}>
     Etes vous sure de vouloir Rejeter cet article ?
         </p>
   </DialogContent>
   <DialogActions>
   <Button  color="primary" onClick={() => delete_article()} type = "submit">
      Confirmer
     </Button>
     <Button onClick={handleClose2} color="primary">
       Annuler
     </Button>
   </DialogActions>
 </Dialog>
 
                        </Card>
        
                    )

                        }
            })}

        </Container>
    );
}