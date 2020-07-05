package com.example.coronawatch.api

import models.DefaultResponse
import models.HealthResponse
import models.InfoResponse
import models.LoginResponse

import retrofit2.Call
import retrofit2.http.Field
import retrofit2.http.FormUrlEncoded
import retrofit2.http.Header
import retrofit2.http.POST


interface Api {
    @FormUrlEncoded
    @POST("Utilisateurs/gestionComptes/comptes/")
    fun comptes(

        @Field("password") password: String,
        @Field("username") username: String,
        @Field("email") email: String


    ): Call<DefaultResponse>

    @FormUrlEncoded
    @POST("Utilisateurs/rest-auth/login/")
    fun login(
        @Field("password") password: String,
        @Field("username") username: String
    ): Call<LoginResponse>


    @FormUrlEncoded
    @POST("/Sante/info_sante/")
    fun sante(
        @Header("Autorization") token :String,
        @Field("poids") poids: Double,
        @Field("temperature") temperature: Double,
        @Field("Rythme_cardiaque") Rythme_cardiaque: Double,
        @Field("dateSaisie") dateSaisie: String,
        @Field("idUtilisateurIs") idUtilisateurIs: Int
    ): Call<HealthResponse>


    @FormUrlEncoded
    @POST("/Utilisateurs/gestionComptes/infos/")
    fun info(

        @Field("nom") nom: String,
        @Field("prenom") prenom: String,
        @Field("dateNaissance") dateNaissance: String,
        @Field("wilaya") wilaya: String,
        @Field("idUtilisateurIp") idUtilisateurIp: Int
    ): Call<InfoResponse>
}

