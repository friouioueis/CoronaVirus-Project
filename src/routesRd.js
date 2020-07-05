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
import err from "@material-ui/icons/Edit"
import art from "@material-ui/icons/Check"
import cloc from "@material-ui/icons/Timelapse"
import val from "@material-ui/icons/NoteAdd"
import his from "@material-ui/icons/History"
import comment from "@material-ui/icons/Comment"
// core components/views for Admin layout
import rediger from "views/RedigerArticles/RedigerArticle";
import article from  "views/ArticleRedige/Articleredige"
import attente from  "views/ArticleAttente/ArticleAttente"
import prof from "views/UserProfile/UserProfile";
import term from "views/ArticleNonTerm/Edit";
import edit from "views/ArticleEdit/ArticleEdit";
import signalMo from "views/SignalModerateur/SignalModerateur"
import comments from "views/CommentSignal/CommentSignal"
import statModerateur from "views/StatistiqueModerateur/StatistiqueModerateur"

const dashboardRoutes = [

  
  {
    path: "/rediger",
    name: "Rediger les articles",
    rtlName: "لوحة القيادة",
    icon: val,
    component:rediger,
    layout: "/redacteur"
  },
  {
    path: "/nonTermines",
    name: "Les articles non termines",
    rtlName: "لوحة القيادة",
    icon: err,
    component:term,
    layout: "/redacteur"
  },
  {
    path: "/enAttente",
    name: "Les articles en attente ",
    rtlName: "لوحة القيادة",
    icon: cloc,
    component:attente,
    layout: "/redacteur"
  },
  {
    path: "/valide",
    name: "Les articles validés ",
    rtlName: "لوحة القيادة",
    icon: art,
    component:article,
    layout: "/redacteur"
  },
  {
    path: "/profile",
    name: "Profile",
    rtlName: "لوحة القيادة",
    icon: err,
    component: prof,
    layout: "/redacteur"
  },
 
  
];

export default dashboardRoutes;
