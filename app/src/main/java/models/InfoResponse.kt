package models

data class InfoResponse (
    val idInfoPer: Int,
    val nom : String,
    val prenom: String,
    val dateNaissance: String,
    val wilaya: String,
    val idUtilisteurIp: Int

)