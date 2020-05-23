import React ,{useState} from "react";

// @material-ui/core components
import Button from '@material-ui/core/Button';
import { makeStyles } from "@material-ui/core/styles";
import Auth from "views/Authentification/AuthView.js";

import {withRouter,Redirect} from 'react-router-dom'

const styles ={
    
}
const useStyles = makeStyles(styles);


export default function Authentification(props) {
//const [token, setToken] = useState("");
var token = ""
//const classes = useStyles();
    
//const history = withRouter()
    const userLogin = (tok) =>{
      alert( tok);
      //setToken({value: tok});
      token = tok ;
      alert (token);
      props.history.push("/agentSante");
     // history.push("/agentSante")
     // alert('here it is')
       
    }
    
return(

  <Auth userLogin={userLogin}/>
  
)
}
