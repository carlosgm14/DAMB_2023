import sys
import serial
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QPushButton

class IntensityWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Cambio de intensidad')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        label_intensity = QLabel('Intensidad:')
        layout.addWidget(label_intensity)

        self.slider_intensity = QSlider()
        self.slider_intensity.setOrientation(Qt.Orientation.Vertical)
        self.slider_intensity.setMinimum(0)
        self.slider_intensity.setMaximum(255)
        self.slider_intensity.setValue(128)
        layout.addWidget(self.slider_intensity)

        self.label_voltage = QLabel('Voltaje del sensor: -')
        layout.addWidget(self.label_voltage)

        btn_send = QPushButton('Enviar')
        btn_send.clicked.connect(self.send_intensity)
        layout.addWidget(btn_send)

        btn_read_voltage = QPushButton('Leer voltaje')
        btn_read_voltage.clicked.connect(self.read_voltage)
        layout.addWidget(btn_read_voltage)

        self.setLayout(layout)

        # Conexión con el puerto serial de Arduino
        try:
            self.arduino = serial.Serial('COM14', 9600)
        except:
            print('Error al conectar con Arduino')
            sys.exit()

    def send_intensity(self):
        # Se envía la intensidad seleccionada al Arduino
        intensity = self.slider_intensity.value()
        self.arduino.write(bytes([intensity]))

    def read_voltage(self):
        # Se lee el voltaje del sensor y se muestra en el QLabel correspondiente
        self.arduino.write(b'V')
        voltage = float(self.arduino.readline().decode('utf-8'))
        self.label_voltage.setText(f'Voltaje del sensor: {voltage:.2f}')

    def closeEvent(self, event):
        # Se cierra la conexión con el Arduino al cerrar la ventana
        self.arduino.close()
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    intensity_window = IntensityWindow()
    intensity_window.show()

    sys.exit(app.exec())