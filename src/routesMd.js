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
import val from "@material-ui/icons/Check"
// core components/views for Admin layout
import valider from "views/valider/infocccpage";

const dashboardRoutes = [

  
  {
    path: "/valider",
    name: "Valider les statistiques",
    rtlName: "لوحة القيادة",
    icon: val,
    component: valider,
    layout: "/moderateur"
  },
  
 

  
];

export default dashboardRoutes;
