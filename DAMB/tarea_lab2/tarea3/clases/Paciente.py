import csv
import datetime
import time
from tabulate import tabulate

class Paciente:
    def __init__(self, nombre, patologia, sensores=[]):
        self.nombre = nombre
        self.patologia = patologia
        self.sensores = sensores
    
    def registrar_lecturas(self, valores=[]):
        i = 0
        for sensor in self.sensores:
            sensor.registrar_lectura(self.nombre, valores[i])
            i+=1#guardar valores 
    
    def reporte_lecturas(self):
        print(('Reporte de lecturas del paciente ' + self.nombre))
        print(('Patología: ' + self.patologia))
        for sensor in self.sensores:
            #nom=(input('Nombre del paciente='))
            #sen=(input('Nombre del sensor='))
            #filename = nom + '_' + sen + '.csv'
            #print(('Lecturas del sensor ' + sen))
            filename = self.nombre + '_' + sensor.nombre + '.csv'
            print(('Lecturas del sensor ' + sensor.nombre))
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)