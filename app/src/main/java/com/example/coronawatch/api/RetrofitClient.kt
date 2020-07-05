package com.example.coronawatch.api

import android.provider.Settings.Global.getString
import android.util.Base64
import androidx.core.content.res.TypedArrayUtils.getText
import com.example.coronawatch.R
import com.example.coronawatch.baseUrl
import com.example.coronawatch.globalToken
import okhttp3.Interceptor
import okhttp3.OkHttpClient
import okhttp3.internal.platform.android.AndroidSocketAdapter
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.converter.moshi.MoshiConverterFactory

object RetrofitClient {

    private const val BASE_URL = "$baseUrl/Utilisateurs/"

    private val okHttpClient = OkHttpClient.Builder()
        .addInterceptor { chain ->
            val original = chain.request()
            val requestBuilder = original.newBuilder()

                .method(original.method, original.body)
            val request = requestBuilder.build()
            chain.proceed(request)
        }.build()

            val instance: Api by lazy{
                val retrofit = Retrofit.Builder()
                    .baseUrl(BASE_URL)
                    .addConverterFactory(GsonConverterFactory.create())
                    .client(okHttpClient)
                    .build()
                    retrofit.create(Api::class.java)
            }

}


object RetrofitClientStats {
    private lateinit var retrofit: Retrofit
    private const val BASE_URL = baseUrl





    private val okHttpClient = OkHttpClient.Builder().addInterceptor(Interceptor {
            chain: Interceptor.Chain ->
        val request = chain.request().newBuilder().addHeader("Authorization" , "Token $globalToken").build()
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