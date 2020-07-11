
package com.example.myapplication

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.bumptech.glide.GlideBuilder
import com.bumptech.glide.annotation.GlideModule
import com.bumptech.glide.load.engine.DiskCacheStrategy
import com.bumptech.glide.module.AppGlideModule
import com.bumptech.glide.request.RequestOptions
import com.bumptech.glide.signature.ObjectKey
import com.example.coronawatch.R


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








