

import android.content.Context

import com.example.coronawatch.classes.Commentaire

import com.example.coronawatch.adapter.CommentsAdapter
import com.example.coronawatch.adapter.RecyclerViewVideoAdapter
import com.example.myapplication.RecyclerViewAdapter



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



    class Time(time: String) {

        val second = time.substring(17, 19).toInt()
        val minute = time.substring(14, 16).toInt()
        val hour = time.substring(11, 13).toInt()
        val day = time.substring(8, 10).toInt()
        val month = time.substring(5, 7).toInt()
        val year = time.substring(0, 4).toInt()

    }

}