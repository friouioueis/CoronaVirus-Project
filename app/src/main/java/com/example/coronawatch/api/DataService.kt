package com.example.coronawatch.api

import com.example.coronawatch.InfoWilaya
import retrofit2.Call
import retrofit2.http.GET

interface DataService {
    @GET("/Region/stat_regions/") fun get_stats_wilaya(): Call<List<InfoWilaya>>
}