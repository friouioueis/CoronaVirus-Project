package com.example.coronawatch.adapter

import android.annotation.SuppressLint
import android.content.Context
import android.graphics.Color
import android.text.method.LinkMovementMethod
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.example.coronawatch.R
import com.example.coronawatch.ui.socialMedia.RobotsFeed
import kotlinx.android.synthetic.main.robot_row.view.*

class CustomRobotsHolder(v: View) : RecyclerView.ViewHolder(v) {

}

class RobotsAdapter(var robotsFeed: RobotsFeed, val nContext: Context?): RecyclerView.Adapter<CustomRobotsHolder>(){
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CustomRobotsHolder {
        val layoutInflater = LayoutInflater.from(parent.context)
        val cellForRow = layoutInflater.inflate(R.layout.robot_row, parent, false)

        return CustomRobotsHolder(cellForRow)
    }

    override fun getItemCount(): Int {
        return robotsFeed.robots.size
    }

    @SuppressLint("SetTextI18n")
    override fun onBindViewHolder(holder: CustomRobotsHolder, position: Int) {

        holder.itemView.title_robot.text = robotsFeed.robots[position].title

        holder.itemView.language_robot.text = robotsFeed.robots[position].language

        holder.itemView.source_robot.text = robotsFeed.robots[position].source
        holder.itemView.source_robot.movementMethod = LinkMovementMethod.getInstance()
        holder.itemView.source_robot.setLinkTextColor(Color.BLUE)

        holder.itemView.link_robot.text = robotsFeed.robots[position].link
        holder.itemView.link_robot.movementMethod = LinkMovementMethod.getInstance()
        holder.itemView.link_robot.setLinkTextColor(Color.BLUE)
    }

}