import csv
import datetime
import time
from tabulate import tabulate
import os
class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def registrar_lectura(self, paciente, valor):
        filename = paciente + '_' + self.nombre + '.csv'
        with open(filename, 'a', newline='') as file:#disponer del archivo creado, se agraga consecutivamente 
            writer = csv.writer(file)
            writer.writerow([valor, datetime.datetime.now()])#fecha y hora

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
            print(('Lecturas del sensor ' + sensor.nombre))
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    reader = csv.reader(file)
                    for rocw in reader:
                       print(row)
            else:
                print(f"El archivo {filename} no existe.")

                
                
ele = 0
while ele != 5:
    print("Menu")
    print('1.Generar datos paciente')
    print('2.Generar Sensores')
    print('3.generar datos')
    print('4.mostrar datos')
    print('5.exit')
    print('Elige una opcion')
    ele = int(input())
    if ele==1:
        n=(input('Nombre del paciente='))
        e=(input('Enferemedad del paciente='))
    elif ele==2:
        s1=(input('nombre sensor 1='))
        s2=(input('nombre sensor 2='))
        sensor1 = Sensor(s1)
        sensor2 = Sensor(s2)
        paciente = Paciente(n,e,  [sensor1, sensor2])

        

    elif ele==3:
        print("Ingrese valor del sensor1")
        vs1=(input('valor sensor 1='))
        print("Ingrese valor del sensor2")
        vs2=(input('valor sensor 2='))
        paciente.registrar_lecturas([vs1, vs2])


    elif ele==4:
        filename = input("Ingrese el nombre del archivo CSV a leer: ")
        paciente.reporte_lecturas(filename)
    elif ele==5:
        print('xd')