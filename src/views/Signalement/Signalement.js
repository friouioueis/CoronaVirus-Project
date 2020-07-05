import React, {useEffect} from "react";
// @material-ui/core components
import {  fade,makeStyles } from "@material-ui/core/styles";
// core components
import GridItem from "components/Grid/GridItem.js";
import Signal from "components/Signal/Signal";
import Profil from "views/UserProfile/UserProfile";
import profile from  "views/Profile/Profile"
import { createBrowserHistory } from "history";
import { Switch, Route, Redirect ,Router} from "react-router-dom";
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

function createData( nomUser, description, lien ) {
  return {nomUser, description, lien };
}

const singnalements = [
  createData('Frozen yoghurt',"hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh","hh"),
  createData('Frozen yoghurt',"hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh","hh"),
  createData('Frozen yoghurt',"hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh","hh"),
  createData('Frozen yoghurt',"hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh","hh"),
  ];

export default function GestionCompte() {
 
  const classes = useStyles();
 
    const histor = createBrowserHistory();
  return (
    <GridItem > 
<Switch>
    <Route  path="/moderateur/signalement/signal" component={Signal} />
    <Route   path="/moderateur/signalement/profile$:id" component={profile} /> 
    <Route   path="/moderateur/profile" component={Profil} />  
    <Redirect from="/moderateur/signalement" to="/moderateur/signalement/signal" />
  </Switch>
     </GridItem> 
  );
}
