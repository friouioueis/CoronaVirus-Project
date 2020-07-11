package com.example.coronawatch.adapter

import android.content.Context
import android.os.Build
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.annotation.RequiresApi
import androidx.recyclerview.widget.RecyclerView
import com.example.coronawatch.R
import com.example.coronawatch.classes.YouTubeVideos
import com.pierfrancescosoffritti.androidyoutubeplayer.core.player.YouTubePlayer
import com.pierfrancescosoffritti.androidyoutubeplayer.core.player.listeners.AbstractYouTubePlayerListener
import com.pierfrancescosoffritti.androidyoutubeplayer.core.player.views.YouTubePlayerView

class VideoAdapter(val videoURLs: ArrayList<YouTubeVideos>, val nContext: Context) : RecyclerView.Adapter<VideoAdapter.YoutubeViewHolder>()
{



    class YoutubeViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {


        val video = itemView.findViewById<YouTubePlayerView>(R.id.videoWebView)

        val title = itemView.findViewById<TextView>(R.id.youtube_video_title)
        val channel = itemView.findViewById<TextView>(R.id.youtube_video_channel)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): YoutubeViewHolder  {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.video_view , parent , false)
        return  YoutubeViewHolder(view)
    }

    override fun getItemCount(): Int {

        return  videoURLs.size
    }

    @RequiresApi(Build.VERSION_CODES.O)
    override fun onBindViewHolder(holderYt: YoutubeViewHolder, position: Int) {

        holderYt.video.initialize(object : AbstractYouTubePlayerListener(){
            override fun onReady(youTubePlayer: YouTubePlayer) {
                super.onReady(youTubePlayer)
                val videoId = videoURLs[position].videoUrl
                youTubePlayer.loadVideo(videoId , 0F)
            }
        })
        holderYt.video.addYouTubePlayerListener(object : AbstractYouTubePlayerListener() {
            override fun onReady(youTubePlayer: YouTubePlayer) {
                val videoId = videoURLs[position].videoUrl
                youTubePlayer.loadVideo(videoId, 0F)
            }
        })


        holderYt.title.text = videoURLs[position].videoTitle
        holderYt.channel.text = videoURLs[position].videoChannel
    }


}