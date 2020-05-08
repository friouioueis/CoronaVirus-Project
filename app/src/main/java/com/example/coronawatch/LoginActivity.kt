package com.example.coronawatch

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_login.*

class LoginActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)


        login_btn.setOnClickListener {

            startActivity(Intent(this , MainActivity::class.java))
        }


        singup_link_btn.setOnClickListener {
            startActivity(Intent(this , SingupActivity::class.java))
        }
    }
}
