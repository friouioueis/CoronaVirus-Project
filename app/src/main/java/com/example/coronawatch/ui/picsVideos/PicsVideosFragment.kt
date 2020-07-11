package com.example.coronawatch.ui.picsVideos


import android.annotation.SuppressLint
import android.os.Build

import android.os.Bundle
import android.view.LayoutInflater

import android.view.View
import android.view.ViewGroup
import androidx.annotation.RequiresApi


import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProviders

import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout
import com.example.coronawatch.*
import com.example.coronawatch.adapter.VideoAdapter
import com.example.coronawatch.classes.YouTubeVideos

import com.example.coronawatch.ui.diagno.PicsVideosViewModel





import com.squareup.okhttp.Callback
import com.squareup.okhttp.OkHttpClient
import com.squareup.okhttp.Request
import com.squareup.okhttp.Response
import java.io.IOException


class PicsVideosFragment : Fragment() {

    private lateinit var picsVideosViewModel: PicsVideosViewModel
    lateinit var youtubeRecyclerView : RecyclerView
    var youtubeVideos  = arrayListOf<YouTubeVideos>()
    lateinit var swipeRefreshLayout: SwipeRefreshLayout
    lateinit var adapterYt : VideoAdapter
    val url = "$baseUrl/Robots/pub/youtube/sorted/"
    companion object {
        fun newInstance() = PicsVideosFragment()
    }

    private lateinit var picsVideosviewModel: PicsVideosViewModel

    @RequiresApi(Build.VERSION_CODES.M)
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {


        val view = inflater.inflate(R.layout.fragment_pics_videos, container, false)
        youtubeRecyclerView = view.findViewById(R.id.youtube_player_view)
        youtubeRecyclerView.setHasFixedSize(true)
        youtubeRecyclerView.layoutManager = LinearLayoutManager(context)

        adapterYt = VideoAdapter(youtubeVideos , view.context)

        youtubeRecyclerView.adapter = adapterYt

        fetchJSON(url, globalToken)
        adapterYt.notifyDataSetChanged()

        swipeRefreshLayout = view.findViewById(R.id.swipe_youtube_refresh_layout) as SwipeRefreshLayout
        swipeRefreshLayout.setOnRefreshListener {

            adapterYt.videoURLs.clear()

            swipeRefreshLayout.isRefreshing = true
            fetchJSON(url, globalToken)

            adapterYt.notifyDataSetChanged()

        }

        return view
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        picsVideosviewModel = ViewModelProviders.of(this).get(PicsVideosViewModel::class.java)
        // TODO: Use the ViewModel
    }



    private fun fetchJSON(url: String, token: String){

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
            override fun onResponse(response: Response?){
                val body = response?.body()?.string()
                try{
                    activity?.runOnUiThread{
                        val buffer  =
                            youtubeVideoParsing(body.toString() , context)
                        youtubeVideos.addAll(buffer)
                        adapterYt?.notifyDataSetChanged()
                    }
                    swipeRefreshLayout.isRefreshing = false
                }catch (e : Exception){

                }
            }
        })

    }

}


/*


* */