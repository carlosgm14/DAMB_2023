import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
import csv
#una cambia solo intensidad, la otra muestra el valor del sensor tambien
#from menu_sensor import IntensityWindow  # Importamos la clase IntensityWindow del primer código
from intensidad_y_sensor import IntensityWindow
# la vaentana se traba al cambiar la intensidad despues de un tiempo
# y no conecta bien con el arduino, por lo que cambia solo un momento
#cuando se pide el valor del sensor, este deja de funcionar y se tiene 
#que cerrar la ventana
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        #condicion cambiar ventana
        self.newWindow = None
        self.init_ui()

    def init_ui(self):    
        self.setWindowTitle('Ingreso menu')
        self.setGeometry(100,100,300,200)

        layout = QVBoxLayout()

        label_username = QLabel('Usuario:')
        layout.addWidget(label_username)

        self.edit_username = QLineEdit()
        layout.addWidget(self.edit_username)

        label_password = QLabel('Contraseña:')
        layout.addWidget(label_password)

        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.edit_password)

        btn_ingresar = QPushButton("Ingresar")
        btn_ingresar.clicked.connect(self.auth)
        layout.addWidget(btn_ingresar)

        self.setLayout(layout)
    
    def auth(self):
        #Botón pulsado
        username = self.edit_username.text()
        password = self.edit_password.text()

        if self.validate_credentials(username, password):
            
            print('Acceso concedido')
              # Ocultamos la ventana de login
            #intensity_window = MainWindow()  # Creamos la ventana de control de intensidad
              # Mostramos la ventana de control de intensidad
            if self.newWindow is None:
                self.newWindow = IntensityWindow()
            self.newWindow.show()
            self.hide()
        else:
            print('Acceso denegado')
    
    def validate_credentials(self, username, password):
        with open('lab4/usuarios.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if row[0] == username and row[1] == password:
                    return True
        return False


def load_stylesheet():
    return """
        QWidget {
            background-color: #87CEFA;
            
        }
        QLabel{
            font-size = 14px;
            color: #000080
        }
        QLineEdit{
            background-color : #FFFFFF;
            border: 1px solid #1E90FF;
            padding: 3px;
            font-size: 14px;
        }
        QPushButton{
            background-color: #1E90FF;
            color : #FFFFFF;
            border: 1px solid #1E90FF;
            padding: 5px;
            font-size: 14px;
        }
        QPushButton:hover{
            background-color: #4169E1;
            border: 1px solid #4169E1;
        }
    """


if __name__ == '__main__':
    app = QApplication(sys.argv)

    stylesheet = load_stylesheet()
    app.setStyleSheet(stylesheet)
    
    login_window = LoginWindow()
    login_window.show()
       
    sys.exit(app.exec())