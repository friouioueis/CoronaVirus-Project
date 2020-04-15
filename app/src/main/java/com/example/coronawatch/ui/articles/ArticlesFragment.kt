package com.example.coronawatch.ui.articles

import android.graphics.Color
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProviders
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.coronawatch.ArticlesAdapter
import com.example.coronawatch.R
import kotlinx.android.synthetic.main.fragment_articles.*
import kotlinx.android.synthetic.main.fragment_articles.view.*

class ArticlesFragment : Fragment() {

    private lateinit var articlesViewModel: ArticlesViewModel
    lateinit var recyclerViewArticles : RecyclerView
    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
    ): View? {
        articlesViewModel =
                ViewModelProviders.of(this).get(ArticlesViewModel::class.java)
        val root = inflater.inflate(R.layout.fragment_articles, container, false)


         recyclerViewArticles = root.findViewById(R.id.recycler_view_articles) as RecyclerView
        recyclerViewArticles.adapter = ArticlesAdapter()

        return root
    }
}
