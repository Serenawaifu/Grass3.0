class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, email, password):
        if email not in self.users:
            self.users[email] = {'password': password, 'proxies': []}
            return f"User {email} added."
        return f"User {email} already exists."

    def get_user(self, email):
        return self.users.get(email, None)
