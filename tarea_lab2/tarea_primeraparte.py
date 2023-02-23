import csv
import datetime
import time
from tabulate import tabulate

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
ele = 0
while ele != 5:
    print("Menu")
    print('1.Generar datos paciente')
    print('2.Generar Sensores')
    print('3.Generar datos')
    print('4.Mostrar datos')
    print('5.DAtos guardados')
    print('6.exit')
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
        print("Ingresar paciente")
        #pap='paciente_' + (input('diga paciente=')) 
        paciente.reporte_lecturas()
    elif ele==5:
        
        pri=(input('nombre paciente= '))
        pri1=(input('nombre sensor= '))
        print(pri + '_'+pri1 + '.csv')
        with open(pri + '_'+pri1 + '.csv', "r") as file: #mode r: read
            reader = csv.reader(file)
            for row in reader:
                print(row)
                print("Nombre: ",row[0])
                print("Gènero: ",row[1])
             


    elif ele==6:
        print('salida')
