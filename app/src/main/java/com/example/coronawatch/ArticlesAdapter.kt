package com.example.coronawatch

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView

class ArticlesAdapter : RecyclerView.Adapter<CustomViewHolder>() {
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CustomViewHolder {
     val layoutInflater = LayoutInflater.from(parent.context)
        val cellForRow = layoutInflater.inflate(R.layout.article_row , parent , false)
        return CustomViewHolder(cellForRow)
    }

    override fun getItemCount(): Int {
        return 3
    }

    override fun onBindViewHolder(holder: CustomViewHolder, position: Int) {

    }


}


class CustomViewHolder(v: View) : RecyclerView.ViewHolder(v) {

}