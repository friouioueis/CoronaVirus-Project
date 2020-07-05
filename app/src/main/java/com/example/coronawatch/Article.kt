
import android.annotation.SuppressLint
import android.content.Context
import android.os.Build
import androidx.annotation.RequiresApi
import com.example.coronawatch.Commentaire

import com.example.coronawatch.adapter.CommentsAdapter
import com.example.myapplication.RecyclerViewAdapter
import com.example.myapplication.RecyclerViewVideoAdapter

import java.time.LocalDate
import java.time.LocalDateTime
import java.time.LocalTime

class Article(
    val username: String,
    val content: String,
    val imageURLs: ArrayList<String>,
    val videoURLs: ArrayList<String>,
    context: Context?,
    time: String,
    val comments: ArrayList<Commentaire>
) {
    val imageAdapter = context?.let { RecyclerViewAdapter(imageURLs, it) }
    val videoAdapter = context?.let { RecyclerViewVideoAdapter(videoURLs , it) }
    val commentsAdapter = context?.let { CommentsAdapter(comments, it) }
    private val dateTime = Article.Time(time)

    val time = "${dateTime.day}-${dateTime.month}-${dateTime.year}  ${time.substring(11, 16)}"
    //val profilePic = ProfilePic
    //val articleImage = articleImage

    // "dateAr":"2020-04-22T00:56:24.066665Z"


    class Time(time: String) {
        //second : String , minute : String , hour : String , day : String ,month : String , Year : String
        val second = time.substring(17, 19).toInt()
        val minute = time.substring(14, 16).toInt()
        val hour = time.substring(11, 13).toInt()
        val day = time.substring(8, 10).toInt()
        val month = time.substring(5, 7).toInt()
        val year = time.substring(0, 4).toInt()

    }

}