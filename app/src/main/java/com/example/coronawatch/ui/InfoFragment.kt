package com.example.coronawatch.ui

import android.content.Intent
import androidx.lifecycle.ViewModelProviders
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import com.example.coronawatch.LoginActivity
import com.example.coronawatch.MainActivity

import com.example.coronawatch.R
import com.example.coronawatch.api.RetrofitClient
import kotlinx.android.synthetic.main.health_fragment.*
import kotlinx.android.synthetic.main.health_fragment.send
import kotlinx.android.synthetic.main.info_fragment.*
import models.HealthResponse
import models.InfoResponse
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import java.text.SimpleDateFormat
import java.util.*

class InfoFragment : Fragment() {

    companion object {
        fun newInstance() = InfoFragment()
    }

    private lateinit var viewModel: InfoViewModel

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.info_fragment, container, false)
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        viewModel = ViewModelProviders.of(this).get(InfoViewModel::class.java)
        send.setOnClickListener {
            val nom = nom.text.toString().trim().toString()
            val prenom = prenom.text.toString().trim().toString()
            val dateNaissance = dateNaissance.text.toString().trim().toString()
            val idUtilisateurIp = LoginActivity.loginUser.id





            RetrofitClient.instance.info(nom.toString(), prenom.toString(), dateNaissance.toString(), wilaya.toString(), idUtilisateurIp)
                .enqueue(object : Callback<InfoResponse> {
                    override fun onFailure(call: Call<InfoResponse>, t: Throwable) {
                        Toast.makeText(activity, t.message, Toast.LENGTH_LONG).show()
                    }

                    override fun onResponse(
                        call: Call<InfoResponse>,
                        response: Response<InfoResponse>
                    ) {
                        Toast.makeText(activity, response.toString(), Toast.LENGTH_LONG).show()

                    }

                })
            startActivity(Intent(activity?.applicationContext, MainActivity::class.java))


        }
    }

}

