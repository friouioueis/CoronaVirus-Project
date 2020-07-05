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
    const [info_youtube, set_info_youtube] = useState([])
    const [info_article, set_info_article] = useState([])
    const [info_facebook, set_info_facebook] = useState([])
    const classes = useStyles();
    const [q, setq] = useState([])
    const [reg, set_reg] = useState("")
    const [open, setOpen] = useState(false);
    const  [ loading ,setLoading ]= React.useState(false);
    const token =localStorage.getItem("token");



    useEffect(() => {
        get_robot_article()
    }, [q])


    const get_robot_article = () => {

        console.log("requete article")
        Axios.get('http://localhost:8000/Robots/articles')
            .then(res => {
                console.log(res.data)
                setLoading(true)
                set_info_article(res.data.results)
            }).catch(error=>alert(error))
    }

    
    const set_refuser_ar = (id,titre,lien,source,date) => {

        console.log("set valider false")
        Axios.put(`http://localhost:8000/Robots/articles/${id}/`, {
            "id": id,
            // "titre":titre,
            // "lien":lien,
            // "source":source,
            // "datePub":date,
            "validerAr": false
        }, { headers: { "Authorization": `Token ${token}` } })
            .then(res => {
                console.log(res)
                // alert("Statisqtique refusé")
                alert("article refusé avec succes")
                get_robot_article()
            })
    }

    const set_acc_ar = (id) => {

        console.log("set valider true")
        Axios.put(`http://localhost:8000/Robots/articles/${id}/`, {
            "id": id,
            "validerAr": true
        }, { headers: { "Authorization": `Token ${token}` } })
            .then(res => {
                console.log(res)
                // alert("Statisqtique refusé")
                alert("article refusé avec succes")
                get_robot_article()
            })
    }

    return (
        <div>
       
            {info_article.map(info => {
              
                if (info.validerAr == null) {
                    return (

                        <Card className={classes.root} style={{padding : "20px"}}>
                            <CardContent>
                                <Typography variant="h5" component="h2">
                                    {info.titre}
                                </Typography>
                                <Typography className={classes.pos} color="textSecondary">
                                    Published on : {info.datePub}
                                </Typography>
                                <Typography variant="body2" component="p">
                                   Source :  {info.source} <br/>
                                   Langue :  {info.langue}
                                </Typography>
                            </CardContent>
                            <CardActions>
                                Link :<Linkify>{info.lien}</Linkify>


                            </CardActions>

                            <div className={classes.divall}>
                                <Button onClick={() => set_acc_ar(info.id,info.titre,info.lien ,info.source ,info.datePub )} className={classes.button} style={{marginRight : "100px"}} variant="contained" color="primary">
                                    Accepter
                                </Button>
                                <Button onClick={() => set_refuser_ar(info.id,info.titre,info.lien ,info.source ,info.datePub )} variant="contained" color="secondary">
                                    Refuser
                                </Button>
                            </div>

                        </Card>

                    )
                }

            }) 
        
        }
        </div>



    )
}

