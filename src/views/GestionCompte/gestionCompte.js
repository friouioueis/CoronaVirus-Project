import React , {useEffect}  from "react";
// @material-ui/core components
import {  fade,makeStyles } from "@material-ui/core/styles";
// core components
import GridItem from "components/Grid/GridItem.js";
import GridContainer from "components/Grid/GridContainer.js";
import Card from "components/Card/Card.js";
import CardBody from "components/Card/CardBody.js";
import Button from '@material-ui/core/Button';
import SearchIcon from '@material-ui/icons/Search';
import InputBase from '@material-ui/core/InputBase';
import ClickAwayListener from "@material-ui/core/ClickAwayListener";
import Axios from 'axios';
import CustomInput from "components/CustomInput/CustomInput.js";
import Table from "components/Table/TableCostum.js";
import Notifications from "@material-ui/icons/Notifications";
import MenuItem from "@material-ui/core/MenuItem";
import MenuList from "@material-ui/core/MenuList";
import Grow from "@material-ui/core/Grow";
import Paper from "@material-ui/core/Paper";
import Hidden from "@material-ui/core/Hidden";
import Poppers from "@material-ui/core/Popper";
import points from "@material-ui/icons/ControlPoint";
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
//import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
// dialog
import TextField from '@material-ui/core/TextField';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import classNames from "classnames";
import generate from "@babel/generator";
const token = localStorage.getItem("token")

const useStyles = makeStyles(theme => ({
  inputRoot: {
    color: 'inherit',
  
  },
  inputInput: {
    padding: theme.spacing(1, 1, 1, 0),
    fontWeight: 'bold ',
    fontFamily: '"Segoe UI"',
    // vertical padding + font size from searchIcon
    paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
    transition: theme.transitions.create('width'),
    width: '100%',
    [theme.breakpoints.up('sm')]: {
      width: '12ch',
      '&:focus': {
        width: '20ch',
      },
    },
  },
  search: {
    position: 'relative',
    border: '1.5px solid #ced4da',
    borderRadius: theme.shape.borderRadius,
   backgroundColor: fade(theme.palette.common.white, 0.15),
    '&:hover': {
      backgroundColor: fade(theme.palette.common.white, 0.25),
    },
    marginLeft: 0,
    width: '100%',
    [theme.breakpoints.up('sm')]: {
      marginLeft: theme.spacing(1),
    width: 'auto',
    },
  },
  searchIcon: {
    padding: theme.spacing(0, 2),
    height: '100%',
    position: 'absolute',
    pointerEvents: 'none',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    
  },
  card: {
       padding : "10px 50px",
      },
  text: {
        fontSize: 20,
        fontWeight: 'bold ',
        fontFamily: '"Segoe UI"', 
        color : '#757575',
       margin : 0
      
      },
  text2: {
        color: "#39aac4",
        fontSize: 25,
        fontWeight: 'bold ',
        fontFamily: '"Segoe UI"', 
        margin :8
        
      },
  Button: {
        minWidth: '80%',
        color : 'white',
        backgroundColor: '#39aac4',
        '&:hover': {
          backgroundColor: "#39aac4",
         }, 
         fontFamily: '"Segoe UI"', 
         fontWeight: 'bold',
      },
    }));
//const useStyles  = makeStyles(styles);
function createData(name, calories, fat) {
    return { name, calories, fat };
  }
  
  const rows = [
    createData('Frozen yoghurt', 159, 6.0),
    createData('Ice cream sandwich', 237, 9.0),
    createData('Eclair', 262, 16.0),
    createData('Cupcake', 305, 3.7),
    createData('Gingerbread', 356, 16.0),
  ];

export default function GestionCompte() {
 
  const classes = useStyles();
  const redacteur= 0 ;
  const moderateur= 0 ;
  const agent= 0 ;
  const total= 0 ;
  const [filtre, setFiltre] = React.useState([]);
  const [data, setData] = React.useState([]);
  const [open, setOpen] = React.useState(false);
  const [rand, setRand] = React.useState("");
  const  [ loading ,setLoading ]= React.useState(false);
  const [openNotification, setOpenNotification] = React.useState(null);
  const [openProfile, setOpenProfile] = React.useState(null);
  const handleClickNotification = event => {
    if (openNotification && openNotification.contains(event.target)) {
      setOpenNotification(null);
    } else {
      setOpenNotification(event.currentTarget);
    }
  };
  const handleCloseNotification = () => {
    setOpenNotification(null);
  };
  const handleClickProfile = event => {
    if (openProfile && openProfile.contains(event.target)) {
      setOpenProfile(null);
    } else {
      setOpenProfile(event.currentTarget);
    }
  };
  const handleCloseProfile = () => {
    setOpenProfile(null);
  };

  const changeRole = ( type, id ) => {
   // alert(type)
   // alert(id)
    Axios.post("http://localhost:8000/Utilisateurs/gestionComptes/roles/",
     {
      "Type": type,
      "idUtilisateurR": id
     },
       { headers: { 'Content-Type' : 'application/json','Authorization': `Token ${token}` } })
    .then(res => {
        console.log(res.data)            
    }).catch(error=> alert(error))
  };
  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };
  const handleChange = (event) => {
    let current = []
    let newlist = []
    let lc =""
    let fl =""
    current = data
    console.log(current)
    newlist = current.filter(
      item=> 
      {lc = item.username.toLowerCase() 
       fl=event.target.value.toLowerCase()
       return(
        lc.includes(fl)
       )
      }
       )
  
  setFiltre(newlist)
  };
  useEffect(() => { 
    fetch("http://localhost:8000/Utilisateurs/gestionComptes/comptes/", {
      method : 'GET',
      headers: {
      'Content-Type' : 'application/json',
      }
    }
    )
    .then((response) => response.json())
    .then(
      (responseJson) => {
        return responseJson
     }).then(data=>{
       setData(data.results);
       setFiltre(data.results)
       setLoading (true)
       console.log(data);
      })
     .catch(error =>alert(error));
   
     },[]);
    
const state ={
  credentials :{
    username :"" , 
    email : "",  
    password1: "", 
    password2 : "", 
     }
}

function formatDate(string){
  var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: "2-digit", minute:"2-digit"};
  return new Date(string).toLocaleDateString([],options);
}
  const subscribe = (event , url) => {
   handleClose()
   console.log(state.credentials)
  // alert(url)
    Axios.post(url,
     state.credentials,
       { headers: { 'Content-Type' : 'application/json','Authorization': `Token ${token}` } })
    .then(res => {
        console.log(res.data)   
        alert("utilisateur  ajouter avec succes")         
    }).catch(error=> {
      if(state.credentials.password1.length < 8){
alert("ERREUR : le mot de passe doit contenir au moins 8 characteres")
      }else{
        if(state.credentials.password1===state.credentials.password2){
          alert("ERREUR : veuillez entrer le mot de passe correctement")
                
      }
      alert("Erreur l'utilisateur ne peut pas etre ajouter ")
    }}
      )
  };

 const generate= () => {
    const min = 1
    const max = 900000
    const rand = (min + Math.random()* (max - min)).toString(36) 
     setRand(rand)
  //   alert(rand)
   //  alert((min + Math.random()* (max - min)).toString(36) )
  }

  var table_info = [
  ]
filtre.map(info => {
  console.log(table_info);
      if ( loading===true) { 
          return (
              table_info.push([
                  info.username, 
                   info.email,
                   formatDate(info.last_login), 
                   info.roles,
                   info.id,
               ])
          )
      }
  })

  console.log(table_info);
  return (
    <GridItem  xs={12} sm={12} md={10}  justify={"center"}  > 
      <Card className={classes.card} >
      <CardBody >
      <GridContainer >
          <GridItem  xs={3} sm={6} md={3}   style={{ borderRight: '1.5px solid #ced4da' }}   >   
          <p className={classes.text}> <p className={classes.text2}  >{redacteur}</p>Rédacteurs</p>    
          </GridItem>
          <GridItem  xs={3} sm={6} md={3}  style={{ borderRight: '1.5px solid #ced4da' }}   >   
          <p className={classes.text}> <p className={classes.text2}  >{moderateur}</p>Moderateurs</p>    
          </GridItem>
          <GridItem  xs={3} sm={6} md={3}  style={{ borderRight: '1.5px solid #ced4da' }}   >   
          <p className={classes.text}> <p className={classes.text2}  >{agent}</p>Agent de santé</p>    
          </GridItem>
          <GridItem  xs={3} sm={6} md={3}   >   
          <p className={classes.text}> <p className={classes.text2}  >{total}</p>Total</p>    
          </GridItem>
     </GridContainer>

     <GridContainer style={{ padding:"40px 10px 10px 0px" }}   >
     <GridItem  xs={6} sm={6} md={6} >   
     <div className={classes.search} >
            <div className={classes.searchIcon}>
              <SearchIcon style={{ color :'#757575' }}  />
            </div>
            <InputBase
              placeholder="Rechercher…"
              classes={{
                root: classes.inputRoot,
                input: classes.inputInput,
              }}
              inputProps={{ 'aria-label': 'search' }}
              onChange ={handleChange}
            />
          </div>

      </GridItem>
      <GridItem  xs={6} sm={6} md={6}>    
     <Button type="submit" className={classes.Button } onClick={handleClickOpen} >
        Ajouter un compte
     </Button> 
     </GridItem>
     </GridContainer >
    
     <GridContainer >
     <Table
              tableHeaderColor= "gray"
              tableHead={["Nom", "Type", "Deriere activité"]}
              tableData={table_info}
            >
  
      </Table>

     </GridContainer>

     <Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title">
        <DialogTitle id="form-dialog-title">Ajouter un compte utilisateur</DialogTitle>
        <DialogContent style={{margin : "10px 50px"}} >
          <DialogContentText>
            Pour ajouter un compte utilisateur et lui affecter un role
          </DialogContentText>
          <TextField
            autoFocus
            required
            margin="dense"
            id="name"
            label="Nom de l'utilisateur"
            type="email"
            fullWidth
            variant="outlined"
            onChange={e => state.credentials.username=(e.target.value)} 
          />
            <TextField
            autoFocus
            required
            margin="dense"
            id="name"
            label="Addresse Email "
            type="email"
            variant="outlined"
            fullWidth
            onChange={e => state.credentials.email=(e.target.value)} 
          />
            <TextField
            autoFocus
            required
            margin="dense"
            id="name"
            label=" Mot de passe "
            type="password"
            variant="outlined"
            onChange={e => state.credentials.password1=(e.target.value)} 
            fullWidth
                    /> 

<TextField
            autoFocus
            required
            margin="dense"
            id="name"
            label=" Confirmer le mot de passe "
            type="password"
            variant="outlined"
            onChange={e => state.credentials.password2=(e.target.value)} 
            fullWidth
                    />
           

        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose} color="primary">
            Annuler
          </Button>
          <Button onClick={(event) => subscribe(event,"http://localhost:8000/Utilisateurs/rest-auth/registration/")} color="primary">
            Ajouter
          </Button>
        </DialogActions>
      </Dialog>
    
    </CardBody>
     </Card>
     </GridItem>
  );
}
