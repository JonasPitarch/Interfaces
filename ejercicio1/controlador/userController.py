from modelo.usuarioModel import User
from modelo.usersModel import Users


class UserController:
    def __init__(self):
        self.users = Users()
    
    def getUserById(self,id:int)->User:
        usersList = self.users.get_users()
        for user in usersList:
            if(user.id == id):
                return user
        return None
    
    def addUser(self, id, nombre):

        user = User(id,nombre)
        self.users.add_user(user)

