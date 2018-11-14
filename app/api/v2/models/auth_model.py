# app/api/v2/models/auth_model.py
from ....store_database import conn_db

class Users:
    """Users mode."""

    def __init__(self):
        self.db = conn_db()

    def insert_new_user(self, user_id, username, email, password, role):
        """Insert new user."""
        database = self.db
        curr = database.cursor()
        query = "INSERT INTO users (user_id, username,email, password,user_type) VALUES (%s,%s,%s,%s,%s);"
        curr.execute(query, (user_id, username, email, password, role))
        database.commit()
        curr.close()
        return {"Message": "User created succefully"}

    def get_all_users(self):
        """Get all users."""
        conn = self.db
        curr = conn.cursor()
        query = """SELECT * FROM users;"""
        curr.execute(query)
        data = curr.fetchall()
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
        database = self.db
        try:
            curr = database.cursor()
            query = "UPDATE users SET user_type=%s WHERE user_id=%s;"
            curr.execute(query, (role, user_id))
            database.commit()
            return {"Message": "Category Updated successfully"}
        except Exception as e:
            return {"Message": e}
    
    
    def delete_users(self, user_id):
        """Delete users."""
        database = self.db
        try:
            curr = database.cursor()
            query = "DELETE FROM users WHERE user_id=%s;"
            curr.execute(query, (user_id,))
            database.commit()
            return {"Message": "User Updated successfully"}

        except Exception as e:
            return {"Message": e}
