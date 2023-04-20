
import serial
import csv
import time

ser = serial.Serial("COM14", 9600)
sensor_min = 0
sensor_max = 1023

def write_csv():
    with open('sensor_values.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Minimum Value', sensor_min])
        writer.writerow(['Maximum Value', sensor_max])
def read_sensor():
    # Lee el valor 
    sensor_value = int(ser.readline().decode().strip())
    # Convierte el valor
    sensor_value_normalized = (sensor_value - sensor_min) / (sensor_max - sensor_min)
    # Retorna el valor normalizado
    return sensor_value_normalized

# Loop principal
while True:
    # Lee el valor 
    sensor_value = read_sensor()
    # Controla el brillo del LED 
    led_value = int(sensor_value * 255)
    ser.write(bytes([led_value]))
    time.sleep(0.1)


    

