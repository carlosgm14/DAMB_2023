import random 
from tabulate import tabulate

#se crea matriz nxn
def crear_matriz(w,y):
    m = list(range(y))
    matriz= [[0 for  j in range (0,W+1)] for i in range (0,y+1)]
    print(tabulate(matriz, headers=m))
    
    return matriz

#se recorre y rellena matriz, se rellena de valores aleatroios 
#para luego rellenar los pacientes y luego los dias 
def rellenar(primera_matriz):
    filas = len(primera_matriz)
    columnas = len(primera_matriz[0])
    re=0
    for f in range(filas):
        
        for c in range(columnas):
            values=["x","0"]
            Crisis = random.choice(values)
            primera_matriz[f][c] = Crisis
            primera_matriz[f][0] = random.randint(1000, 9999)
            
    
    for c in range(columnas):
        primera_matriz[0][c] = "dia " + str(re)
        re = re+1
        primera_matriz[0][0]= "paciente"
        segu=primera_matriz
    return segu 

#encuentra la posicion del paciente
#def find_number(hola, numero):
#    for i in range(len(hola)):
#        for j in range(len(hola[i])):
#            if hola[i][j] == numero:
#                return (i, j)
#    return None

#encuentra la posicion del dia
def find_day(hola, letra):
    for i in range(len(hola)):
        for j in range(len(hola[i])):
            if hola[i][j] == letra:
                return (i, j)
    return None

# numero de x en un dia
def count_x(hola, el_dia):
    count = 0
    for row in hola:
        if row[el_dia] == 'x':
            count += 1
    return count
# numero de x de un paciente
def coco(hola, numero):
    for fila in hola:
       if fila[0] == numero:
           if  'x' in fila:
               coun = fila.count('x')

    return(coun)


#no recorre correctamente el menu en una funcion
ele = 0
while ele != 5:
    print('1.Generar datos')
    print('2.Graficar matriz')
    print('3.numero de crisis al dia')
    print('4.estadistica del paciente')
    print('5.exit')
    print('Elige una opcion')
    ele = int(input())
    if ele==1:
        W=int(input('cuantos dias='))
        y=int(input('cuantos pacientes='))
        primera_matriz=crear_matriz(W,y)
        hola= rellenar(primera_matriz)
    elif ele==2:
        print(tabulate(hola))
    elif ele==3:
        print("Ingrese dia(poner dia 'numero del dia a elejir', ej: dia 1)")
        letra=str(input())
        mol=find_day(hola, letra)
        #print(mol)
        el_dia=mol[1]
        x_count = count_x(hola, el_dia)
        print(f"numero de crisis dia: {x_count}")
    elif ele==4:
        print("Ingresar paciente")
        numero=int(input())
#           fol=find_number(hola, numero)
#            print(fol)
#            el_paciente=fol[0]
        milo=coco(hola, numero)
        print(f"numero de crisis paciente: {milo}")
        porcent1=milo/W
        print(f"valor porcentaje paciente: {porcent1}%")
    elif ele==5:
        print('xd')
        
    
        







