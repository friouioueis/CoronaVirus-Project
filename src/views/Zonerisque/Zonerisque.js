import React , {useEffect} from "react";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
// core components
import GridItem from "components/Grid/GridItem.js";
import GridContainer from "components/Grid/GridContainer.js";
import Card from "components/Card/Card.js";
import CardBody from "components/Card/CardBody.js";
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import {
    fade,
    withStyles,
  } from '@material-ui/core/styles';
  import InputBase from '@material-ui/core/InputBase';
  import InputLabel from '@material-ui/core/InputLabel';
  import FormControl from '@material-ui/core/FormControl';
  import FormControlLabel from '@material-ui/core/FormControlLabel';
  import { Scrollbars } from 'react-custom-scrollbars';
  import Checkbox from '@material-ui/core/Checkbox';
  import ListItem from '@material-ui/core/ListItem';
  import SearchIcon from '@material-ui/icons/Search';


const   useStyles = makeStyles(theme => ({
  paper: {
    marginTop: "80px",
 
  },
  
  Button: {
    minWidth: '50%',
    color : 'white',
  
    backgroundColor: '#39aac4',
    '&:hover': {
      backgroundColor: "#39aac4",
     }, 
     fontFamily: '"Segoe UI"', 
     fontWeight: 'bold',
  },
  text: {
    fontSize: 20,
    fontWeight: 'bold',
    fontFamily: "Segoe UI" 
   
   
  },
  textField: {
    marginLeft: theme.spacing(1),
    marginRight: theme.spacing(1),
    width: 200,
  },
  check: {
    fontSize: 20,
    fontWeight: 'bold',
    fontFamily: "Segoe UI",
    //display : "block" ,
    padding: '15px 5px',
    marginBottom: 30,
  },
  title: {
    fontSize: 25,
    fontWeight: 'bold',
    fontFamily: '"Segoe UI"', 
    color : '#757575',
    padding: '30px 10px',
   // borderRight: '1px solid #ced4da',
  },
 
  item: {
    fontFamily: '"Segoe UI"',
    fontSize: 14,
    padding : "20px",
    listStyleType: "none",
    fontWeight: 'bold', 
    cursor : 'pointer',
    color : '#757575',
    '&:hover': {
      backgroundColor: "#d6cfc7",
     }, 
  },
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
      //width: '12ch',
      '&:focus': {
        width: '20ch',
      },
    },
  },
  search: {
    position: 'relative',
    border: '1.5px solid #ced4da',
    top : "25px",
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
}));
//const useStyles  = makeStyles(styles);
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


  const renderThumb = ({ style, ...props }) => {
    const thumbStyle = {
      borderRadius: 8,
      backgroundColor:  '#757575',
      margin : 3,
      width : 5
    };
    return <div style={{ ...style, ...thumbStyle }} {...props} />;
  };
  
  const CustomScrollbars = props => (
    <Scrollbars
      renderThumbVertical={renderThumb}
      {...props}
    />
  );

  

export default function Zone() {

const token= localStorage.getItem("token");
const  [ wilayas ,setWilayas ]= React.useState([]);
var check= false
const  [ loading ,setLoading ]= React.useState(true);
const  [ open ,setOpen ]= React.useState(false);
//var open = false
const [nomWilaya, setNom] = React.useState("Wilaya");
const [idWilaya, setId] = React.useState(0);
const [filtre, setFiltre] = React.useState([]);
const [selectedDate, setSelectedDate] = React.useState(new Date('2014-08-18T21:11:54'));
const classes = useStyles();  
 const [selectedIndex, setSelectedIndex] = React.useState(0);
const handleListItemClick = (event, index,w) => {
  setSelectedIndex(index);
  setNom(w.nomRegion);
 setId(w.idRegion);
};
const handleDateChange = (date) => {
  setSelectedDate(date);
};
const handleChange = (event) => {
  let current = []
  let newlist = []
  let lc =""
  let fl =""
  current = wilayas
  newlist = current.filter(
    item=> 
    {lc = item.nomRegion.toLowerCase() 
     fl=event.target.value.toLowerCase()
     return(
      lc.includes(fl)
     )
    }
     )

setFiltre(newlist)
};

useEffect(() => { 
  fetch("http://127.0.0.1:8000/Region/regions/", {
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
   }).then(wilayas=>{
     setWilayas(wilayas.results);
     setFiltre(wilayas.results)
     console.log(wilayas);
    })
   .catch(error =>alert(error));
 
   },[]);
   
   
  const lis = filtre.map((w,key1)=>{  
    return (
    <ListItem 
    button 
    key ={key1}
    className={classes.item} 
    selected={selectedIndex === key1 } 
    value={w.nomRegion}
    onClick={(event) => handleListItemClick(event, key1,w)} 
    > 
    {w.nomRegion}
    </ListItem> 
    );
});


const region = {
  properties :{
    is_risque : false
  }
}

const state ={
  credentials :{
    nbrPorteurVirus :0 , 
    casConfirme : 0,  
    casRetablis:0 , 
    nbrDeces : 0 , 
    nbrGuerisons:0, 
    dateSt : "2020-03-28T02:21:56Z",
    idRegionSt : idWilaya,
    idAgentSt : localStorage.getItem("idUser")
  }
}

const update = (event,urlRg,urlStat) => {
    setOpen(false)
    console.log(state.credentials)
  const request = urlRg+ idWilaya+'/isRisque/'
    if (idWilaya===0){alert ("please enter a wilaya")}
    else{
    fetch(urlStat, {
      method : 'POST',
      headers:{
      'Content-Type' : 'application/json',
      'Authorization' : 'Token '+token
    },
      body:  JSON.stringify(state.credentials)
    })
    .then(data => data.json())
    .then(
      data => {
       console.log(data)
    
      }
    )
  .then(
     fetch(request, {
       method : 'PATCH',
       headers:{
        'Content-Type' : 'application/json',
        'Authorization' : 'Token '+token
      },
       body:  JSON.stringify(region.properties)
     })
     .then(data1 => data1.json())
     .then(
       data1 => {
        console.log(data1)
        alert("Statistique inséerés avec success ")
       }
     ).catch(error =>alert(error)))
     .catch(error =>alert(error));
    
      }
    
}



  return (
    
    <GridItem  xs={12} sm={6} md={9}  > 
      <Card>
      <CardBody style={{ padding: 0 }}  justify={"center"}>

      <GridContainer >
          <GridItem  xs={5} sm={6} md={3} >   
          <div className={classes.title}  style={{  borderRight: '1.5px solid #ced4da',borderBottom: '1.5px solid #ced4da'}}>Wilayas</div>    
          </GridItem>
          <GridItem  xs={5} sm={6} md={6} >   
     <div className={classes.search} >
            <div className={classes.searchIcon}>
              <SearchIcon style={{ color :'#757575' }}  />
            </div>
            <InputBase
              placeholder="Rechercher une wilaya …"
              classes={{
                root: classes.inputRoot,
                input: classes.inputInput,
              }}
              inputProps={{ 'aria-label': 'search' }}
              onChange ={handleChange}
            />
          </div>

      </GridItem>
      </GridContainer >  

      <GridContainer >
          <GridItem  xs={5} sm={6} md={3}     >      
          <CustomScrollbars  value =  {lis} style={{ borderRight: '1.5px solid #ced4da' }}  >
          {lis} 
          </CustomScrollbars>
         </GridItem>
     
          <GridItem  xs={7} sm={6} md={9} style={{marginBottom: '15px'}}  > 
          <div className={classes.title} >{nomWilaya}</div> 
          <form className={classes.root} >
              <FormControl >
                  <InputLabel shrink className={classes.text} >
                  Porteurs de virus
                  </InputLabel>
                  <BootstrapInput   type='text' name="porteur" 
                  onChange={e => state.credentials.nbrPorteurVirus=(e.target.value)}  />
              </FormControl>

              <FormControl>
                  <InputLabel shrink className={classes.text}   >
                  Nombre de guerisons
                  </InputLabel>
                  <BootstrapInput type='text' name="nbrGuerisons" 
                  onChange={e => state.credentials.nbrGuerisons=(e.target.value)}  />
              </FormControl>
              
              <FormControl >
                  <InputLabel  shrink className={classes.text} >
                  Cas confirmés
                  </InputLabel>
                  <BootstrapInput  type='text' name="casConfirme" 
                  onChange={e => state.credentials.casConfirme=(e.target.value)} />
              </FormControl>

              <FormControl >
                  <InputLabel  shrink className={classes.text}  >
                  Nombre de décés
                  </InputLabel>
                  <BootstrapInput  type='text' name="nbrDeces" 
                  onChange={e => state.credentials.nbrDeces=(e.target.value)} />
              </FormControl>

              <FormControl >
                  <InputLabel  shrink className={classes.text} >
                  Cas rétablis
                  </InputLabel>
                  <BootstrapInput  type='text' name="casRetablis" 
                  onChange={e => state.credentials.casRetablis=(e.target.value)}/>   
              </FormControl>

              <FormControlLabel value="end" control={<Checkbox color="default" />}  className={classes.check } label="Signaler comme zone de risque" labelPlacement="end" 
              onClick={event => {
                 if (check===false){
                   region.properties.is_risque= true
                  check=true
                  }
                 else{
                   region.properties.is_risque= false
                   check=false
                  }
                
                }} />

              <FormControl >
              <InputLabel  shrink className={classes.text} >
                  Date
                  </InputLabel>
                <BootstrapInput 
                  id="datetime-local"
                  type="datetime-local"
                  defaultValue="0000-00-00T00:00"
                InputLabelProps={{
                  shrink: true,
                }}
                onChange={e => 
                  state.credentials.dateSt=(e.target.value)
                } />
            
              </FormControl>               
         

              <Button  className={classes.Button } type="submit" onClick={(event) => update(event,"http://127.0.0.1:8000/Region/regions/","http://127.0.0.1:8000/Region/stat_regions/")} >
               Envoyer
               </Button>
               

              </form>
          </GridItem>
          </GridContainer>
      
  
    </CardBody>
     </Card>
     <Dialog open={open} onClose={event => setOpen(false)} aria-labelledby="form-dialog-title">
   <DialogTitle id="form-dialog-title">Connexion</DialogTitle>
   <DialogContent>
     <DialogContentText>
     choisissez le role que vous voulez s'authentifié avec :
     </DialogContentText>
       
     
   </DialogContent>
   <DialogActions>

     <Button onClick={event => setOpen(false)} color="primary">
       Annuler
     </Button>
     <Button type="submit" color="primary" >
      Connexion
     </Button>

   </DialogActions>
 </Dialog>
     </GridItem>
  );
}
