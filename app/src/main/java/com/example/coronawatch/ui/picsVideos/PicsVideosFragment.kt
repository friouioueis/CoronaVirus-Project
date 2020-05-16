package com.example.coronawatch.ui.diagno

import androidx.lifecycle.ViewModelProviders
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup

import com.example.coronawatch.R
class PicsVideosFragment : Fragment() {

    companion object {
        fun newInstance() = PicsVideosFragment()
    }

    private lateinit var picsVideosviewModel: PicsVideosViewModel

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_pics_videos, container, false)
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        picsVideosviewModel = ViewModelProviders.of(this).get(PicsVideosViewModel::class.java)
        // TODO: Use the ViewModel
    }

}
