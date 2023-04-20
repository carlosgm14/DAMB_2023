import serial
import matplotlib.pyplot as plt
from drawnow import drawnow

ser = serial.Serial("COM14",9600)

plt.ion()
fig=plt.figure()

data=[]

def update_graph():
    plt.title("brr")
    plt.plot(data,':ks')


def pausar():
    global paused 
    if event.dbclick:
        paused = not paused
    

x = fig.canvas.mpl_connect('button_press_event', pausar)


while True:
    value=ser.readline().decode().strip()
    data.append(value)

    if len(data) > 50:
        data.pop(0)
    if not paused:
      drawnow(update_graph)
