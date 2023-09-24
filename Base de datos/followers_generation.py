from database_manager import SocialMediaDatabaseManager
import random

db_manager = SocialMediaDatabaseManager()
all_users = db_manager.get_all_users()[1]

for usuario in all_users:
    cantidad_a_seguir = random.randint(0, 50)

    usuarios_a_seguir = random.sample(all_users, cantidad_a_seguir)

    for seguido in usuarios_a_seguir:
        if seguido != usuario:
            db_manager.add_follow_relationship(usuario, seguido)