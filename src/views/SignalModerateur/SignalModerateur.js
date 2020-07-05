import React, {useEffect} from "react";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
import InputLabel from "@material-ui/core/InputLabel";
// core components
import GridItem from "components/Grid/GridItem.js";
import GridContainer from "components/Grid/GridContainer.js";
import Card from "components/Card/Card.js";
import CardHeader from "components/Card/CardHeader.js";
import CardBody from "components/Card/CardBody.js";
import CardFooter from "components/Card/CardFooter.js";
import Axios from 'axios';
import Table from "components/Table/Table.js";
import Next from '@material-ui/icons/NavigateNextOutlined';
import Previous from '@material-ui/icons/NavigateBeforeOutlined';


const styles = {
    card: {
        padding : "10px 10px",
        maxWidth : "90%"
           },
    media: {
         maxHeight: "100%",
         maxWidth :"100%"
          },
  cardCategoryWhite: {
    color: "rgba(255,255,255,.62)",
    margin: "0",
    fontSize: "14px",
    marginTop: "0",
    marginBottom: "0"
  },
  text: {
    fontSize: 14,
    fontFamily: '"Segoe UI"', 
    margin :"0px 0px 10px 0px"
  },
  pages:{
    marginLeft : "40%"
},
  cardTitleWhite: {
    color: "#FFFFFF",
    marginTop: "0px",
    minHeight: "auto",
    fontWeight: "300",
    fontFamily: "'Roboto', 'Helvetica', 'Arial', sans-serif",
    marginBottom: "3px",
    textDecoration: "none"
  }
};
//alert(window.location.pathname)
const useStyles = makeStyles(styles);

export default function SignalModerateur() {
  const classes = useStyles();
  const  [ data ,setData ]= React.useState([]);
  const [id , setId] = React.useState(localStorage.getItem("idUser"))
  const  [ singnalements ,setSingnalements]= React.useState([]);
  const  [ loading ,setLoading ]= React.useState(false);
  const [page, setPage] = React.useState(1);
  const [current, setCurrent] = React.useState(10);
  const [next, setNext] = React.useState(null);
  const [previous, setPrevious] = React.useState(null);
  const handleChangeNextPage = (event, value) => {
    if(next != null){
    setPage(page+10);
    setCurrent(current+10)
    getSignal(next)
    }
  };
  const handleChangePreviousPage = (event, value) => {
    if(previous != null){
    setPage(page-10);
    setCurrent(current-10)
    getSignal(previous)
    }
  };
  const getSignal = (url) => {
    Axios.get(url)
    .then(res => {
        console.log(res.data)
        setData(res.data.results)
        setLoading(true)  
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
  };

  useEffect(() => { 
   getSignal(`http://localhost:8000/Signal/moderateur/${localStorage.getItem("idUser")}/signals/`)
   },[]);
       
   var table_info = []
   data.map(signal => {
       if (loading===true) {
           return (
               table_info.push([ signal.descriptionSg,signal.typeSg,<a href={signal.lienSg}> lien de signamlement </a>,<p> {signal.validerSg ?'Validé': 'Refusé' }</p>])
           )
       }

   })

  return (
    <div>
      <GridContainer>
        <GridItem xs={12} sm={12} md={11}>
          <Card>
            <CardHeader color="info" >
              <h4 className={classes.cardTitleWhite}>Historique des signalements </h4>
              <p className={classes.cardCategoryWhite}>
             Signalement validés et refusé
            </p>
            </CardHeader>
            <CardBody>
            <Table
                    tableHead={["Description","Type", "lien de signalemnt", "Validation"]}
                    tableData={
                        table_info
                    }
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
 
    </div>
  );
}
