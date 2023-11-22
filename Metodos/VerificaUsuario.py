import database_manager

def obtener_info_usuario(username):
    db = database_manager.SocialMediaDatabaseManager()

    success, user_info = db.get_user_info(username)

    if success:
        return {
            "username": user_info["username"],
            "email": user_info["email"],
            "first_name": user_info["first_name"],
            "last_name": user_info["last_name"],
            "date_of_birth": user_info["date_of_birth"],
            "country": user_info["country"],
            "phone_number": user_info["phone_number"],
        }
    else:
        return None
