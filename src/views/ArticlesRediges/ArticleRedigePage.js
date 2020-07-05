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
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import Next from '@material-ui/icons/NavigateNextOutlined';
import Previous from '@material-ui/icons/NavigateBeforeOutlined';

const useStyles = makeStyles(theme => ({
    root: {
        maxWidth: 1000,
        marginBottom: 73,
        padding : "15px 45px"
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
    const  [ valider ,setValider ]= React.useState(false);
    const  [ open ,setOpen ]= React.useState(false);
    const  [ id ,setId ]= React.useState(0);
    const  [ red ,setRed ]= React.useState(0);
    const  [ cont ,setCont ]= React.useState("");
    const [page, setPage] = React.useState(1);
    const [current, setCurrent] = React.useState(10);
    const [next, setNext] = React.useState(null);
    const [previous, setPrevious] = React.useState(null);
    const handleChangeNextPage = (event, value) => {
          if(next != null){
      setPage(page+10);
      setCurrent(current+10)
      get_Articles_redige(next)
      }
    };
    const handleChangePreviousPage = (event, value) => {
      if(previous != null){
      setPage(page-10);
      setCurrent(current-10)
      get_Articles_redige(previous)
      }
    };

    const handleExpandClick = () => {
        setExpanded(!expanded);
    };
    const handleClickOpen =  (e,val,id,rd,ct) => {
        e.preventDefault()
        setOpen(true)
        setValider(val)
        setRed(rd)
        setId(id)
        setCont(ct)
       // alert(val)
      };
   
     const handleClose = () => {
        setOpen(false)
      };

    useEffect(() => {
        get_Articles_redige('http://localhost:8000/articles/articlesTermines/')
    }, [q])


    const get_Articles_redige = (url) => {
       //  alert(token)
        console.log("dada")
        Axios.get(url, 
        { headers: { "Authorization": `Token ${token}` } })
            .then(res => {
                console.log(res.data.results)
                setActicleredigi(res.data.results)
                if(res.data.next != null){
    
                    setNext(res.data.next)
                    }else{
                        setNext(null)
                    }
                    if(res.data.previous != null){
                    setPrevious(res.data.previous)
                    }else{
                        setPrevious(null)
                    }
            }).then(  
                Axios.get(`http://localhost:8000/Utilisateurs/gestionComptes/comptes/`)
                .then(res => {
                    setUser(res.data.results)
                    console.log(res.data.results)
                    setLoading (true)
                })
                   ) 
    }

    const set_valider_ar = () => {

        console.log("set valider true")
        Axios.patch(`http://localhost:8000/articles/articles/${id}/`, {
            "contenuAr": cont,
            "validerAR": valider,
            "idRedacteurAr": red,
            "idModerateurAr" : localStorage.getItem("idUser")
        }, { headers: { "Authorization": `Token ${token}` } })
            .then(res => {
                console.log(res)
                alert(valider ?'Article validé avec success': 'Article refusé avec success' )
                window.location.reload(false);
                
            })
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

                            <CardActions disableSpacing>
                                <Grid
                                    container
                                    direction="row"
                                    justify="space-between"
                                    alignItems="center"
                                >
                                    <Button onClick={(e) => handleClickOpen(e,true,article.idArticle,article.idRedacteurAr,article.contenuAr) } variant="contained" color="primary" className={classes.accbutt}>
                                        {/* <FavoriteIcon /> */}
                            Accepter
                        </Button>
                        <Button onClick={(e) => handleClickOpen(e,false,article.idArticle,article.idRedacteurAr,article.contenuAr) } variant="outlined" color="primary" className={classes.refbutt}>
                                        {/* <FavoriteIcon /> */}
                         Refuser
                        </Button>
                                </Grid>

                            </CardActions>
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
     {valider ?'Etes vous sure de vouloir valider cet article ?': 'Etes vous sure de vouloir rejeter cet article ?' 
     }
         </p>
   </DialogContent>
   <DialogActions>
   <Button  color="primary" onClick={() => set_valider_ar()} type = "submit">
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
  <div className={classes.pages}>
 <Previous onClick={handleChangePreviousPage}></Previous>
            <p style={{display : "inline-block", margin : "20px" }}>{page} - {current}</p>
    <Next onClick={handleChangeNextPage}></Next>
   
</div>

        </Container>
    );
}


