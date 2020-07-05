import React from "react";

// @material-ui/core components
import Button from '@material-ui/core/Button';
import { makeStyles } from "@material-ui/core/styles";
import { blackColor }from "assets/jss/material-dashboard-react.js"
import InputLabel from '@material-ui/core/InputLabel';
import Input from '@material-ui/core/Input';
import FormControl from '@material-ui/core/FormControl';
import InputBase from '@material-ui/core/InputBase';
import Select from '@material-ui/core/Select';
import GridContainer from "components/Grid/GridContainer.js";
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import RadioGroup from '@material-ui/core/RadioGroup';
import Radio from '@material-ui/core/Radio';
import Axios from 'axios';
import logo from "assets/img/white.png";

//import auth from './Authentification/auth.js'
import {
    fade,
    withStyles,
  } from '@material-ui/core/styles';
//import Authentification from "layouts/Authentification";
import {useHistory} from 'react-router-dom'
import {Redirect} from 'react-router-dom'
import { Switch, TextField, MenuItem } from "@material-ui/core";
import { async } from "q";
//import history from "../utils/history"


const useStyles = makeStyles(theme => ({
    background:{
          position: "relative",
          zIndex: "1",
          width: "100%",
          minHeight: "1000px",
         background: blackColor,
          opacity: ".8",
          top: 0,
          left: 0,
          bottom : 0,
    
    },
    Button: {
        minWidth: '50%',
        color : 'white',
        marginTop : "15px",
        backgroundColor: '#39aac4',
        '&:hover': {
          backgroundColor: "#39aac4",
         }, 
         fontFamily: '"Segoe UI"', 
         fontWeight: 'bold',
      },
  
      text: {
        fontSize: 18,
        fontWeight: 'bold',
        fontFamily: '"Segoe UI"', 
     
        color:'white'
       
       
      },
      form: {
        position: "relative",
          zIndex : 5,
          top: "100px",
          left: "30%",
          width: "50%",
          height: "50%",
         // position : 'absolute',

      },
    
      select : {
        borderRadius: 4,
    backgroundColor: "white",
         
      }
}
));

const BootstrapInput = withStyles(theme => ({
    /*root: {
      flexGrow: 1,
      'label + &': {
        marginTop: theme.spacing(3),
      },
      
    },*/
    input: {
      borderRadius: 4,
      position: 'relative',
      backgroundColor: theme.palette.common.white,
      border: '1px solid #ced4da',
      fontSize: 'auto',
      maxWidth: 'auto',
     marginBottom: 15,
      padding: '5px 50px',
      transition: theme.transitions.create(['border-color', 'box-shadow']),
      // Use the system font instead of the default Roboto font.
      fontFamily: [
        '-apple-system',
        'BlinkMacSystemFont',
        '"Segoe UI"',
        'Roboto',
        '"Helvetica Neue"',
        'Arial',
        'sans-serif',
        '"Apple Color Emoji"',
        '"Segoe UI Emoji"',
        '"Segoe UI Symbol"',
      ].join(','),
      '&:focus': {
        boxShadow: `${fade("#39aac4", 0.25)} 0 0 0 0.1rem`,
        borderColor: "#39aac4",
       
      },
    },
    
  }))(InputBase);
  //const useStyles = makeStyles(styles);

class AuthView extends React.Component {

  constructor(props) {
      super(props);
      this.state = {
        credentials :{username :'' , password:''} ,
        role :'',
        check : false,
        roles : [],
        open : false,
        lis : [],
        error : false,
        token : null
      }
  }

   handleClickOpen =  () => {
    console.log("token")  
    console.log(this.state.token)
    this.setState({open : true});
  };

 handleClose = () => {
  this.setState({open : false});
  };
  handleChange = (event) => {
    this.setState({role : event.target.value});
  }
  handleCheck = (event) => {
    this.setState({check : true});
    }

  handlesubmit = (e) => {
      e.preventDefault()
      this.setState({token :null})
      Axios.post('http://127.0.0.1:8000/Utilisateurs/rest-auth/login/',
      this.state.credentials, { headers: { 'Content-Type' : 'application/json' } }
      ).then (data=>  { 
        localStorage.setItem("token",data.data.key)
        this.setState({token : data.data.key})
        localStorage.setItem("idUser",data.data.user.id)
        console.log(data) 
        this.setState({roles : data.data.user.roles})
        console.log (data.data.user.roles) 
        }).catch(error =>
          {
            this.setState({roles: []})
            this.setState({error : true})
            alert("nom d'utilisateur ou mot de passe incorrect")
          }
          )
  }

  handleLogin = () => {
    this.setState({open : false});
   
    this.state.roles.map((r)=>{ 
    
      if (r.Type === this.state.role && r.Type=== 'as'){
     //alert(r.Type)
     this.props.history.push("/agentSante")
     localStorage.setItem("role","agentSante")
      }
      else if (r.Type === this.state.role && r.Type=== 'md') {
      //  alert(r.Type)
        this.props.history.push("/moderateur")
        localStorage.setItem("role","moderateur")
      } 
      else if (r.Type === this.state.role && r.Type=== 'rd') {
        //  alert(r.Type)
          this.props.history.push("/redacteur")
          localStorage.setItem("role","redacteur")
        }
        else if (r.Type === this.state.role && r.Type=== 'ad') {
          //  alert(r.Type)
            this.props.history.push("/admin1")
            localStorage.setItem("role","admin1")
          }
      });
    };
   



  render() {
      const { classes } = this.props;

      return (
        <div  style={{  position: "relative",
           zIndex: "1",
           width: "100%",
           minHeight: "1000px",
          background: blackColor,
           opacity: ".8",
           top: 0,
           left: 0,
           bottom : 0}} >
 <center>
              <form onSubmit={this.handlesubmit}
                style={{ 
                  position: "relative",
                  zIndex : 5,
                  top: "30px",
                  width: "50%",
                  height: "50%",
                 }}  >   

        <img src={logo} alt="logo" 
                style={{ 
                  width: "40%",
                  height: "30%",
                 }} />
                 <br></br>

                
                <label   
                  style={{ 
                  fontSize: 30,
                  fontFamily: '"Segoe UI"', 
                  color:'white',
                }} > Connexion</label>  
         
<br></br>
<br></br>
                    <label   
                  style={{ 
                  fontSize: 18,
                  fontWeight: 'bold',
                  fontFamily: '"Segoe UI"', 
                  color:'white'
                }} > Nom d'utilisateur</label>  
                  <br></br>
                  <BootstrapInput  type='text' name="username" 
                  onChange={e => this.state.credentials.username=(e.target.value)}
                   />

            <br></br>

              <label   
               style={{ 
                fontSize: 18,
                fontWeight: 'bold',
                fontFamily: '"Segoe UI"', 
                color:'white'
               }}
              > mot de passe</label>    
              <br></br>
                  <BootstrapInput  type='password' name="password" 
                  onChange={e =>this.state.credentials.password=(e.target.value)}
                   />
            
              <br></br>

              <Button 
            type="submit" 
            onClick={this.handleClickOpen}  
            style={{ 
              width: '40%',
              color : 'white',
              marginTop : "15px",
              backgroundColor: '#39aac4',
              '&:hover': {
                backgroundColor: "#39aac4",
               }, 
               fontFamily: '"Segoe UI"', 
               fontWeight: 'bold',
           }}
           >
               Envoyer
               </Button>
              </form>
              </center>
         
   <Dialog open={this.state.open} onClose={this.handleClose} aria-labelledby="form-dialog-title">
   <DialogTitle id="form-dialog-title">Connexion</DialogTitle>
   <DialogContent>
     <DialogContentText>
     choisissez le role que vous voulez s'authentifié avec :
     </DialogContentText>
     <RadioGroup
          aria-label="ringtone"
          name="ringtone"
          onChange={this.handleChange}
        >
          {
         this.state.roles.map((option , key ) => (
          <FormControlLabel value={option.Type} key={key} control={<Radio />} label=
            {(function() {
              switch (option.Type) {
             case 'as':
               return "agent de santé"  
             case 'md':
               return "moderateur" 
             case 'si':
               return "simple"
             case 'ad':
               return "admin" 
             case 'rd':
                return "redacteur" 
             default:
               return "default";
           }
       
         })()}  

           onChange={this.handleChange}/>
            
          
        ))}</RadioGroup>
        
     
   </DialogContent>
   <DialogActions>
     <Button onClick={this.handleClose} color="primary">
      Annuler
     </Button>
     <Button onClick={this.handleLogin} color="primary">
      Connexion
     </Button>
   </DialogActions>
 </Dialog>
              </div>
 
     

      );

  }



}



export default withStyles(useStyles)(AuthView);
 