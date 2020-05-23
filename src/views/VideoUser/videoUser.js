import React from "react";
// @material-ui/core components
import {  fade,makeStyles } from "@material-ui/core/styles";
// core components
import GridItem from "components/Grid/GridItem.js";
import Article from "components/Article/Article.js";

import GridContainer from "components/Grid/GridContainer.js";
import Card from "components/Card/Card.js";
import CardBody from "components/Card/CardBody.js";
import CardHeader from "components/Card/CardHeader.js";
import CardIcon from "components/Card/CardIcon.js";
import CardFooter from "components/Card/CardFooter.js";
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';




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

const articles = [
  createData('Frozen yoghurt', "14 Novembre 2020 18:18", "Infection corna verus dans alger","hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh","hh"),
  createData('Ice cream sandwich',"14/11/2020","Infection corna verus dans alger", "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh","hh"),
  createData('Eclair', "14/11/2020", "Infection corna verus dans alger","hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh","hh"),
  createData('Cupcake', "14/11/2020", "Infection corna verus dans alger","hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh","hh"),
  createData('Gingerbread', "14/11/2020", "Infection corna verus dans alger","hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh","hh"),
];

export default function GestionCompte() {
 
  const classes = useStyles();
  
  

  return (
    <GridItem >
        <Article article={articles}></Article>         
     </GridItem> 
  );
}
