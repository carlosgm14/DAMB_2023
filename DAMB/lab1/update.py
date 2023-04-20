import csv 

update_records=[]
with open('patient_records.csv', "r") as file:  
    reader = csv.reader(file,delimiter=";")
    header = next(reader)
    nombre = input("nombre del paciente que desea actualizar")
    x=0
    for row in reader :
        if row[0]== nombre:
            row[1]==input("ingresa genero")
            row[2]==input("ingrese edad")
            row[3]==input("ingrese enfermedad")
        else:
            x=1
        update_records.append(row)
if x==1:
            print("no se encuentra paciente ")
            x=0
        
           
       
        

with open('patient_records.csv', "w", newline="") as file:  
    writer=csv.writer(file, delimiter=";")
    writer.writerow(header)
    writer.writerows(update_records)
   
