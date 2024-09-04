import random
#import csv
#import openpyxl
from tabulate import tabulate


print('Hola, ¿cómo estás?')
print('Selecciona la opción que deseas realizar en este momento:')

#Aqui van todas las listas que se usaran despues 

unidades_registradas= []

def MenuPrincipal():
    print('\n\t Menú Principal')
    print('\t1. Registro')
    print('\t2. Préstamo')
    print('\t3. Retorno')
    print('\t4. Reportes')
    print('\t5. Salir')

    opcion = input('\nOpción deseada: ')

    if opcion == '1':
        MenuRegistro()
    elif opcion == '2':
        MenuPrestamo()
    elif opcion == '3':
        MenuRetorno()
    elif opcion == '4':
        MenuReportes()
    elif opcion == '5':
        print('\nGracias por usar el sistema. ¡Hasta luego!')
    else:
        print('\nOpción inválida. Por favor, selecciona una opción válida.')
        MenuPrincipal()

def MenuRegistro():
    print('\nEn este momento estás en Registro, ¿qué deseas hacer?')
    print('\t1. Unidades')
    print('\t2. Clientes')
    print('\t3. Volver al Menú Principal')

    opcionRegistro = input('\nOpción deseada: ')

    if opcionRegistro == '1':
        MenuUnidad()
    elif opcionRegistro == '2':
        RegistroCliente()
    elif opcionRegistro == '3':
        MenuPrincipal()
    else:
        print('\nOpción inválida. Por favor, selecciona una opción válida.')
        MenuRegistro()

def MenuUnidad():
    print('\n¿Que deseas realizar?')
    print('\t1. Agregar nueva undiad')
    print('\t2. Ver unidades')
    print('\t3. Volver al Menú Principal')

    opcionUnidad = input('\nOpción deseada: ')
    
    if opcionUnidad == '1':
        RegistrarUnidad()
    elif opcionUnidad == '2':
        VerUnidad()
    elif opcionUnidad == '3':
        MenuPrincipal()
    else:
        print('\nOpción inválida. Por favor, selecciona una opción válida.')
        MenuRegistro()

def RegistrarUnidad():
    # Generar clave única para la unidad
    clave = random.randint(1, 1000)
    
    # Solicitar la rodada de la bicicleta
    while True:
        rodada = input("Ingrese la rodada de la bicicleta (20, 26 o 29): ")
        if rodada in ["20", "26", "29"]:
            break
        else:
            print("Rodada inválida. Por favor, ingrese 20, 26 o 29.")
    
    # Guardar los datos de la unidad
        unidad = {
            "clave": clave,
            "rodada": rodada
        }
        unidades_registradas.append(unidad)
        
        print(f"\nSe ha registrado la siguiente unidad:")
        print(f"Clave: {clave}")
        print(f"Rodada: {rodada}")
        print("\nRegistro de unidad completado.")
        MenuUnidad()

def VerUnidad():
    print("\n\tListado de Unidades Registradas")
    
    if not unidades_registradas:
        print("No se han registrado unidades.")
        return
    
    # Crear la tabla con la librería tabulate
    tabla = [[unidad["clave"], unidad["rodada"]] for unidad in unidades_registradas]
    print(tabulate(tabla, headers=["Clave", "Rodada"], tablefmt="grid"))
    MenuUnidad()
    
    
def RegistroCliente():
    # Aquí va el código para el registro de cliente
    pass

def MenuPrestamo():
    # Aquí va el código para el menú de préstamo
    pass

def MenuRetorno():
    # Aquí va el código para el menú de retorno
    pass

def MenuReportes():
    # Aquí va el código para el menú de reportes
    pass

MenuPrincipal()