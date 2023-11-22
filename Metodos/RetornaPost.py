import database_manager

def get_posts(username):
    db = database_manager.SocialMediaDatabaseManager()

    success, posts = db.get_following(username)

    if not success:
        return None

    all_posts = []

    for usuario_seguido in posts:
        success, user_posts = db.get_user_posts(usuario_seguido)

        if success:
            all_posts.extend(user_posts)

    return all_posts
