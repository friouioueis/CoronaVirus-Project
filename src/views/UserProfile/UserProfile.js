import React , { useEffect } from "react";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
import InputLabel from "@material-ui/core/InputLabel";
// core components
import GridItem from "components/Grid/GridItem.js";
import GridContainer from "components/Grid/GridContainer.js";
import CustomInput from "components/CustomInput/CustomInput.js";
import Button from "components/CustomButtons/Button.js";
import Card from "components/Card/Card.js";
import CardHeader from "components/Card/CardHeader.js";
import CardAvatar from "components/Card/CardAvatar.js";
import CardBody from "components/Card/CardBody.js";
import CardFooter from "components/Card/CardFooter.js";
import Input from '@material-ui/core/Input';
import Axios from 'axios';
import avatar from "assets/img/faces/marc.jpg";
import FormControl from '@material-ui/core/FormControl';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

const styles = {
  cardCategoryWhite: {
    color: "rgba(255,255,255,.62)",
    margin: "0",
    fontSize: "14px",
    marginTop: "0",
    marginBottom: "0"
  },
  cardTitleWhite: {
    color: "#FFFFFF",
    marginTop: "0px",
    minHeight: "auto",
    fontWeight: "300",
    fontFamily: "'Roboto', 'Helvetica', 'Arial', sans-serif",
    marginBottom: "3px",
    textDecoration: "none"
  }
};

const useStyles = makeStyles(styles);

export default function UserProfile() {
  const classes = useStyles();
  const  [ data ,setData ]= React.useState([]);
  const token = localStorage.getItem("token")
  const  [ open ,setOpen ]= React.useState(false);
  const handleClickOpen =  () => {
   // e.preventDefault()
    setOpen(true)
    //setValider(val)
  };

 const handleClose = () => {
    setOpen(false)
  };
   const credentials ={
    nom: data.nom,
    prenom: data.prenom,
    dateNaissance : data.dateNaissance,
     wilaya : data.wilaya,
     idUtilisateurIp : localStorage.getItem("idUser")
    }
 
  useEffect(() => {
    var id =localStorage.getItem("idUser")
    Axios.get(`http://localhost:8000/Utilisateurs/gestionComptes/infos/${id}/`, 
    { headers: {  'Content-Type' : 'application/json',"Authorization": `Token ${token}` } })
        .then(res => {
            console.log(res.data)
            setData(res.data) 
          
        }).catch(error =>alert(error));   
},[])

const update = (e) => {
 e.preventDefault()
  var id =localStorage.getItem("idUser")
 // alert(credentials.nom)
  console.log(credentials)
  Axios.put(`http://localhost:8000/Utilisateurs/gestionComptes/infos/${id}/`,credentials
  , { headers: { 'Authorization': `Token ${token}` } })
      .then(res => {
          console.log(res)
          alert("modification sauvgarder avec succes")
         window.location.reload(false);

      }).catch(error =>alert(error));
}

  return (
    <div>
      <GridContainer>
        <GridItem xs={12} sm={12} md={8}>
          <Card>
            <CardHeader color="info">
              <h4 className={classes.cardTitleWhite}>Modifier votre profile</h4>
              <p className={classes.cardCategoryWhite}>Completer votre profile</p>
            </CardHeader>
            <CardBody>
              <form>
              <GridContainer>

                <GridItem xs={12} sm={12} md={3}>
                <FormControl>
                <InputLabel shrink className={classes.text} >
                   Nom
                  </InputLabel>
                  <Input
                    labelText="Nom"
                    id="nom"
                    onChange={e => credentials.nom=(e.target.value)}
                    formControlProps={{
                      fullWidth: true
                    }}
                  />
                  </FormControl>
                </GridItem>
                <GridItem xs={12} sm={12} md={3}>
                <InputLabel shrink className={classes.text} >
                   Prenom
                  </InputLabel>
                  <Input
                    labelText="Prenom"
                    id="prenom"
                    onChange={e => credentials.prenom=(e.target.value)}
                    formControlProps={{
                      fullWidth: true
                    }}
                  />
                </GridItem>
                <GridItem xs={12} sm={12} md={4}>
                <InputLabel shrink className={classes.text} >
                   E-mail
                  </InputLabel>
                  <Input
                    labelText="Addresse email"
                    id="email-address"
                    onChange={e =>credentials.email=(e.target.value)}
                    formControlProps={{
                      fullWidth: true
                    }}
                  />
                </GridItem>
              </GridContainer>
              <GridContainer>
               
                <GridItem xs={12} sm={12} md={6} style={{marginTop : "50px"}}>
                <InputLabel shrink className={classes.text} >
                   Date de naissance
                  </InputLabel>
                  
                   <Input 
                  id="datetime-local"
                  type="date"
                  defaultValue="0000-00-00"
                InputLabelProps={{
                  shrink: true,
                }}
                onChange={e =>credentials.dateNaissance=(e.target.value)} />

                </GridItem>
                <GridItem xs={12} sm={12} md={6}  style={{marginTop : "50px"}}>
                <InputLabel shrink className={classes.text} >
                  Wilaya
                  </InputLabel>
                  <Input
                    labelText="Wilaya"
                    id="wilaya"
                    onChange={e => credentials.wilaya=(e.target.value)}
                    formControlProps={{
                      fullWidth: true
                    }}
                   
                  />
                </GridItem>
              </GridContainer>

              </form>
            </CardBody>
            <CardFooter>
              <Button color="info" onClick={(e) =>update(e)}>Mise a jour de profile</Button>
            </CardFooter>
         
          </Card>
        </GridItem>
      

        <GridItem xs={12} sm={12} md={4}>
          <Card profile>
            <CardAvatar profile>
              <a href="#pablo" onClick={e => e.preventDefault()}>
                <img src={avatar} alt="..." />
              </a>
            </CardAvatar>
            <CardBody profile>
             
                  <h4 className={classes.cardTitle}>{data.nom} {data.prenom}</h4>
              <p className={classes.description}>
               Date de naissance : {data.dateNaissance}
               </p>
               <p className={classes.description}>
               Wilaya : {data.wilaya}
               </p>

            </CardBody>
          </Card>
        </GridItem>

        <GridItem xs={12} sm={12} md={8}>
        <Card>
            <CardHeader color="info">
              <h4 className={classes.cardTitleWhite}>Modifier le mot de passe</h4>
              <p className={classes.cardCategoryWhite}>Completer votre profile</p>
            </CardHeader>
            <CardBody>
            <GridContainer>

                <GridItem xs={12} sm={12} md={6}  style={{marginTop : "20px"}}>
                <Input
                    placeholder="mot de passe"
                    id="password"
                    type="password"
                 
                   
                  />
                </GridItem>
                <GridItem xs={12} sm={12} md={6} style={{marginTop : "20px"}}>
                <Input
                    placeholder="Confirmer le mot de passe"
                    id="password"
                    type="password"
                 
                   
                  />
                </GridItem>
              </GridContainer>
            </CardBody>
            <CardFooter>
              <Button color="info" onClick={()=>update()}>Mise a jour de mot de passe </Button>
            </CardFooter>
     
            </Card>
        </GridItem>
      </GridContainer>
    </div>
  );
}
