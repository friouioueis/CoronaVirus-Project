package models

data class HealthResponse (
    val idInfoSante: Int ,
    val poids: Double ,
    val temperature: Double ,
    val Rythme_cardiaque: Double ,
    val dateSaisie: String ,
    val idUtilisateurIs: Int
    )

