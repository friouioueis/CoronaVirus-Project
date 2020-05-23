import React , { Component, useState, useEffect }from "react";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
// core components
import GridItem from "components/Grid/GridItem.js";
import GridContainer from "components/Grid/GridContainer.js";
import Table from "components/Table/Table.js";
import Card from "components/Card/Card.js";
import CardHeader from "components/Card/CardHeader.js";
import CardBody from "components/Card/CardBody.js";
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
    }
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
  }
};

const useStyles = makeStyles(styles);

export default function TableList() {
  const classes = useStyles();
  const token = localStorage.getItem("token")
  const [info_Regions, set_info_Regions] = useState([])
  const [q, setq] = useState([])
  const [reg, setReg] = useState("")
  useEffect(() => {
    get_info_wilaya()
}, [q])

const get_info_wilaya = () => {

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
        setReg(res.data.nomRegion)
    })
}

var table_info = [
]
info_Regions.map(info => {
    
    
        return (
           // get_rg_name(info.idRegionSt),
           // alert(reg),
            table_info.push([info.dateSt,info.idRegionSt, info.nbrPorteurVirus, info.casConfirme, info.casRetablis, info.nbrDeces, info.nbrGuerisons,info.validerSt])
        )
    

})

  return (
    <GridContainer>
      <GridItem xs={12} sm={12} md={12}>
        <Card>
          <CardHeader style={{ backgroundColor: "#757575" }}>
            <h4 className={classes.cardTitleWhite}>Statistiques</h4>
            <p className={classes.cardCategoryWhite}>
            Statistiques validés et non validés
            </p>
          </CardHeader>
          <CardBody>
            <Table
              tableHeaderColor="primary"
              tableHead={["Date", "Region", "Porteurs de virus", "Cas confirme", "Cas retablis", "Decédés","guerisons","Validation"]}
              tableData={table_info}
            />
          </CardBody>
        </Card>
      </GridItem>
     
    </GridContainer>
  );
}
