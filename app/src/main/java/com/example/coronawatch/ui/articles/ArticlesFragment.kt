
package com.example.coronawatch.ui.articles

import Article
import android.annotation.SuppressLint
import android.annotation.TargetApi
import android.os.Build
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProviders
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout
import com.example.coronawatch.*
import com.example.coronawatch.adapter.ArticlesAdapter
import com.google.android.material.snackbar.Snackbar
import com.squareup.okhttp.Callback
import com.squareup.okhttp.OkHttpClient
import com.squareup.okhttp.Request
import com.squareup.okhttp.Response
import java.io.IOException


class ArticlesFragment : Fragment() {

    private lateinit var articlesViewModel: ArticlesViewModel
    lateinit var recyclerView: RecyclerView
    lateinit var swipeRefreshLayout: SwipeRefreshLayout
    var articlesFeed = ArticlesFeed(arrayListOf() , "" , false)
    private var adapter = ArticlesAdapter(articlesFeed, this.context)
    val url = "$baseUrl/articles/articlesValides"

    val token = globalToken
    @TargetApi(Build.VERSION_CODES.M)
    @SuppressLint("ResourceAsColor")
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        articlesViewModel =
            ViewModelProviders.of(this).get(ArticlesViewModel::class.java)
        val root = inflater.inflate(R.layout.fragment_articles, container, false)

        recyclerView = root.findViewById(R.id.recycler_view_articles) as RecyclerView
        recyclerView.layoutManager = LinearLayoutManager(this.context)
        recyclerView.adapter = adapter
        swipeRefreshLayout = root.findViewById(R.id.swipe_refresh_layout) as SwipeRefreshLayout

        swipeRefreshLayout.setOnRefreshListener {

            adapter.articlesFeed.articles.clear()


            fetchJSON(url, token)

            adapter.notifyDataSetChanged()

        }

        recyclerView.addOnScrollListener(object : RecyclerView.OnScrollListener() {
            override fun onScrollStateChanged(recyclerView: RecyclerView, newState: Int) {
                super.onScrollStateChanged(recyclerView, newState)
                if (!recyclerView.canScrollVertically(1)) {
                    if(articlesFeed.hasNext)
                       {
                           swipeRefreshLayout.isRefreshing = true
                           fetchJSON(articlesFeed.next , token)

                       }
                }
            }
        })

        fetchJSON(url, token)
        adapter.notifyDataSetChanged()

        return root
    }

    private fun fetchJSON(url: String, token: String) {
        swipeRefreshLayout.isRefreshing = true
        val url = url


        val token = "Token $token"

        val request = Request.Builder().url(url).header("Authorization", token)
            .build()
        val client = OkHttpClient()
        client.newCall(request).enqueue(object : Callback {
            override fun onFailure(request: Request?, e: IOException?) {
                swipeRefreshLayout.isRefreshing = false
                print("Failed to execute request")
            }

            @SuppressLint("UseRequireInsteadOfGet")
            override fun onResponse(response: Response?) {
                val body = response?.body()?.string()
                println("FFFFFFFFFFF$body")
                try {
                    activity?.runOnUiThread {
                        val buffer  =
                            parentFragment?.context?.let { articlesParsing(body.toString() , it) }!!
                        articlesFeed.articles.addAll(buffer.articles)
                        articlesFeed.next = buffer.next
                        articlesFeed.hasNext = buffer.hasNext

                        adapter.notifyDataSetChanged()
                    }

                    swipeRefreshLayout.isRefreshing = false

                } catch (e: org.json.JSONException) {

                    view?.let {
                        Snackbar.make(it, "حدث خطأ في الإتصال ", Snackbar.LENGTH_LONG)
                            .setAction("Action", null).show()
                    }


                    println("حدث خطأ في الإتصال ")
                }catch (e: java.lang.reflect.InvocationTargetException){
                    view?.let {
                        Snackbar.make(it, "حدث خطأ في الإتصال ", Snackbar.LENGTH_LONG)
                            .setAction("Action", null).show()
                    }
                }


            }


        })

    }



}

class ArticlesFeed(var articles: ArrayList<Article> , var next : String ,var hasNext : Boolean)

