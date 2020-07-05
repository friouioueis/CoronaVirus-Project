import React, { Component, useState, useEffect } from "react";
// @material-ui/core components
import {  fade,makeStyles } from "@material-ui/core/styles";
// core components
import GridItem from "components/Grid/GridItem.js";
import Article from "components/Article/Article.js";
import Axios from 'axios';
import GridContainer from "components/Grid/GridContainer.js";
import Card from "components/Card/Card.js";
import CardBody from "components/Card/CardBody.js";
import CardHeader from "components/Card/CardHeader.js";
import CardIcon from "components/Card/CardIcon.js";
import CardFooter from "components/Card/CardFooter.js";
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CardMedia from '@material-ui/core/CardMedia';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

const useStyles = makeStyles(theme => ({
 
  card: {
       padding : "10px 50px",
       maxWidth : "70%"
          },
  title: {
        fontSize: 22,
        fontWeight: 'bold ',
        fontFamily: '"Segoe UI"', 
        color : '#757575',
        margin :0
      },
text: {
        fontSize: 16,
        fontFamily: '"Segoe UI"', 
        margin :"0px 0px 10px 0px"
      },
 
  Button: {
        minWidth: '70%',
        color : 'white',
        backgroundColor: '#39aac4',
        '&:hover': {
          backgroundColor: "#39aac4",
         }, 
         fontFamily: '"Segoe UI"', 
         fontWeight: 'bold',
      },
      Button2: {
        minWidth: '70%',
        float :  "right",
        color : 'white',
        backgroundColor: '#39aac4',
        '&:hover': {
          backgroundColor: "#39aac4",
         }, 
         fontFamily: '"Segoe UI"', 
         fontWeight: 'bold',
      },
    }));

function createData( nomAuteur, date,titre, description, lienVideo ) {
  return { nomAuteur, date,titre, description, lienVideo };
}




export default function GestionCompte() {
const  [ loading ,setLoading ]= React.useState(false);
const  [ user ,setUser ]= React.useState([]);
const  [ data ,setData ]= React.useState([]);
const  [ valider ,setValider ]= React.useState(false);
const  [ open ,setOpen]= React.useState(false);
const  [ id ,setId ]= React.useState(0);
const token = localStorage.getItem("token")

const handleClickOpen =  ( id, val) => {
  setValider(val)
  setId (id)
  setOpen(true)
};

const handleClose = () => {
  setOpen(false)
};


function formatDate(string){
  var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: "2-digit", minute:"2-digit"};
  return new Date(string).toLocaleDateString([],options);
}
var articles = [
]


useEffect(() => {
  Axios.get('http://localhost:8000/articles/video/', 
  { headers: {  'Content-Type' : 'application/json',"Authorization": `Token ${token}` } })
      .then(res => {
          console.log(res.data)
          setData(res.data.results) 
      }).then(  
          Axios.get('http://localhost:8000/Utilisateurs/gestionComptes/comptes/')
          .then(res => {
              setUser(res.data.results)
              console.log(res.data.results)
              setLoading (true)
              
          })
        )    
},[])
const classes = useStyles();

const valider_vd = () => {
  handleClose()
  console.log("set valider true")
  Axios.patch(`http://localhost:8000/articles/video/${id}/`, {
      "validerVthema": valider,
      'idModerateurVthema' : localStorage.getItem("idUser")
  }, { headers: { 'Authorization': `Token ${ localStorage.getItem("token")}` } })
      .then(res => {
          console.log(res)
          alert(valider?" video valider avec success":"video  refusé avec success")
          window.location.reload(false);
      }).catch(error =>alert(error));
}
  
data.map(info => {
  // console.log(reg.find( reg => reg.idRegion === info.idRegionSt))
    if ( loading===true & !info.validerVthema ) {
      console.log( user.find( user => user.id === info.idUtilisateurVThema).username)
     // alert( info.lienVthema.substr(22))
        return (
            articles.push([
                user.find( user => user.id === info.idUtilisateurVThema).username,
                formatDate(info.dateSt),
                 info.titreVthema, 
                 info.descriptionVthema,
                  info.lienVthema.substr(21), 
                info.idVideoThema
                ])
               
        )
    
    }

})

  return (
  
    <GridItem >
      {loading?

      articles.map((prop, key) => {
        console.log(data)
    return (
    <Card className={classes.card} >
        <CardHeader >
        <GridContainer >
        <GridItem  xs={2} sm={6} md={1} >   
          <Avatar  >   {prop[0][0].toUpperCase()} </Avatar> 
        </GridItem>
        <GridItem  xs={10} sm={6} md={11} >   
          <p className={classes.title}  style={{  fontWeight: 'bold '}}>
               {prop[0]}
           </p>
   

        </GridItem>
        </GridContainer >    
        </CardHeader>
         
    <CardBody >
        <h2 className={classes.text} style={{ fontSize: 25 , fontWeight: 'bold '}}>{prop[2]}</h2>   
        <p className={classes.text}>
        {prop[3]}</p>
    <GridContainer >
    <GridItem  xs={6} sm={6} md={6} >   
    <CardMedia
       component="video"  image='vid.mp4'  className={classes.media}   controls
    />
   
     <iframe frameBorder="0"  title="Video player" src="C:/Users/HP/Documents/semestre2/Projet/corona6/ProjetCorona_WatchEquipe4-backend2/vid.MP4" controls />
     
  </GridItem>
    </GridContainer>
    </CardBody>
    <CardFooter>
   
    <GridItem  xs={6} sm={6} md={6} >   
    <Button type="submit" onClick={() => handleClickOpen(prop[5], true)}  className={classes.Button }  >
        Accepter
     </Button> 
    </GridItem>

    <GridItem  xs={6} sm={6} md={6} >   
        <Button type="submit" onClick={() => handleClickOpen(prop[5], false)}  className={classes.Button2}  >
        Refuser
     </Button> 
    </GridItem>
    </CardFooter>
    <Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title">
   <DialogTitle id="form-dialog-title">Confirmation</DialogTitle>
   <DialogContent>
     <p className={classes.text}>
     {valider ?'Etes vous sure de vouloir valider cette video ?': 'Etes vous sure de vouloir rejeter cette video?' }
         </p>
   </DialogContent>
   <DialogActions>
   <Button  color="primary" onClick={()=>valider_vd()} type = "submit">
      Confirmer
     </Button>
     <Button onClick={handleClose} color="primary">
       Annuler
     </Button>
   </DialogActions>
 </Dialog>
     </Card>

      );
    }) : "pas de videos thematique a valider"}
     </GridItem> 
    
  );
}
