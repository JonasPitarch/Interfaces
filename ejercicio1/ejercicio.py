import sys

from controlador.userController import UserController
from vista.listaWidgetsusuario import ListaWidgetUsuario
from vista.userWidget import UserWidget
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel,QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import pyqtSlot

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.userController = UserController()
        self.userWidget = UserWidget(self.userController)
        self.setStyleSheet("background-color: orange;")
        self.resize(1920,1080)

        users = self.userController.users.get_users()
        listaWidgetUsuario = ListaWidgetUsuario(users)

        central_widget = QWidget()  # Widget que servirá como contenedor central
        layout = QHBoxLayout()  # Diseño vertical para organizar los widgets


        listaWidgetUsuario.usuarioSeleccionado.connect(self.usuarioSeleccionado)


        layout.addWidget(listaWidgetUsuario,1)
        layout.addWidget(self.userWidget,1)

        # Configurar el widget central con el diseño
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)  # Establecer el widget central en la ventana principal
    
    @pyqtSlot(str)
    def usuarioSeleccionado(self, id):
        user = self.userController.getUserById(int(id))
        self.userWidget.actualizaDatos(user.id, user.username) 
        self.userWidget.update()
        print('nuevo')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())