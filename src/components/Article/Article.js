import React from "react";
// @material-ui/core components
import {  fade,makeStyles } from "@material-ui/core/styles";
// core components
import GridItem from "../Grid/GridItem.js";
import GridContainer from "../Grid/GridContainer.js";
import Card from "../Card/Card.js";
import CardBody from "../Card/CardBody.js";
import CardHeader from "components/Card/CardHeader.js";
import CardIcon from "../Card/CardIcon.js";
import CardFooter from "../Card/CardFooter.js";
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CardMedia from '@material-ui/core/CardMedia';



const useStyles = makeStyles(theme => ({
 
  card: {
       padding : "10px 50px",
       maxWidth : "70%"
          },
  title: {
        fontSize: 22,
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
      media: {
        height: 140,
      },
    }));
//const useStyles  = makeStyles(styles);


export default function GestionCompte(props) {
  const classes = useStyles();
  const {article}  = props;
  
  return (
    
    <GridItem >
      {article.map((prop, key) => {
    return (
    <Card className={classes.card} >
        <CardHeader >
        <GridContainer >
        <GridItem  xs={2} sm={6} md={1} >   
          <Avatar  >NO</Avatar> 
        </GridItem>
        <GridItem  xs={10} sm={6} md={11} >   
          <p className={classes.title}  style={{  fontWeight: 'bold '}}>
               {prop.nomAuteur}
           </p>
           <p className={classes.title} style={{ fontSize: 13}}>
               {prop.date}
              </p>

        </GridItem>
        </GridContainer >    
        </CardHeader>
         
    <CardBody >
        <h2 className={classes.text} style={{ fontSize: 25 , fontWeight: 'bold '}}>{prop.titre}</h2>   
        <p className={classes.text}>
        {prop.description}</p>
    <GridContainer >
    <GridItem  xs={6} sm={6} md={6} >   
    <CardMedia
          className={classes.media}   src=""    
    />
    <a href="C:/Users/HP/Music/Fullmetal ALchemist BrotherHood[720p] [Dual-Audio][eng subbed]{Neroextreme}_NTRG/video.mkv">hhhh</a>
      </GridItem>
    </GridContainer>
    </CardBody>
    <CardFooter>
   
    <GridItem  xs={6} sm={6} md={6} >   
    <Button type="submit" className={classes.Button }  >
        Accepter
     </Button> 
    </GridItem>

    <GridItem  xs={6} sm={6} md={6} >   
        <Button type="submit" className={classes.Button2}  >
        Refuser
     </Button> 
    </GridItem>
    </CardFooter>
     </Card>

      );
    })}
     </GridItem> 
    
    );
}
