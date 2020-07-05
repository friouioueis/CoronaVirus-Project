package com.example.coronawatch

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.example.coronawatch.api.RetrofitClient

import kotlinx.android.synthetic.main.activity_login.*
import kotlinx.android.synthetic.main.activity_singup.*
import models.LoginResponse
import models.User
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class LoginActivity : AppCompatActivity() {

    companion object{
        lateinit var loginUser: User
        lateinit var token: String
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        login_btn.setOnClickListener {
            val intent = Intent(this, MainActivity::class.java)

            val username = email_login.text.toString().trim()
            val password = password_login.text.toString().trim()

            if (username.isEmpty()) {
                email_login.error = "عليك إدخال إسم المستخدم"
                email_login.requestFocus()
                return@setOnClickListener
            }

            if (password.isEmpty()) {
                password_login.error = "عليك إدخال كلمة المرور"
                password_login.requestFocus()
                return@setOnClickListener
            }

            RetrofitClient.instance.login(username, password)
                .enqueue(object : Callback<LoginResponse> {
                    override fun onFailure(call: Call<LoginResponse>, t: Throwable) {
                        Toast.makeText(applicationContext, t.message, Toast.LENGTH_LONG).show()
                    }

                    override fun onResponse(
                        call: Call<LoginResponse>,
                        response: Response<LoginResponse>

                    )
                    {   if(response.code()==200){

                     loginUser = response.body()!!.user
                        token = response.body()!!.key
                        Toast.makeText(applicationContext, "لقد تم الدخول بنجاح", Toast.LENGTH_LONG).show()
                        startActivity(intent)
                    } else{
                        Toast.makeText(applicationContext, "خاطئ", Toast.LENGTH_LONG).show()
                    }
                    }
                })



            singup_link_btn.setOnClickListener {
                startActivity(Intent(this, SingupActivity::class.java))
            }
        }
    }
}



