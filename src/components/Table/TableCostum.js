import React from "react";
import PropTypes from "prop-types";
import classNames from "classnames";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
import Table from "@material-ui/core/Table";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import Notifications from "@material-ui/icons/Notifications";
import MenuItem from "@material-ui/core/MenuItem";
import MenuList from "@material-ui/core/MenuList";
import Grow from "@material-ui/core/Grow";
import Paper from "@material-ui/core/Paper";
import Avatar from '@material-ui/core/Avatar';
import ClickAwayListener from "@material-ui/core/ClickAwayListener";
import Axios from 'axios';
import Hidden from "@material-ui/core/Hidden";
import Poppers from "@material-ui/core/Popper";
import Button from "components/CustomButtons/Button.js";
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Radio from '@material-ui/core/Radio';
//import styles from "assets/jss/material-dashboard-react/components/headerLinksStyle.js";
// core components
import styles from "assets/jss/material-dashboard-react/components/tableStyle.js";
import GridItem from "components/Grid/GridItem.js";
import GridContainer from "components/Grid/GridContainer.js";

const useStyles = makeStyles(styles);
const token = localStorage.getItem("token")
export default function CustomTable(props) {
    const [openNotification, setOpenNotification] = React.useState(null);
    const [openProfile, setOpenProfile] = React.useState(null);
    const [notif, setNotif] = React.useState(null);
    const handleClickNotification = (event,key) => {
      setNotif(key)
      //console.log(table[0].role.find( reg => reg.Type === "md"))
      if (openNotification && openNotification.contains(event.target)) {
        setOpenNotification(null);
      } else {
        setOpenNotification(event.currentTarget);
      }
    };
    const handleCloseNotification = () => {
      setOpenNotification(null);
    };
    const handleClickProfile = event => {
      if (openProfile && openProfile.contains(event.target)) {
        setOpenProfile(null);
      } else {
        setOpenProfile(event.currentTarget);
      }
    };
    const handleCloseProfile = () => {
      setOpenProfile(null);
    };

    const changeRole = ( type, id ) => {
      //alert(type)
      //alert(id)
    //alert( table[notif].id)
    //console.log(table.role.find( reg => reg.Type === "md"))
     if (!table[notif].role.find( reg => reg.Type === type) ){
      Axios.post("http://localhost:8000/Utilisateurs/gestionComptes/roles/",
       {
        "Type": type,
        "idUtilisateurR": table[notif].id
       },
         { headers: { 'Content-Type' : 'application/json','Authorization': `Token ${token}` } })
      .then(res => {
          console.log(res.data)    
          window.location.reload(false);        
      }).catch(error=> alert(error))
    }else{
      alert("il est deja affecter a ce role !")
    }
    };
  var table =[]
  const classes = useStyles();
  const { tableHead, tableData, tableHeaderColor } = props;
  return (
    <div className={classes.tableResponsive}>
      <Table className={classes.table}>
        {tableHead !== undefined ? (
          <TableHead className={classes[tableHeaderColor + "TableHeader"]}>
            <TableRow className={classes.tableHeadRow}>
              {tableHead.map((prop, key) => {
                return (
                  <TableCell
                    className={classes.tableCell + " " + classes.tableHeadCell}
                    key={key}
                  >
                    <b> {prop}</b>
                  </TableCell>
                  
                );
              })}
              <TableCell > </TableCell>
            </TableRow>
          </TableHead>
        ) : null}
        <TableBody>
          {tableData.map((prop, key) => {
             table.push({"id" : prop[4],"role":prop[3]})
             console.log(table)
            return (
              <TableRow key={key} className={classes.tableBodyRow}>
                    <TableCell className={classes.tableCell} key={key}>
                    <GridContainer   >
                  <GridItem  xs={6} sm={6} md={2} >  
            <Avatar className={classes.orange} style={{ backgroundColor: '#00acc1', marginTop : 5 }} >{ prop[0][0].toUpperCase()}</Avatar>
                    </GridItem>
                    <GridItem  xs={6} sm={6} md={6} >  
                      <p style={{ fontSize: 14 }}><b>{prop[0]}</b>  <br></br>{prop[1]}</p>  
                      </GridItem>
                  </GridContainer>
                    </TableCell>
                    <TableCell className={classes.tableCell} key={key}>
                      
          {
         prop[3].map((option , key ) => (
          <p>
            {(function() {
              switch (option.Type) {
             case 'as':
               return "agent de santé"  
             case 'md':
               return "moderateur"
             case 'si':
               return "simple"
             case 'ad':
               return "admin" 
             case 'rd':
                return "redacteur" 
             default:
               return <p>hello</p>;
           }
       
         })()}  

          </p>
            
          
        ))}
                    </TableCell>
                    <TableCell className={classes.tableCell} key={key}>
                      { prop[2] }
                    </TableCell>
                 
                <TableCell>
        <div className={classes.manager}>
        <Button
          color={window.innerWidth > 959 ? "transparent" : "white"}
          justIcon={window.innerWidth > 959}
          simple={!(window.innerWidth > 959)}
          aria-owns={openNotification ? "notification-menu-list-grow" : null}
          aria-haspopup="true"
          onClick={(event) => handleClickNotification(event,key)}
          className={classes.buttonLink}
        >
        <b> ... </b>
        
        </Button>
        <Poppers
          open={Boolean(openNotification)}
          anchorEl={openNotification}
          key={key}
          transition
          disablePortal
          className={
            classNames({ [classes.popperClose]: !openNotification }) +
            " " +
            classes.popperNav
          }
        >
          {({ TransitionProps, placement }) => (
            <Grow
              {...TransitionProps}
              id="notification-menu-list-grow"
              style={{
                transformOrigin:
                  placement === "bottom" ? "center top" : "center bottom"
              }}
            >
              <Paper key={key}>
                <ClickAwayListener onClickAway={handleCloseNotification}>
                  <MenuList role="menu" key={key}>
                    <MenuItem
                      onClick={() => changeRole("md",key)}
                      className={classes.dropdownItem}
                    >
                    Ajouter comme moderateur
                    </MenuItem>
                    <MenuItem
                      onClick={() => changeRole("rd",key)}
                      className={classes.dropdownItem}
                    >
                      Ajouter comme redacteur
                    </MenuItem>
                    <MenuItem
                      onClick={() => changeRole("as",key)}
                      className={classes.dropdownItem}
                    >
                      Ajouter comme agent de santé
                    </MenuItem>
                 
                  </MenuList>
                </ClickAwayListener>
              </Paper>
            </Grow>
          )}
        </Poppers>
      </div>
               </TableCell>
              </TableRow>
            );
          })}
              
        </TableBody>
      </Table>
    </div>
  );
}

CustomTable.defaultProps = {
  tableHeaderColor: "gray"
};

CustomTable.propTypes = {
  tableHeaderColor: PropTypes.oneOf([
    "warning",
    "primary",
    "danger",
    "success",
    "info",
    "rose",
    "gray",
  ]),
  tableHead: PropTypes.arrayOf(PropTypes.string),
  tableData: PropTypes.arrayOf(PropTypes.arrayOf(PropTypes.string))
};
