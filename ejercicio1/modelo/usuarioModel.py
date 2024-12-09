from datetime import datetime


class User:
    """
    Clase que representa un usuario.
    """



    def __init__(self, id, username, email, password, created_at, is_active=True):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at
        self.is_active = is_active

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"

    def to_dict(self):
        """
        Convierte la instancia en un diccionario.
        """
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at,
            "is_active": self.is_active
        }
    
    def get_id(self):
        return self.id
    def get_name(self):
        return self.username