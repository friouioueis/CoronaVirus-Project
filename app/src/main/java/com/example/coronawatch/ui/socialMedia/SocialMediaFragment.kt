package com.example.coronawatch.ui.socialMedia

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProviders
import com.example.coronawatch.R
class SocialMediaFragment : Fragment() {

    private lateinit var socialMediaViewModel: SocialMediaViewModel

    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
    ): View? {
        socialMediaViewModel =
                ViewModelProviders.of(this).get(SocialMediaViewModel::class.java)
        val root = inflater.inflate(R.layout.fragment_social_media, container, false)
        val textView: TextView = root.findViewById(R.id.text_gallery)
        socialMediaViewModel.text.observe(viewLifecycleOwner, Observer {
            textView.text = it
        })
        return root
    }
}
