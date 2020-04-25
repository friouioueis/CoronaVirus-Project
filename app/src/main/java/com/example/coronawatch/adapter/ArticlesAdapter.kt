package com.example.coronawatch.adapter

import android.content.Context
import android.os.Build
import android.text.Html
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.view.inputmethod.EditorInfo
import androidx.annotation.RequiresApi
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.coronawatch.Commentaire
import com.example.coronawatch.R
import com.example.coronawatch.ui.articles.ArticlesFeed
import kotlinx.android.synthetic.main.article_row.view.*
import java.time.LocalTime


class ArticlesAdapter(
    var articlesFeed: ArticlesFeed,
    val nContext: Context?
) : RecyclerView.Adapter<CustomViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CustomViewHolder {
        val layoutInflater = LayoutInflater.from(parent.context)
        val cellForRow = layoutInflater.inflate(R.layout.article_row, parent, false)

        return CustomViewHolder(cellForRow)
    }

    override fun getItemCount(): Int {
        return articlesFeed.articles.size
    }

    @RequiresApi(Build.VERSION_CODES.O)
    override fun onBindViewHolder(holder: CustomViewHolder, position: Int) {
        holder.itemView.username_article.text = articlesFeed.articles[position].username
        holder.itemView.article_content.setText(Html.fromHtml(articlesFeed.articles[position].content))
        //.text = articlesFeed.articles[position].content
        holder.itemView.image_recyclerview.layoutManager =
            LinearLayoutManager(nContext, LinearLayoutManager.HORIZONTAL, false)


        holder.itemView.image_recyclerview.adapter = articlesFeed.articles[position].imageAdapter
        holder.itemView.tv_time.text = articlesFeed.articles[position].time
        holder.itemView.list_view_comments.layoutManager = LinearLayoutManager(nContext , LinearLayoutManager.VERTICAL , false)
        holder.itemView.list_view_comments.adapter = articlesFeed.articles[position].commentsAdapter

        holder.itemView.edit_text_add_comment.setOnEditorActionListener { v, actionId, event ->
            var handled = false
            if (actionId == EditorInfo.IME_ACTION_DONE) {
                //adding a comment
                articlesFeed.articles[position].comments.add(Commentaire(holder.itemView.edit_text_add_comment.text.toString() , "now"))
                articlesFeed.articles[position].commentsAdapter?.notifyDataSetChanged()
                holder.itemView.edit_text_add_comment.text.clear()
                holder.itemView.edit_text_add_comment.isFocusable = false
                handled = true
            }
            handled
        }
    }
}


class CustomViewHolder(v: View) : RecyclerView.ViewHolder(v) {

}