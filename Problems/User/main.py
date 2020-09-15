class User:
    # create the class attributes
    users = []
    n_active = int()

    # create the __init__ method
    def __init__(self, active, user_name):
        self.active = active
        self.user_name = user_name
        if active:
            User.n_active += 1
        User.users.append(self.user_name)
