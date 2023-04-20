import csv
import datetime
import time
import os
from tabulate import tabulate
from clases.Paciente import Paciente 
from clases.Sensor import Sensor 

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
                
                print("valor: ",row[0])
                print("Fecha: ",row[1])
             
    elif ele==6:
        print('salida')
