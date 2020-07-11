package com.example.coronawatch.adapter

import android.content.Context
import android.net.Uri
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.MediaController
import android.widget.VideoView
import androidx.recyclerview.widget.RecyclerView
import com.example.coronawatch.R

class RecyclerViewVideoAdapter(videoURLs: ArrayList<String> ,  nContext: Context) : RecyclerView.Adapter<RecyclerViewVideoAdapter.VideoViewHolder>() {


    private val videoURLs = videoURLs
    private  val ncontext  = nContext

    class VideoViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {

        val video = itemView.findViewById<VideoView>(R.id.article_videoview)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecyclerViewVideoAdapter.VideoViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.video_list , parent , false)
        return  VideoViewHolder(view)
    }

    override fun getItemCount(): Int {

        return  videoURLs.size
    }

    override fun onBindViewHolder(holder: VideoViewHolder, position: Int) {
        println("GGGGGGGGG${videoURLs[position]}")
        val mediaController = MediaController(ncontext)
        mediaController.setAnchorView(holder.video)
        val video = Uri.parse(videoURLs[position])
        holder.video.setMediaController(mediaController)
        holder.video.setVideoURI(video)
        holder.video.setZOrderOnTop(true)
        holder.video.canScrollHorizontally(0)
        holder.video.start()

        /*holder.video.setVideoURI(Uri.parse(videoURLs[position]))
            holder.video.setOnClickListener {
                if (holder.video.isPlaying)
                    holder.video.pause()
                else
                    holder.video.start()
            }*/
    }




}
