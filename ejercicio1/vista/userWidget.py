from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QLineEdit
from PyQt6.QtCore import pyqtSlot
from controlador.userController import UserController

class UserWidget(QWidget):
    def __init__(self, usercontroller:UserController):
        super().__init__()
        uic.loadUi("ejercicios_7/ejercicio1/vista/userWidgetView.ui", self)  # Carga la interfaz en esta clase
        self.idWidget = self.findChild(QLineEdit, 'idEdit')
        self.nombreWidget = self.findChild(QLineEdit, 'nombreEdit')
        self.setStyleSheet("background-color: blue;")
        self.usercontroller = usercontroller
    
    

    def addUser(self):
        id = self.idWidget.text()
        nombre=self.nombreWidget.text()
        user = User(id,nombre, "Ana", "pruebas","sadabdoba")
        self.usercontroller.addUser
        self.addUser(user)




    def actualizaDatos(self, id:int, nombre:str):
        self.idWidget.setText(str(id))
        self.nombreWidget.setText(str(nombre))
        print(f'id: {id}, nombre: {nombre}')