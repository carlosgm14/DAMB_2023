import sys
from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton
import csv
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):    
        self.setWindowTitle('Ingreso al sistema DABM')
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
        #print("Botón pulsado")
        username = self.edit_username.text()
        password = self.edit_password.text()

        if self.validate_credentials(username, password):
            print('Acceso concedido')
        else:
            print('Acceso denegado')
    
    def validate_credentials(self,username,password):
        with open('usuarios.csv', newline='') as csvfile:
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

    login_window=LoginWindow()
    login_window.show()

    sys.exit(app.exec())