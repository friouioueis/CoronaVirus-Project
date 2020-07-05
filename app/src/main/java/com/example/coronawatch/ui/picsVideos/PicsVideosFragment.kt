package com.example.coronawatch.ui.picsVideos

import android.R
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

import com.example.coronawatch.YouTubeVideos
import com.example.coronawatch.baseUrl
import com.example.coronawatch.globalToken
import com.example.coronawatch.ui.diagno.PicsVideosViewModel


import com.example.coronawatch.youtubeVideoParsing
import com.example.myapplication.VideoAdapter


import com.squareup.okhttp.Callback
import com.squareup.okhttp.OkHttpClient
import com.squareup.okhttp.Request
import com.squareup.okhttp.Response
import java.io.IOException


class PicsVideosFragment : Fragment() {

    private lateinit var picsVideosViewModel: PicsVideosViewModel
    lateinit var youtubeRecyclerView : RecyclerView
    var youtubeVideos  = arrayListOf<YouTubeVideos>()
    lateinit var adapterYt : VideoAdapter

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

        fetchJSON("$baseUrl/Robots/pub/youtube/sorted/", globalToken)
        adapterYt.notifyDataSetChanged()

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
                }catch (e : Exception){

                }
            }
        })

    }

}


/*


* */