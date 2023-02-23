import csv
with open('patient_records.csv', "r") as file:  
    reader = csv.reader(file,delimiter=";")
    next(reader)
    for row in reader:
        print("nombre",row[0])
        print("genero",row[1])
        print("edad",row[2])
        print("enfermedad",row[3])
        print("/n")

        