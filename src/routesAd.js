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
import stat from "@material-ui/icons/Dashboard";
// core components/views for Admin layout
import zone from "views/Zonerisque/Zonerisque.js";
import gestion from "views/GestionCompte/gestionCompte.js";
import Dashboard from "views/Dashboard/Dashboard";
import videoUser from "views/VideoUser/videoUser.js";
import statistique from "views/Statistiques/Statistiques";
import articles from "views/ArticlesRediges/ArticleRedigePage";
import prof from "views/UserProfile/UserProfile";
//import rediger from "views/RedigerArticles/RedigerArticle"

const dashboardRoutes = [
  {
    path: "/dashboard",
    name: "Dashboard",
    rtlName: "لوحة القيادة",
    icon: stat,
    component: Dashboard,
    layout: "/admin1"
  },
 
  {
    path: "/gestionDeCompte",
    name: "Gestion de compte",
    rtlName: "لوحة القيادة",
    icon: setting,
    component: gestion,
    layout: "/admin1"
  },
  {
    path: "/profile",
    name: "Profile",
    rtlName: "لوحة القيادة",
    icon: video,
    component: prof,
    layout: "/admin1"
  },
  
];

export default dashboardRoutes;
