package com.example.coronawatch

import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.example.coronawatch.api.RetrofitClient
import com.facebook.CallbackManager
import com.facebook.FacebookCallback
import com.facebook.FacebookException
import com.facebook.login.LoginResult
import com.facebook.login.widget.LoginButton

import kotlinx.android.synthetic.main.activity_login.*
import kotlinx.android.synthetic.main.activity_singup.*
import models.LoginResponse
import models.User
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class LoginActivity : AppCompatActivity() {

    private lateinit var login : LoginButton;
    private val callbackManager = CallbackManager.Factory.create()


    companion object{
        lateinit var loginUser: User
        lateinit var token: String
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        login = findViewById(R.id.facebook_button)

        login.registerCallback(callbackManager , object : FacebookCallback<LoginResult> {

            override fun onSuccess(result: LoginResult?) {

                Toast.makeText(applicationContext , "تم الدخول بنجاح" , Toast.LENGTH_SHORT ).show()


                    startActivity(Intent(applicationContext, MainActivity::class.java))

            }

            override fun onCancel() {
                println("cancel")
            }

            override fun onError(error: FacebookException?) {
                println("error")
            }


        }

        )




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

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        callbackManager.onActivityResult(requestCode , resultCode , data)
        super.onActivityResult(requestCode, resultCode, data)
    }
}



