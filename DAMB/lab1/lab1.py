import random 

from tabulate import tabulate

num= random.randint(0,9999)
##values=["x","0"]
##Crisis = random.choice(values)



matriz_1=[]

def listaAleatorios(n):
      lista = [0]  * n
      for i in range(n):
          lista[i] = random.randint(0, 9999)
      return lista

print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())

aleatorios=listaAleatorios(n)
print(aleatorios)




def crear_matriz(w,y):
    m = list(range(y))
    matriz= [[0 for  j in range (0,W+1)] for i in range (0,y+1)]
    print(tabulate(matriz, headers=m))
    
    return matriz

W=int(input('cuantos dias='))
y=int(input('cuantos pacientes='))
primera_matriz=crear_matriz(W,y)


def rellenar(primea_matriz):
    filas = len(primea_matriz)
    columnas = len(primea_matriz[0])
    re=0
    for f in range(filas):
        for c in range(columnas):
            values=["x","0"]
            Crisis = random.choice(values)
            primea_matriz[f][c] = Crisis
            primea_matriz[f][0] = random.randint(1000, 9999)
            
    
    for c in range(columnas):
        primea_matriz[0][c] = "dia " + str(re)
        re = re+1
        primera_matriz[0][0]= "paciente"
        segu=primera_matriz
    return segu        

crear_matriz(W,y)
hola= rellenar(primera_matriz)
print(tabulate(hola))



print("Ingrese posicion")
numero=int(input())
print("Ingrese posicion d")
letra=str(input())
lista = []



def find_number(hola, numero):
    for i in range(len(hola)):
        for j in range(len(hola[i])):
            if hola[i][j] == numero:
                return (i, j)
    return None


print(find_number(hola, numero))
fol=find_number(hola, numero)
print(fol)
el_paciente=fol[0]
print(el_paciente)

def find_day(hola, letra):
    for i in range(len(hola)):
        for j in range(len(hola[i])):
            if hola[i][j] == letra:
                return (i, j)
    return None

mol=find_day(hola, letra)
print(mol)
el_dia=mol[1]
print('que dia es')
print(el_dia)

#el_dia=fol[1]
#print(el_paciente)

#def n_cas_d(hola,el_dia,con1):
#    filas1 = len(hola)
#    columnas1 = len(hola[0])
#    re=0
#    for f in range(filas1):
#        for c in range(columnas1):
#            if hola[f][el_dia] == '0':
#                con1=con1+1
#               
#    return  con1
#contin=n_cas_d(hola,el_dia,con1)


def count_x(hola, el_dia):
    count = 0
    for row in hola:
        if row[el_dia] == 'x':
            count += 1
    return count
x_count = count_x(hola, el_dia)
print(f"numero de crisis dia: {x_count}")

#def coun(hola, el_paciente):
  #  count1 = 0
 #   for row in el_paciente:
 #       if  hola[row]=='x':
 #           count1 += 1
 #   return count1
#cou = coun(hola, el_paciente)
def coco(hola, numero):
    for fila in hola:
       if fila[0] == numero:
           if '0' in fila or 'x' in fila:
               coun = fila.count('x')

    return(coun)
milo=coco(hola, numero)
print(f"numero de crisis paciente: {milo}")

porcent1=milo/W
print(f"valor porcentaje paciente: {porcent1}%")
porcent2=x_count/y
print(f"Valor porcentaje dia: {porcent2}%")
