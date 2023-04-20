import serial
import csv
import time

ser = serial.Serial('COM14', 9600)  # Reemplazar 'COM3' por el puerto serial que esté utilizando
led_pin = 9

# Configuración del archivo CSV
csv_file = open('sensor_data.csv', mode='w', newline='')
fieldnames = ['time_stamp', 'sensor_value']
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
writer.writeheader()

while True:
    try:
        sensor_value = int(ser.readline().strip().decode('utf-8'))
        print('Valor del sensor: ', sensor_value)

        if sensor_value > 750:  
            brightness = 0  
        elif sensor_value > 500:  
            brightness = 64  
        elif sensor_value > 250:  
            brightness = 128  
        else:  
            brightness = 255  

        # Encender el LED con el brillo correspondiente
        arduino_data = str(brightness) + '\n'
        ser.write(arduino_data.encode())

        # Escribir los datos del sensor en el archivo CSV
        time_stamp = time.time()
        writer.writerow({'time_stamp': time_stamp, 'sensor_value': sensor_value})

        time.sleep(0.1)

    except KeyboardInterrupt:
        ser.close()
        csv_file.close()
        break