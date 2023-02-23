import pandas as pd
import matplotlib.pyplot as plt 
import os
import numpy as np
import math
#color = list(np.random.choice(range(256), size=3))
#cwd = os.getcwd()
#archivo= cwd +"/ecg_data.csv"
#ecg_data=pd.read_csv(archivo)

#Time = ecg_data['time']
#Signal =ecg_data['signal']

#plt.plot(Time,Signal)
#plt.xlabel('time (s)')
#plt.ylabel('ecg signal (mv)')
#plt.title('Ecg signal over time')
#plt.show()
################################################3
#x=[20,25,30,35,40,45,50]
#y=[102,104,105,107,112,119,124]
#plt.scatter(x,y)
#plt.title("Imc vs azucar en sangre")
#plt.xlabel("IMC")
#plt.ylabel("azucar en sangre")
#plt.show()

#labes = ["cancer de prostata ","cancer de pulmon","cancer de piel","cancer de mama"]
#values = [30,20,43,23]

#plt.bar(labes,values, color=('red','green','yellow','orange'))
#plt.title("frecuencia del cancer")
#plt.xlabel("tipo cancer")
#plt.ylabel("porcentaje cancer")
#plt.show()

#data= np.random.rand(5,5)
#print(data)
#plt.imshow(data,cmap='coolwarm')
#plt.title("titulo")
#plt.xlabel("soy")
#plt.ylabel("un lindo")
#plt.show()

#data=[20,21,23,214,245,346,47,25,1,234,245,23,143,34]
##plt.show()

#labels=["cirugia","radiacion", "quimioterapia", "otros"]
#values=[50,30,15,5]
#plt.pie(values,labels=labels)
#plt.show()


#cwd= os.getcwd()
#archivo= cwd + "/vital_signs.csv"
#vital_signs=pd.read_csv(archivo,index_col='timestamp',parse_dates=True)

#calcular frecuencia promedio por hora

#heart_rate=vital_signs['heart_rate'].resample('1H').mean()
#print(heart_rate)


#cwd= os.getcwd()
#archivo= cwd + "/patient_data.csv"
#patient_data=pd.read_csv(archivo)
#archivo2= cwd + "/population_data.csv"
#population_data=pd.read_csv(archivo2)
#merge_data=pd.merge(patient_data,population_data,on='Zip Code')
#print(merge_data)
#merge_data['Chronic Condition %'] =merge_data['Chronic Condition Count'] / merge_data['Population'] * 100
#print(merge_data)



cwd = os.getcwd()
archivo= cwd +"/ecg_data.csv"
ecg_data=pd.read_csv(archivo)

Time = ecg_data['time']
Signal =ecg_data['signal']

description = ecg_data['signal'].describe()
#print(description)

promedio=np.mean(ecg_data.signal)
#print(promedio)

promedio_dianamico= pd.DataFrame.rolling(ecg_data.signal,window=(100)).mean()#*1.2
#print(promedio_dianamico)
promedio_dianamico= [promedio*1.2 if math.isnan(x) else (x*1.2) for x in promedio_dianamico]
ecg_data['promedio_dinamico']= promedio_dianamico
#print(promedio_dianamico)
#print(ecg_data['signal'].head(50))
#print(ecg_data['signal'].tail(50))

##deteccion de picos
cont=0
rango=[]
maximo_y=[]
maximo_x=[]
for punto in ecg_data.signal :
    if (punto <= ecg_data.promedio_dinamico[cont]) and (len(rango)<1):
        cont+=1
    elif (punto > ecg_data.promedio_dinamico[cont]):
        rango.append(punto)
        cont+=1
    else:
        maximo = max(rango)
        maximo_y.append(maximo)
        maximox=cont-len(rango) + rango.index(maximo)
        maximo_x.append(maximox)

        rango=[]
        cont+=1

cont=0
dist=[]
while cont < len(maximo_x)-1:
    distancia=maximo_x[cont+1]-maximo_x[cont]
    distancia = distancia / 100
    dist.append(distancia)
bpm=60 / np.mean(dist)
print("BPM",round(bpm,1))

 
plt.plot(Time,Signal)
plt.plot(ecg_data.promedio_dinamico,color='red')
plt.scatter(maximo_x,maximo_y,color="blue")
plt.xlabel('time (s)')
plt.ylabel('ecg signal (mv)')
plt.title('Ecg signal over time')
plt.show()

