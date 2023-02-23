import csv
import datetime
import time
import os
from tabulate import tabulate
class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def registrar_lectura(self, paciente, valor):
        filename = paciente + '_' + self.nombre + '.csv'
        with open(filename, 'a', newline='') as file:#disponer del archivo creado, se agraga consecutivamente 
            writer = csv.writer(file)
            writer.writerow([valor, datetime.datetime.now()])#fecha y hora
