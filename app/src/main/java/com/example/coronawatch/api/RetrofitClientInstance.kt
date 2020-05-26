package com.example.coronawatch.api

import android.content.Context
import android.content.SharedPreferences
import okhttp3.Interceptor
import okhttp3.OkHttpClient
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.converter.moshi.MoshiConverterFactory

object RetrofitClientInstance {
    private lateinit var retrofit: Retrofit
    private const val BASE_URL = "https://a471c202.ngrok.io"





    private val okHttpClient = OkHttpClient.Builder().addInterceptor(Interceptor {
            chain: Interceptor.Chain ->
        val request = chain.request().newBuilder().addHeader("Authorization" , "Token 5dfd1c7e93af18c660fa6b297999bb5c3b0e9e39").build()
        return@Interceptor chain.proceed(request)
    })

    val retrofitInstance: Retrofit
        get() {
            retrofit = Retrofit.Builder()
                .baseUrl(BASE_URL).client(okHttpClient.build())
                .addConverterFactory(MoshiConverterFactory.create())
                .build()
            return retrofit
        }
}