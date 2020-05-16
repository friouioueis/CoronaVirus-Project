package com.example.coronawatch.api

import models.DefaultResponse
import models.LoginResponse

import retrofit2.Call
import retrofit2.http.Field
import retrofit2.http.FormUrlEncoded
import retrofit2.http.POST


interface Api {
    @FormUrlEncoded
    @POST("gestionComptes/comptes/")
    fun comptes(

        @Field("password") password: String,
        @Field("username") username: String,
        @Field("email") email: String


    ): Call<DefaultResponse>

    @FormUrlEncoded
    @POST("rest-auth/login/")
    fun login(
        @Field("password") password: String,
        @Field("username") username: String
    ): Call<LoginResponse>

}


