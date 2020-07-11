package com.example.coronawatch.classes

import java.io.Serializable

class Wilaya(id: Int, nom: String, latitude: Double, longitude: Double) :Serializable {
    var id = id
    var nom = nom
    var latitude = latitude
    var longitude = longitude
}