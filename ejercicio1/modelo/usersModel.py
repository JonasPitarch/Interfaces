from modelo.usuarioModel import User
from datetime import date

class Users:
    """
    Clase que representa un usuario.
    """

    def __init__(self):
        hoy = date.today()
        self.users:list[User] = [
            User(0,'nombre','email','pass',hoy,True),
            User(1,'nombre1','email1','pass1',hoy,True),
            User(2,'nombre2','email2','pass2',hoy,True)
        ]


    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"

    def to_dict(self):
        litToDic:list[dict[str,any]] = []
        for user in self.users:
            litToDic.append(user.to_dict())
        return litToDic
    
    def get_users(self)->list[User]:
        return self.users
    
    def add_user(self,user:User)->list[User]:
        self.users.append(user)
        return self.users
    
    def delete_user_by_id(self,id:int)->list[User]:
        users = list(filter(lambda user : user.getId() != id , self.get_users()))
        self.users = users