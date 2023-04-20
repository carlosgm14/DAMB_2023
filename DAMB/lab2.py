
def listaAleatorios(n):
      lista = [0]  * n
      for i in range(n):
          lista[i] = random.randint(0, 9999)
      return lista

print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())

aleatorios=listaAleatorios(n)

def operaciones(hola):
    filas = len(hola)
    columnas = len(hola[0])
    
    for f in range(filas):
        for c in range(columnas):
            gog=lista.append(numero)
            print(gog)
    return gog
dada= operaciones(hola)
print((dada)) 



#crear_matriz(W,y)
print("Ingresar paciente")
numero=int(input())
print("Ingrese dia(poner dia 'numero del dia a elejir', ej: dia 1)")
letra=str(input())


fol=find_number(hola, numero)
print(fol)
el_paciente=fol[0]
print(el_paciente)

mol=find_day(hola, letra)
print(mol)
el_dia=mol[1]
print('que dia es')
print(el_dia)

x_count = count_x(hola, el_dia)
print(f"numero de crisis dia: {x_count}")

milo=coco(hola, numero)
print(f"numero de crisis paciente: {milo}")

porcent1=milo/W
print(f"valor porcentaje paciente: {porcent1}%")
porcent2=x_count/y
print(f"Valor porcentaje dia: {porcent2}%")