# app/api/v2/models/auth_model.py
from ....store_database import conn_db

class Users:
    """Users mode."""

    def __init__(self):
        self.db = conn_db()
        self.curr = self.db.cursor()

    def insert_new_user(self, user_id, username, email, password, role):
        """Insert new user."""
        query = "INSERT INTO users (user_id, username,email, password,user_type) VALUES (%s,%s,%s,%s,%s);"
        self.curr.execute(query, (user_id, username, email, password, role))
        self.db.commit()
        self.curr.close()
        return {"Message": "User created succefully"}

    def get_all_users(self):
        """Get all users."""
        query = """SELECT * FROM users;"""
        self.curr.execute(query)
        data = self.curr.fetchall()
        all_users = []

        for k, v in enumerate(data):
            user_id, username, email, password, role = v
            users = {"user_id": user_id,
                     "username": username,
                     "email": email,
                     "password": password,
                     "role": role}
            all_users.append(users)
        return all_users

    def update_user(self, user_id, role):
        """Update product category."""
        query = "UPDATE users SET user_type=%s WHERE user_id=%s;"
        self.curr.execute(query, (role, user_id))
        self.db.commit()
        return {"Message": "Category Updated successfully"}
 
    def delete_users(self, user_id):
        """Delete users."""
        query = "DELETE FROM users WHERE user_id=%s;"
        self.curr.execute(query, (user_id,))
        self.db.commit()
        return {"Message": "User Updated successfully"}

