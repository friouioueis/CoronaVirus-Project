package com.example.coronawatch.ui.health

import android.app.Activity
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
import models.DefaultResponse
import models.HealthResponse

import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import java.text.SimpleDateFormat
import java.util.*


class HealthFragment : Fragment() {

    companion object {
        fun newInstance() = HealthFragment()
    }

    private lateinit var viewModel: HealthViewModel

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.health_fragment, container, false)
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        viewModel = ViewModelProviders.of(this).get(HealthViewModel::class.java)


        send.setOnClickListener {
            val poids = editTextPoids.text.toString().trim().toString()
            val temperature = editTextTemperature.text.toString().trim().toString()
            val Rythme_cardiaque = coeur.text.toString().trim().toString()

            val sdf = SimpleDateFormat("yyyy/M/dd hh:mm")
            val dateSaisie = sdf.format(Date())
            val idUtilisateurIs = LoginActivity.loginUser.id
            val token = LoginActivity.token


            if (poids==null) {
                editTextPoids.error = "عليك إدخال وزنك"
                editTextPoids.requestFocus()
                return@setOnClickListener
            }

            if (temperature==null) {
                editTextTemperature.error ="عليك إدخال درجة حرارة جسمك"
                editTextTemperature.requestFocus()
                return@setOnClickListener
            }

            if (Rythme_cardiaque==null) {
                coeur.error = "عليك إدخال معدل نبضات قلبك"
                coeur.requestFocus()
                return@setOnClickListener
            }

            RetrofitClient.instance.sante(token, poids.toDouble(), temperature.toDouble(), Rythme_cardiaque.toDouble(), dateSaisie,id)
                .enqueue(object : Callback<HealthResponse> {
                    override fun onFailure(call: Call<HealthResponse>, t: Throwable) {
                        Toast.makeText(activity, t.message, Toast.LENGTH_LONG).show()
                    }

                    override fun onResponse(
                        call: Call<HealthResponse>,
                        response: Response<HealthResponse>
                    ) {
                        Toast.makeText(activity, response.toString(), Toast.LENGTH_LONG).show()

                    }

                })
            startActivity(Intent(activity?.applicationContext, MainActivity::class.java))


        }
    }

}
