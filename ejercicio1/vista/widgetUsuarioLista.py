from PyQt6.QtWidgets import QPushButton, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QFrame
from PyQt6.QtCore import pyqtSignal, pyqtSlot, Qt
from PyQt6.QtGui import QMouseEvent

class WidgetUsuarioLista(QWidget):

    # Definir una señal personalizada
    mouseClicked = pyqtSignal(str)
    
    def __init__(self,userId, userName):
        super().__init__()
        self.userId = userId
        self.userName = userName

        # Crear los widgets internos
        self.imagenUsuario  = QLabel(str(self.userId))
        self.imagenUsuario.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nombreUsuario  = QLabel(self.userName)
        self.nombreUsuario.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.botonesLayout  = QVBoxLayout()
        self.botonEditar    = QPushButton('Editar')
        self.botonBorrar    = QPushButton('Borrar')
        self.botonesLayout.addWidget(self.botonEditar)
        self.botonesLayout.addWidget(self.botonBorrar)

        # Configurar el diseño del contenedor
        layout = QHBoxLayout()
        layout.addWidget(self.imagenUsuario, 1)
        layout.addWidget(self.nombreUsuario, 2)
        layout.addLayout(self.botonesLayout, 1)
        frame = QFrame()
        frame.setLayout(layout)
        
        ventanaLayout = QHBoxLayout()
        ventanaLayout.addWidget(frame)

        # Aplicar el diseño al contenedor
        self.setLayout(ventanaLayout)
        self.setFixedHeight(100)
        self.setStyleSheet("background-color: green;")
        
    @pyqtSlot(QMouseEvent)
    def mousePressEvent(self, event: QMouseEvent):
        # Emitir una señal cuando se detecte un clic
        self.mouseClicked.emit(str(self.userId))