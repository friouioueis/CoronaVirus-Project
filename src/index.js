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
import React ,{useState} from "react" ;
import ReactDOM from "react-dom";
import { createBrowserHistory } from "history";
import { Router, Route, Switch, Redirect } from "react-router-dom";

// core components
import Admin from "layouts/Admin.js";
import AgentSante from "layouts/AgentSante.js";
import RTL from "layouts/RTL.js";
import Auth from "views/Authentification/AuthView.js";
import Moderateur from "layouts/Moderateur";
import Redacteur from "layouts/Redacteur";
import Profile from "views/UserProfile/UserProfile";
//import Auth from "layouts/Authentification.js";

import "assets/css/material-dashboard-react.css?v=1.8.0";

const hist = createBrowserHistory();

ReactDOM.render(

 // <Auth />,
<Router history={hist}>
    <Switch>
      <Route path="/agentSante" token={hist.token} component={AgentSante} />
      <Route  path="/moderateur" component={Moderateur} />
      <Route  path="/redacteur" component={Redacteur} />
      <Route  path="/admin1" component={Admin} />  
      <Route  exact path="/login" component={Auth} />    
      <Redirect from="/" to="login" />
    </Switch>
  </Router>,
  document.getElementById("root")
);
