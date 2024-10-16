import csv
import openpyxl
from datetime import datetime, timedelta
from tabulate import tabulate
import pandas as pd
import numpy as np
import logging
import sys

def main():
    print('Hola, ¿cómo estás?')
    print('Selecciona la opción que deseas realizar en este momento:')
    MenuPrincipal()


def cargar_datos(nombre_archivo):
    try:
        with open(f"{nombre_archivo}.csv", 'r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            datos = list(lector)
            for dato in datos:
                # Convertir campos de clave a enteros
                for clave in ['clave', 'clave_cliente', 'Folio']:
                    if clave in dato and dato[clave].isdigit():
                        dato[clave] = int(dato[clave])
                
                # Convertir otros campos numéricos a enteros
                for clave in ['Clave Unidad', 'Clave Cliente', 'Días Prestamo']:
                    if clave in dato and dato[clave].isdigit():
                        dato[clave] = int(dato[clave])
            return datos
    except FileNotFoundError:
        print(f"Archivo {nombre_archivo}.csv no encontrado. Se creará uno nuevo.")
        return []

# Actualizar la función para guardar datos
def guardar_datos(nombre_archivo, datos, campos):
    with open(f"{nombre_archivo}.csv", 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for fila in datos:
            fila_str = {k: str(v) for k, v in fila.items()}
            escritor.writerow(fila_str)


# Cargar datos al inicio del programa
unidades_registrados = cargar_datos("unidades")
prestamos_registrados = cargar_datos("prestamos")
clientes_registrados = cargar_datos("clientes")

continuar = True


def MenuPrincipal():
    global continuar
    while continuar:
        print("\nMenú Principal")
        print('\t1. Registro')
        print('\t2. Préstamo')
        print('\t3. Retorno')
        print('\t4. Informes')
        print('\t5. Salir')

        opcion = input('\nOpción deseada: ')

        if opcion == '1':
            MenuRegistro()
        elif opcion == '2':
            MenuPrestamo()
        elif opcion == '3':
            MenuRetorno()
        elif opcion == '4':
            MenuInformes()
        elif opcion == '5':
            if ConfirmarSalida():
                print('\nGracias por usar el sistema. ¡Hasta luego!')
                GuardarYSalir()
                sys.exit()  # Usamos sys.exit() para cerrar el programa
        else:
            print('\nOpción inválida. Por favor, selecciona una opción válida.')

def GuardarYSalir():
    guardar_todos_los_datos()
    print('\nDatos guardados. Gracias por usar el sistema. ¡Hasta luego!')

def guardar_todos_los_datos():
    guardar_datos("unidades", unidades_registrados, ["clave", "rodada", "color"])
    guardar_datos("prestamos", prestamos_registrados, ["Folio", "Clave Unidad", "Clave Cliente", "Fecha Prestamo", "Días Prestamo", "Fecha Retorno"])
    guardar_datos("clientes", clientes_registrados, ["clave_cliente", "apellidos", "nombres", "telefono"])

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

def generar_siguiente_clave(lista_datos, clave_campo):
    if not lista_datos:
        return "1"
    claves_existentes = [int(item[clave_campo]) for item in lista_datos]
    siguiente_numero = max(claves_existentes) + 1
    return str(siguiente_numero)

def mostrar_catalogo_unidades():
    print("\nCatálogo de Unidades:")
    if not unidades_registrados:
        print("No hay unidades registradas.")
    else:
        for unidad in unidades_registrados:
            print(f"Clave: {unidad['clave']} - Rodada: {unidad['rodada']} - Color: {unidad['color']}")

def mostrar_catalogo_clientes():
    print("\nCatálogo de Clientes:")
    if not clientes_registrados:
        print("No hay clientes registrados.")
    else:
        for cliente in clientes_registrados:
            print(f"Clave: {cliente['clave_cliente']} - Nombre: {cliente['nombres']} {cliente['apellidos']}")

def MenuUnidad():
    print("Menú Principal > Menu Registro > Menu Unidad")
    while True:
        print('\n')
        print('\n¿Qué deseas realizar?')
        print('\t1. Agregar nueva unidad')
        print('\t2. Volver al Menú de Registro')

        opcionUnidad = input('\nOpción deseada: ')
        
        if opcionUnidad == '1':
            RegistrarUnidad()
        elif opcionUnidad == '2':
            return  # Esto hará que salgamos de la función y volvamos al MenuRegistro
        else:
            print('\nOpción inválida. Por favor, selecciona una opción válida.')

def MenuRegistro():
    print("Menú Principal > Menu Registro")
    while True:
        print('\n')
        print('\n¿Qué deseas hacer?')
        print('\t1. Unidades')
        print('\t2. Clientes')
        print('\t3. Volver al Menú Principal')

        opcionRegistro = input('\nOpción deseada: ')

        if opcionRegistro == '1':
            MenuUnidad()
        elif opcionRegistro == '2':
            MenuCliente()
        elif opcionRegistro == '3':
            return
        else:
            print('\nOpción inválida. Por favor, selecciona una opción válida.')

def RegistrarUnidad():
    print("\nPara cancelar en cualquier momento, ingrese 'cancelar'.")
    
    clave = generar_siguiente_clave(unidades_registrados, "clave")
    
    while True:
        rodada = input("\nIngrese la rodada de la bicicleta (20, 26 o 29): ")
        if rodada.lower() == 'cancelar':
            print("Operación cancelada.")
            return MenuUnidad()
        if rodada in ["20", "26", "29"]:
            print("Rodada válida.")
            break
        else:
            print("Rodada inválida. Por favor, ingrese 20, 26 o 29.")
    
    while True:
        color = input("\nIngrese el color de la bicicleta (máximo 15 caracteres): ")
        if color.lower() == 'cancelar':
            print("Operación cancelada.")
            return MenuUnidad()
        if not color.isalpha():
            print('No se permiten números, solo datos tipo texto.')
            continue
        if 1 <= len(color) <= 15:
            print("Color válido.")
            break
        else:
            print("Color inválido. Debe tener entre 1 y 15 caracteres.")
    
    unidad = {
        "clave": clave,
        "rodada": rodada,
        "color": color
    }
    unidades_registrados.append(unidad)
    guardar_todos_los_datos()
        
    print("\nSe ha registrado la siguiente unidad:")
    print(f"Clave: {clave}")
    print(f"Rodada: {rodada}")
    print(f"Color: {color}")
    print("\nRegistro de unidad completado.")
    MenuUnidad()


def MenuCliente():
    print("Menú Principal > Menu Registro > Menu Cliente")
    
    print('\n')
    print('\n¿Qué deseas realizar?')
    print('\t1. Registrar nuevo cliente')
    print('\t2. Volver al Menú Principal')

    opcionCliente = input('\nOpción deseada: ')
    
    if opcionCliente == '1':
        RegistrarCliente()
    elif opcionCliente == '2':
        MenuPrincipal()
    else:
        print('\nOpción inválida. Por favor, selecciona una opción válida.')
        MenuCliente()

def RegistrarCliente():
    print("\nPara cancelar en cualquier momento, ingrese 'cancelar'.")

    clave_cliente = generar_siguiente_clave(clientes_registrados, "clave_cliente")

    # Validar apellidos
    while True:
        apellidos = input("Ingrese los apellidos del cliente (máximo 40 caracteres): ")
        if apellidos.lower() == 'cancelar':
            print("Operación cancelada.")
            return MenuCliente()
        if 1 <= len(apellidos) <= 40:
            break
        else:
            print("Apellidos inválidos. Deben contener entre 1 y 40 caracteres.")
    
    # Validar nombres
    while True:
        nombres = input("Ingrese los nombres del cliente (máximo 40 caracteres): ")
        if nombres.lower() == 'cancelar':
            print("Operación cancelada.")
            return MenuCliente()
        if 1 <= len(nombres) <= 40:
            break
        else:
            print("Nombres inválidos. Deben contener entre 1 y 40 caracteres.")
    
    # Validar teléfono
    while True:
        telefono = input("Ingrese el número de teléfono del cliente (10 dígitos): ")
        if telefono.lower() == 'cancelar':
            print("Operación cancelada.")
            return MenuCliente()
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
    guardar_todos_los_datos()
    
    print("\nCliente registrado con éxito:")
    print(tabulate([cliente.values()], headers=cliente.keys(), tablefmt="grid"))

    MenuCliente()


def MenuPrestamo():
    print("Menú Principal > Menu Prestamo")
    while True:
        print('\n')
        print('\n¿Qué deseas realizar?')
        print('\t1. Registrar un nuevo préstamo')
        print('\t2. Volver al Menú Principal')

        opcionPrestamo = input('\nOpción deseada: ')
        
        if opcionPrestamo == '1':
            RegistrarPrestamo()
        elif opcionPrestamo == '2':
            return
        else:
            print('\nOpción inválida. Por favor, selecciona una opción válida.')

def RegistrarPrestamo():
    print("\nPara cancelar en cualquier momento, ingrese 'cancelar'.")

    folio = generar_siguiente_clave(prestamos_registrados, "Folio")
    
    #Esta funcion 
    mostrar_catalogo_unidades()

    # Validar clave de la unidad
    while True:
        clave_unidad = input("Ingrese la clave de la unidad: ")
        if clave_unidad.lower() == 'cancelar':
            print("Operación cancelada.")
            return MenuPrestamo()
        if clave_unidad.isdigit() and int(clave_unidad) > 0:
            if any(unidad['clave'] == clave_unidad for unidad in unidades_registrados):
                break
            else:
                print("Clave de unidad no encontrada. Por favor, ingrese una clave de unidad registrada.")
        else:
            print("Clave de unidad inválida. Debe ser un número entero mayor a cero.")
        
    # Mostrar catálogo de clientes antes de pedir la clave del cliente
    mostrar_catalogo_clientes()
    
    # Validar clave del cliente
    while True:
        clave_cliente = input("Ingrese la clave del cliente: ")
        if clave_cliente.lower() == 'cancelar':
            print("Operación cancelada.")
            return MenuPrestamo()
        if clave_cliente.isdigit() and int(clave_cliente) > 0:
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
        if fecha_prestamo.lower() == 'cancelar':
            print("Operación cancelada.")
            return MenuPrestamo()
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
        if dias_prestamo.lower() == 'cancelar':
            print("Operación cancelada.")
            return MenuPrestamo()
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
    guardar_todos_los_datos()
    

    print("\nDatos del préstamo registrado:")
    print(tabulate([prestamo.values()], headers=prestamo.keys(), tablefmt="grid"))

    input("\nPresione Enter para continuar...")

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
    print("Menú Principal > Menu Retorno")
    while True:
        print('\n')
        print('\n\tMenú de Retorno')
        print('\t1. Registrar retorno')
        print('\t2. Volver al Menú Principal')

        opcionRetorno = input('\nOpción deseada: ')
            
        if opcionRetorno == '1':
            RegistrarRetorno()
        elif opcionRetorno == '2':
            return
        else:
            print('\nOpción inválida. Por favor, selecciona una opción válida.')

def MostrarPrestamosPendientes():
    print("\n\tPréstamos Pendientes de Retorno")
    
    prestamos_pendientes = [p for p in prestamos_registrados if p["Fecha Retorno"] == ""]
    
    if not prestamos_pendientes:
        print("No hay préstamos pendientes de retorno.")
    else:
        tabla = [[p["Folio"], p["Clave Unidad"], p["Clave Cliente"], p["Fecha Prestamo"], p["Días Prestamo"]] for p in prestamos_pendientes]
        print(tabulate(tabla, headers=["Folio", "Clave Unidad", "Clave Cliente", "Fecha Prestamo", "Días Prestamo"], tablefmt="grid"))
    
def RegistrarRetorno():
    while True:
        MostrarPrestamosPendientes()

        folio = input("Ingrese el folio del préstamo a retornar (o 'cancelar' para volver al menú): ")
        
        if folio.lower() == 'cancelar':
            print("Operación cancelada.")
            return MenuRetorno()
        
        if not folio.isdigit():
            print("Error: El folio debe ser un número entero positivo.")
            continue
        
        prestamo = next((p for p in prestamos_registrados if p["Folio"] == int(folio)), None)
        
        if prestamo is None:
            print(f"Error: No se encontró un préstamo con el folio {folio}.")
            continue
        
        if prestamo["Fecha Retorno"]:
            print(f"Error: El préstamo con folio {folio} ya ha sido retornado en la fecha {prestamo['Fecha Retorno']}.")
            continue
        
        fecha_actual = datetime.now().date()
        fecha_prestamo = datetime.strptime(prestamo["Fecha Prestamo"], "%m-%d-%Y").date()
        dias_prestamo = prestamo["Días Prestamo"]
        fecha_limite = fecha_prestamo + timedelta(days=dias_prestamo)
        
        if fecha_actual > fecha_limite:
            dias_retraso = (fecha_actual - fecha_limite).days
            print(f"Advertencia: El préstamo está retrasado por {dias_retraso} día(s).")
        
        confirmacion = input(f"¿Está seguro de que desea registrar el retorno del préstamo {folio}? (s/n): ")
        if confirmacion.lower() != 's':
            print("Operación cancelada.")
            continue
        
        prestamo["Fecha Retorno"] = fecha_actual.strftime("%m-%d-%Y")
        
        try:
            guardar_todos_los_datos()
            print(f"\nPréstamo con folio {folio} ha sido marcado como retornado en la fecha {prestamo['Fecha Retorno']}.")
            print("\nDatos actualizados del préstamo:")
            print(tabulate([prestamo.values()], headers=prestamo.keys(), tablefmt="grid"))
            input("\nPresione Enter para continuar...")
            return MenuRetorno()
        except Exception as e:
            print(f"Error al guardar los datos: {str(e)}")
            print("Los cambios no se han guardado. Por favor, inténtelo de nuevo.")
            continue

def ExportarReporte(datos, headers, nombre_archivo):
    while True:
        print("\n¿Desea exportar este reporte?")
        print("1. Exportar como CSV")
        print("2. Exportar como Excel")
        print("3. No exportar")
        
        opcion = input("\nOpción deseada: ")
        
        if opcion == "1":
            ExportarCSV(datos, headers, nombre_archivo)
            break
        elif opcion == "2":
            ExportarExcel(datos, headers, nombre_archivo)
            break
        elif opcion == "3":
            print("No se exportará el reporte.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def ExportarCSV(datos, headers, nombre_archivo):
    nombre_archivo = f"{nombre_archivo}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(nombre_archivo, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(datos)
    print(f"Reporte exportado como CSV: {nombre_archivo}")

def ExportarExcel(datos, headers, nombre_archivo):
    nombre_archivo = f"{nombre_archivo}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active
    
    # Añadir encabezados
    ws.append(headers)
    
    # Añadir datos
    for row in datos:
        ws.append(row)
    
    # Ajustar automáticamente el tamaño de las columnas
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter  # Obtener la letra de la columna
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))  # Medir la longitud del valor
            except:
                pass
        adjusted_width = (max_length + 2)  # Ajustar el ancho con un pequeño margen
        ws.column_dimensions[column].width = adjusted_width

    # Guardar el archivo
    wb.save(nombre_archivo)
    print(f"Reporte exportado como Excel: {nombre_archivo}")

def MenuInformes():
    print("Menú Principal > Menu Informes")
    while True:
        print('\n')
        print('\n\tMenú de Informes')
        print('\t1. Reportes')
        print('\t2. Análisis')
        print('\t3. Volver al Menú Principal')

        opcion = input('\nOpción deseada: ')

        if opcion == '1':
            MenuReportes()
        elif opcion == '2':
            MenuAnalisis()
        elif opcion == '3':
            return
        else:
            print('\nOpción inválida. Por favor, selecciona una opción válida.')

def MenuReportes():
    print("Menú Principal > Menu Informes > Menu Reportes")
    
    print('\n')
    print('\n\tMenú de Reportes')
    print('\t1. Ver usuarios registrados')
    print('\t2. Ver préstamos no devueltos')
    print('\t3. Buscar préstamos por duración')
    print('\t4. Listado de unidades')
    print('\t5. Reporte de retrasos')
    print('\t6. Volver al Menú Principal')

    opcion = input('\nOpción deseada: ')

    if opcion == '1':
        VerUsuariosRegistrados()
    elif opcion == '2':
        VerPrestamosNoDevueltos()
    elif opcion == '3':
        BuscarPrestamosPorFechas()
    elif opcion == '4':
        MenuListadoUnidades()
    elif opcion == '5':
        ReporteRetrasos()
    elif opcion == '6':
        MenuInformes()
    else:
        print('\nOpción inválida. Por favor, selecciona una opción válida.')

def ReporteRetrasos():
    print("\n\tReporte de Préstamos con Retraso")
    print("\nPara cancelar en cualquier momento, escriba 'cancelar'.")
    
    fecha_actual = datetime.now().date()
    prestamos_retrasados = []

    for prestamo in prestamos_registrados:
        try:
            if input("\nProcesando préstamos... Presione Enter para continuar o escriba 'cancelar' para salir: ").lower() == 'cancelar':
                print("Operación cancelada.")
                return MenuReportes()

            fecha_prestamo = datetime.strptime(prestamo["Fecha Prestamo"], "%m-%d-%Y").date()
            fecha_debida = fecha_prestamo + timedelta(days=int(prestamo["Días Prestamo"]))
            
            if not prestamo["Fecha Retorno"]:
                dias_retraso = (fecha_actual - fecha_debida).days
                fecha_retorno = "No retornado"
            else:
                fecha_retorno = datetime.strptime(prestamo["Fecha Retorno"], "%m-%d-%Y").date()
                dias_retraso = (fecha_retorno - fecha_debida).days

            if dias_retraso > 0:
                unidad = next((u for u in unidades_registrados if u["clave"] == prestamo["Clave Unidad"]), None)
                cliente = next((c for c in clientes_registrados if c["clave_cliente"] == prestamo["Clave Cliente"]), None)
                
                prestamos_retrasados.append({
                    "Días de retraso": dias_retraso,
                    "Fecha de retorno": fecha_retorno if isinstance(fecha_retorno, str) else fecha_retorno.strftime("%m-%d-%Y"),
                    "Fecha en que se debió haber retornado": fecha_debida.strftime("%m-%d-%Y"),
                    "Clave de unidad": prestamo["Clave Unidad"],
                    "Rodada": unidad["rodada"] if unidad else "N/A",
                    "Color": unidad["color"] if unidad else "N/A",
                    "Nombre completo del cliente": f"{cliente['nombres']} {cliente['apellidos']}" if cliente else "N/A",
                    "Teléfono de contacto": cliente["telefono"] if cliente else "N/A"
                })
        except (ValueError, KeyError) as e:
            print(f"Error al procesar préstamo: {e}")
            continue

    if not prestamos_retrasados:
        print("No hay préstamos con retraso.")
        return MenuReportes()

    prestamos_retrasados.sort(key=lambda x: x["Días de retraso"], reverse=True)

    headers = ["Días de retraso", "Fecha de retorno", "Fecha en que se debió haber retornado", "Clave de unidad", "Rodada", "Color", "Nombre completo del cliente", "Teléfono de contacto"]
    
    datos = [[p[h] for h in headers] for p in prestamos_retrasados]
    
    print(tabulate(datos, headers=headers, tablefmt="grid"))
    
    while True:
        opcion = input("\n¿Desea exportar el reporte? (s/n) o escriba 'cancelar' para salir: ").lower()
        if opcion == 'cancelar':
            print("Operación cancelada.")
            return MenuReportes()
        elif opcion == 's':
            try:
                ExportarReporte(datos, headers, "reporte_prestamos_retrasados")
                print("\nReporte exportado exitosamente.")
            except Exception as e:
                print(f"\nError al exportar el reporte: {e}")
            break
        elif opcion == 'n':
            break
        else:
            print("Opción no válida. Por favor, ingrese 's' para sí, 'n' para no, o 'cancelar' para salir.")

    input("\nPresione Enter para volver al menú de reportes (o escriba 'cancelar' para salir): ")
    return MenuReportes()


def MenuListadoUnidades():
    print("Menú Principal > Menu Informes > Menu Reportes > Menu Listado de Unidades")
    
    print('\n')
    print('\n\tListado de Unidades')
    print('\t1. Completo')
    print('\t2. Por rodada')
    print('\t3. Por color')
    print('\t4. Volver al Menú de Reportes')

    opcion = input('\nOpción deseada: ')

    if opcion == '1':
        ListadoUnidadesCompleto()
    elif opcion == '2':
        ListadoUnidadesPorRodada()
    elif opcion == '3':
        ListadoUnidadesPorColor()
    elif opcion == '4':
        MenuReportes()
    else:
        print('\nOpción inválida. Por favor, selecciona una opción válida.')

def ListadoUnidadesCompleto():
    print("\n\tListado Completo de Unidades")
    
    if not unidades_registrados:
        print("No hay unidades registradas.")
        return

    headers = ["Clave", "Rodada", "Color"]
    datos = [[u["clave"], u["rodada"], u["color"]] for u in unidades_registrados]
    
    print(tabulate(datos, headers=headers, tablefmt="grid"))
    
    ExportarReporte(datos, headers, "listado_unidades_completo")

def ListadoUnidadesPorRodada():
    print("\n\tListado de Unidades por Rodada")
    
    if not unidades_registrados:
        print("No hay unidades registradas.")
        return

    rodadas = sorted(set(u["rodada"] for u in unidades_registrados))
    
    headers = ["Clave", "Rodada", "Color"]
    datos = []
    
    for rodada in rodadas:
        print(f"\nRodada: {rodada}")
        unidades_rodada = [u for u in unidades_registrados if u["rodada"] == rodada]
        datos_rodada = [[u["clave"], u["rodada"], u["color"]] for u in unidades_rodada]
        datos.extend(datos_rodada)
        print(tabulate(datos_rodada, headers=headers, tablefmt="grid"))
    
    ExportarReporte(datos, headers, "listado_unidades_por_rodada")
    
    MenuListadoUnidades()

def ListadoUnidadesPorColor():
    print("\n\tListado de Unidades por Color")
    
    if not unidades_registrados:
        print("No hay unidades registradas.")
        return

    colores = sorted(set(u["color"] for u in unidades_registrados))
    
    headers = ["Clave", "Rodada", "Color"]
    datos = []
    
    for color in colores:
        print(f"\nColor: {color}")
        unidades_color = [u for u in unidades_registrados if u["color"] == color]
        datos_color = [[u["clave"], u["rodada"], u["color"]] for u in unidades_color]
        datos.extend(datos_color)
        print(tabulate(datos_color, headers=headers, tablefmt="grid"))
    
    ExportarReporte(datos, headers, "listado_unidades_por_color")
    
    MenuListadoUnidades()

def VerUsuariosRegistrados():
    print("\n\tListado de Usuarios Registrados")
    
    if not clientes_registrados:
        print("No hay usuarios registrados.")
        return
    
    headers = ["Clave Cliente", "Apellidos", "Nombres", "Teléfono"]
    datos = [[c["clave_cliente"], c["apellidos"], c["nombres"], c["telefono"]] for c in clientes_registrados]
    
    print(tabulate(datos, headers=headers, tablefmt="grid"))
    
    ExportarReporte(datos, headers, "usuarios_registrados")
    
    MenuReportes()

def VerPrestamosNoDevueltos():
    print("\n\tListado de Préstamos No Devueltos")
    
    prestamos_no_devueltos = [p for p in prestamos_registrados if p["Fecha Retorno"] == ""]
    
    if not prestamos_no_devueltos:
        print("No hay préstamos pendientes de devolución.")
        return
    
    headers = ["Folio", "Clave Unidad", "Clave Cliente", "Fecha Prestamo", "Días Prestamo"]
    datos = [[p["Folio"], p["Clave Unidad"], p["Clave Cliente"], p["Fecha Prestamo"], p["Días Prestamo"]] for p in prestamos_no_devueltos]
    
    print(tabulate(datos, headers=headers, tablefmt="grid"))
    
    ExportarReporte(datos, headers, "prestamos_no_devueltos")
    
    MenuReportes()

def BuscarPrestamosPorFechas():
    print("Ingrese las fechas para buscar los préstamos. Escriba 'cancelar' en cualquier momento para salir.")

    # Solicitar fechas de inicio y retorno
    while True:
        fecha_inicio = input("\nIngrese la fecha de inicio de préstamo (formato MM-DD-YYYY): ")
        if fecha_inicio.lower() == "cancelar":
            print("Búsqueda cancelada. Volviendo al menú de reportes.")
            MenuReportes()
            return
        try:
            fecha_inicio = datetime.strptime(fecha_inicio, "%m-%d-%Y")
            break
        except ValueError:
            print("Formato de fecha inválido. Intente de nuevo o escriba 'cancelar' para salir.")

    while True:
        fecha_retorno = input("Ingrese la fecha de retorno de préstamo (formato MM-DD-YYYY): ")
        if fecha_retorno.lower() == "cancelar":
            print("Búsqueda cancelada. Volviendo al menú de reportes.")
            MenuReportes()
            return
        try:
            fecha_retorno = datetime.strptime(fecha_retorno, "%m-%d-%Y")
            if fecha_retorno >= fecha_inicio:
                break
            else:
                print("La fecha de retorno no puede ser anterior a la fecha de inicio.")
        except ValueError:
            print("Formato de fecha inválido. Intente de nuevo o escriba 'cancelar' para salir.")

    # Verificar si existen préstamos registrados
    if not prestamos_registrados:
        print("No hay préstamos registrados.")
        return

    # Filtrar los préstamos que se encuentren dentro del rango de fechas
    prestamos_encontrados = [
        p for p in prestamos_registrados
        if fecha_inicio <= datetime.strptime(p["Fecha Prestamo"], "%m-%d-%Y") <= fecha_retorno
    ]

    if not prestamos_encontrados:
        print(f"No se encontraron préstamos entre {fecha_inicio.strftime('%m-%d-%Y')} y {fecha_retorno.strftime('%m-%d-%Y')}.")
        return
    
    # Mostrar los préstamos encontrados
    print(f"\n\tListado de Préstamos entre {fecha_inicio.strftime('%m-%d-%Y')} y {fecha_retorno.strftime('%m-%d-%Y')}")
    headers = ["Folio", "Clave Unidad", "Clave Cliente", "Fecha Prestamo", "Días Prestamo", "Fecha Retorno"]
    datos = [
        [p["Folio"], p["Clave Unidad"], p["Clave Cliente"], p["Fecha Prestamo"], p["Días Prestamo"], p["Fecha Retorno"]]
        for p in prestamos_encontrados
    ]
    
    print(tabulate(datos, headers=headers, tablefmt="grid"))
    
    # Exportar el reporte si es necesario
    try:
        ExportarReporte(datos, headers, f"prestamos_{fecha_inicio.strftime('%m-%d-%Y')}_a_{fecha_retorno.strftime('%m-%d-%Y')}")
    except Exception as e:
        print(f"Error al exportar el reporte: {e}")
    
    # Volver al menú de reportes
    MenuReportes()

def MenuAnalisis():
    print("Menú Principal > Menu Informes > Menu Analisis")
    
    print('\n')
    print('\n\tMenú de Análisis')
    print('\t1. Duración de los préstamos')
    print('\t2. Ranking de clientes')
    print('\t3. Preferencias de rentas')
    print('\t4. Volver al Menú de Informes')

    opcion = input('\nOpción deseada: ')

    if opcion == '1':
        AnalisisDuracionPrestamos()
    elif opcion == '2':
        RankingClientes()
    elif opcion == '3':
        MenuPreferenciasRentas()
    elif opcion == '4':
        MenuInformes()
    else:
        print('\nOpción inválida. Por favor, selecciona una opción válida.')
        MenuAnalisis()

import pandas as pd
import logging
from tabulate import tabulate

def RankingClientes():
    try:
        print("\n\tRanking de Clientes")

        # Asegúrate de que los datos se lean correctamente desde los CSV, forzando las claves a string
        df_prestamos = pd.read_csv('prestamos.csv', dtype={'Clave Cliente': str})
        df_clientes = pd.read_csv('clientes.csv', dtype={'clave_cliente': str})

        # Limpieza de espacios en blanco o caracteres especiales
        df_prestamos['Clave Cliente'] = df_prestamos['Clave Cliente'].str.strip()
        df_clientes['clave_cliente'] = df_clientes['clave_cliente'].str.strip()

        # Verificar si los datos han sido cargados correctamente
        if df_prestamos.empty or df_clientes.empty:
            print("No hay datos suficientes para generar el ranking.")
            return

        # Agrupar por la clave del cliente y contar la cantidad de préstamos
        df_ranking = df_prestamos.groupby('Clave Cliente').size().reset_index(name='Cantidad de Prestamos')

        # Realizar el merge
        df_ranking = df_ranking.merge(df_clientes, left_on='Clave Cliente', right_on='clave_cliente', how='left', indicator=True)

        # Mostrar las coincidencias del merge
        print(df_ranking['_merge'].value_counts())

        # Verificar filas que no coincidieron en el merge
        print("Filas que no coincidieron en el merge:")
        print(df_ranking[df_ranking['_merge'] != 'both'])

        # Seleccionar columnas relevantes para el ranking
        df_ranking = df_ranking[['Cantidad de Prestamos', 'clave_cliente', 'nombres', 'apellidos', 'telefono']]
        df_ranking = df_ranking.sort_values(by='Cantidad de Prestamos', ascending=False)
        
        # Mostrar el DataFrame final y exportar si hay datos
        if df_ranking.empty:
            print("No hay datos para mostrar en el ranking.")
        else:
            print(tabulate(df_ranking.values, headers=['Préstamos', 'Clave Cliente', 'Nombre', 'Apellidos', 'Teléfono'], tablefmt="grid"))
            ExportarReporte(df_ranking.values, ['Préstamos', 'Clave Cliente', 'Nombre', 'Apellidos', 'Teléfono'], "ranking_clientes")

    except Exception as e:
        logging.error(f"Error en RankingClientes: {str(e)}")
        print(f"Ocurrió un error al generar el ranking de clientes: {str(e)}")
    
    MenuAnalisis()


def AnalisisDuracionPrestamos():
    try:
        print("\n\tAnálisis de Duración de los Préstamos")
        
        if not prestamos_registrados:
            print("No hay datos de préstamos para analizar.")
            return

        df = pd.DataFrame(prestamos_registrados)
        df['Días Prestamo'] = pd.to_numeric(df['Días Prestamo'], errors='coerce')
        
        if df['Días Prestamo'].isnull().all():
            print("No hay datos válidos de duración de préstamos para analizar.")
            return

        descripcion = df['Días Prestamo'].describe(percentiles=[.25, .5, .75])
        moda = df['Días Prestamo'].mode().values
        desviacion_estandar = df['Días Prestamo'].std()
        
        resultados = {
            "Media": descripcion['mean'],
            "Mediana": descripcion['50%'],
            "Moda": moda[0] if len(moda) > 0 else None,
            "Mínimo": descripcion['min'],
            "Máximo": descripcion['max'],
            "Desviación Estándar": desviacion_estandar,
            "Primer Cuartil (25%)": descripcion['25%'],
            "Tercer Cuartil (75%)": descripcion['75%']
        }
        
        tabla_resultados = [[k, v] for k, v in resultados.items()]
        headers = ["Estadística", "Valor"]
        print(tabulate(tabla_resultados, headers=headers, tablefmt="grid"))
        
        ExportarReporte(tabla_resultados, headers, "analisis_duracion_prestamos")

    except Exception as e:
        logging.error(f"Error en AnalisisDuracionPrestamos: {str(e)}")
        print("Ocurrió un error al analizar la duración de los préstamos.")
    
    MenuAnalisis()

def MenuPreferenciasRentas():
    while True:
        try:
            print('\n')
            print('\n\tPreferencias de Rentas')
            print('\t1. Cantidad de préstamos por rodada')
            print('\t2. Cantidad de préstamos por color')
            print('\t3. Volver al Menú de Análisis')

            opcion = input('\nOpción deseada: ')

            if opcion == '1':
                ReportePrestamosPorRodada()
            elif opcion == '2':
                ReportePrestamosPorColor()
            elif opcion == '3':
                return
            else:
                print('\nOpción inválida. Por favor, selecciona una opción válida.')
        except Exception as e:
            logging.error(f"Error en MenuPreferenciasRentas: {str(e)}")
            print("Ocurrió un error. Por favor, inténtalo de nuevo.")

import pandas as pd
from tabulate import tabulate
import logging

def ReportePrestamosPorRodada():
    try:
        print("\n\tReporte de Préstamos por Rodada")

        if not prestamos_registrados or not unidades_registrados:
            print("No hay datos suficientes para generar el reporte.")
            return

        df_prestamos = pd.DataFrame(prestamos_registrados)
        df_unidades = pd.DataFrame(unidades_registrados)

        # Asegurarse de que 'Clave Unidad' y 'clave' sean del mismo tipo (string)
        df_prestamos['Clave Unidad'] = df_prestamos['Clave Unidad'].astype(str)
        df_unidades['clave'] = df_unidades['clave'].astype(str)

        # Realizar el merge
        df_prestamos = df_prestamos.merge(df_unidades[['clave', 'rodada']], left_on='Clave Unidad', right_on='clave', how='left')

        if 'rodada' not in df_prestamos.columns:
            print("La columna 'rodada' no está presente después del merge.")
            return

        if df_prestamos['rodada'].isnull().all():
            print("No hay datos válidos de rodada para generar el reporte.")
            return

        df_ranking_rodada = df_prestamos['rodada'].value_counts().reset_index()
        df_ranking_rodada.columns = ['Rodada', 'Cantidad de Préstamos']
        df_ranking_rodada = df_ranking_rodada.sort_values(by='Cantidad de Préstamos', ascending=False)

        print(tabulate(df_ranking_rodada.values, headers=['Rodada', 'Cantidad de Préstamos'], tablefmt="grid"))
        ExportarReporte(df_ranking_rodada.values, ['Rodada', 'Cantidad de Préstamos'], "reporte_prestamos_por_rodada")

    except Exception as e:
        logging.error(f"Error en ReportePrestamosPorRodada: {str(e)}")
        print(f"Ocurrió un error al generar el reporte de préstamos por rodada: {str(e)}")
    
    MenuPreferenciasRentas()

def ReportePrestamosPorColor():
    try:
        print("\n\tReporte de Préstamos por Color")

        if not prestamos_registrados or not unidades_registrados:
            print("No hay datos suficientes para generar el reporte.")
            return

        df_prestamos = pd.DataFrame(prestamos_registrados)
        df_unidades = pd.DataFrame(unidades_registrados)

        # Asegurarse de que 'Clave Unidad' y 'clave' sean del mismo tipo (string)
        df_prestamos['Clave Unidad'] = df_prestamos['Clave Unidad'].astype(str)
        df_unidades['clave'] = df_unidades['clave'].astype(str)

        # Realizar el merge
        df_prestamos = df_prestamos.merge(df_unidades[['clave', 'color']], left_on='Clave Unidad', right_on='clave', how='left')

        if 'color' not in df_prestamos.columns:
            print("La columna 'color' no está presente después del merge.")
            return

        if df_prestamos['color'].isnull().all():
            print("No hay datos válidos de color para generar el reporte.")
            return

        df_ranking_color = df_prestamos['color'].value_counts().reset_index()
        df_ranking_color.columns = ['Color', 'Cantidad de Préstamos']
        df_ranking_color = df_ranking_color.sort_values(by='Cantidad de Préstamos', ascending=False)

        print(tabulate(df_ranking_color.values, headers=['Color', 'Cantidad de Préstamos'], tablefmt="grid"))
        ExportarReporte(df_ranking_color.values, ['Color', 'Cantidad de Préstamos'], "reporte_prestamos_por_color")

    except Exception as e:
        logging.error(f"Error en ReportePrestamosPorColor: {str(e)}")
        print(f"Ocurrió un error al generar el reporte de préstamos por color: {str(e)}")
    
    MenuPreferenciasRentas()

if __name__ == "__main__":
    main()
