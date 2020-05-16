package com.example.coronawatch

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

import android.widget.Toast
import com.example.coronawatch.api.RetrofitClient
import kotlinx.android.synthetic.main.activity_sign_up.*

import models.DefaultResponse

import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response


class SingupActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_sign_up)

        singup_btn.setOnClickListener {
            val username = editTextUsername.text.toString().trim()
            val password = editTextPassword.text.toString().trim()
            val email = editTextEmail.text.toString().trim()

            if (username.isEmpty()) {
                editTextUsername.error = "عليك إدخال إسم المستخدم"
                editTextUsername.requestFocus()
                return@setOnClickListener
            }

            if (password.isEmpty()) {
                editTextPassword.error = "عليك إدخال كلمة المرور"
                editTextPassword.requestFocus()
                return@setOnClickListener
            }

            if (email.isEmpty()) {
                editTextEmail.error = "عليك إدخال البريد الإلكتروني"
                editTextEmail.requestFocus()
                return@setOnClickListener
            }
            val roles = listOf<Any>()
            RetrofitClient.instance.comptes(password, username, email)
                .enqueue(object : Callback<DefaultResponse> {
                    override fun onFailure(call: Call<DefaultResponse>, t: Throwable) {
                        Toast.makeText(applicationContext, t.message, Toast.LENGTH_LONG).show()
                    }

                    override fun onResponse(
                        call: Call<DefaultResponse>,
                        response: Response<DefaultResponse>
                    ) {
                        Toast.makeText(applicationContext, response.toString(), Toast.LENGTH_LONG).show()

                    }

                })
            startActivity(Intent(this, MainActivity::class.java))


        }
        singin_link_btn.setOnClickListener {
            startActivity(Intent(this, LoginActivity::class.java))
        }
    }
}

