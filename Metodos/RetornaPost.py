import database_manager

def get_posts(username):
    db = database_manager.SocialMediaDatabaseManager()

    success, all_users = db.get_all_users()

    if not success:
        return None

    all_posts = {}

    for usuario in all_users:
        success, user_posts = db.get_user_posts(usuario)

        if success:
            sorted_user_posts = sorted(user_posts, key=lambda x: x['fecha'], reverse=True)
            all_posts[usuario] = sorted_user_posts

    return all_posts
