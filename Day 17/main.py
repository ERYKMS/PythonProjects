class User:
    def __init__(self,user_id,user_name):
        self.id=user_id
        self.name=user_name
        self.followers=0
        self.following=0

    def follow(self,user):
        user.followers +=1
        self.following +=1



user_1 =User(5,"angela")
print(user_1.name)
user_2=User(8,"jack")
print(user_2.name)