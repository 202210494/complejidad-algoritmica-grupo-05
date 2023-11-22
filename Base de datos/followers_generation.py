import random

from database_manager import SocialMediaDatabaseManager

db_manager = SocialMediaDatabaseManager()
all_users = db_manager.get_all_users()[1]


def generar(max_follows: int = 50) -> bool:
    try:
        for usuario in all_users:
            cantidad_a_seguir = random.randint(0, max_follows)

            usuarios_a_seguir = random.sample(all_users, cantidad_a_seguir)

            for seguido in usuarios_a_seguir:
                if seguido != usuario:
                    db_manager.add_follow_relationship(usuario, seguido)
        return True

    except:  # noqa: E722
        return False
