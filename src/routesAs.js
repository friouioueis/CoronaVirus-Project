/*!

=========================================================
* Material Dashboard React - v1.8.0
=========================================================

* Product Page: https://www.creative-tim.com/product/material-dashboard-react
* Copyright 2019 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/material-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
// @material-ui/icons
import LocationOn from "@material-ui/icons/LocationOn";
import setting from "@material-ui/icons/Settings";
import video from "@material-ui/icons/Videocam";
import stat from "@material-ui/icons/List";
// core components/views for Admin layout
import zone from "views/Zonerisque/Zonerisque.js";
import gestion from "views/GestionCompte/gestionCompte.js";
import videoUser from "views/VideoUser/videoUser.js";
import statistique from "views/Statistiques/Statistiques";
import articles from "views/ArticlesRediges/ArticleRedigePage";
//import rediger from "views/RedigerArticles/RedigerArticle"

const dashboardRoutes = [

  {
    path: "/ZoneDeRisque",
    name: "Zones de risque",
    rtlName: "لوحة القيادة",
    icon: LocationOn,
    component: zone,
    layout: "/agentSante"
  },
  {
    path: "/Statistiques",
    name: "Statistiques",
    rtlName: "لوحة القيادة",
    icon: stat,
    component: statistique,
    layout: "/agentSante"
  },

  
 /* {
    path: "/rediger",
    name: "Rediger articles",
    rtlName: "لوحة القيادة",
    icon: LocationOn,
    component: rediger,
    layout: "/agentSante"
  },
  */
 
  {
    path: "/gestionDeCompte",
    name: "Gestion de compte",
    rtlName: "لوحة القيادة",
    icon: setting,
    component: gestion,
    layout: "/agentSante"
  },
  {
    path: "/videoUser",
    name: "videos des utilisateurs",
    rtlName: "لوحة القيادة",
    icon: video,
    component: videoUser,
    layout: "/agentSante"
  },
  
];

export default dashboardRoutes;
