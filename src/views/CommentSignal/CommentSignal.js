// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
// core components
import GridItem from "components/Grid/GridItem.js";
import GridContainer from "components/Grid/GridContainer.js";
import Table from "components/Table/Table.js";
import Card from "components/Card/Card.js";
import CardHeader from "components/Card/CardHeader.js";
import CardBody from "components/Card/CardBody.js";
import Button from '@material-ui/core/Button';
import DeleteIcon from '@material-ui/icons/DeleteOutlineTwoTone';
import IconButton from '@material-ui/core/IconButton';
import Tooltip from '@material-ui/core/Tooltip';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import Next from '@material-ui/icons/NavigateNextOutlined';
import Previous from '@material-ui/icons/NavigateBeforeOutlined';
import React, { Component, useState, useEffect } from 'react';
import Axios from 'axios';

const styles = {
    cardCategoryWhite: {
        "&,& a,& a:hover,& a:focus": {
            color: "rgba(255,255,255,.62)",
            margin: "0",
            fontSize: "14px",
            marginTop: "0",
            marginBottom: "0"
        },
        "& a,& a:hover,& a:focus": {
            color: "#FFFFFF"
        },
    }, 
    
    pages:{
        marginLeft : "50%"
    },
    cardTitleWhite: {
        color: "#FFFFFF",
        marginTop: "0px",
        minHeight: "auto",
        fontWeight: "300",
        fontFamily: "'Roboto', 'Helvetica', 'Arial', sans-serif",
        marginBottom: "3px",
        textDecoration: "none",
        "& small": {
            color: "#777",
            fontSize: "65%",
            fontWeight: "400",
            lineHeight: "1"
        }
    },
    icon: {
        color: "red",
    }
};

const useStyles = makeStyles(styles);

export default function TableList() {
    const [comment_signal, set_comment_signal] = useState([])
    const classes = useStyles();
    const [user, setUser] = useState([])
    const token = localStorage.getItem("token");
    const  [ loading ,setLoading ]= React.useState(false);
    const  [ open ,setOpen ]= React.useState(false);
    const  [ idCom ,setIdCom ]= React.useState(0);
    const [page, setPage] = React.useState(1);
  const [current, setCurrent] = React.useState(10);
  const [next, setNext] = React.useState(null);
  const [previous, setPrevious] = React.useState(null);

    const handleChangeNextPage = (event, value) => {
        if(next != null){
         //   alert ("next")
        setPage(page+10);
        setCurrent(current+10)
        get_comment_signal(next)
        }
      };
      const handleChangePreviousPage = (event, value) => {
        if(previous != null){
         //   alert ("previous")
        setPage(page-10);
        setCurrent(current-10)
        get_comment_signal(previous)
        }
      };
    const handleClickOpen =  ( idCom) => {
        setIdCom (idCom)
        setOpen(true)
      };
   
     const handleClose = () => {
        setOpen(false)
      };

    useEffect(() => {
        get_comment_signal('http://localhost:8000/articles/commentaires')
    }, [])

    const get_comment_signal = (url) => {
        console.log("dada")
        Axios.get(url)
            .then(res => {
                console.log(res.data.results)
                set_comment_signal(res.data.results)
                if(res.data.next != null){
                    setNext(res.data.next)
                    }else{
                        setNext(null)
                    }
                    if(res.data.previous != null){
                    setPrevious(res.data.previous)
                    }else{
                        setPrevious(null)
                    }
            }).then(  
                Axios.get(`http://localhost:8000/Utilisateurs/gestionComptes/comptes/`)
                .then(res => {
                    setUser(res.data.results)
                    console.log(res.data.results)
                    setLoading (true)
                })
                   ) 
    }
 
    var table_info = []
    comment_signal.map(comment => {
        console.log( user.find( user => user.id === comment.idUtilisateurCom))
        if (comment.signalerCom === false && loading===true) {
            return (
                table_info.push([ user.find( user => user.id === comment.idUtilisateurCom).username, comment.contenuCom, <Tooltip title="Delete"><IconButton onClick={() => handleClickOpen(comment.idCommentaire)} aria-label="delete" className={classes.icon}><DeleteIcon style={{color : "#757575"}} /></IconButton></Tooltip>])
            )
        }

    })

    const delete_comment = (id) => {
        handleClose()
        Axios.delete(`http://localhost:8000/articles/commentaires/${id}/`, { headers: { "Authorization": `Token ${token}` } })
            .then(res => {
                console.log(res)
                alert("Commentaire supprimer avec succes")
            })
         window.location.reload(false);
    }


    return (
        <Card>
               <CardHeader color = "info">
            <h4 className={classes.cardTitleWhite}> Commentaires signalés</h4>
            <p className={classes.cardCategoryWhite}>
             Suprimer les commentaires non desirables
            </p>
          </CardHeader>
            <CardBody>
                <Table
                    tableHead={["Utilisateur", "Contenu", "Action"]}
                    tableData={
                        table_info
                    }
                />
            </CardBody>
    <Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title">
   <DialogTitle id="form-dialog-title">Confirmation</DialogTitle>
   <DialogContent>
     <DialogContentText>
    
     </DialogContentText>
     <p className={classes.text}>
         etes vous sure de vouloir supprimer ce commentaire??
         </p>
   </DialogContent>
   <DialogActions>
   <Button  color="primary" onClick={()=>delete_comment(idCom)}>
      Confirmer
     </Button>
     <Button onClick={handleClose} color="primary">
       Annuler
     </Button>
   </DialogActions>
 </Dialog>
 <div className={classes.pages}>
 <Previous onClick={handleChangePreviousPage}></Previous>
            <p style={{display : "inline-block", margin : "20px" }}>{page} - {current}</p>
    <Next onClick={handleChangeNextPage}></Next>
   
</div>
        </Card>
    )
}