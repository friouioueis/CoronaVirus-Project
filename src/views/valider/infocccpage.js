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
import DeleteIcon from '@material-ui/icons/Delete';
import IconButton from '@material-ui/core/IconButton';
import Tooltip from '@material-ui/core/Tooltip';
import React, { Component, useState, useEffect } from 'react';
import Axios from 'axios';
import Snackbar from '@material-ui/core/Snackbar';
// import MuiAlert from '@material-ui/lab/Alert';


// function Alert(props) {
//     return <MuiAlert elevation={6} variant="filled" {...props} />;
// }

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

{/* <span class="material-icons">
check_box
</span> */}

const useStyles = makeStyles(styles);

export default function TableList() {
    const [info_Regions, set_info_Regions] = useState([])
    const classes = useStyles();
    const [q, setq] = useState([])
    //const [reg, setReg] = useState("")
    var reg = "wilaya"
    const token = localStorage.getItem("token")



    useEffect(() => {
        get_info_wilaya()
    }, [q])

    const get_info_wilaya = () => {
        console.log("dada")
        Axios.get('http://127.0.0.1:8000/Region/stat_regions/', 
        { headers: {  'Content-Type' : 'application/json',"Authorization": `Token ${token}` } })
            .then(res => {
                console.log(res.data)
                set_info_Regions(res.data)
            })
    }

    const get_rg_name = (id) => {
            console.log("dada")
        Axios.get(`http://localhost:8000/Region/regions/${id}/`)
            .then(res => {
                //console.log(res.data)
                reg=res.data.nomRegion
               // alert(reg)
               // return reg 
                //setReg(res.data.nomRegion)
            })
    }

    const set_valider_rg = ( id_stat) => {
        console.log("set valider true")
        Axios.patch(`http://localhost:8000/Region/stat_regions/${id_stat}/`, {
            "validerSt": true,
            'idModerateurSt' : localStorage.getItem("idUser")
        }, { headers: { 'Authorization': `Token ${token}` } })
            .then(res => {
                console.log(res)
                get_info_wilaya()
            })
    }

    const set_refuser_rg = ( id_stat) => {

        console.log("set valider true")
        Axios.patch(`http://localhost:8000/Region/stat_regions/${id_stat}/`, {
            'validerSt': false,
            'idModerateurSt' : localStorage.getItem("idUser")
        }, { headers: { 'Content-Type' : 'application/json', "Authorization": `Token ${token}` } })
            .then(res => {
                console.log(res)
                get_info_wilaya()
            })
    }

   


    var table_info = [
    ]
    info_Regions.map(info => {
       
        if (info.validerSt === false && info.idModerateurSt===null) { 
            get_rg_name(info.idRegionSt)
            return (
                table_info.push([info.idRegionSt, info.nbrPorteurVirus, info.casConfirme, info.nbrGuerisons, info.nbrDeces, info.casRetablis, <div><Tooltip title="Accepter"><IconButton onClick={() => set_valider_rg(info.idStatistique)} aria-label="delete" className={classes.icon2}><span class="material-icons">check_box</span></IconButton></Tooltip><Tooltip title="Supprimer"><IconButton onClick={() => set_refuser_rg(info.idStatistique)} aria-label="delete" className={classes.icon}><DeleteIcon /></IconButton></Tooltip></div>])
            )
        
        }

    })

    return (
        <Card>
            <CardBody>
                <Table
                    tableHeaderColor="primary"
                    tableHead={["Wilaya", "Porteurs", "Guerisons", "Malades", "Décés", "Rétablis", "Action"]}
                    tableData={
                        table_info
                    }
                />
                {/* <Snackbar open={open} autoHideDuration={6000} onClose={handleClose}>
                    <Alert onClose={handleClose} severity="success">
                        This is a success message!
                    </Alert>
                </Snackbar> */}
            </CardBody>
        </Card>

    )
}

// ["19", "19", "19", "19", "19", "19", <div><Tooltip title="Accepter"><IconButton aria-label="delete" className={classes.icon2}><span class="material-icons">check_box</span></IconButton></Tooltip><Tooltip title="Supprimer"><IconButton aria-label="delete" className={classes.icon}><DeleteIcon /></IconButton></Tooltip></div>],
