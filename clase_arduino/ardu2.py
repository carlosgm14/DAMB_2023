import serial, time, struct
ard = serial.Serial("COM14",9600)
#time.sleep(2)
#ard.write(b'1')
#ard.close()

#while True:
#    data= input("Introduce ON/OFF/salir ")
#    if data == "SALIR":
#        data=="s"
#    if data == "ON":
#        data=="O"
#    if data == "OFF":
#        data=="F"
#        break
#    else:
#        ard.write(data.encode())

while True:
    data= int(input("Introduce valor 0-100:  "))
    print("brillo:", data, "%")
    valor= int(255*data/100)
    ard.write(struct.pack(">B",valor))
    time.sleep(0.5)



    import serial, time, struct
ard = serial.Serial("COM14",9600)


while True:
    data= int(input("Introduce valor 0-100:  "))
    print("brillo:", data, "%")
    valor= int(255*data/100)
    ard.write(struct.pack(">B",valor))
    time.sleep(0.5) 
with open("csv/valores.csv", "r") as file:
        lectura = csv.reader(file, delimiter= ";")
        for fila in lectura:
            max = float(fila[0])
            min = float(fila[1])


    while (True):
        data = arduino.readline().decode().strip()
        if (data == ''):
            data = max
        sensor = float(data)
        valor = int((max - sensor) * 255 / (max - min))
        print()
        print('El valor luminico es:', data)
        
        if (valor > 255):
            valor = 255
        elif (valor < 0):
            valor = 0
        
        arduino.write(struct.pack(">B",valor))