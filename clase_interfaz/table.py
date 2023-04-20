import csv, sys 
from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap

class UserTable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("tabla de usuarios")
        self.setGeometry(100,100,500,500)

        #crear tabla
        self.table= QTableWidget(self)
        self.table.setGeometry(50,50,400,400)
        #leer archivo csv
        with open("usuarios.csv",newline="") as csvfile:
            reader = csv.reader(csvfile,delimiter=",")
            data=[row for row in reader]


            #agregar los datos a la tabla 
            headers= ["nombre","contraseña","perfil"]
            self.table.setColumnCount(len(headers))
            self.table.setHorizontalHeaderLabels(headers)
            self.table.setRowCount(len(data))


            for i,row in enumerate(data):
                for j,item in enumerate(row):
                    self.table.setItem(i,j,QTableWidgetItem(item))

if __name__=="__main__":
    app = QApplication(sys.argv)
    user_table=UserTable()
    user_table.show()

    sys.exit(app.exec())
        