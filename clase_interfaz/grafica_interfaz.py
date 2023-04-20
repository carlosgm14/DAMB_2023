import sys
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication,QMainWindow,QSizePolicy,QVBoxLayout, QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class MedicoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gràfica Médica")
        self.setGeometry(100,100,800,600)
        
        #widget para la grafica
        self.grafica_widget = QWidget(self)
        self.setCentralWidget(self.grafica_widget)

        #crear grafica en matplot
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)

        layout = QVBoxLayout(self.grafica_widget)
        layout.addWidget(self.canvas)

        #generar datos
        x = [0,1,2,3,4,5,6,7,8,9]
        y =[78,81,82,83,85,86,87,88,89,90]

        ax = self.fig.add_subplot()
        ax.plot(x,y)
        ax.set_xlabel("Tiempo")
        ax.set_ylabel("Oximetrìa")
        ax.set_title("Evolución del paciente")

        self.canvas.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        self.canvas.updateGeometry()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = MedicoApp()
    ventana.show()

    sys.exit(app.exec())