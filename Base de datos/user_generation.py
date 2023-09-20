from faker import Faker

from database_manager import SocialMediaDatabaseManager

# Inicializar clases
db_manager = SocialMediaDatabaseManager()
fake = Faker()

# Agregar 1500 usuarios a la base de datos
for _ in range(1500):
    username = fake.unique.user_name()
    email = f"{username}@gmail.com"
    password = fake.password()
    first_name = fake.first_name()
    last_name = fake.last_name()
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=80)
    country = fake.country()
    phone_number = fake.phone_number()

    db_manager.add_user(
        username,
        email,
        password,
        first_name,
        last_name,
        date_of_birth,
        country,
        phone_number,
    )
