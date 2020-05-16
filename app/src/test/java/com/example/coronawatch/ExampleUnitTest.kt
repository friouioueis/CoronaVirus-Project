package com.example.coronawatch

import com.example.coronawatch.api.RetrofitClient
import models.LoginResponse
import org.junit.Test

import org.junit.Assert.*

/**
 * Example local unit test, which will execute on the development machine (host).
 *
 * See [testing documentation](http://d.android.com/tools/testing).
 */
class ExampleUnitTest {
    @Test
    fun login_test() {
        assertEquals(   "248c591d00accc787b2e72f2e1f",RetrofitClient.instance.login("kaouthar","kaouthar").toString() )
    }





    }


