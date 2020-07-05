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
import Check from '@material-ui/icons/CheckBoxOutlined';
import Next from '@material-ui/icons/NavigateNextOutlined';
import Previous from '@material-ui/icons/NavigateBeforeOutlined';
import IconButton from '@material-ui/core/IconButton';
import Tooltip from '@material-ui/core/Tooltip';
import React, { Component, useState, useEffect } from 'react';
import Axios from 'axios';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';


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
    },
    icon2: {
        color: "green",
    }
};


const useStyles = makeStyles(styles);

export default function TableList() {
    const [info_Regions, set_info_Regions] = useState([])
    const classes = useStyles();
    const  [ open ,setOpen ]= React.useState(false);
  const  [ valider ,setValider ]= React.useState(false);
  const  [ idstat ,setIdstat ]= React.useState(false);
    const [reg, setReg] = useState([])
    const token = localStorage.getItem("token")
    const  [ loading ,setLoading ]= React.useState(false);
    const [page, setPage] = React.useState(1);
    const [current, setCurrent] = React.useState(10);
    const [next, setNext] = React.useState(null);
    const [previous, setPrevious] = React.useState(null);

    const handleChangeNextPage = (event, value) => {
        if(next != null){
        setPage(page+10);
        setCurrent(current+10)
        get_info_wilaya(next)
        }
      };
      const handleChangePreviousPage = (event, value) => {
        if(previous != null){
        setPage(page-10);
        setCurrent(current-10)
        get_info_wilaya(previous)
        }
      };
    const handleClickOpen =  ( id_stat, val) => {
        setValider(val)
        setIdstat (id_stat)
        setOpen(true)
      };
   
     const handleClose = () => {
        setOpen(false)
      };

    useEffect(() => {
        Axios.get('http://localhost:8000/Region/stat_regions_non_valid/', 
        { headers: {  'Content-Type' : 'application/json',"Authorization": `Token ${token}` } })
            .then(res => {
                console.log(res.data)
                set_info_Regions(res.data.results) 
                setNext(res.data.next) 
            }).then(  
                Axios.get(`http://localhost:8000/Region/regions/`)
                .then(res => {
                    setReg(res.data.results)
                    console.log(res.data.results)
                    setLoading (true)
                })
                   )    
    },[])

    const get_info_wilaya = (url) => {
        Axios.get(url, 
        { headers: {  'Content-Type' : 'application/json',"Authorization": `Token ${token}` } })
            .then(res => {
                console.log(res.data)
                set_info_Regions(res.data.results)  
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
            })
    }

    const set_valider_rg = ( id_stat ) => {
        handleClose()
        console.log("set valider true")
        Axios.patch(`http://localhost:8000/Region/stat_regions/${id_stat}/`, {
            "validerSt": valider,
            'idModerateurSt' : localStorage.getItem("idUser")
        }, { headers: { 'Authorization': `Token ${token}` } })
            .then(res => {
                console.log(res)
                alert(" Statistique changé avec success")

                window.location.reload(false);
            }).catch(error =>alert(error));
    }
   
    function formatDate(string){
        var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: "2-digit", minute:"2-digit"};
        return new Date(string).toLocaleDateString([],options);
      }

    var table_info = [
    ]
 info_Regions.map(info => {
       console.log(reg.find( reg => reg.idRegion === info.idRegionSt))
        if ( loading===true) { 
            return (
                table_info.push([
                    formatDate(info.dateSt),
                    reg.find( reg => reg.idRegion === info.idRegionSt).nomRegion,
                     info.nbrPorteurVirus, 
                     info.casConfirme,
                      info.nbrGuerisons, 
                      info.nbrDeces,
                       info.casRetablis, 
                    <div><Tooltip title="Accepter">
                    <IconButton onClick={() => handleClickOpen(info.idStatistique, true)}
                     aria-label="delete" className={classes.icon2}>
                     <Check style = {{color :"#757575"}} />
                    </IconButton></Tooltip><Tooltip title="Supprimer">
                  <IconButton onClick={() => handleClickOpen(info.idStatistique, false)} 
                 aria-label="delete" className={classes.icon}>
              <DeleteIcon style = {{color :"#757575"}} /></IconButton></Tooltip></div>])
            )
        
        }

    })

    return (
        <Card>
             <CardHeader color = "info">
            <h4 className={classes.cardTitleWhite}>Statistiques de Santé</h4>
            <p className={classes.cardCategoryWhite}>
            Valider ou refuser les statistiques des wilayas
            </p>
          </CardHeader>
            <CardBody>
                <Table
                    
                    tableHead={["date","Wilaya", "Porteurs", "Guerisons", "Malades", "Décés", "Rétablis", "Action"]}
                    tableData={
                       table_info
                    }
                />
            </CardBody>
   <Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title">
   <DialogTitle id="form-dialog-title">Confirmation</DialogTitle>
   <DialogContent>
     <p className={classes.text}>
     {valider ?'Etes vous sure de vouloir valider ce statistique ?': 'Etes vous sure de vouloir rejeter ce statistique?' }
         </p>
   </DialogContent>
   <DialogActions>
   <Button  color="primary" onClick={()=>set_valider_rg(idstat)} type = "submit">
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
