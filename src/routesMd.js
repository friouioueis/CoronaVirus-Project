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
import note from "@material-ui/icons/Note";
import val from "@material-ui/icons/Check"
import err from "@material-ui/icons/Warning"
import his from "@material-ui/icons/History"
import comment from "@material-ui/icons/Comment"
import video from "@material-ui/icons/Videocam";
import you from "@material-ui/icons/Store";
import gg from "@material-ui/icons/ExtensionRounded";
// core components/views for Admin layout
import valider from "views/valider/infocccpage";
import prof from "views/UserProfile/UserProfile";
import signal from "views/Signalement/Signalement";
import signalMo from "views/SignalModerateur/SignalModerateur"
import comments from "views/CommentSignal/CommentSignal"
import statModerateur from "views/StatistiqueModerateur/StatistiqueModerateur"
import rediger from "views/RedigerArticles/RedigerArticle.js";
import article from  "views/ArticlesRediges/ArticleRedigePage"
import choose from  "views/ChooseSite/choosesite2"
import videoUser from "views/VideoUser/videoUser.js";
import info from "views/InfoExtraite/lesInfoExtraite"
import infoYout from "views/InfoExtraiteYoutube/lesinfoextraiteyoutube"
import infoGgle from "views/InfoExtraiteGoogle/lesinfogooglenew"

const dashboardRoutes = [

  
  {
    path: "/valider",
    name: "Valider les statistiques",
    rtlName: "لوحة القيادة",
    icon: val,
    component: valider,
    layout: "/moderateur"
  },
  {
    path: "/MesStatistiques",
    name: "Statistiques traités",
    rtlName: "لوحة القيادة",
    icon: his,
    component: statModerateur,
    layout: "/moderateur"
  },
  {
    path: "/signalement",
    name: "Valider les signalements",
    rtlName: "لوحة القيادة",
    icon: err,
    component: signal,
    layout: "/moderateur"
  },
  {
    path: "/videoUser",
    name: "videos des utilisateurs",
    rtlName: "لوحة القيادة",
    icon: video,
    component: videoUser,
    layout: "/moderateur"
  },
  {
    path: "/MesSignalements",
    name: "Signalements traités",
    rtlName: "لوحة القيادة",
    icon: his,
    component: signalMo,
    layout: "/moderateur"
  },
  {
    path: "/articles",
    name: "Valider les articles",
    rtlName: "لوحة القيادة",
    icon: note,
    component:article,
    layout: "/moderateur"
  },
  {
    path: "/Commentaires",
    name: "Commentaires signalés",
    rtlName: "لوحة القيادة",
    icon: comment,
    component: comments,
    layout: "/moderateur"
  },
  {
    path: "/profile",
    name: "Profile",
    rtlName: "لوحة القيادة",
    icon: comment,
    component: prof,
    layout: "/moderateur"
  },
  {
    path: "/chooseSite",
    name: "Choisir les sites ",
    rtlName: "لوحة القيادة",
    icon: you,
    component: choose,
    layout: "/moderateur"
  },
  {
    path: "/toutInfoExtraite",
    name: "les articles extraits ",
    rtlName: "لوحة القيادة",
    icon: gg,
    component: info,
    layout: "/moderateur"
  },
  {
    path: "/infoExtraiteYoutube",
    name: "les articles extraits Youtube",
    rtlName: "لوحة القيادة",
    icon: gg,
    component: infoYout,
    layout: "/moderateur"
  },
  {
    path: "/infoExtraiteGoogle",
    name: "les articles extraits Google",
    rtlName: "لوحة القيادة",
    icon: gg,
    component: infoGgle,
    layout: "/moderateur"
  },

  
];

export default dashboardRoutes;
