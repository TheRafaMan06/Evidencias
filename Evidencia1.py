import random
#import csv
#import openpyxl
from datetime import datetime
from tabulate import tabulate


print('Hola, ¿cómo estás?')
print('Selecciona la opción que deseas realizar en este momento:')

#Aqui van todas las listas que se usaran despues 

unidades_registradas= []
prestamos_registrados = []
clientes_registrados = []


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
        if ConfirmarSalida():
            print('\nGracias por usar el sistema. ¡Hasta luego!')
            return
        else:
            MenuPrincipal()
    else:
        print('\nOpción inválida. Por favor, selecciona una opción válida.')
        MenuPrincipal()

def ConfirmarSalida():
    """Función para confirmar si el usuario realmente quiere salir."""
    while True:
        confirmacion = input("¿Estás seguro de que deseas salir? (s/n): ").strip().lower()
        if confirmacion == 's':
            return True
        elif confirmacion == 'n':
            return False
        else:
            print("Opción inválida. Por favor, ingresa 's' para sí o 'n' para no.")

def MenuRegistro():
    print('\nEn este momento estás en Registro, ¿qué deseas hacer?')
    print('\t1. Unidades')
    print('\t2. Clientes')
    print('\t3. Volver al Menú Principal')

    opcionRegistro = input('\nOpción deseada: ')

    if opcionRegistro == '1':
        MenuUnidad()
    elif opcionRegistro == '2':
        MenuCliente()
    elif opcionRegistro == '3':
        MenuPrincipal()
    else:
        print('\nOpción inválida. Por favor, selecciona una opción válida.')
        MenuRegistro()

def MenuUnidad():
    print('\n¿Que deseas realizar?')
    print('\t1. Agregar nueva unidad')
    print('\t2. Ver unidades')
    print('\t3. Volver al Menú de Registro')

    opcionUnidad = input('\nOpción deseada: ')
    
    if opcionUnidad == '1':
        RegistrarUnidad()
    elif opcionUnidad == '2':
        VerUnidad()
    elif opcionUnidad == '3':
        MenuRegistro()
    else:
        print('\nOpción inválida. Por favor, selecciona una opción válida.')
        MenuUnidad()

def RegistrarUnidad():
    """ Aqui tengo un problema con que aunque ponga un numero incorrecto, sigue dando para adelante"""
    # Generar clave única para la unidad
    clave = random.randint(1, 1000)
    
    # Solicitar la rodada de la bicicleta
    while True:
        rodada = input("\nIngrese la rodada de la bicicleta (20, 26 o 29): ")
        if rodada in ["20", "26", "29"]:
            print("Rodada valida.")
        else:
            print("Rodada inválida. Por favor, ingrese 20, 26 o 29.")
            
                
    # Guardar los datos de la unidad
        unidad = {
            "clave": clave,
            "rodada": rodada
        }
        unidades_registradas.append(unidad)
        
        print("\nSe ha registrado la siguiente unidad:")
        print(f"Clave: {clave}")
        print(f"Rodada: {rodada}")
        print("\nRegistro de unidad completado.")
        MenuUnidad()

def VerUnidad():
    print("\n\tListado de Unidades Registradas")
    
    if not unidades_registradas:
        print("No se han registrado unidades.")
        MenuUnidad()
        return
    
    # Crear la tabla con la librería tabulate
    tabla = [[unidad["clave"], unidad["rodada"]] for unidad in unidades_registradas]
    print(tabulate(tabla, headers=["Clave", "Rodada"], tablefmt="grid"))
    
    MenuRegistro()

def MenuCliente():
    print('\n¿Qué deseas realizar?')
    print('\t1. Registrar nuevo cliente')
    print('\t2. Ver clientes')
    print('\t3. Volver al Menú Principal')

    opcionCliente = input('\nOpción deseada: ')
    
    if opcionCliente == '1':
        RegistrarCliente()
    elif opcionCliente == '2':
        VerClientes()
    elif opcionCliente == '3':
        MenuPrincipal()
    else:
        print('\nOpción inválida. Por favor, selecciona una opción válida.')
        MenuCliente()

def RegistrarCliente():
    """Función para registrar un nuevo cliente con las restricciones especificadas."""

    clave_cliente = random.randint(1, 1000)

    # Validar apellidos
    while True:
        apellidos = input("Ingrese los apellidos del cliente (máximo 40 caracteres): ")
        if 1 <= len(apellidos) <= 40:
            break
        else:
            print("Apellidos inválidos. Deben contener entre 1 y 40 caracteres.")
    
    # Validar nombres
    while True:
        nombres = input("Ingrese los nombres del cliente (máximo 40 caracteres): ")
        if 1 <= len(nombres) <= 40:
            break
        else:
            print("Nombres inválidos. Deben contener entre 1 y 40 caracteres.")
    
    # Validar teléfono
    while True:
        telefono = input("Ingrese el número de teléfono del cliente (10 dígitos): ")
        if telefono.isdigit() and len(telefono) == 10:
            break
        else:
            print("Número de teléfono inválido. Debe contener exactamente 10 dígitos.")
    
    cliente = {
        "clave_cliente": clave_cliente,
        "apellidos": apellidos,
        "nombres": nombres,
        "telefono": telefono
    }
    clientes_registrados.append(cliente)
    
    print("\nCliente registrado con éxito:")
    print(tabulate([cliente.values()], headers=cliente.keys(), tablefmt="grid"))

    MenuCliente()

def VerClientes():
    print("\n\tListado de Clientes Registrados")
    
    if not clientes_registrados:
        print("No se han registrado clientes.")
        MenuCliente()
        return
    
    tabla = [[c["clave_cliente"], c["apellidos"], c["nombres"], c["telefono"]] for c in clientes_registrados]
    print(tabulate(tabla, headers=["Clave Cliente", "Apellidos", "Nombres", "Teléfono"], tablefmt="grid"))
    
    MenuCliente()


def MenuPrestamo():
    print('\n¿Que deseas realizar?')
    print('\t1. Registrar un nuevo préstamo')
    print('\t2. Ver préstamos registrados')
    print('\t3. Volver al Menú Principal')

    opcionPrestamo = input('\nOpción deseada: ')
    
    if opcionPrestamo == '1':
        RegistrarPrestamo()
    elif opcionPrestamo == '2':
        VerPrestamos()
    elif opcionPrestamo == '3':
        MenuPrincipal()
    else:
        print('\nOpción inválida. Por favor, selecciona una opción válida.')
        MenuPrestamo()

def RegistrarPrestamo():
    """Función para registrar un préstamo con las restricciones adicionales."""

    folio = random.randint(1, 1000)
    
    # Validar clave de la unidad
    while True:
        clave_unidad = input("Ingrese la clave de la unidad (número entero mayor a cero): ")
        if clave_unidad.isdigit() and int(clave_unidad) > 0:
            clave_unidad = int(clave_unidad)
            if any(unidad['clave'] == clave_unidad for unidad in unidades_registradas):
                break
            else:
                print("Clave de unidad no encontrada. Por favor, ingrese una clave de unidad registrada.")
        else:
            print("Clave de unidad inválida. Debe ser un número entero mayor a cero.")
    
    # Validar clave del cliente
    while True:
        clave_cliente = input("Ingrese la clave del cliente (número entero mayor a cero): ")
        if clave_cliente.isdigit() and int(clave_cliente) > 0:
            clave_cliente = int(clave_cliente)
            if any(cliente['clave_cliente'] == clave_cliente for cliente in clientes_registrados):
                break
            else:
                print("Clave del cliente no encontrada. Por favor, ingrese una clave de cliente registrada.")
        else:
            print("Clave del cliente inválida. Debe ser un número entero mayor a cero.")
    
    # Validar fecha del préstamo
    fecha_actual = datetime.now().strftime("%m-%d-%Y")
    while True:
        fecha_prestamo = input(f"Ingrese la fecha del préstamo (por defecto {fecha_actual} o formato mm-dd-aaaa): ")
        if fecha_prestamo == "":
            fecha_prestamo = fecha_actual
            break
        else:
            try:
                fecha_prestamo_dt = datetime.strptime(fecha_prestamo, "%m-%d-%Y")
                if fecha_prestamo_dt.date() >= datetime.now().date():
                    fecha_prestamo = fecha_prestamo_dt.strftime("%m-%d-%Y")
                    break
                else:
                    print("Fecha inválida. La fecha no puede ser anterior a la fecha actual.")
            except ValueError:
                print("Fecha inválida. Debe estar en el formato mm-dd-aaaa.")
    
    # Validar cantidad de días del préstamo
    while True:
        dias_prestamo = input("Ingrese la cantidad de días del préstamo (entre 1 y 14 días): ")
        if dias_prestamo.isdigit() and 1 <= int(dias_prestamo) <= 14:
            dias_prestamo = int(dias_prestamo)
            break
        else:
            print("Cantidad de días inválida. Debe ser un número entero entre 1 y 14 días.")
    
    fecha_retorno = ""

    prestamo = {
        "Folio": folio,
        "Clave Unidad": clave_unidad,
        "Clave Cliente": clave_cliente,
        "Fecha Prestamo": fecha_prestamo,
        "Días Prestamo": dias_prestamo,
        "Fecha Retorno": fecha_retorno
    }
    prestamos_registrados.append(prestamo)
    
    print("\nDatos del préstamo registrado:")
    print(tabulate([prestamo.values()], headers=prestamo.keys(), tablefmt="grid"))

    MenuPrestamo()

def VerPrestamos():
    print("\n\tListado de Préstamos Registrados")
    
    if not prestamos_registrados:
        print("No se han registrado préstamos.")
        return
    
    tabla = [[p["Folio"], p["Clave Unidad"], p["Clave Cliente"], p["Fecha Prestamo"], p["Días Prestamo"], p["Fecha Retorno"]] for p in prestamos_registrados]
    print(tabulate(tabla, headers=["Folio", "Clave Unidad", "Clave Cliente", "Fecha Prestamo", "Días Prestamo", "Fecha Retorno"], tablefmt="grid"))
    
    MenuPrestamo()
    

def MenuRetorno():
    # Aquí va el código para el menú de retorno
    pass

def MenuReportes():
    # Aquí va el código para el menú de reportes
    pass

MenuPrincipal()
