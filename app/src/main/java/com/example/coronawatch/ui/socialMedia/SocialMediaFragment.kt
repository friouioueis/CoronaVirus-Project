package com.example.coronawatch.ui.socialMedia

import android.annotation.SuppressLint
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProviders
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout
import com.example.coronawatch.*
import com.example.coronawatch.adapter.ArticlesAdapter
import com.example.coronawatch.adapter.RobotsAdapter
import com.example.coronawatch.ui.articles.ArticlesFeed
import com.google.android.material.snackbar.Snackbar
import com.squareup.okhttp.Callback
import com.squareup.okhttp.OkHttpClient
import com.squareup.okhttp.Request
import com.squareup.okhttp.Response
import java.io.IOException

class SocialMediaFragment : Fragment() {

    lateinit var recyclerView: RecyclerView
    lateinit var swipeRefreshLayout: SwipeRefreshLayout
    var robotsFeed = RobotsFeed(arrayListOf() , "" , false)
    private var adapter = RobotsAdapter(robotsFeed, this.context)
    val url = "$baseUrl/Robots/articles/"
    val token = globalToken
    private lateinit var socialMediaViewModel: SocialMediaViewModel

    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
    ): View? {
        socialMediaViewModel =
                ViewModelProviders.of(this).get(SocialMediaViewModel::class.java)
        val root = inflater.inflate(R.layout.fragment_social_media, container, false)

        recyclerView = root.findViewById(R.id.recycler_view_robots) as RecyclerView
        recyclerView.layoutManager = LinearLayoutManager(this.context)
        recyclerView.adapter = adapter
        swipeRefreshLayout = root.findViewById(R.id.swipe_robots_refresh_layout) as SwipeRefreshLayout
        swipeRefreshLayout.setOnRefreshListener {

            adapter.robotsFeed.robots.clear()


            fetchJSON(url, token)

            adapter.notifyDataSetChanged()

        }
        recyclerView.addOnScrollListener(object : RecyclerView.OnScrollListener() {
            override fun onScrollStateChanged(recyclerView: RecyclerView, newState: Int) {
                super.onScrollStateChanged(recyclerView, newState)
                if (!recyclerView.canScrollVertically(1)) {
                    if(robotsFeed.hasNext)
                    {
                        swipeRefreshLayout.isRefreshing = true
                        fetchJSON(robotsFeed.next , token)

                    }
                }
            }
        })
        fetchJSON(url, token)
        adapter.notifyDataSetChanged()

        return root
    }

    private fun fetchJSON(url: String, token: String){
        swipeRefreshLayout.isRefreshing = true
        val url = url
        val token = "Token $token"
        val request = Request.Builder().url(url).header("Authorization", token)
            .build()
        val client = OkHttpClient()
        client.newCall(request).enqueue(object : Callback{
            override fun onFailure(request: Request?, e: IOException?){
                swipeRefreshLayout.isRefreshing = false
                print("Failed to execute request")
            }
            @SuppressLint("UseRequireInsteadOfGet")
            override fun onResponse(response: Response?){
                val body = response?.body()?.string()
                try{
                    activity?.runOnUiThread {
                        val buffer  =
                            parentFragment?.context?.let { robotsParsing(body.toString() , it) }!!
                        robotsFeed.robots.addAll(buffer.robots)
                        robotsFeed.next = buffer.next
                        robotsFeed.hasNext = buffer.hasNext

                        adapter.notifyDataSetChanged()
                    }
                    swipeRefreshLayout.isRefreshing = false
                }catch (e: org.json.JSONException) {
                    view?.let {
                        Snackbar.make(it, "حدث خطأ في الإتصال ", Snackbar.LENGTH_LONG)
                            .setAction("Action", null).show()

                    }
                }}
        })
    }

}










class Robots(
    val title : String,
    val language : String,
    val source : String,
    val link : String

)

class RobotsFeed(var robots: ArrayList<Robots> , var next : String ,var hasNext : Boolean)
