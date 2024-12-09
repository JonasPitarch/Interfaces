from controlador.userController import UserController
from vista.widgetUsuarioLista import WidgetUsuarioLista
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFrame, QHBoxLayout, QLabel
from PyQt6.QtCore import pyqtSlot, pyqtSignal, Qt

class ListaWidgetUsuario(QWidget):
    
    usuarioSeleccionado = pyqtSignal(str)
    
    def __init__(self, users):
        super().__init__()

        self.users = users
        layout = QVBoxLayout()
        frame = QFrame()
        frame.setLayout(layout)
        
        frameHeader = QFrame()
        layoutHeader = QHBoxLayout()
        idLabel = QLabel('ID')
        idLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        nombreLabel = QLabel('Nombre')
        nombreLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        actionsLabel = QLabel('Actions')
        actionsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutHeader.addWidget(idLabel)
        layoutHeader.addWidget(nombreLabel)
        layoutHeader.addWidget(actionsLabel)
        frameHeader.setLayout(layoutHeader)
        frameHeader.setStyleSheet("background-color: yellow;")
        
        layout.addWidget(frameHeader)
        
        
        for user in self.users:
            userWidget = WidgetUsuarioLista(user.get_id(),user.get_name())
            userWidget.mouseClicked.connect(self.envioSenal)
            layout.addWidget(userWidget)

        layout.addStretch()  # Agrega un espacio extra al final
        
        ventanaLayout = QVBoxLayout()
        ventanaLayout.addWidget(frame)

        # Aplicar el diseño al contenedor
        self.setLayout(ventanaLayout)
        self.setStyleSheet("background-color: cyan;")

    @pyqtSlot(str)
    def envioSenal(self, texto):
        self.usuarioSeleccionado.emit(texto)