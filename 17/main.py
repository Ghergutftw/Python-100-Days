class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def print_info(self):
        return f'ID = {self.id} \nusername = {self.username} \nfollowers = {self.followers}'

    def follow(self,user):
        self.followers += 1
        user.following += 1


user_1 = User(1, "maria")
user_2 = User(2,"georgiana")
user_1.follow(user_2)
info = user_1.print_info()
print(info)


#