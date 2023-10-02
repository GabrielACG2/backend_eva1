from ProductoTecnologico import ProductoTecnologico
from Consola import Consola
from Tv import Tv
from Scoter import Scoter
from Bicicleta import Bicicleta

def menu():
    print("Escoja lo que desea agregar o cotizar")
    print("1. Registrar TV")
    print("2. Registrar Consola")
    print("3. Registrar Bicicleta")
    print("4. Registrar Scooter")
    print("5. Mostrar productos registrados")
    print("6. Salir")






lista_tvs = []
lista_consolas = []
lista_scooters = []
lista_bicicleta= []


def registrar_tv(lista_tvs):
    print("Registro de TV:")
    marca = input("Ingrese la marca del TV: ")
    voltaje = int(input("Ingrese el voltaje del TV: "))
    precio = float(input("Ingrese el precio del TV: "))
    eficiencia = input("Ingrese la eficiencia del TV (A, B, C, D, E, F): ")
    tamaño = float(input("Ingrese el tamaño del TV en pulgadas: "))

    if voltaje < 0 or precio < 0 or tamaño < 0:
        print("Valores inválidos. Intente nuevamente.")
        return

    tv = Tv(tamaño, marca, voltaje, precio, eficiencia)
    lista_tvs.append(tv)
    print("TV registrado exitosamente.")
    




def registrar_consola(mostrarconsola):
    marca = input("Ingrese la marca de la Consola: ")
    voltaje = input("Ingrese un voltaje de la Consola: ")
    eficiencia = input("Ingrese el nivel de eficiencia (A, B, C, D, E o F) de la Consola: ")
    precio = float(input("Ingrese un valor de la Consola: "))
    nombreConsola = input("Ingrese un nombre de la Consola: ")
    version = input("Ingrese la versión de la Consola (Lite o otro): ")
    consola = Consola(voltaje, precio, eficiencia, marca, nombreConsola, version)
    mostrarconsola.append(consola)
    print("Registrado!!!!")





def registrar_scooter(lista_scooters):
    print("Registro de Scooter:")
    aro = float(input("Ingrese tamaño del aro: "))
    velocidad = float(input("Ingrese velocidad (km/h): "))
    peso = float(input("Ingrese peso del scooter (kg): "))
    marca = input("Ingrese la marca del scooter: ")
    voltaje = int(input("Ingrese el voltaje del scooter: "))
    precio = float(input("Ingrese el precio del scooter: "))
    eficiencia = input("Ingrese la eficiencia del scooter (A, B, C, D, E, F): ")
    if voltaje < 0 or precio < 0 or aro < 0 or velocidad < 0 or peso < 0:
        print("Valores inválidos. Intente nuevamente.")
        return

    scooter = Scoter(aro, velocidad, peso, marca, voltaje, precio, eficiencia)
    lista_scooters.append(scooter)
    print("Scooter registrado exitosamente.")






def registrar_bicicleta(lista_bicicleta):
    marca = input("Ingrese la marca de la Bici: ")
    aro = input("Ingrese el aro de la Bicii: ")
    peso = float(input("Ingrese el peso en kg de la Bici: ")) 
    precio = float(input("Ingrese el valor de la Bici: "))  
    costodespachobase = float(input("Ingrese el costo de despacho base de la Bici: "))  
    bicicleta = Bicicleta(aro, peso, precio, marca,costodespachobase)
    lista_bicicleta.append(bicicleta)
    print("Bici Registrada!")





def mostrar_productos_registrados():
    print("Cosas Ingresadas")
    for tv in lista_tvs:
        print("Televisores")
        print(tv.marca)
        print(tv.voltaje)
        print(tv.eficiencia)
        print(tv.precio)
        print(tv.get_tamano())
    for consola in lista_consolas:
        print("Consolas")
        print(consola.marca)
        print(consola.voltaje) 
        print(consola.eficiencia) 
        print(consola.precio) 
    for scooter in lista_scooters:
        print("Scooters")
        print(scooter.marca)
        print(scooter.voltaje)
        print(scooter.eficiencia)
        print(scooter.precio)
        print(scooter.get_aro())
        print(scooter.get_velocidad())
        print(scooter.get_peso())
    for bicicleta in lista_bicicleta:
        print("Bicicletas")
        print(bicicleta.get_marca())
        print(bicicleta.get_aro())
        print(bicicleta.get_peso())
        print(bicicleta.get_precio())




while True:
    menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        registrar_tv(lista_tvs)
    elif opcion == 2:
        registrar_consola(lista_consolas)
    elif opcion == 3:
        registrar_bicicleta(lista_bicicleta)
    elif opcion == 4:
        registrar_scooter(lista_scooters)
    elif opcion == 5:
        mostrar_productos_registrados()
    elif opcion == 6:
        break
    else:
        print("ERROR")