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
import Next from '@material-ui/icons/NavigateNextOutlined';
import Previous from '@material-ui/icons/NavigateBeforeOutlined';
import CardFooter from "components/Card/CardFooter";
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
  }
};

const useStyles = makeStyles(styles);

export default function TableList() {
  const classes = useStyles();
  const token = localStorage.getItem("token")
  const [info_Regions, set_info_Regions] = useState([])
  const [q, setq] = useState([])
  const [reg, setReg] = useState([])
  const  [ loading ,setLoading ]= React.useState(false);
  const [page, setPage] = React.useState(1);
  const [current, setCurrent] = React.useState(10);
  const [next, setNext] = React.useState(null);
  const [previous, setPrevious] = React.useState(null);
  const handleChangeNextPage = (event, value) => {
    if(next != null){
    setPage(page+10);
    setCurrent(current+10)
    getStat(next)
    }
  };
  const handleChangePreviousPage = (event, value) => {
    if(previous != null){
    setPage(page-10);
    setCurrent(current-10)
    getStat(previous)
    }
  };
  const getStat = (url) => {
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
        }).then(  
            Axios.get(`http://localhost:8000/Region/regions/`)
            .then(res => {
               //reg=res.data.nomRegion
               // alert(reg)
               // return reg 
                setReg(res.data.results)
                console.log(res.data.results)
                setLoading (true)
            })
               )    
  };
  useEffect(() => {
  getStat(`http://localhost:8000/Region/agent/${localStorage.getItem("idUser")}/stats_refus/`)
},[])



var table_info = [
]
function formatDate(string){
  var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: "2-digit", minute:"2-digit"};
  return new Date(string).toLocaleDateString([],options);
}
info_Regions.map(info => { 
  if (loading===true) {
    var valid = "";
    if (info.validerSt=== null){
      valid = "pas encore validé"
    }else{
      if (info.validerSt){
        valid ='Validé'
      }else{
        valid ='Non validé' 
      }
    }

        return (
         
            table_info.push([
              formatDate(info.dateSt),
              reg[info.idRegionSt-1].nomRegion, 
              info.nbrPorteurVirus,
              info.casConfirme,
              info.casRetablis,
              info.nbrDeces, info.nbrGuerisons,
            <p>{valid}</p>
          ])
        )
        }
 })

  return (
    <GridContainer>
      <GridItem xs={12} sm={12} md={12}>
        <Card>
          <CardHeader color="info">
            <h4 className={classes.cardTitleWhite}>Statistiques</h4>
            <p className={classes.cardCategoryWhite}>
            Statistiques validés et non validés
            </p>
          </CardHeader>
          <CardBody>
            <Table
              tableHead={["Date", "Region", "Porteurs de virus", "Cas confirme", "Cas retablis", "Decédés","guerisons","Validation"]}
              tableData={table_info}
            />
          </CardBody>
          <CardFooter>
          <div className={classes.pages}>
          <Previous onClick={handleChangePreviousPage}></Previous>
            <p style={{display : "inline-block", margin : "20px" }}>{page} - {current}</p>
          <Next onClick={handleChangeNextPage}></Next>
   
</div>
          </CardFooter>
        </Card>
      </GridItem>
      
    </GridContainer>
  );
}
