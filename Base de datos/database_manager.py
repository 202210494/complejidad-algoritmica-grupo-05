import sqlite3
from datetime import date


class SocialMediaDatabaseManager:
    def __init__(self, database_name="social_media.db"):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def add_user(
        self,
        username: str,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        date_of_birth: date,
        country: str,
        phone_number: str,
    ) -> bool:
        """
        Agrega un usuario a la base de datos de usuarios.

        Args:
            username (str): Nombre de usuario.
            email (str): Email del usuario.
            password (str): Contraseña del usuario.
            first_name (str): Nombre del usuario.
            last_name (str): Apellido del usuario.
            date_of_birth (date): Fecha de nacimiento del usuario.
            country (str): País del usuario.
            phone_number (str): Número de teléfono del usuario.

        Returns:
            bool: Devuelve True si la operación tuvo éxito, False en caso contrario.
        """
        try:
            self.cursor.execute(
                """
                    INSERT INTO users (username, email, password, first_name, last_name, date_of_birth, country, phone_number)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,  # noqa: E501
                (
                    username,
                    email,
                    password,
                    first_name,
                    last_name,
                    date_of_birth,
                    country,
                    phone_number,
                ),
            )
            self.conn.commit()
            return True

        except sqlite3.IntegrityError:
            return False

    def remove_user(self, username: str) -> bool:
        """
        Elimina un usuario de la base de datos de usuarios.

        Args:
            username (str): Username del usuario que se quiere eliminar de la base de datos.

        Returns:
            bool: Devuelve True si la operación tuvo éxito, False en caso contrario.
        """
        try:
            self.cursor.execute("DELETE FROM users WHERE username = ?", (username,))
            self.conn.commit()
            return True

        except sqlite3.Error:
            return False

    def get_all_users(self) -> tuple[bool, list[str]]:
        """
        Devuelve una lista con todos los usernames de los usuarios registrados.

        Returns:
            tuple[bool, list[str]]: Devuelve una tupla con un booleano que indica si la operación tuvo éxito y una lista con los usernames de los usuarios.
        """
        try:
            self.cursor.execute("SELECT username FROM users")
            all_users = [row[0] for row in self.cursor.fetchall()]
            return True, all_users

        except sqlite3.Error:
            return False, []

    def add_follow_relationship(self, username: str, username_followed: str) -> bool:
        """
        Agrega una relación de follow de username a username_followed

        Args:
            username (str): Usuario que quiere seguir a username_followed.
            username_followed (str): Usuario el cuál va a ser seguido por username.

        Returns:
            bool: Devuelve True si la operación tuvo éxito, False en caso contrario.
        """
        try:
            self.cursor.execute(
                """
                INSERT INTO user_followers (user, user_followed)
                VALUES (?, ?)
            """,
                (username, username_followed),
            )

            self.conn.commit()
            return True

        except sqlite3.Error:
            return False

    def remove_follow_relationship(self, username: str, username_followed: str) -> bool:
        """
        Elimina la relación de follow entre username y username_followed
        Si no existe la relación, no hace nada.

        Args:
            username (str): Usuario que desea eliminar la relación de follow.
            username_followed (str): Usuario al que se `username` quiere dejar de seguir.

        Returns:
            bool: Devuelve True si la operación tuvo éxito, False en caso contrario.
        """
        try:
            self.cursor.execute(
                """
                DELETE FROM user_followers
                WHERE user = ? AND user_followed = ?
            """,
                (username, username_followed),
            )

            self.conn.commit()
            return True

        except sqlite3.Error:
            return False

    def get_following(self, username: str) -> tuple[bool, list[str]]:
        """
        Este método recibe como parámetro un username y devuelve
        una lista con todos los usuarios que ese usuario sigue.

        Args:
            username (str): Usuario del que se quieren conocer los usuarios que sigue.

        Returns:
            tuple[bool, list[str]]: Devuelve una tupla con un booleano que indica si la operación tuvo éxito y una lista con los usernames de los usuarios que sigue.
        """
        try:
            self.cursor.execute(
                """
                SELECT user_followed
                FROM user_followers
                WHERE user = ?
            """,
                (username,),
            )
            following = [row[0] for row in self.cursor.fetchall()]
            return True, following

        except sqlite3.Error:
            return False, []

    def get_followers(self, username: str) -> tuple[bool, list[str]]:
        """
        Este método recibe como parámetro un username y devuelve
        una lista con todos los usuarios que siguen a ese usuario.

        Args:
            username (str): Usuario del que se quieren conocer los seguidores.

        Returns:
            tuple[bool, list[str]]: Devuelve una tupla con un booleano que indica si la operación tuvo éxito y una lista con los usernames de los seguidores.
        """
        try:
            self.cursor.execute(
                """
                SELECT user
                FROM user_followers
                WHERE user_followed = ?
            """,
                (username,),
            )
            followers = [row[0] for row in self.cursor.fetchall()]
            return True, followers

        except sqlite3.Error:
            return False, []
