import database_manager

def amigos_en_comun(username):
    db = database_manager.SocialMediaDatabaseManager()

    success, following = db.get_following(username)

    if not success:
        return None

    amigos_en_comun = {}

    for usuario_seguido in following:
        success, amigos_usuario_seguido = db.get_following(usuario_seguido)

        if success:
            amigos_en_comun[usuario_seguido] = list(set(following) & set(amigos_usuario_seguido))

    return amigos_en_comun
