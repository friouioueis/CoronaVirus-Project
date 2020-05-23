import React from "react";
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
import CustomInput from "components/CustomInput/CustomInput.js";
import Table from "components/Table/TableCostum.js";
import points from "@material-ui/icons/ControlPoint";
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
//import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
// dialog
import TextField from '@material-ui/core/TextField';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

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

  const [open, setOpen] = React.useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };


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
              tableData={rows}
            >
  
      </Table>

     </GridContainer>

     <Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title">
        <DialogTitle id="form-dialog-title">Subscribe</DialogTitle>
        <DialogContent>
          <DialogContentText>
            To subscribe to this website, please enter your email address here. We will send updates
            occasionally.
          </DialogContentText>
          <TextField
            autoFocus
            margin="dense"
            id="name"
            label="Email Address"
            type="email"
            fullWidth
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose} color="primary">
            Cancel
          </Button>
          <Button onClick={handleClose} color="primary">
            Subscribe
          </Button>
        </DialogActions>
      </Dialog>
    
    </CardBody>
     </Card>
     </GridItem>
  );
}
