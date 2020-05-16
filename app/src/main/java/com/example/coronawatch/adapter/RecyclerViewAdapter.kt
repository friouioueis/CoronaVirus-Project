package com.example.coronawatch

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.Toast
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide


class RecyclerViewAdapter(imageURLs: ArrayList<String>, nContext: Context) : RecyclerView.Adapter<RecyclerViewAdapter.ViewHolder>() {

    private val imageURLs = imageURLs
    private  val ncontext  = nContext

    public class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {

        val image = itemView.findViewById<ImageView>(R.id.article_imageview)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.image_list , parent , false)
        return  ViewHolder(view)
    }

    override fun getItemCount(): Int {

        return  imageURLs.size
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        Glide.with(ncontext)
            .asBitmap()
            .load(imageURLs[position])
            .into(holder.image)
        holder.image.setOnClickListener(View.OnClickListener {
            Toast.makeText(ncontext , imageURLs.get(position) , Toast.LENGTH_SHORT).show()
        })
    }
}