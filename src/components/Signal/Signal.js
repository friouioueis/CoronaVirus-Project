import React , {useEffect} from "react";
// @material-ui/core components
import {  fade,makeStyles ,
  withStyles } from "@material-ui/core/styles";
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
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import InputBase from '@material-ui/core/InputBase';
import InputLabel from '@material-ui/core/InputLabel';
import FormControl from '@material-ui/core/FormControl';
import Next from '@material-ui/icons/NavigateNextOutlined';
import Previous from '@material-ui/icons/NavigateBeforeOutlined';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import CardAvatar from "components/Card/CardAvatar.js";
import avatar from "assets/img/faces/marc.jpg";
import { Switch, Route, Redirect, Router } from "react-router-dom";
import routes from "routesMd.js";
import stat from "@material-ui/icons/List";
import { Icon } from "@material-ui/core";
import { NavLink } from "react-router-dom";
import zone from  "views/Zonerisque/Zonerisque"
import Axios from 'axios';
import { async } from "q";
const useStyles = makeStyles(theme => ({
 
  card: {
       padding : "10px 10px",
       maxWidth : "60%",
      // maxHeight: "1000px",
       
          },
   ButtonM: {
            minWidth: '60%',
            color : 'white',
          
            backgroundColor: '#39aac4',
            '&:hover': {
              backgroundColor: "#39aac4",
             }, 
             fontFamily: '"Segoe UI"', 
             fontWeight: 'bold',
          },
cardDiv: {
    //    float : "left",
       margin : "10px"
        },
  title: {
    fontWeight: 'bold ',
        fontSize: 22,
        fontFamily: '"Segoe UI"', 
        color : '#757575',
        margin :0,
        '&:hover': {
            color: "#39aac4",
           },
      },
      stitle: {
        fontSize: 14,
        fontFamily: '"Segoe UI"', 
        color : '#757575',
        margin :0,
       
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
      pages:{
        marginLeft : "30%"
    },
      media: {
        maxHeight: "80%",
        maxWidth :"80%"
      },
    }));
    
const BootstrapInput = withStyles(theme => ({
  root: {
    flexGrow: 1,
    'label + &': {
      marginTop: theme.spacing(3),
    },
    
  },
  input: {
    borderRadius: 4,
    position: 'relative',
    backgroundColor: theme.palette.common.white,
    border: '1px solid #ced4da',
    fontSize: 'auto',
    maxWidth: 'auto',
    marginRight: 30,
    marginBottom: 30,
    padding: '7px 30px',
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
const BootstrapInput2 = withStyles(theme => ({
  root: {
    flexGrow: 1,
    'label + &': {
      marginTop: theme.spacing(3),
    },
    
  },
  input: {
    borderRadius: 4,
    position: 'relative',
    backgroundColor: theme.palette.common.white,
    border: '1px solid #ced4da',
    fontSize: 'auto',
    maxWidth: 'auto',
    height : "90px",
    marginRight: 30,
    marginBottom: 30,
    padding: '7px 30px',
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

function createData( nomUser, description, lien ) {
  return {nomUser, description, lien };
}

export default function Signal(props) {
  const classes = useStyles();
  const  [ open ,setOpen ]= React.useState(false);
  const  [ open2 ,setOpen2 ]= React.useState(false);
  const  [ valider ,setValider ]= React.useState(false);
   const  [ loading ,setLoading ]= React.useState(false);
  const  [ id ,setId ]= React.useState(0);
  const  [ nomUser ,setNomUser ]= React.useState("");
  const  [ singnalements ,setSingnalements]= React.useState([]);
  const singnalement= []
  const token = localStorage.getItem("token")
  const [page, setPage] = React.useState(1);
  const [current, setCurrent] = React.useState(10);
  const [next, setNext] = React.useState(null);
  const [previous, setPrevious] = React.useState(null);
  const [lien, setLien] = React.useState("");
  const [des, setDes] = React.useState("");
  const handleChangeNextPage = (event, value) => {
  //  alert (next)
    if(next != null){
    setPage(page+10);
    setCurrent(current+10)
    getSignalements(next)
    }
  };
  const handleChangePreviousPage = (event, value) => {
    if(previous != null){
    //    alert ("previous")
    setPage(page-10);
    setCurrent(current-10)
    getSignalements(previous)
    }
  };
  const handleClickOpen =  (idSignal,val,lien,des) => {
    setOpen(true)
    setId(idSignal)
    setValider(val)
    setLien(lien.substr(22))
 //   alert(lien.substr(22))
    setDes(des)
  

  };
  const handleClickOpen2 =  () => {
    setOpen2(true)
 
  
  };
  const mail ={
    subject: "",
    message: "",
    email_from : "",
    recipient_list : "",
    attach : ""
  }
 const handleClose = () => {
    setOpen(false)
  };
  const handleClose2 = () => {
    setOpen2(false)
    window.location.reload(false);
  };

  const getSignalements = (url) => {
    Axios.get(url,
    { headers: { 'Content-Type' : 'application/json' } }
    ).then (data=>  { 
      console.log(data.data.results)
      if(data.data.results.length!=0){
        setLoading(true)
      }
      setSingnalements(data.data.results)
      if(data.data.next != null){
        setNext(data.data.next)
        }else{
            setNext(null)
        }
        if(data.data.previous != null){
        setPrevious(data.data.previous)
        }else{
            setPrevious(null)
        }
      }).catch(error =>
        {
          alert(error)
        }
        )  
}
function formatDate(string){
  var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: "2-digit", minute:"2-digit"};
  return new Date(string).toLocaleDateString([],options);
}
const accepter = (idSignal) => {
  //getSignalements()
  handleClose()
  console.log("set valider true")
  console.log(mail)
  //alert("validé : "+ valider)
  Axios.patch(`http://localhost:8000/Signal/signal/${idSignal}/`, {
      "validerSg": valider ,
      "idModerateurSg":localStorage.getItem("idUser")
  }, { headers: { "Authorization": `Token ${token}` } })
      .then(res => {
          console.log(res)
      })
      handleClickOpen2()
}

const envoyerMail = () => {
  mail.attach=lien
  mail.message=des
  //alert(mail.message)
  //alert(mail.attach)
  //alert(mail.subject)
  //getSignalements()
  console.log(mail)
  //console.log("set valider true")
  Axios.post(`http://localhost:8000/Signal/email/`,mail, { headers: { 'Content-Type' : 'application/json'} })
      .then(res => {
          console.log(res)
         
      }).catch(error=>alert("im here"))
}


  useEffect(() => { 
    getSignalements('http://localhost:8000/Signal/signal_non_valide/')
    /*
    Axios.get('http://localhost:8000/Signal/signal/',
    { headers: { 'Content-Type' : 'application/json' } }
    ).then (data=>  { 
      console.log(data.data)
      setNext(data.data.next)
      if(data.data.results.length!=0){
        setLoading(true)
      }
      setSingnalements(data.data.results)
      }).catch(error =>
        {
          alert(error)
        }
        )*/
      },[]);
      console.log(mail)
  return (
    
    <GridItem >
       
      {loading?

      singnalements.map((prop, key) => {
        const url= '/moderateur/signalement/profile$'+ prop.idUtilisateurSg.id
    return (
   
    <Card className={classes.card} key ={key}>
        <CardHeader >
        <GridContainer >
        <GridItem  xs={2} sm={6} md={1} >   
          <Avatar>{prop.idUtilisateurSg.username[0].toUpperCase()}</Avatar> 
        </GridItem>
        <GridItem  xs={6} sm={6} md={7} >   
        <NavLink
            to={url} 
    
          > 
          <p className={classes.title}  >
             
             {prop.idUtilisateurSg.username}
        
        
           </p>  </NavLink> 

           <p className={classes.stitle} >
               {formatDate(prop.dateSg)}
              </p>

        </GridItem>
        </GridContainer >    
        </CardHeader>
         
    <CardBody >
     
    <GridContainer >
    <GridItem  xs={12} sm={12} md={12} >   
    <h2 className={classes.text} style={{ fontSize: 16 , fontWeight: 'bold '}}>Description de signalement : </h2>   
        <p className={classes.text}>
        {prop.descriptionSg}</p>
   </GridItem>
   <center>
    <GridItem  xs={12} sm={12} md={10} >   
     <a href ={prop.lienSg} ><img src={prop.lienSg} className={classes.media} alt="..." /></a>
    </GridItem>
    </center>
    </GridContainer>
    </CardBody>
    <CardFooter>
   
    <GridItem  xs={6} sm={6} md={6} >   
    <Button  className={classes.Button }  onClick = {() =>handleClickOpen(prop.idSignal,true,prop.lienSg, prop.descriptionSg)}  >
        Accepter
     </Button> 
    </GridItem>

    <GridItem  xs={6} sm={6} md={6} >   
        <Button className={classes.Button2} onClick = {() =>handleClickOpen(prop.idSignal,false)} >
        Refuser
     </Button> 
    </GridItem>
    </CardFooter>
   
     </Card>

      );
    }) : "pas de signalments à valider"}

<div className={classes.pages}>
 <Previous onClick={handleChangePreviousPage}></Previous>
            <p style={{display : "inline-block", margin : "20px" }}>{page} - {current}</p>
    <Next onClick={handleChangeNextPage}></Next>
   
</div>

<Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title">
   <DialogTitle id="form-dialog-title">Confirmation</DialogTitle>
   <DialogContent>
     <DialogContentText>
    
     </DialogContentText>
     <p className={classes.text}>
     {valider ?'Etes vous sure de vouloir valider ce signalement ?': 'Etes vous sure de vouloir rejeter ce signalement?' }
         </p>
   </DialogContent>
   <DialogActions>
   <Button onClick={() =>accepter(id)} color="primary">
      Confirmer
     </Button>
     <Button onClick={handleClose} color="primary">
       Quitter
     </Button>
   </DialogActions>
 </Dialog>
 
 <Dialog open={open2} onClose={handleClose2} aria-labelledby="form-dialog-title">
   <DialogTitle id="form-dialog-title">Confirmation</DialogTitle>
   <DialogContent>
     <DialogContentText>
     <p className={classes.text}>
    Voulez vous envoyer un mail aux membre de CCC ?</p>
     </DialogContentText>
     <center>
     <form className={classes.root} >
              <FormControl >
                  <InputLabel shrink className={classes.text} >
                   Objet
                  </InputLabel>
                  <BootstrapInput   type='text' name="E-mail" 
                  onChange={e => mail.subject=(e.target.value)}  />
              </FormControl>
<br></br>
              <FormControl>
                  <InputLabel shrink className={classes.text}   >
                 Source
                  </InputLabel>
                  <BootstrapInput type='text' name="objet" 
                  onChange={e => mail.email_from=(e.target.value)}  />
              </FormControl>
              <br></br>   
              <FormControl>
                  <InputLabel shrink className={classes.text}   >
                 Distinataire
                  </InputLabel>
                  <BootstrapInput type='text' name="objet" 
                  onChange={e => mail.recipient_list=(e.target.value)}  />
              </FormControl>
              <br></br>       
              <FormControl >
                  <InputLabel  shrink className={classes.text} >
                 Message
                  </InputLabel>
                  <BootstrapInput  type='text' name="message" value={des} 
                  />
              </FormControl>
              <br></br>
              <FormControl>
                  <InputLabel shrink className={classes.text}   >
                 Piece jointe
                  </InputLabel>
                  <BootstrapInput type='text' name="objet" value={lien}
                   />
              </FormControl>
              <br></br> 
                           
              <Button  className={classes.ButtonM } type="submit" onClick={e =>envoyerMail()} >
               Envoyer
               </Button>
              </form>
              </center>
   </DialogContent>
   <DialogActions>
     <Button onClick={handleClose2} color="primary">
       Annuler
     </Button>
   </DialogActions>
 </Dialog>
 
     </GridItem> 
    
    );
}
