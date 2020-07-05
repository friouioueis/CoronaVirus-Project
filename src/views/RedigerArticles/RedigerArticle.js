
import React, { Component, useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import SunEditor from 'suneditor-react';
import 'suneditor/dist/css/suneditor.min.css'; // Import Sun Editor's CSS File
import Button from '@material-ui/core/Button';
// import { useSnackbar } from 'notistack';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import moment from "moment";
import { withStyles } from '@material-ui/core/styles';
import Axios from 'axios';

// const { enqueueSnackbar } = useSnackbar();

const useStyles = makeStyles(theme => ({
    accbutt: {
        backgroundColor: '#00acc1',
        '&:hover': {
            backgroundColor: '#00acc1',
        },

    },
}));

class RecipeReviewCard extends React.Component {
 
    constructor(props) {
        super(props);

        this.state = {
            article: "",
            photos: null,
            open : false
        }
    }

   handleClickOpen =  () => {
    this.setState({open : true});
        //setValider(val)
      };
   
  handleClose = () => {
    this.setState({open : false});
      };

    handleChange = (e) => {

        console.log(this.state.article)
        console.log(e); //Get Content Inside Editor
        this.setState({

            article: e

        })


        console.log("after " + this.state.article)


    }

   

    handlesubmit = (e) => {
        e.preventDefault()
       
        console.log("axios post")
        const token = localStorage.getItem("token")
        this.handleClose()
        Axios.post('http://localhost:8000/articles/articles/', {
            "dateAr" :   moment().format("YYYY-MM-DD[T]HH:mm:ss"),
            "contenuAr": this.state.article,
            "terminerAR" : false,
            "idRedacteurAr": localStorage.getItem("idUser")
        }, { headers: { "Authorization": `Token ${token}` } }
        ).then(res => {
            console.log(res)
            console.log(res.data.idArticle)
            window.location.reload(false);
            // this.handleClickVariant('success')
        })
    }
  set_terminer = (e) => {
    e.preventDefault()
    
    console.log("axios post")
    const token = localStorage.getItem("token")
    this.handleClose()
    Axios.post('http://localhost:8000/articles/articles/', {
        "dateAr" :  moment().format("YYYY-MM-DD[T]HH:mm:ss"),
        "contenuAr": this.state.article,
        "terminerAR" : true,
        "idRedacteurAr": localStorage.getItem("idUser")
    }, { headers: { "Authorization": `Token ${token}` } }
    ).then(res => {
        console.log(res)
        console.log(res.data.idArticle)
        alert("Article terminer avec succes , il ajouter a la liste des articles en attente de validation")
        window.location.reload(false);
        // this.handleClickVariant('success')
    })
    }

       render() {
        const { classes } = this.props;

        return (
            <div>
                <SunEditor onChange={this.handleChange} setOptions={{
                    height: 100,
                    "buttonList": [
                        ["undo",
                            "redo",
                            "font",
                            "fontSize",
                            "formatBlock"],
                        ["bold",
                            "underline",
                            "italic",
                            "strike",
                            "subscript",
                            "superscript"],
                        ["fontColor",
                            "hiliteColor"],
                        ["removeFormat",
                            "outdent",
                            "indent"],
                        ["align",
                            "horizontalRule",
                            "list",
                            "lineHeight"],
                        ["table",
                            "link"],
                        ["image",
                            "video"],

                    ],
                }} />
                <br></br>
             
                    <Button type="submit" variant="contained" color="primary" onClick={() => this.handleClickOpen()} className={classes.accbutt}>
                        Terminer
                    </Button>

    


                  
<Dialog open={this.state.open} onClose={this.handleClose} aria-labelledby="form-dialog-title">
   <DialogTitle id="form-dialog-title">Confirmation</DialogTitle>
   <DialogContent>
     <p className={classes.text}>
     Enregistrer cet article dans la liste des articles non encore terminé ou bien confirmer qu'il est terminé pour etre validé par un moderateur
         </p>
   </DialogContent>
   <DialogActions>
   <Button  color="primary" onClick={this.handlesubmit}  type = "submit">
     Enregistrer comme brouillant
     </Button>
     <Button onClick={this.set_terminer} color="primary">
      Terminer
     </Button>
   </DialogActions>
 </Dialog>
            </div>

        );

    }



}



export default withStyles(useStyles)(RecipeReviewCard);