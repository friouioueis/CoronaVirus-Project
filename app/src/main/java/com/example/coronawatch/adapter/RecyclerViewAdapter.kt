
package com.example.myapplication

import android.content.Context
import android.net.Uri
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.MediaController
import android.widget.TextView
import android.widget.VideoView
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.bumptech.glide.GlideBuilder
import com.bumptech.glide.annotation.GlideModule
import com.bumptech.glide.load.engine.DiskCacheStrategy
import com.bumptech.glide.module.AppGlideModule
import com.bumptech.glide.request.RequestOptions
import com.bumptech.glide.signature.ObjectKey
import com.example.coronawatch.R
import com.example.coronawatch.YouTubeVideos

import com.example.coronawatch.apiKey
import com.pierfrancescosoffritti.androidyoutubeplayer.core.player.views.YouTubePlayerView


@GlideModule
class GlideApp  : AppGlideModule()
{
    override fun applyOptions(context: Context, builder: GlideBuilder) {
        super.applyOptions(context, builder)
        builder.apply { RequestOptions().diskCacheStrategy(DiskCacheStrategy.ALL).signature(
            ObjectKey(System.currentTimeMillis().toShort())
        ) }
    }

}

class RecyclerViewAdapter(imageURLs: ArrayList<String>, nContext: Context) : RecyclerView.Adapter<RecyclerViewAdapter.ImageViewHolder>() {

    private val imageURLs = imageURLs
    private  val ncontext  = nContext

    class ImageViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {

        val image = itemView.findViewById<ImageView>(R.id.article_imageview)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ImageViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.image_list , parent , false)
        return  ImageViewHolder(view)
    }

    override fun getItemCount(): Int {

        return  imageURLs.size
    }


    override fun onBindViewHolder(holder: ImageViewHolder, position: Int) {
        Glide.with(ncontext)
            .asBitmap()
            .load(imageURLs[position])

            .into(holder.image)


    }
}



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




class VideoAdapter(val videoURLs: ArrayList<YouTubeVideos>, val nContext: Context) : RecyclerView.Adapter<VideoAdapter.YoutubeViewHolder>()
     {

 /*  override fun onInitializationSuccess(provider: YouTubePlayer.Provider?, player: YouTubePlayer?, wasRestored: Boolean) {

        if (!wasRestored) {
            player?.cueVideo("wKJ9KzGQq0w");
        }
    }
    override fun onInitializationFailure(p0: YouTubePlayer.Provider?, p1: YouTubeInitializationResult?) {
    }
*/


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

    override fun onBindViewHolder(holder: YoutubeViewHolder, position: Int) {



        //holder.video.loadData(videoURLs[position].videoUrl , "text/html" , "utf-8")
        holder.title.text = videoURLs[position].videoTitle
        holder.channel.text = videoURLs[position].videoChannel
    }

//   override fun onInitializationSuccess(youTubeThumbnailView: YouTubeThumbnailView?, youTubeThumbnailLoader: YouTubeThumbnailLoader?) {
//        youTubeThumbnailLoader?.setVideo(videoURLs[0].videoUrl)
//        youTubeThumbnailLoader?.setOnThumbnailLoadedListener(object : OnThumbnailLoadedListener {
//            override fun onThumbnailLoaded(
//                youTubeThumbnailView: YouTubeThumbnailView,
//                s: String
//            ) {
//                youTubeThumbnailLoader.release()
//            }
//
//            override fun onThumbnailError(
//                youTubeThumbnailView: YouTubeThumbnailView,
//                errorReason: YouTubeThumbnailLoader.ErrorReason
//            ) {
//            }
//        })
//    }
//
//    override fun onInitializationFailure(
//        p0: YouTubeThumbnailView?,
//        p1: YouTubeInitializationResult?
//    ) {
//        TODO("not implemented") //To change body of created functions use File | Settings | File Templates.
//    }


}
