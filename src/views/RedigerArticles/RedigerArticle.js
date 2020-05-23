
import React, { Component, useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import SunEditor from 'suneditor-react';
import 'suneditor/dist/css/suneditor.min.css'; // Import Sun Editor's CSS File
import Button from '@material-ui/core/Button';
// import { useSnackbar } from 'notistack';

import { withStyles } from '@material-ui/core/styles';
import Axios from 'axios';

// const { enqueueSnackbar } = useSnackbar();

const useStyles = makeStyles(theme => ({
    accbutt: {
        backgroundColor: '#00acc1',
        '&:hover': {
            backgroundColor: '#00acc1',
        },

    },
}));






class RecipeReviewCard extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            article: "",
            photos: null
        }
    }




    handleChange = (e) => {

        console.log(this.state.article)
        console.log(e); //Get Content Inside Editor
        this.setState({

            article: e

        })


        console.log("after " + this.state.article)
        // var table_of_links = this.state.article.match(/src="[^"]+"/g)
        // for (let i = 0; i < table_of_links.length; i++)
        //     table_of_links[i] = table_of_links[i].slice(5, -1);
        // console.log(table_of_links)
        // console.log("done")

    }

    // handleClickVariant = variant => () => {
    //     // variant could be success, error, warning, info, or default
    //     enqueueSnackbar('This is a success message!', { variant });
    // };

    // ["https://images.itnewsinfo.com/lmi/articles/grande/000000070828.jpg"]

    // file_slected_listner = (e) => {
    //     let image = e.target.files[0]
    //     // console.log(e.target.files[0])
    //     this.setState({

    //         photos: image

    //     })
    //     console.log(image)
    //     console.log(this.state.photos)
    // }

    handlesubmit = (e) => {
        e.preventDefault()
        console.log("axios post")
        const token = "e237da47a10c7bc096c8515a4923b92c953bb33d"

        Axios.post('http://localhost:8000/articles/articles/', {
            "contenuAr": this.state.article,
            "idRedacteurAr": 1
        }, { headers: { "Authorization": `Token ${token}` } }
        ).then(res => {
            console.log(res)
            console.log(res.data.idArticle)
            // this.handleClickVariant('success')
        })
    }

    // handlesubmit = (e) => {
    //     e.preventDefault()
    //     let file = this.state.photos
    //     var formdata = new FormData()
    //     formdata.append("image", file, file.name)
    //     formdata.append("idArticlePh", 1)

    //     console.log(formdata)
    //     console.log(this.state.photos)



    //     console.log("axios post")

    //     const token = "eaedf22be03cc027b467b8ce2f53e848bde1deba"

    //     Axios.post('http://localhost:8000/articles/photos_articles/', {
    //         formdata
    //     }, { headers: { "Authorization": `Token ${token}`, 'Content-Type': 'multipart/form-data' } }
    //     ).then(res => {
    //         console.log(res)
    //         // console.log(res.data.idArticle)
    //         // this.handleClickVariant('success')
    //     })
    // }







    render() {
        const { classes } = this.props;

        return (
            <div>


                {/* <input onChange={(e) => this.file_slected_listner(e)} id="" type="file" src="" alt="" /> */}


                <SunEditor onChange={this.handleChange} setOptions={{
                    height: 500,
                    "buttonList": [

                        ["undo",
                            "redo",
                            "font",
                            "fontSize",
                            "formatBlock"],
                        ["bold",
                            "underline",
                            "italic",
                            "strike",
                            "subscript",
                            "superscript"],
                        ["fontColor",
                            "hiliteColor"],
                        ["removeFormat",
                            "outdent",
                            "indent"],
                        ["align",
                            "horizontalRule",
                            "list",
                            "lineHeight"],
                        ["table",
                            "link"],
                        ["image",
                            "video"],

                    ],
                }} />

                <form onSubmit={this.handlesubmit}>
                    <Button type="submit" variant="contained" color="primary" className={classes.accbutt}>
                        Postuler
                    </Button>

                </form>



            </div>

        );

    }



}



export default withStyles(useStyles)(RecipeReviewCard);