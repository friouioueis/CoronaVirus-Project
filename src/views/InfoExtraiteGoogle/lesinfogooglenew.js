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
import Linkify from 'react-linkify';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import Next from '@material-ui/icons/NavigateNextOutlined';
import Previous from '@material-ui/icons/NavigateBeforeOutlined';
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
    const [info_googlenews, set_info_googlenews] = useState([])
    const classes = useStyles();
    const [q, setq] = useState([])
    const [reg, set_reg] = useState("")
    const [open, setOpen] = useState(false);
    const token = localStorage.getItem("token")
    const [page, setPage] = React.useState(1);
    const [current, setCurrent] = React.useState(10);
    const [next, setNext] = React.useState(null);
    const [previous, setPrevious] = React.useState(null);
    const handleChangeNextPage = (event, value) => {
//alert(next)
          if(next != null){
      setPage(page+10);
      setCurrent(current+10)
      get_robot_google(next)
      }
    };
    const handleChangePreviousPage = (event, value) => {
      if(previous != null){
      setPage(page-10);
      setCurrent(current-10)
      get_robot_google(previous)
      }
    };

    useEffect(() => {
        get_robot_google('http://localhost:8000/Robots/googleNews/')
    }, [])


    const get_robot_google = (url) => {

        console.log("requete article google")
        Axios.get(url)
            .then(res => {
                console.log(res.data)
                set_info_googlenews(res.data.results)
               
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

    
    const set_refuser_ar = (id,titre,lien,source,date) => {

        console.log("set valider false")
        Axios.put(`http://localhost:8000/Robots/googleNews/${id}/`, {
            "idPubGN": id,
            // "titre":titre,
            // "lien":lien,
            // "source":source,
            // "datePub":date,
            "validerGN": false
        }, { headers: { "Authorization": `Token ${token}` } })
            .then(res => {
                console.log(res)
                // alert("Statisqtique refusé")
            
                alert("Article refusé avec succés!")
                window.location.reload(false);

            })
    }

    const set_acc_ar = (id) => {
        console.log("set valider true")
        Axios.put(`http://localhost:8000/Robots/googleNews/${id}/`, {
            "idPubGN": id,
            "validerGN": true
        }, { headers: { "Authorization": `Token ${token}` } })
            .then(res => {
                console.log(res)
             
                alert("Article validé avec succés!")
                window.location.reload(false);
                // alert("Statisqtique refusé")
            })
    }

    return (
        <div>
            {info_googlenews.map(info => {
                if (info.validerGN === null) {
                    return (

                        <Card className={classes.root} style={{padding : "20px"}}>
                            <CardContent>
                                <Typography variant="h5" component="h2">
                                    {info.titre}
                                </Typography>
                                <Typography className={classes.pos} color="textSecondary">
                                    Auteur : {info.auteur} <br/>
                                    Published on : {info.dateGN} <br/>
                                    Langue : {info.langue}
                                </Typography>
                            </CardContent>
                            <CardActions>
                                <GridContainer>
                                    <GridItem   xs={12} sm={12} md={12} >
                                <Typography>
                                Source  : 
                                </Typography>
                              {info.source}
                                </GridItem>
                                <GridItem   xs={12} sm={12} md={12} >
                                <Typography>
                                Link :
                                </Typography><Linkify>{info.lienPubGN}</Linkify>
                                </GridItem>
                                </GridContainer>
                            </CardActions>

                            <div className={classes.divall}>
                                <Button onClick={() => set_acc_ar(info.idPubGN,info.titre,info.lien ,info.source ,info.datePub )} style={{marginRight : "100px"}} variant="contained" color="primary">
                                    Accepter
                                </Button>
                                <Button onClick={() => set_refuser_ar(info.idPubGN,info.titre,info.lien ,info.source ,info.datePub )} variant="contained" color="secondary">
                                    Refuser
                                </Button>
                            </div>
   
                        </Card>

                    )
                }

            })}
                                     <div className={classes.pages}>
 <Previous onClick={handleChangePreviousPage}></Previous>
            <p style={{display : "inline-block", margin : "20px" }}>{page} - {current}</p>
    <Next onClick={handleChangeNextPage}></Next>
   
</div>
        </div>



    )
}

