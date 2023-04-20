import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QPushButton
import serial

class IntensityWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Cambio de intensidad')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        label_intensity = QLabel('Intensidad:')
        layout.addWidget(label_intensity)

        self.slider_intensity = QSlider()
        self.slider_intensity.setOrientation(Qt.Orientation.Vertical)
        self.slider_intensity.setMinimum(0)
        self.slider_intensity.setMaximum(255)
        self.slider_intensity.setValue(128)
        layout.addWidget(self.slider_intensity)

        btn_send = QPushButton('Enviar')
        btn_send.clicked.connect(self.send_intensity)
        layout.addWidget(btn_send)

        self.setLayout(layout)
        

        # Conexión Arduino
        try:
            self.arduino = serial.Serial('COM14', 9600)
        except:
            print('Error al conectar con Arduino')
            sys.exit()

    def send_intensity(self):
        # La intensidad se envia con el valor de la barra 
        intensity = self.slider_intensity.value()
        #self.arduino.write(f'{intensity}\n'.encode())
        self.arduino.write(intensity.to_bytes(1, 'big'))

    def closeEvent(self, event):
        self.arduino.close()
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    intensity_window = IntensityWindow()
    intensity_window.show()

    sys.exit(app.exec()) 