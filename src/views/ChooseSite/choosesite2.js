import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import List from '@material-ui/core/List';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import Checkbox from '@material-ui/core/Checkbox';
import Button from '@material-ui/core/Button';
import Divider from '@material-ui/core/Divider';
import { InputLabel, Select, MenuItem } from "@material-ui/core"
import { KeyboardDatePicker, MuiPickersUtilsProvider } from '@material-ui/pickers';
import Icon from '@material-ui/core/Icon';
import Axios from 'axios';


const useStyles = makeStyles((theme) => ({
  root: {
    margin: 'auto',
  },
  cardHeader: {
    padding: theme.spacing(1, 2),
  },
  list: {
    width: "100%",
    height: 230,
    backgroundColor: theme.palette.background.paper,
    overflow: 'auto',
  },
  button: {
    margin: theme.spacing(0.5, 0),
  },
}));

function not(a, b) {
  return a.filter((value) => b.indexOf(value) === -1);
}

function intersection(a, b) {
  return a.filter((value) => b.indexOf(value) !== -1);
}

function union(a, b) {
  return [...a, ...not(b, a)];
}

export default function TransferList() {
  const classes = useStyles();
  const [checked, setChecked] = React.useState([]);
  const [left, setLeft] = React.useState(["bbc", "france24", "cnn", "un", "arabia", "who", "youtube", "google news"]);
  const [right, setRight] = React.useState([]);
  const [lang, setlang] = useState("")
  const [selectedDatestart, setSelectedDatestart] = useState("");
  const [selectedDateend, setSelectedDateend] = useState("");
  const token =  localStorage.getItem("token");

  const handleDateStartChange = (e) => {
    // console.log(e.target.value)
    setSelectedDatestart(e.target.value);
  };

  const handleDateEndChange = (e) => {
    // console.log(e.target.value)
    setSelectedDateend(e.target.value);
  };

  const handlechange = (e) => {
    // console.log("you have choosen : " + e.target.value)
    setlang(e.target.value)
  }


  const leftChecked = intersection(checked, left);
  const rightChecked = intersection(checked, right);

  const handleToggle = (value) => () => {
    const currentIndex = checked.indexOf(value);
    const newChecked = [...checked];

    if (currentIndex === -1) {
      newChecked.push(value);
    } else {
      newChecked.splice(currentIndex, 1);
    }

    setChecked(newChecked);
  };

  const numberOfChecked = (items) => intersection(checked, items).length;

  const handleToggleAll = (items) => () => {
    if (numberOfChecked(items) === items.length) {
      setChecked(not(checked, items));
    } else {
      setChecked(union(checked, items));
    }
  };

  const handleCheckedRight = () => {
    setRight(right.concat(leftChecked));
    setLeft(not(left, leftChecked));
    setChecked(not(checked, leftChecked));
  };

  const handleCheckedLeft = () => {
    setLeft(left.concat(rightChecked));
    setRight(not(right, rightChecked));
    setChecked(not(checked, rightChecked));
  };

  const handlesubmit = () => {
    console.log(right.join())
    console.log(lang)
    console.log(selectedDatestart)
    console.log(selectedDateend)
    var source = "" 
    source = (right.join()).toString()
    console.log(source)

    console.log("set valider true")
    Axios.post(`http://localhost:8000/Robots/spider/run/`, {
      "langue":lang,
      "source":source,
      "dateDebut":selectedDatestart,
      "dateFin":selectedDateend
  }, { headers: { "Authorization": `Token ${token}` } })
      .then(res => {
        console.log(res)
        alert("Votre demande est prise en charge")
        window.location.reload(false);
      }).catch(error=>alert("Verifier votre connexion internet "))

  };


  // const handleChangelangue = (event) => {
  //   setlangue(event.target.value);
  //   console.log(langue)
  // };
  const customList = (title, items) => (
    <Card  style={{width : "300px"}}>
      <CardHeader
        className={classes.cardHeader}
        avatar={
          <Checkbox
            onClick={handleToggleAll(items)}
            checked={numberOfChecked(items) === items.length && items.length !== 0}
            indeterminate={numberOfChecked(items) !== items.length && numberOfChecked(items) !== 0}
            disabled={items.length === 0}
            inputProps={{ 'aria-label': 'all items selected' }}
          />
        }
        title={title}
      // subheader={`${numberOfChecked(items)}/${items.length} selected`}
      />
      <Divider />
      <List className={classes.list} dense component="div" role="list">
        {items.map((value) => {
          const labelId = `transfer-list-all-item-${value}-label`;

          return (
            <ListItem key={value} role="listitem" button onClick={handleToggle(value)}>
              <ListItemIcon>
                <Checkbox
                  checked={checked.indexOf(value) !== -1}
                  tabIndex={-1}
                  disableRipple
                  inputProps={{ 'aria-labelledby': labelId }}
                />
              </ListItemIcon>
              <ListItemText id={labelId} primary={`${value}`} />
            </ListItem>
          );
        })}
        <ListItem />
      </List>
    </Card>
  );

  return (
    <div >
      <p>Choisissez les sites d'ou vous voulez extraires les articles </p>
      <Grid container spacing={2} justify="center" alignItems="center" className={classes.root}>
        <Grid item>{customList('Les sites disponibles', left)}</Grid>
        <Grid item>
          <Grid container direction="column" alignItems="center">
            <Button
              variant="outlined"
              size="small"
              className={classes.button}
              onClick={handleCheckedRight}
              disabled={leftChecked.length === 0}
              aria-label="move selected right"
            >
              &gt;
          </Button>
            <Button
              variant="outlined"
              size="small"
              className={classes.button}
              onClick={handleCheckedLeft}
              disabled={rightChecked.length === 0}
              aria-label="move selected left"
            >
              &lt;
          </Button>
          </Grid>
        </Grid>
        <Grid item>{customList('Les sites choisi', right)}</Grid>
      </Grid>
      {/* <Button className={classes.button} onClick={handlesubmit} justify="center" alignItems="center" variant="contained" color="primary">
    Primary
  </Button> */}

      {/* <MuiPickersUtilsProvider utils={DateFnsUtils}>

        <KeyboardDatePicker
          disableToolbar
          variant="inline"
          format="MM/dd/yyyy"
          margin="normal"
          id="date-picker-inline"
          label="Date picker inline"
          value={selectedDate}
          onChange={handleDateChange}
          KeyboardButtonProps={{
            'aria-label': 'change date',
          }}
        />
      </MuiPickersUtilsProvider> */}


      <Grid container spacing={2} justify="center" alignItems="center" className={classes.root} style={{marginTop : "30px"}}>
      
        <InputLabel id="demo-simple-select-label">Choisir la langue : </InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={lang}
          onChange={handlechange}
        >
          <MenuItem value="ar">العربية</MenuItem>
          <MenuItem value="fr">Français</MenuItem>
        </Select>
      </Grid>
      <Grid container spacing={2} justify="center" alignItems="center" className={classes.root}>
        <h4>Date de debut : </h4>
        <input value={selectedDatestart} onChange={handleDateStartChange} type="datetime-local" name="" id="" style={{marginLeft : "50px"}} />
      </Grid>
      <Grid container spacing={2} justify="center" alignItems="center" className={classes.root}>
        <h4>Date de fin : </h4>
        <input value={selectedDateend} onChange={handleDateEndChange} type="datetime-local" name="" id="" style={{marginLeft : "70px"}}/>
      </Grid>

      <Grid container spacing={2} justify="center" alignItems="center" className={classes.root}>
        <Button onClick={handlesubmit}
          variant="contained"
          color="primary"
        >
          Envoyer
      </Button>
   
      </Grid>

    </div>


  );
}
