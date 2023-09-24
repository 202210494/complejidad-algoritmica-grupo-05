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

    def remove_user(self, username) -> bool:
        try:
            self.cursor.execute("DELETE FROM users WHERE username = ?", (username,))
            self.conn.commit()
            return True

        except sqlite3.Error:
            return False

    def add_follow_relationship(self, username, username_followed) -> bool:
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

    def remove_follow_relationship(self, username, username_followed) -> bool:
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
