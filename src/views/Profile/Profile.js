import React, {useEffect} from "react";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
import InputLabel from "@material-ui/core/InputLabel";
// core components
import GridItem from "components/Grid/GridItem.js";
import GridContainer from "components/Grid/GridContainer.js";
import CustomInput from "components/CustomInput/CustomInput.js";
import Button from "components/CustomButtons/Button.js";
import Card from "components/Card/Card.js";
import CardHeader from "components/Card/CardHeader.js";
import CardAvatar from "components/Card/CardAvatar.js";
import CardBody from "components/Card/CardBody.js";
import CardFooter from "components/Card/CardFooter.js";
import Axios from 'axios';
import avatar from "assets/img/faces/marc.jpg";
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
          pages:{
            marginLeft : "40%"
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

export default function UserProfile() {
  const classes = useStyles();
  const  [ loading ,setLoading ]= React.useState(false);
  const  [ data ,setData ]= React.useState([]);
  const [page, setPage] = React.useState(1);
  const [current, setCurrent] = React.useState(10);
  const [next, setNext] = React.useState(null);
  const [previous, setPrevious] = React.useState(null);
   const handleChangeNextPage = (event, value) => {
   // alert (next)
    if(next != null){
    setPage(page+10);
    setCurrent(current+10)
    getSignal(next)
    }
  };
  const handleChangePreviousPage = (event, value) => {
    if(previous != null){
      //  alert ("previous")
    setPage(page-10);
    setCurrent(current-10)
    getSignal(previous)
    }
  };
  const getSignal = (url) => {
    Axios.get(url)
    .then(res => {
      console.log(res)
      setData(res.data.results)
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
  function formatDate(string){
    var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: "2-digit", minute:"2-digit"};
    return new Date(string).toLocaleDateString([],options);
  }
  useEffect(() => { 
        Axios.get(`http://localhost:8000/Signal/utilisateur/${parseInt(window.location.pathname.substr(32))}/signals/`)
        .then(res => {
            console.log(res.data)
            setData(res.data.results)
            setLoading(true)  
          //  alert(res.data.next)
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
    
       },[]);
   
  return (
    <div>
      <GridContainer>
        <GridItem xs={12} sm={12} md={8}>
          <Card>
            <CardHeader color="info" >
              <h4 className={classes.cardTitleWhite}>Historique des signalements de {loading? data[0].idUtilisateurSg.username.toUpperCase():""}</h4>
            </CardHeader>
            <CardBody>
    {data.map((prop, key) => {
      if(loading && prop.validerSg!= null){
      console.log(data[0].idUtilisateurSg.username)
    return (

      <Card className={classes.card} key ={key}>
        
      <CardBody >
          <p className={classes.text} style={{ fontSize: 14 ,color: '#757575'}}>
         {formatDate(prop.dateSg)}</p>

     <GridContainer >
     <GridItem  xs={12} sm={12} md={6} >   
     <h2 className={classes.text} style={{ fontWeight: 'bold '}}>Description de signalement : </h2>   
         <p className={classes.text}>
         {prop.descriptionSg}</p>
    </GridItem>
     <GridItem  xs={12} sm={12} md={6} >   
    
     <a href ={prop.lienSg} ><img src={prop.lienSg} className={classes.media} alt="..." /> </a> 
       </GridItem>
     </GridContainer>
     </CardBody>
     <CardFooter>
         <p className={classes.text} style={{ fontSize: 14 , color: '#757575'}}> {prop.validerSg ?'Signalement validé par :'+prop.idModerateurSg : 'Signalement non validé ' }</p>
     </CardFooter>
        </Card>
    );
  }
})}

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
        {loading?
        <GridItem xs={12} sm={12} md={4}>
          <Card profile>
            <CardAvatar profile>
              <a href="#pablo" onClick={e => e.preventDefault()}>
                <img src={avatar} alt="..." />
              </a>
            </CardAvatar>
            <CardBody profile>
            <p className={classes.text} style={{  fontWeight: 'bold '}} >Informations de l'utilisateur: </p> 
            <p className={classes.text}>{data[0].idUtilisateurSg.username}</p>
            <p className={classes.text}>{data[0].idUtilisateurSg.email}</p>
            </CardBody>

          </Card>
        </GridItem>
        : ""}
      </GridContainer>
      
    </div>
  );
}
