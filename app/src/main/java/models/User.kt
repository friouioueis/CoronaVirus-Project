package models

import com.google.gson.annotations.SerializedName

data class User(
    @SerializedName("date_joined")
    val dateJoined: String,
    val email: String,
    val groups: List<Any>,
    var id: Int,
    val infos: Any,
    @SerializedName("is_active")
    val isActive: Boolean,
    @SerializedName("is_admin")
    val isAdmin: Boolean,
    @SerializedName("is_staff")
    val isStaff: Boolean,
    @SerializedName("is_superuser")
    val isSuperuser: Boolean,
    @SerializedName("last_login")
    val lastLogin: String,
    val password: String,
    val roles: List<Any>,
    @SerializedName("user_permissions")
    val userPermissions: List<Any>,
    val username: String
)