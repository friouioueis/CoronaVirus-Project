@file:Suppress("SENSELESS_COMPARISON")

package com.example.coronawatch

import Article
import android.content.Context
import com.example.coronawatch.ui.articles.ArticlesFeed
import org.json.JSONArray
import org.json.JSONException
import org.json.JSONObject
import java.lang.NullPointerException

fun articlesParsing(dataString: String, nContext: Context?): ArticlesFeed {
    println("HHHHHHHHHHHHHHHHHHHHH$dataString")
    val data = JSONObject(dataString)
    val json = data.getJSONArray("results")
    var feed = arrayListOf<Article>()


    var i = json.length() - 1

    while (i >= 0) {

        val jsonArticle = json.getJSONObject(i)




        val stringPhoto = jsonArticle.getString("photos")


        val jsonPhoto = JSONArray(stringPhoto)
        var j = 0
        var imagesArrayList = arrayListOf<String>()

        while (j < jsonPhoto.length()) {
            try {
                val image = JSONObject(jsonPhoto[j].toString())
                imagesArrayList.add(image["lienPhAc"].toString())
            } catch (e: NullPointerException) {

            }

            j++
        }


        val stringVideo = jsonArticle.getString("videos")


        val jsonVideo = JSONArray(stringVideo)
        j = 0
        var videoArrayList = arrayListOf<String>()

        while (j < jsonVideo.length()) {
            try {
                val video = JSONObject(jsonVideo[j].toString())
                videoArrayList.add(video["lienViAc"].toString())
                println("vvvvvvvvvvvvvvvv${video["lienViAc"].toString()}")
            } catch (e: NullPointerException) {

            }

            j++
        }




        println(jsonArticle["contenuAr"].toString())
        feed.add(
            Article(
                "user name",
                jsonArticle["contenuAr"].toString(),
                imagesArrayList
                ,
                videoArrayList
                ,
                nContext
                ,
                jsonArticle["dateAr"].toString()
                ,
                arrayListOf(
                    Commentaire("commentaire 1", "now"),
                    Commentaire("commentaire 2", "now")


                )
            )
        )
        i--
    }

    return ArticlesFeed(feed , data.getString("next") , data.getString("next") != "null")
}

fun statsParsing(dataString: String , nContext: Context?) : ArrayList<InfoWilaya>{
    val data = JSONObject(dataString)
    val json = data.getJSONArray("results")
    var feedStat = arrayListOf<InfoWilaya>()
    var i = json.length() - 1

    while (i >= 0) {
        val jsonStat = json.getJSONObject(i)
        feedStat.add(InfoWilaya(
            jsonStat["idStatistique"].toString().toInt(),
            jsonStat["nbrPorteurVirus"].toString().toInt(),
            jsonStat["casConfirme"].toString().toInt(),
            jsonStat["casRetablis"].toString().toInt(),
            jsonStat["nbrDeces"].toString().toInt(),
            jsonStat["nbrGuerisons"].toString().toInt(),
            jsonStat["dateSt"].toString(),
            0,
            jsonStat["idRegionSt"].toString().toInt(),
            jsonStat["idModerateurSt"].toString().toInt()
        ))
        i--
    }
    return feedStat
}
class CountryInfo(val casConfirme: Int,
                  val casRetablis: Int,
                  val nbrDeces: Int,
                  val nbrPorteurVirus: Int,
                  val match: Boolean

)
fun countriesParsing(dataString: String , nContext: Context?) : CountryInfo{
    println(dataString)
    val data = JSONObject(dataString)
    if(data.getString("message") == "OK"){
        try {
            val country: JSONObject = data.getJSONObject("data")
            val covid19Stats: JSONArray = country.getJSONArray("covid19Stats")


            var confirmed = 0
            var recovered = 0
            var deaths = 0
            println(covid19Stats.toString())
            var i = 0
            while(i < covid19Stats.length())
            {
                var element = covid19Stats[i] as JSONObject
                try{
                    if(element.getString("confirmed") != null)  confirmed += element.getString("confirmed").toInt()
                    if(element.getString("recovered") != null) recovered += element.getString("recovered").toInt()
                    if(element.getString("deaths") != null) deaths += element.getString("deaths").toInt()

                }catch (e :NumberFormatException)
                {

                }
                i++
            }


            return CountryInfo(confirmed,
                recovered,
                deaths,
                confirmed -(recovered+deaths),
                true


            )
        }catch (e : JSONException){
            return CountryInfo(0,
                0,
                0,
                0,
                false

            )
        }

    }
    else{
        return CountryInfo(0,
            0,
            0,
            0,
            false

        )
    }



}



fun youtubeVideoParsing(dataString: String, nContext: Context?): ArrayList<YouTubeVideos> {

    val data = JSONObject(dataString)
    val json = data.getJSONArray("results")
    var feed = arrayListOf<YouTubeVideos>()


    var i = 0

    while (i < json.length()) {

        val jsonYoutube = json.getJSONObject(i)



        feed.add(
            YouTubeVideos(

                jsonYoutube["videoId"].toString(),
                jsonYoutube["titreYt"].toString(),
                jsonYoutube["chaineYt"].toString()

            )
        )
        i++
    }

    return feed
}

