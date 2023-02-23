import csv

patient_records=[["juan perez", "hombre",30,"Enfermedad Cardiaca"], 
                 ["lina alvares","mujer",25,"sana"],
                 ["valentina vargas","mujer",26,"diabetes"]]

with open("patient_records.csv","w", newline="") as file:
  writer=csv.writer(file ,delimiter=  ";")
  writer.writerow(["nombre","genero","edad","enfermedad"])
  writer.writerows (patient_records)
