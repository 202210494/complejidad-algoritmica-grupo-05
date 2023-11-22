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

    def get_user_info(self, username: str) -> tuple[bool, dict]:
        """
        Este método recibe como parámetro un username y devuelve
        un diccionario con toda la información del usuario.

        Args:
            username (str): Usuario del que se quiere obtener la información.

        Returns:
            tuple[bool, dict]: Devuelve una tupla con un booleano que indica si la operación tuvo éxito y un diccionario con toda la información del usuario.
        """
        try:
            self.cursor.execute(
                """
                SELECT *
                FROM users
                WHERE username = ?
            """,
                (username,),
            )
            user_info = self.cursor.fetchone()

            return True, dict(
                zip(
                    [
                        "username",
                        "email",
                        "password",
                        "first_name",
                        "last_name",
                        "date_of_birth",
                        "country",
                        "phone_number",
                    ],
                    user_info[1:],
                )
            )

        except:  # noqa: E722
            return False, {}

    def get_user_count(self) -> tuple[bool, int]:
        """
        Este método devuelve el número de usuarios registrados en la base de datos.

        Returns:
            tuple[bool, int]: Devuelve una tupla con un booleano que indica si la operación tuvo éxito y un entero con el número de usuarios registrados.
        """
        try:
            self.cursor.execute("SELECT COUNT(*) FROM users")
            user_count = self.cursor.fetchone()[0]
            return True, user_count

        except sqlite3.Error:
            return False, 0

    def add_post(
        self,
        username: str,
        content: str,
    ) -> bool:
        """
        Agrega un post a la base de datos.

        Args:
            username (str): Username del usuario que publica el post.
            content (str): Contenido del post.

        Returns:
            bool: Devuelve True si la operación tuvo éxito, False en caso contrario.
        """
        try:
            self.cursor.execute(
                """
                INSERT INTO posts (user, content)
                VALUES (?,?)
            """,
                (username, content),
            )

            self.conn.commit()
            return True

        except sqlite3.Error:
            return False

    def get_user_posts(self, username: str) -> tuple[bool, list[dict]]:
        """
        Devuelve una lista con todos los posts de un usuario.

        Args:
            username (str): Username del usuario del que se quieren obtener los posts.

        Returns:
            tuple[bool, list[dict]]: Devuelve una tupla con un booleano que indica si la operación tuvo éxito y una lista con los posts del usuario.
        """
        try:
            self.cursor.execute(
                """
                SELECT content, date_posted
                FROM posts
                WHERE user =?
            """,
                (username,),
            )
            posts = [
                dict(zip(["content", "date_posted"], post))
                for post in self.cursor.fetchall()
            ]
            return True, posts

        except sqlite3.Error:
            return False, []

    def get_user_by_substring(self, substring: str) -> tuple[bool, list[str]]:
        """
        Devuelve una lista con todos los usernames que comienzan con un substring.

        Args:
            substring (str): Substring que los usernames deben comenzar con.

        Returns:
            tuple[bool, list[str]]: Devuelve una tupla con un booleano que indica si la operación tuvo éxito y una lista con los usernames que comienzan con el substring.
        """
        try:
            self.cursor.execute(
                """
                SELECT username
                FROM users
                WHERE username LIKE?
            """,
                (f"{substring}%",),
            )
            users = [row[0] for row in self.cursor.fetchall()]
            return True, users

        except sqlite3.Error:
            return False, []
