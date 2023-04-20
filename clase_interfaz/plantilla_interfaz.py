import sys
from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Elementos de una interfaz")
        self.setGeometry(100,100,500,500)

        #insertar imagen
        self.label_image = QLabel(self)
        self.label_image.setGeometry(50,50,225,225)
        pixmap = QPixmap("logo.png")
        self.label_image.setPixmap(pixmap)

        #crear un menu de selección (Combobox)
        self.label_combo = QLabel("Día de la semana",self)
        self.label_combo.setGeometry(50,280,100,20)
        self.combo_dias = QComboBox(self)
        self.combo_dias.setGeometry(50,310,100,20)
        self.combo_dias.addItems(["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"])

        #Crear grupo de botones de opción para el género
        self.label_radio = QLabel("Género",self)
        self.label_radio.setGeometry(50,325,100,20)
        self.radio_masculino = QRadioButton("Masculino",self)
        self.radio_masculino.setGeometry(50,340,100,20)
        self.radio_femenino = QRadioButton("Femenino",self)
        self.radio_femenino.setGeometry(50,360,100,20)

        #Crear casillas de verificación
        self.label_checkbox = QLabel("salud:",self)
        self.label_checkbox.setGeometry(250,270,100,20)
        self.checkbox_diabetes =QCheckBox("Diabetes",self)
        self.checkbox_diabetes.setGeometry(250,290,100,20)
        self.checkbox_hipertencion =QCheckBox("hipertencion",self)
        self.checkbox_hipertencion.setGeometry(250,310,100,20)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    #stylesheet = load_stylesheet()
    #app.setStyleSheet(stylesheet)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())




