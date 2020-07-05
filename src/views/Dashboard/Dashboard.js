import React , { Component, useState, useEffect } from "react";
// react plugin for creating charts
import ChartistGraph from "react-chartist";
// @material-ui/core
import { makeStyles } from "@material-ui/core/styles";
import Icon from "@material-ui/core/Icon";
// @material-ui/icons
import Store from "@material-ui/icons/Store";
import Warning from "@material-ui/icons/Warning";
import DateRange from "@material-ui/icons/DateRange";
import LocalOffer from "@material-ui/icons/LocalOffer";
import Update from "@material-ui/icons/Update";
import ArrowUpward from "@material-ui/icons/ArrowUpward";
import AccessTime from "@material-ui/icons/AccessTime";
import Accessibility from "@material-ui/icons/Accessibility";
import BugReport from "@material-ui/icons/BugReport";
import Code from "@material-ui/icons/Code";
import Cloud from "@material-ui/icons/Cloud";
// core components
import GridItem from "components/Grid/GridItem.js";
import GridContainer from "components/Grid/GridContainer.js";
import Table from "components/Table/Table.js";
import Tasks from "components/Tasks/Tasks.js";
import CustomTabs from "components/CustomTabs/CustomTabs.js";
import Danger from "components/Typography/Danger.js";
import Card from "components/Card/Card.js";
import CardHeader from "components/Card/CardHeader.js";
import CardIcon from "components/Card/CardIcon.js";
import CardBody from "components/Card/CardBody.js";
import CardFooter from "components/Card/CardFooter.js";
import Axios from 'axios';

import { bugs, website, server } from "variables/general.js";

import {
  dailySalesChart,
  emailsSubscriptionChart,
  completedTasksChart
} from "variables/charts.js";

import styles from "assets/jss/material-dashboard-react/views/dashboardStyle.js";

const useStyles = makeStyles(styles);

export default function Dashboard() {
  const [data, setData] = useState([])
  const [val, setVal] = useState([])
  const [ref, setRef] = useState([])

  const [dataS, setDataS] = useState([])
  const [valS, setValS] = useState([])
  const [refS, setRefS] = useState([])
  const classes = useStyles();
  const [loading, setLoading] = useState(false)
 //var data
  useEffect(() => {

    Axios.get(`http://localhost:8000/dashboard/`, 
    { headers: {  'Content-Type' : 'application/json' } })
        .then(res => {
            console.log(res)
            console.log(res.data.nbr_articles)
            setData(res.data.nbr_articles)
            setVal(res.data.nbr_articles_valid)
            setRef(res.data.nbr_articles_refus)
// SANTE
setDataS(res.data.nbr_stat)
setValS(res.data.nbr_stat_valid)
setRefS(res.data.nbr_stat_refus)
            setLoading (true)
            console.log(data)
            //articleV.data.labels = res.data
            
   
        }).catch(error =>alert(error));   
},[])

const articleE ={
  data: {
    labels: [],
    series: []
  }
}

const articleV ={
  data: {
    labels: [],
    series: []
  }
}

const articleR ={
  data: {
    labels: [],
    series: []
  }
}

const santeE ={
  data: {
    labels: [],
    series: []
  }
}

const santeV ={
  data: {
    labels: [],
    series: []
  }
}

const santeR ={
  data: {
    labels: [],
    series: []
  }
}
function formatDate(string){
  var options = {month: 'numeric', day: 'numeric'};
  return new Date(string).toLocaleDateString([],options);
}

data.map(info => {
  if ( loading===true) { 
    return (
    articleE.data.labels.push([
      formatDate(info.dateAr)
   ]),
   articleE.data.series.push([
    info.total
   ])
)

}
})

dataS.map(info => {
  if ( loading===true) { 
    return (
    santeE.data.labels.push([
      formatDate(info.dateSt)
   ]),
   santeE.data.series.push([
    info.total
   ])
)

}
})

val.map(info => {
  if ( loading===true) { 
    return (
    articleV.data.labels.push([
      formatDate(info.dateAr)
   ]),
   articleV.data.series.push([
    info.total
   ])
)

}
})

valS.map(info => {
  if ( loading===true) { 
    return (
    santeV.data.labels.push([
      formatDate(info.dateSt)
   ]),
   santeV.data.series.push([
    info.total
   ])
)

}
})

ref.map(info => {
  if ( loading===true) { 
    return (
    articleR.data.labels.push([
      formatDate(info.dateAr)
   ]),
   articleR.data.series.push([
    info.total
   ])
)

}
})

refS.map(info => {
  if ( loading===true) { 
    return (
    santeR.data.labels.push([
      formatDate(info.dateSt)
   ]),
   santeR.data.series.push([
    info.total
   ])
)

}
})

console.log(data)
  return (

    <div>
        <h4 className={classes.cardTitleBlack} style={{paddingLeft : "20px"}}>Historique des articles</h4>
      <GridContainer style={{paddingLeft : "20px", paddingRight : "20px"}}>
 
          <GridItem xs={12} sm={12} md={4}>
          <Card chart>
            <CardHeader color="warning">
              <ChartistGraph
                className="ct-chart"
                data={articleE.data}
                type="Bar"
                options={emailsSubscriptionChart.options}
                responsiveOptions={emailsSubscriptionChart.responsiveOptions}
                listener={emailsSubscriptionChart.animation}
              />
            </CardHeader>
            <CardBody>
              <h4 className={classes.cardTitle}>Articles ecrits</h4>
            </CardBody>
            <CardFooter chart>
              <div className={classes.stats}>
                <AccessTime /> campaign sent 2 days ago
              </div>
            </CardFooter>
          </Card>
        </GridItem>

        <GridItem xs={12} sm={12} md={4}>
          <Card chart>
            <CardHeader color="success">
              <ChartistGraph
                className="ct-chart"
                data={articleV.data}
                type="Bar"
                options={emailsSubscriptionChart.options}
                responsiveOptions={emailsSubscriptionChart.responsiveOptions}
                listener={emailsSubscriptionChart.animation}
              />
            </CardHeader>
            <CardBody>
              <h4 className={classes.cardTitle}>Articles validés</h4>
            </CardBody>
            <CardFooter chart>
              <div className={classes.stats}>
                <AccessTime /> campaign sent 2 days ago
              </div>
            </CardFooter>
          </Card>
        </GridItem>
       
        <GridItem xs={12} sm={12} md={4}>
          <Card chart>
            <CardHeader color="danger">
              <ChartistGraph
                className="ct-chart"
                data={articleR.data}
                type="Bar"
                options={emailsSubscriptionChart.options}
                responsiveOptions={emailsSubscriptionChart.responsiveOptions}
                listener={emailsSubscriptionChart.animation}
              />
            </CardHeader>
            <CardBody>
              <h4 className={classes.cardTitle}>Articles refusées</h4>
            </CardBody>
            <CardFooter chart>
              <div className={classes.stats}>
                <AccessTime /> campaign sent 2 days ago
              </div>
            </CardFooter>
          </Card>
        </GridItem>
      </GridContainer>




      <h4 className={classes.cardTitleBlack} style={{paddingLeft : "20px"}}>Historique des statistiques de santé</h4>
      <GridContainer>
          <GridItem xs={12} sm={12} md={4}>
          <Card chart>
            <CardHeader color="warning">
              <ChartistGraph
                className="ct-chart"
                data={santeE.data}
                type="Bar"
                options={emailsSubscriptionChart.options}
                responsiveOptions={emailsSubscriptionChart.responsiveOptions}
                listener={emailsSubscriptionChart.animation}
              />
            </CardHeader>
            <CardBody>
              <h4 className={classes.cardTitle}>Statistiques de santé</h4>
            </CardBody>
            <CardFooter chart>
              <div className={classes.stats}>
                <AccessTime /> campaign sent 2 days ago
              </div>
            </CardFooter>
          </Card>
        </GridItem>

        <GridItem xs={12} sm={12} md={4}>
          <Card chart>
            <CardHeader color="success">
              <ChartistGraph
                className="ct-chart"
                data={santeV.data}
                type="Bar"
                options={emailsSubscriptionChart.options}
                responsiveOptions={emailsSubscriptionChart.responsiveOptions}
                listener={emailsSubscriptionChart.animation}
              />
            </CardHeader>
            <CardBody>
              <h4 className={classes.cardTitle}>Statistiques validés</h4>
            </CardBody>
            <CardFooter chart>
              <div className={classes.stats}>
                <AccessTime /> campaign sent 2 days ago
              </div>
            </CardFooter>
          </Card>
        </GridItem>
       
        <GridItem xs={12} sm={12} md={4}>
          <Card chart>
            <CardHeader color="danger">
              <ChartistGraph
                className="ct-chart"
                data={santeR.data}
                type="Bar"
                options={emailsSubscriptionChart.options}
                responsiveOptions={emailsSubscriptionChart.responsiveOptions}
                listener={emailsSubscriptionChart.animation}
              />
            </CardHeader>
            <CardBody>
              <h4 className={classes.cardTitle}>Statistiques refusées</h4>
            </CardBody>
            <CardFooter chart>
              <div className={classes.stats}>
                <AccessTime /> campaign sent 2 days ago
              </div>
            </CardFooter>
          </Card>
        </GridItem>


      </GridContainer>

    </div>
  );
}
