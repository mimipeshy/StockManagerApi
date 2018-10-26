users = []


class UserModel:
    all_users = []
    user = []

    def __init__(self, email, password):
        self.email = email
        self.password_hash = password

    def save(self):
        """this saves product data"""
        new_user = {
            "user_id": len(users) + 1,
            "email": self.email,
            "password": self.password_hash,

        }
        users.append(new_user)
