package com.example.coronawatch.adapter

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.coronawatch.Commentaire

import com.example.coronawatch.R
import com.example.coronawatch.RecyclerViewAdapter
import kotlinx.android.synthetic.main.comment_row.view.*

class CommentsAdapter(comments: ArrayList<Commentaire>, nContext: Context) :
    RecyclerView.Adapter<RecyclerViewAdapter.ViewHolder>() {

    private val comments = comments

    private  val ncontext  = nContext

    public class CommentsHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val username = itemView.findViewById<TextView>(R.id.user_name)
        val timeComment = itemView.findViewById<TextView>(R.id.time_comment)
        val content = itemView.findViewById<TextView>(R.id.comment_content)
    }

    override fun onCreateViewHolder(
        parent: ViewGroup,
        viewType: Int
    ): RecyclerViewAdapter.ViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.comment_row , parent , false)
        return RecyclerViewAdapter.ViewHolder(view)
    }

    override fun getItemCount(): Int {
    return comments.size
    }

    override fun onBindViewHolder(holder: RecyclerViewAdapter.ViewHolder, position: Int) {
        holder.itemView.user_name.text = comments[position].username
        holder.itemView.time_comment.text = comments[position].time
        holder.itemView.comment_content.text = comments[position].content
    }

}