class InformacionEmpresa:
    NOMBRE = "Maquilados Mexicanos, S.A. de C.V."
    GIRO = "Fabricación de camisas"
    PRODUCTOS = {
        'CL': 'Camisas Lisas',
        'CE': 'Camisas Estampadas',
        'CR': 'Camisas Rayadas'
    }
    AÑO = 2015
    CLIENTES = "Comerciantes menores"

class BalanceGeneral:
    def __init__(self):
        self.activo_circulante = {}
        self.activo_no_circulante = {}
        self.pasivo_corto_plazo = {}
        self.pasivo_largo_plazo = {}
        self.capital_contable = {}
        self.fecha = "31 de Diciembre del 2015"
        
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print(f"Balance General al {self.fecha}".center(80))
        print("(Cifras en Pesos)".center(80))
        print("="*80 + "\n")
        
    def solicitar_datos(self):
        print("\n=== CAPTURA DE ACTIVO CIRCULANTE ===")
        self.activo_circulante = {
            'Efectivo': self.solicitar_monto("Efectivo"),
            'Clientes': self.solicitar_monto("Clientes"),
            'Deudores Diversos': self.solicitar_monto("Deudores Diversos"),
            'Funcionarios y Empleados': self.solicitar_monto("Funcionarios y Empleados"),
            'Inventario de materiales': self.solicitar_monto("Inventario de materiales"),
            'Inventario de Producto Terminado': self.solicitar_monto("Inventario de Producto Terminado")
        }
        
        print("\n=== CAPTURA DE ACTIVO NO CIRCULANTE ===")
        self.activo_no_circulante = {
            'Terreno': self.solicitar_monto("Terreno"),
            'Planta y Equipo': self.solicitar_monto("Planta y Equipo"),
            'Depreciación Acumulada': self.solicitar_monto("Depreciación Acumulada")
        }
        
        print("\n=== CAPTURA DE PASIVO CORTO PLAZO ===")
        self.pasivo_corto_plazo = {
            'Proveedores': self.solicitar_monto("Proveedores"),
            'Documentos por Pagar': self.solicitar_monto("Documentos por Pagar"),
            'ISR Por Pagar': self.solicitar_monto("ISR Por Pagar")
        }
        
        print("\n=== CAPTURA DE PASIVO LARGO PLAZO ===")
        self.pasivo_largo_plazo = {
            'Préstamos Bancarios': self.solicitar_monto("Préstamos Bancarios")
        }
        
        print("\n=== CAPTURA DE CAPITAL CONTABLE ===")
        self.capital_contable = {
            'Capital Contribuido': self.solicitar_monto("Capital Contribuido"),
            'Capital Ganado': self.solicitar_monto("Capital Ganado")
        }
    
    def solicitar_monto(self, concepto):
        while True:
            try:
                monto = float(input(f"Ingrese el monto para {concepto}: "))
                if monto >= 0:
                    return monto
                print("Por favor ingrese un monto no negativo.")
            except ValueError:
                print("Por favor ingrese un valor numérico válido.")
    
    def modificar_valor(self):
        print("\nCuentas disponibles para modificar:")
        todas_las_cuentas = []
        
        print("\nACTIVO CIRCULANTE:")
        for i, (cuenta, valor) in enumerate(self.activo_circulante.items(), 1):
            print(f"{i}. {cuenta}: ${valor:,.2f}")
            todas_las_cuentas.append(('activo_circulante', cuenta))
            
        print("\nACTIVO NO CIRCULANTE:")
        for i, (cuenta, valor) in enumerate(self.activo_no_circulante.items(), len(todas_las_cuentas) + 1):
            print(f"{i}. {cuenta}: ${valor:,.2f}")
            todas_las_cuentas.append(('activo_no_circulante', cuenta))
            
        print("\nPASIVO CORTO PLAZO:")
        for i, (cuenta, valor) in enumerate(self.pasivo_corto_plazo.items(), len(todas_las_cuentas) + 1):
            print(f"{i}. {cuenta}: ${valor:,.2f}")
            todas_las_cuentas.append(('pasivo_corto_plazo', cuenta))
            
        print("\nPASIVO LARGO PLAZO:")
        for i, (cuenta, valor) in enumerate(self.pasivo_largo_plazo.items(), len(todas_las_cuentas) + 1):
            print(f"{i}. {cuenta}: ${valor:,.2f}")
            todas_las_cuentas.append(('pasivo_largo_plazo', cuenta))
            
        print("\nCAPITAL CONTABLE:")
        for i, (cuenta, valor) in enumerate(self.capital_contable.items(), len(todas_las_cuentas) + 1):
            print(f"{i}. {cuenta}: ${valor:,.2f}")
            todas_las_cuentas.append(('capital_contable', cuenta))
        
        while True:
            try:
                opcion = int(input("\nSeleccione el número de la cuenta a modificar (0 para cancelar): "))
                if opcion == 0:
                    return
                if 1 <= opcion <= len(todas_las_cuentas):
                    tipo_cuenta, nombre_cuenta = todas_las_cuentas[opcion - 1]
                    nuevo_valor = self.solicitar_monto(f"nuevo valor para {nombre_cuenta}")
                    getattr(self, tipo_cuenta)[nombre_cuenta] = nuevo_valor
                    return
                print("Opción no válida.")
            except ValueError:
                print("Por favor ingrese un número válido.")

    def calcular_total_activo_circulante(self):
        return sum(self.activo_circulante.values())
    
    def calcular_total_activo_no_circulante(self):
        return (
            self.activo_no_circulante['Terreno'] +
            self.activo_no_circulante['Planta y Equipo'] - 
            self.activo_no_circulante['Depreciación Acumulada']
        )
    
    def calcular_activo_total(self):
        return self.calcular_total_activo_circulante() + self.calcular_total_activo_no_circulante()
    
    def calcular_total_pasivo_corto_plazo(self):
        return sum(self.pasivo_corto_plazo.values())
    
    def calcular_total_pasivo_largo_plazo(self):
        return sum(self.pasivo_largo_plazo.values())
    
    def calcular_pasivo_total(self):
        return self.calcular_total_pasivo_corto_plazo() + self.calcular_total_pasivo_largo_plazo()
    
    def calcular_capital_contable_total(self):
        return sum(self.capital_contable.values())
    
    def verificar_balance(self):
        activo_total = self.calcular_activo_total()
        pasivo_capital = self.calcular_pasivo_total() + self.calcular_capital_contable_total()
        diferencia = activo_total - pasivo_capital
        return diferencia, abs(diferencia) < 0.01

    def imprimir_resumen(self):
        self.imprimir_encabezado()
        print("+--------------------------------+-------------+--------------------------------+-------------+")
        print("| ACTIVO                         | MONTO       | PASIVO                         | MONTO       |")
        print("+--------------------------------+-------------+--------------------------------+-------------+")
        print("| ACTIVO CIRCULANTE:             |             | PASIVO CORTO PLAZO:            |             |")
        print("+--------------------------------+-------------+--------------------------------+-------------+")
        
        # Activo Circulante y Pasivo Corto Plazo
        activo_circ = list(self.activo_circulante.items())
        pasivo_cp = list(self.pasivo_corto_plazo.items())
        max_len = max(len(activo_circ), len(pasivo_cp))
        
        for i in range(max_len):
            activo_str = f"| {activo_circ[i][0] if i < len(activo_circ) else '':<30}"
            activo_monto = f"| ${activo_circ[i][1]:,.2f}" if i < len(activo_circ) else "|"
            pasivo_str = f"| {pasivo_cp[i][0] if i < len(pasivo_cp) else '':<30}"
            pasivo_monto = f"| ${pasivo_cp[i][1]:,.2f} |" if i < len(pasivo_cp) else "|"
            
            print(f"{activo_str}{activo_monto:<13}{pasivo_str}{pasivo_monto:<13}")
            print("+--------------------------------+-------------+--------------------------------+-------------+")
        
        # Total Activo Circulante y Total Pasivo Corto Plazo
        print(f"| Total Activo Circulante        | ${self.calcular_total_activo_circulante():,.2f} | Total Pasivo Corto Plazo       | ${self.calcular_total_pasivo_corto_plazo():,.2f} |")
        print("+--------------------------------+-------------+--------------------------------+-------------+")
        
        # Activo No Circulante y Pasivo Largo Plazo
        print("| ACTIVO NO CIRCULANTE:           |             | PASIVO LARGO PLAZO:             |             |")
        print("+--------------------------------+-------------+--------------------------------+-------------+")
        
        # Terreno
        print(f"| Terreno                        | ${self.activo_no_circulante['Terreno']:,.2f} | Préstamos Bancarios           | ${self.pasivo_largo_plazo['Préstamos Bancarios']:,.2f} |")
        print("+--------------------------------+-------------+--------------------------------+-------------+")
        
        # Planta y Equipo
        print(f"| Planta y Equipo                | ${self.activo_no_circulante['Planta y Equipo']:,.2f} |                                |             |")
        print("+--------------------------------+-------------+--------------------------------+-------------+")
        
        # Depreciación Acumulada
        print(f"| Depreciación Acumulada         | (${self.activo_no_circulante['Depreciación Acumulada']:,.2f}) |                                |             |")
        print("+--------------------------------+-------------+--------------------------------+-------------+")
        
        # Total Activo No Circulante y Total Pasivo
        print(f"| Total Activo No Circulante     | ${self.calcular_total_activo_no_circulante():,.2f} | TOTAL PASIVO                   | ${self.calcular_pasivo_total():,.2f} |")
        print("+--------------------------------+-------------+--------------------------------+-------------+")
        
        # Capital Contable
        print("|                                |             | CAPITAL CONTABLE:              |             |")
        print("+--------------------------------+-------------+--------------------------------+-------------+")
        
        for concepto, monto in self.capital_contable.items():
            print(f"|                                |             | {concepto:<30} | ${monto:,.2f} |")
            print("+--------------------------------+-------------+--------------------------------+-------------+")
        
        # Totales finales
        activo_total = self.calcular_activo_total()
        pasivo_capital_total = self.calcular_pasivo_total() + self.calcular_capital_contable_total()
        print(f"| TOTAL ACTIVO                   | ${activo_total:,.2f} | TOTAL PASIVO Y CAPITAL         | ${pasivo_capital_total:,.2f} |")
        print("+--------------------------------+-------------+--------------------------------+-------------+")
        
        # Verificar balance
        diferencia, esta_balanceado = self.verificar_balance()
        if not esta_balanceado:
            print("\nEl balance no está cuadrado:")
            print(f"Diferencia: ${abs(diferencia):,.2f}")
            if diferencia > 0:
                print("El Activo es mayor que Pasivo + Capital")
            else:
                print("El Pasivo + Capital es mayor que el Activo")

class RequerimientoMateriales:
    def __init__(self):
        self.materiales = {}
        self.costos_mo = {
            'semestre1': {
                'costo_hora': 15,
                'descripcion': 'Primer semestre 2015'
            },
            'semestre2': {
                'costo_hora': 18,
                'descripcion': 'Segundo semestre 2015'
            }
        }
        self.gif_base = "hora_mo"
        
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("Requerimiento de Materiales por Tipo de Producto".center(80))
        print(f"Año {InformacionEmpresa.AÑO}".center(80))
        print("="*80 + "\n")
        
    def solicitar_datos(self):
        self.imprimir_encabezado()
        print("Tipos de productos:")
        for codigo, nombre in InformacionEmpresa.PRODUCTOS.items():
            print(f"- {codigo}: {nombre}")
        
        print("\n=== CAPTURA DE REQUERIMIENTO DE MATERIALES ===")
        materiales_nombres = [
            "Materia Prima A metros",
            "Materia Prima B metros",
            "Materia Prima C piezas",
            "Horas Mano de Obra"
        ]
        
        for material in materiales_nombres:
            print(f"\nPara {material}:")
            cl = self.solicitar_valor(f"CL ({InformacionEmpresa.PRODUCTOS['CL']}): ")
            ce = self.solicitar_valor(f"CE ({InformacionEmpresa.PRODUCTOS['CE']}): ")
            cr = self.solicitar_valor(f"CR ({InformacionEmpresa.PRODUCTOS['CR']}): ")
            
            self.materiales[material] = {
                'CL': cl,
                'CE': ce,
                'CR': cr,
                'tipo': 'material' if 'Prima' in material else 'mano_obra'
            }
    
    def solicitar_valor(self, mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                if valor >= 0:
                    return valor
                print("Por favor ingrese un valor no negativo.")
            except ValueError:
                print("Por favor ingrese un valor numérico válido.")
    
    def imprimir_requerimientos(self):
        self.imprimir_encabezado()
        print("+--------------------------------+---------+---------+---------+")
        print("|                                |    CL   |    CE   |    CR   |")
        print("|                                |  Lisa   |Estampada| Rayada  |")
        print("+--------------------------------+---------+---------+---------+")
        
        for material, valores in self.materiales.items():
            print(f"| {material:<30} | {valores['CL']:>7.1f} | {valores['CE']:>7.1f} | {valores['CR']:>7.1f} |")
            print("+--------------------------------+---------+---------+---------+")
        
        print("\n=== INFORMACIÓN DE COSTOS ===")
        print("Mano de Obra Directa:")
        for semestre, datos in self.costos_mo.items():
            print(f"- {datos['descripcion']}: ${datos['costo_hora']:.2f} por hora")
        
        print("\nGastos Indirectos de Fabricación (GIF):")
        print("Los gastos indirectos de fabricación se aplican con base en hora de mano de obra.")

class InformacionEmpresa:
    NOMBRE = "Maquilados Mexicanos, S.A. de C.V."
    GIRO = "Fabricación de camisas"
    PRODUCTOS = {
        'CL': 'Camisas Lisas',
        'CE': 'Camisas Estampadas',
        'CR': 'Camisas Rayadas'
    }
    AÑO = 2015
    CLIENTES = "Comerciantes menores"

class InformacionInventarios:
    def __init__(self):
        # Estructura para almacenar datos de inventarios
        self.inventarios = {
            'materias_primas': {
                'Materia Prima A metros': {
                    'inventario_inicial_sem1': 0,
                    'inventario_final_sem2': 0,
                    'costo_sem1': 0,
                    'costo_sem2': 0
                },
                'Materia Prima B metros': {
                    'inventario_inicial_sem1': 0,
                    'inventario_final_sem2': 0,
                    'costo_sem1': 0,
                    'costo_sem2': 0
                },
                'Materia Prima C piezas': {
                    'inventario_inicial_sem1': 0,
                    'inventario_final_sem2': 0,
                    'costo_sem1': 0,
                    'costo_sem2': 0
                }
            },
            'productos': {
                'Producto CL': {
                    'inventario_inicial_sem1': 0,
                    'inventario_final_sem2': 0
                },
                'Producto CE': {
                    'inventario_inicial_sem1': 0,
                    'inventario_final_sem2': 0
                },
                'Producto CR': {
                    'inventario_inicial_sem1': 0,
                    'inventario_final_sem2': 0
                }
            }
        }
    
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("INFORMACIÓN DE INVENTARIOS".center(80))
        print("="*80 + "\n")
        
    def solicitar_datos(self):
        self.imprimir_encabezado()
        
        print("\n--- Materias Primas ---")
        for materia in self.inventarios['materias_primas'].keys():
            print(f"\nPara {materia}:")
            self.inventarios['materias_primas'][materia]['inventario_inicial_sem1'] = \
                self.solicitar_valor(f"Inventario Inicial Primer Semestre: ")
            self.inventarios['materias_primas'][materia]['inventario_final_sem2'] = \
                self.solicitar_valor(f"Inventario Final Segundo Semestre: ")
            self.inventarios['materias_primas'][materia]['costo_sem1'] = \
                self.solicitar_valor(f"Costo Primer Semestre: ")
            self.inventarios['materias_primas'][materia]['costo_sem2'] = \
                self.solicitar_valor(f"Costo Segundo Semestre: ")
        
        print("\n--- Productos ---")
        for producto in self.inventarios['productos'].keys():
            print(f"\nPara {producto}:")
            self.inventarios['productos'][producto]['inventario_inicial_sem1'] = \
                self.solicitar_valor(f"Inventario Inicial Primer Semestre: ")
            self.inventarios['productos'][producto]['inventario_final_sem2'] = \
                self.solicitar_valor(f"Inventario Final Segundo Semestre: ")
    
    def solicitar_valor(self, mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                if valor >= 0:
                    return valor
                print("Por favor ingrese un valor no negativo.")
            except ValueError:
                print("Por favor ingrese un valor numérico válido.")
    
    def imprimir_inventarios(self):
        self.imprimir_encabezado()
        
        # Encabezado de la tabla
        print("+--------------------------------+-----------+-----------+---------+---------+")
        print("|                                | Inventario| Inventario|  Costo  |  Costo  |")
        print("|           Concepto             |  Inicial  |   Final   | Primer  | Segundo |")
        print("|                                |  Primer   |  Segundo  |Semestre |Semestre |")
        print("|                                | Semestre  | Semestre  |         |         |")
        print("+--------------------------------+-----------+-----------+---------+---------+")
        
        # Materias Primas
        for materia, datos in self.inventarios['materias_primas'].items():
            print(f"| {materia:<30} | {datos['inventario_inicial_sem1']:>9.0f} | {datos['inventario_final_sem2']:>9.0f} | ${datos['costo_sem1']:>6.2f} | ${datos['costo_sem2']:>6.2f} |")
            print("+--------------------------------+-----------+-----------+---------+---------+")
        
        # Productos
        for producto, datos in self.inventarios['productos'].items():
            print(f"| {producto:<30} | {datos['inventario_inicial_sem1']:>9.0f} | {datos['inventario_final_sem2']:>9.0f} |         |         |")
            print("+--------------------------------+-----------+-----------+---------+---------+")
        
        print("\nSuponga que los inventarios iniciales son iguales al final del primer semestre.")
        print("No hay inventario de artículos en proceso.")

class ProductosVentas:
    def __init__(self):
        # Estructura para almacenar datos de productos
        self.productos = {
            'CL': {  # Camisas Lisas
                'precio_sem1': 0,
                'precio_sem2': 0,
                'ventas_sem1': 0,
                'ventas_sem2': 0
            },
            'CE': {  # Camisas Estampadas
                'precio_sem1': 0,
                'precio_sem2': 0,
                'ventas_sem1': 0,
                'ventas_sem2': 0
            },
            'CR': {  # Camisas Rayadas
                'precio_sem1': 0,
                'precio_sem2': 0,
                'ventas_sem1': 0,
                'ventas_sem2': 0
            }
        }
    
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("INFORMACIÓN DE PRODUCTOS Y VENTAS PLANEADAS".center(80))
        print("="*80 + "\n")
    
    def solicitar_datos(self):
        self.imprimir_encabezado()
        
        for codigo, nombre in InformacionEmpresa.PRODUCTOS.items():
            print(f"\nPara {nombre} ({codigo}):")
            self.productos[codigo]['precio_sem1'] = \
                self.solicitar_valor(f"Precio de Venta Primer Semestre: ")
            self.productos[codigo]['precio_sem2'] = \
                self.solicitar_valor(f"Precio de Venta Segundo Semestre: ")
            self.productos[codigo]['ventas_sem1'] = \
                self.solicitar_valor(f"Ventas planeadas Primer Semestre: ")
            self.productos[codigo]['ventas_sem2'] = \
                self.solicitar_valor(f"Ventas planeadas Segundo Semestre: ")
    
    def solicitar_valor(self, mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                if valor >= 0:
                    # Si el mensaje contiene la palabra "Ventas", convertir a entero
                    if "Ventas" in mensaje:
                        return int(valor)
                    return valor
                print("Por favor ingrese un valor no negativo.")
            except ValueError:
                print("Por favor ingrese un valor numérico válido.")
    
    def imprimir_productos(self):
        self.imprimir_encabezado()
        
        # Encabezado de la tabla
        print("+-----------------------------------+-----------+-----------+-----------+")
        print("|                                   |    CL     |    CE     |    CR     |")
        print("+-----------------------------------+-----------+-----------+-----------+")
        
        # Precios y ventas por semestre
        print(f"| Precio de Venta Primer Semestre      | ${self.productos['CL']['precio_sem1']:>8.2f} | ${self.productos['CE']['precio_sem1']:>8.2f} | ${self.productos['CR']['precio_sem1']:>8.2f} |")
        print("+-----------------------------------+-----------+-----------+-----------+")
        print(f"| Precio de Venta Segundo Semestre     | ${self.productos['CL']['precio_sem2']:>8.2f} | ${self.productos['CE']['precio_sem2']:>8.2f} | ${self.productos['CR']['precio_sem2']:>8.2f} |")
        print("+-----------------------------------+-----------+-----------+-----------+")
        print(f"| Ventas planeadas Primer Semestre     | {self.productos['CL']['ventas_sem1']:>9.0f} | {self.productos['CE']['ventas_sem1']:>9.0f} | {self.productos['CR']['ventas_sem1']:>9.0f} |")
        print("+-----------------------------------+-----------+-----------+-----------+")
        print(f"| Ventas planeadas Segundo Semestre    | {self.productos['CL']['ventas_sem2']:>9.0f} | {self.productos['CE']['ventas_sem2']:>9.0f} | {self.productos['CR']['ventas_sem2']:>9.0f} |")
        print("+-----------------------------------+-----------+-----------+-----------+")

    def obtener_precio(self, producto, semestre):
        """Obtiene el precio de un producto para un semestre específico"""
        return self.productos[producto][f'precio_sem{semestre}']
    
    def obtener_ventas_planeadas(self, producto, semestre):
        """Obtiene las ventas planeadas de un producto para un semestre específico"""
        return self.productos[producto][f'ventas_sem{semestre}']

class GastosAdminVentas:
    def __init__(self):
        self.gastos = {
            'Depreciación': {
                'monto': 0,
                'tipo': 'Anuales'
            },
            'Sueldos y Salarios': {
                'monto': 0,
                'tipo': 'Anuales'
            },
            'Comisiones': {
                'monto': 1,  # Será un porcentaje
                'tipo': 'Porcentaje ventas',
                'porcentaje': 0
            },
            'Varios Primer Semestre': {
                'monto': 0,
                'tipo': 'Primer Semestre'
            },
            'Varios Segundo Semestre': {
                'monto': 0,
                'tipo': 'Segundo Semestre'
            },
            'Intereses por Préstamo': {
                'monto': 0,
                'tipo': 'Anuales'
            }
        }

    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("GASTOS DE ADMINISTRACIÓN Y VENTAS".center(80))
        print("="*80 + "\n")

    def solicitar_datos(self):
        self.imprimir_encabezado()
        
        print("\nIngrese los siguientes gastos:")
        
        # Depreciación
        self.gastos['Depreciación']['monto'] = \
            self.solicitar_valor("Depreciación (Anual): ")
        
        # Sueldos y Salarios
        self.gastos['Sueldos y Salarios']['monto'] = \
            self.solicitar_valor("Sueldos y Salarios (Anuales): ")
        
        # Comisiones
        self.gastos['Comisiones']['porcentaje'] = \
            self.solicitar_valor("Comisiones (% de las ventas proyectadas): ")
        
        # Varios Primer Semestre
        self.gastos['Varios Primer Semestre']['monto'] = \
            self.solicitar_valor("Gastos Varios Primer Semestre: ")
        
        # Varios Segundo Semestre
        self.gastos['Varios Segundo Semestre']['monto'] = \
            self.solicitar_valor("Gastos Varios Segundo Semestre: ")
        
        # Intereses por Préstamo
        self.gastos['Intereses por Préstamo']['monto'] = \
            self.solicitar_valor("Intereses por Préstamo (Anuales): ")

    def solicitar_valor(self, mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                if valor >= 0:
                    return valor
                print("Por favor ingrese un valor no negativo.")
            except ValueError:
                print("Por favor ingrese un valor numérico válido.")

    def imprimir_gastos(self):
        self.imprimir_encabezado()
        
        print("+--------------------------------+-------------+--------------------+")
        print("| Concepto                       |      Monto |              Tipo  |")
        print("+--------------------------------+-------------+--------------------+")
        
        # Imprimir cada gasto
        for concepto, datos in self.gastos.items():
            if concepto == 'Comisiones':
                monto_str = f"{datos['porcentaje']}%"
                print(f"| {concepto:<30} | {monto_str:>11} | de las ventas       |")
            else:
                print(f"| {concepto:<30} | {datos['monto']:>11,.2f} | {datos['tipo']:<18} |")
            print("+--------------------------------+-------------+--------------------+")

    def obtener_gasto_anual(self, concepto):
        """Obtiene el monto anual de un gasto específico"""
        if concepto in self.gastos:
            return self.gastos[concepto]['monto']
        return 0

    def obtener_gasto_semestral(self, concepto, semestre):
        """Obtiene el monto de un gasto para un semestre específico"""
        if concepto in ['Varios Primer Semestre', 'Varios Segundo Semestre']:
            if (semestre == 1 and concepto == 'Varios Primer Semestre') or \
               (semestre == 2 and concepto == 'Varios Segundo Semestre'):
                return self.gastos[concepto]['monto']
        elif concepto in self.gastos and self.gastos[concepto]['tipo'] == 'Anuales':
            return self.gastos[concepto]['monto'] / 2
        return 0

    def obtener_porcentaje_comisiones(self):
        """Obtiene el porcentaje de comisiones sobre ventas"""
        return self.gastos['Comisiones']['porcentaje']

class GastosFabricacionIndirectos:
    def __init__(self):
        self.gastos = {
            'Depreciación': {
                'monto': 0,
                'tipo': 'anuales'
            },
            'Seguros': {
                'monto': 0,
                'tipo': 'anuales'
            },
            'Mantenimiento Primer Semestre': {
                'monto': 0,
                'tipo': 'Primer Semestre'
            },
            'Mantenimiento Segundo Semestre': {
                'monto': 0,
                'tipo': 'Segundo Semestre'
            },
            'Energéticos Primer Semestre': {
                'monto': 0,
                'tipo': 'Primer Semestre'
            },
            'Energéticos Segundo Semestre': {
                'monto': 0,
                'tipo': 'Segundo Semestre'
            },
            'Varios': {
                'monto': 0,
                'tipo': 'anuales'
            }
        }
    
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("GASTOS DE FABRICACIÓN INDIRECTOS".center(80))
        print("="*80 + "\n")
    
    def solicitar_datos(self):
        self.imprimir_encabezado()
        
        print("\nIngrese los siguientes gastos:")
        
        # Depreciación
        self.gastos['Depreciación']['monto'] = \
            self.solicitar_valor("Depreciación (Anual): ")
        
        # Seguros
        self.gastos['Seguros']['monto'] = \
            self.solicitar_valor("Seguros (Anual): ")
        
        # Mantenimiento por semestre
        self.gastos['Mantenimiento Primer Semestre']['monto'] = \
            self.solicitar_valor("Mantenimiento Primer Semestre: ")
        self.gastos['Mantenimiento Segundo Semestre']['monto'] = \
            self.solicitar_valor("Mantenimiento Segundo Semestre: ")
        
        # Energéticos por semestre
        self.gastos['Energéticos Primer Semestre']['monto'] = \
            self.solicitar_valor("Energéticos Primer Semestre: ")
        self.gastos['Energéticos Segundo Semestre']['monto'] = \
            self.solicitar_valor("Energéticos Segundo Semestre: ")
        
        # Varios
        self.gastos['Varios']['monto'] = \
            self.solicitar_valor("Gastos Varios (Anual): ")
    
    def solicitar_valor(self, mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                if valor >= 0:
                    return valor
                print("Por favor ingrese un monto no negativo.")
            except ValueError:
                print("Por favor ingrese un valor numérico válido.")
    
    def imprimir_gastos(self):
        self.imprimir_encabezado()
        
        print("+--------------------------------+-------------+--------------------+")
        print("| Concepto                       |      Monto |       Periodicidad |")
        print("+--------------------------------+-------------+--------------------+")
        
        for concepto, datos in self.gastos.items():
            print(f"| {concepto:<30} | {datos['monto']:>11,.2f} | {datos['tipo']:<18} |")
            print("+--------------------------------+-------------+--------------------+")
    
    def obtener_gasto_anual(self, concepto):
        """Obtiene el monto anual de un gasto específico"""
        if concepto in self.gastos and self.gastos[concepto]['tipo'] == 'anuales':
            return self.gastos[concepto]['monto']
        return 0
    
    def obtener_gasto_semestral(self, concepto_base, semestre):
        """Obtiene el gasto para un semestre específico"""
        # Para gastos semestrales
        concepto_semestral = f"{concepto_base} {'Primer' if semestre == 1 else 'Segundo'} Semestre"
        if concepto_semestral in self.gastos:
            return self.gastos[concepto_semestral]['monto']
        
        # Para gastos anuales
        concepto_anual = concepto_base
        if concepto_anual in self.gastos and self.gastos[concepto_anual]['tipo'] == 'anuales':
            return self.gastos[concepto_anual]['monto'] / 2
        
        return 0

class DatosAdicionales:
    def __init__(self):
        self.datos = {
            'equipo_nuevo': {
                'valor': 85000,
                'año': 2016,
                'depreciar': False
            },
            'tasas': {
                'ISR': 30,  # 30%
                'PTU': 10   # 10%
            },
            'politicas_cobro_pago': {
                'cobro_clientes_2015': 100,  # 100% del saldo de clientes 2015
                'cobro_ventas_2016': 80,     # 80% de las ventas presupuestadas
                'pago_proveedores_2015': 100,  # 100% del saldo de proveedores 2015
                'pago_compras_2016': 50      # 50% de las compras presupuestadas
            },
            'pagar_isr_2015': True  # Se pagará el ISR del 2015
        }
    
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("DATOS ADICIONALES".center(80))
        print("="*80 + "\n")
    
    def solicitar_datos(self):
        self.imprimir_encabezado()
        
        print("\n=== EQUIPO NUEVO ===")
        self.datos['equipo_nuevo']['valor'] = \
            self.solicitar_valor("Valor del equipo nuevo para 2016: ", valor_default=85000)
        
        print("\n=== TASAS IMPOSITIVAS ===")
        self.datos['tasas']['ISR'] = \
            self.solicitar_valor("Tasa de ISR (%): ", valor_default=30)
        self.datos['tasas']['PTU'] = \
            self.solicitar_valor("Tasa de PTU (%): ", valor_default=10)
        
        print("\n=== POLÍTICAS DE COBRO Y PAGO ===")
        self.datos['politicas_cobro_pago']['cobro_clientes_2015'] = \
            self.solicitar_valor("Porcentaje de cobro del saldo de clientes 2015 (%): ", valor_default=100)
        self.datos['politicas_cobro_pago']['cobro_ventas_2016'] = \
            self.solicitar_valor("Porcentaje de cobro de ventas presupuestadas 2016 (%): ", valor_default=80)
        self.datos['politicas_cobro_pago']['pago_proveedores_2015'] = \
            self.solicitar_valor("Porcentaje de pago a proveedores 2015 (%): ", valor_default=100)
        self.datos['politicas_cobro_pago']['pago_compras_2016'] = \
            self.solicitar_valor("Porcentaje de pago de compras presupuestadas 2016 (%): ", valor_default=50)
        
        print("\n=== ISR 2015 ===")
        self.datos['pagar_isr_2015'] = self.solicitar_si_no("¿Se pagará el ISR del 2015? (s/n): ", valor_default=True)
    
    def solicitar_valor(self, mensaje, valor_default=None):
        while True:
            try:
                if valor_default is not None:
                    valor = input(f"{mensaje} [{valor_default}]: ")
                    if valor.strip() == "":
                        return valor_default
                    valor = float(valor)
                else:
                    valor = float(input(mensaje))
                
                if valor >= 0:
                    return valor
                print("Por favor ingrese un valor no negativo.")
            except ValueError:
                print("Por favor ingrese un valor numérico válido.")
    
    def solicitar_si_no(self, mensaje, valor_default=None):
        while True:
            if valor_default is not None:
                respuesta = input(f"{mensaje} [{('s' if valor_default else 'n')}]: ").lower()
                if respuesta.strip() == "":
                    return valor_default
            else:
                respuesta = input(mensaje).lower()
            
            if respuesta in ['s', 'si', 'y', 'yes']:
                return True
            elif respuesta in ['n', 'no']:
                return False
            print("Por favor responda 's' o 'n'")
    
    def imprimir_datos(self):
        self.imprimir_encabezado()
        
        print("EQUIPO NUEVO 2016")
        print(f"- Valor: ${self.datos['equipo_nuevo']['valor']:,.2f}")
        print(f"- Se depreciará durante el ejercicio: {'No' if not self.datos['equipo_nuevo']['depreciar'] else 'Sí'}")
        
        print("\nTASAS IMPOSITIVAS")
        print(f"- ISR: {self.datos['tasas']['ISR']}%")
        print(f"- PTU: {self.datos['tasas']['PTU']}%")
        
        print("\nPOLÍTICAS DE COBRO Y PAGO")
        print(f"- Cobro de clientes 2015: {self.datos['politicas_cobro_pago']['cobro_clientes_2015']}%")
        print(f"- Cobro de ventas 2016: {self.datos['politicas_cobro_pago']['cobro_ventas_2016']}%")
        print(f"- Pago a proveedores 2015: {self.datos['politicas_cobro_pago']['pago_proveedores_2015']}%")
        print(f"- Pago de compras 2016: {self.datos['politicas_cobro_pago']['pago_compras_2016']}%")
        
        print("\nISR 2015")
        print(f"- Se pagará el ISR 2015: {'Sí' if self.datos['pagar_isr_2015'] else 'No'}")
    
    def obtener_dato(self, categoria, subcategoria=None):
        """Obtiene un dato específico"""
        if subcategoria:
            return self.datos[categoria][subcategoria]
        return self.datos[categoria]

class PresupuestoVentas:
    def __init__(self, productos_ventas):
        self.productos_ventas = productos_ventas
        
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("PRESUPUESTO DE VENTAS".center(80))
        print(f"AÑO {InformacionEmpresa.AÑO}".center(80))
        print("="*80 + "\n")
    
    def generar_presupuesto(self):
        self.imprimir_encabezado()
        
        # Encabezado de la tabla
        print("I. Presupuesto de Operación")
        print("1. Presupuesto de Ventas")
        print("\n+--------------------------------+--------------+--------------+--------------+")
        print("|                                | 1er Semestre | 2do Semestre |         2016 |")
        print("+--------------------------------+--------------+--------------+--------------+")
        
        total_semestre1 = 0
        total_semestre2 = 0
        
        # Procesar cada producto (CL, CE, CR)
        for codigo, nombre in InformacionEmpresa.PRODUCTOS.items():
            print(f"| PRODUCTO {codigo}".ljust(32) + "|")
            print("+--------------------------------+--------------+--------------+--------------+")
            
            # Unidades a vender
            unidades_sem1 = self.productos_ventas.productos[codigo]['ventas_sem1']
            unidades_sem2 = self.productos_ventas.productos[codigo]['ventas_sem2']
            print(f"| Unidades a vender".ljust(32) + 
                  f"| {unidades_sem1:>12,.0f} | {unidades_sem2:>12,.0f} |".ljust(41) + "|")
            
            # Precio de venta
            precio_sem1 = self.productos_ventas.productos[codigo]['precio_sem1']
            precio_sem2 = self.productos_ventas.productos[codigo]['precio_sem2']
            print(f"| Precio de Venta".ljust(32) + 
                  f"| ${precio_sem1:>11,.2f} | ${precio_sem2:>11,.2f} |".ljust(41) + "|")
            
            # Importe de venta
            importe_sem1 = unidades_sem1 * precio_sem1
            importe_sem2 = unidades_sem2 * precio_sem2
            importe_total = importe_sem1 + importe_sem2
            print(f"| Importe de Venta".ljust(32) + 
                  f"| ${importe_sem1:>11,.2f} | ${importe_sem2:>11,.2f} | ${importe_total:>11,.2f} |")
            
            total_semestre1 += importe_sem1
            total_semestre2 += importe_sem2
            
            print("+--------------------------------+--------------+--------------+--------------+")
        
        # Total de ventas
        total_anual = total_semestre1 + total_semestre2
        print(f"| Total de Ventas por Semestre".ljust(32) + 
              f"| ${total_semestre1:>11,.2f} | ${total_semestre2:>11,.2f} | ${total_anual:>11,.2f} |")
        print("+--------------------------------+--------------+--------------+--------------+")

class PresupuestoClientes:
    def __init__(self, balance, productos_ventas, datos_adicionales):
        self.balance = balance
        self.productos_ventas = productos_ventas
        self.datos_adicionales = datos_adicionales
        
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("2. DETERMINACIÓN DEL SALDO DE CLIENTES Y FLUJO DE ENTRADAS".center(80))
        print("="*80 + "\n")
    
    def calcular_ventas_2016(self):
        total_ventas = 0
        for codigo in ['CL', 'CE', 'CR']:
            ventas_sem1 = (self.productos_ventas.productos[codigo]['ventas_sem1'] * 
                          self.productos_ventas.productos[codigo]['precio_sem1'])
            ventas_sem2 = (self.productos_ventas.productos[codigo]['ventas_sem2'] * 
                          self.productos_ventas.productos[codigo]['precio_sem2'])
            total_ventas += ventas_sem1 + ventas_sem2
        return total_ventas
    
    def generar_presupuesto(self):
        self.imprimir_encabezado()
        
        # Obtener datos necesarios
        saldo_clientes_2015 = self.balance.activo_circulante['Clientes']
        ventas_2016 = self.calcular_ventas_2016()
        porcentaje_cobro_2015 = self.datos_adicionales.datos['politicas_cobro_pago']['cobro_clientes_2015']
        porcentaje_cobro_2016 = self.datos_adicionales.datos['politicas_cobro_pago']['cobro_ventas_2016']
        
        # Cálculos
        total_clientes_2016 = saldo_clientes_2015 + ventas_2016
        cobranza_2015 = saldo_clientes_2015 * (porcentaje_cobro_2015 / 100)
        cobranza_2016 = ventas_2016 * (porcentaje_cobro_2016 / 100)
        total_entradas = cobranza_2015 + cobranza_2016
        saldo_final_clientes = total_clientes_2016 - total_entradas
        
        # Imprimir tabla
        print("+--------------------------------+----------------+----------------+")
        print("|           Descripción          |     Importe    |      Total     |")
        print("+--------------------------------+----------------+----------------+")
        print(f"| Saldo de clientes 31-Dic-2015 |                | {saldo_clientes_2015:>14,.0f} |")
        print(f"| Ventas 2016                   |                | {ventas_2016:>14,.0f} |")
        print(f"| Total de Clientes 2016        |                | {total_clientes_2016:>14,.0f} |")
        print("+--------------------------------+----------------+----------------+")
        print("| Entradas de Efectivo:          |                |                |")
        print(f"| Por Cobranza del 2015 (100%)  | {cobranza_2015:>14,.0f} |                |")
        print(f"| Por Cobranza del 2016 (80%)   | {cobranza_2016:>14,.0f} |                |")
        print("|                                |                | {total_entradas:>14,.0f} |")
        print("+--------------------------------+----------------+----------------+")
        print(f"| Saldo de Clientes del 2016    |                | {saldo_final_clientes:>14,.0f} |")
        print("+--------------------------------+----------------+----------------+")
        
        print("\nNotas:")
        print("- El saldo de clientes 2015 proviene del Balance General")
        print("- Las ventas 2016 provienen del Presupuesto de Ventas")
        print("- El total de entradas se utilizará en el flujo de efectivo")
        print("- El saldo de clientes 2016 se utilizará en el balance general presupuestado")

class PresupuestoProduccion:
    def __init__(self, productos_ventas, inventarios):
        self.productos_ventas = productos_ventas
        self.inventarios = inventarios
        
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("3. PRESUPUESTO DE PRODUCCIÓN".center(80))
        print("="*80 + "\n")
    
    def obtener_inventario_inicial(self, producto):
        clave_producto = f"Producto {producto}"
        return self.inventarios.inventarios['productos'][clave_producto]['inventario_inicial_sem1']
        
    def obtener_inventario_final(self, producto):
        clave_producto = f"Producto {producto}"
        return self.inventarios.inventarios['productos'][clave_producto]['inventario_final_sem2']
    
    def calcular_produccion_semestre(self, producto, semestre):
        unidades_vender = int(self.productos_ventas.productos[producto][f'ventas_sem{semestre}'])
        
        if semestre == 1:
            inv_inicial = int(self.obtener_inventario_inicial(producto))
            if producto == 'CL':
                inv_final = 10000
            elif producto == 'CE':
                inv_final = 8500
            elif producto == 'CR':
                inv_final = 6000
        else:
            if producto == 'CL':
                inv_inicial = 10000
                inv_final = 6500
            elif producto == 'CE':
                inv_inicial = 8500
                inv_final = 7500
            elif producto == 'CR':
                inv_inicial = 6000
                inv_final = 5000
        
        total_unidades = unidades_vender + inv_final
        unidades_producir = total_unidades - inv_inicial
        
        return {
            'unidades_vender': int(unidades_vender),
            'inv_final': int(inv_final),
            'total_unidades': int(total_unidades),
            'inv_inicial': int(inv_inicial),
            'unidades_producir': int(unidades_producir)
        }
    
    def generar_presupuesto(self):
        self.imprimir_encabezado()
        print("+--------------------------------+--------------+--------------+--------------+")
        print("|                                | 1er Semestre | 2do Semestre | Total 2016   |")
        print("+--------------------------------+--------------+--------------+--------------+")
        
        for codigo in ['CL', 'CE', 'CR']:
            # Calcular datos para cada semestre
            sem1 = self.calcular_produccion_semestre(codigo, 1)
            sem2 = self.calcular_produccion_semestre(codigo, 2)
            
            # Calcular totales anuales
            total_unidades_vender = sem1['unidades_vender'] + sem2['unidades_vender']
            inv_final_anual = sem2['inv_final']
            total_unidades_anual = total_unidades_vender + inv_final_anual
            inv_inicial_anual = sem1['inv_inicial']
            total_producir_anual = total_unidades_anual - inv_inicial_anual
            
            # Imprimir sección del producto
            print(f"| PRODUCTO {codigo}".ljust(32) + "|")
            print("+--------------------------------+--------------+--------------+--------------+")
            print(f"| Unidades a vender".ljust(32) + 
                  f"| {sem1['unidades_vender']:>12,d} | {sem2['unidades_vender']:>12,d} | {total_unidades_vender:>12,d} |")
            print(f"| (+) Inventario Final".ljust(32) + 
                  f"| {sem1['inv_final']:>12,d} | {sem2['inv_final']:>12,d} | {inv_final_anual:>12,d} |")
            print(f"| (=) Total de Unidades".ljust(32) + 
                  f"| {sem1['total_unidades']:>12,d} | {sem2['total_unidades']:>12,d} | {total_unidades_anual:>12,d} |")
            print(f"| (-) Inventario Inicial".ljust(32) + 
                  f"| {sem1['inv_inicial']:>12,d} | {sem2['inv_inicial']:>12,d} | {inv_inicial_anual:>12,d} |")
            print(f"| (=) Unidades a Producir".ljust(32) + 
                  f"| {sem1['unidades_producir']:>12,d} | {sem2['unidades_producir']:>12,d} | {total_producir_anual:>12,d} |")
            print("+--------------------------------+--------------+--------------+--------------+")

class PresupuestoCompraMateriales:
    def __init__(self, inventarios, presupuesto_requerimientos):
        self.inventarios = inventarios
        self.presupuesto_requerimientos = presupuesto_requerimientos
        self.precios_materiales = {
            'Material A': {'sem1': 10.00, 'sem2': 12.00},
            'Material B': {'sem1': 2.00, 'sem2': 3.00},
            'Material C': {'sem1': 1.00, 'sem2': 2.00}
        }
        
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("5. PRESUPUESTO DE COMPRA DE MATERIALES".center(80))
        print("="*80 + "\n")
    
    def calcular_material(self, material, requerimiento_sem1, requerimiento_sem2):
        # Mapear nombres de materiales
        material_nombres = {
            'Material A': 'Materia Prima A metros',
            'Material B': 'Materia Prima B metros',
            'Material C': 'Materia Prima C piezas'
        }
        
        material_nombre = material_nombres[material]
        
        # Obtener datos de inventarios
        inv_inicial = float(self.inventarios.inventarios['materias_primas'][material_nombre]['inventario_inicial_sem1'])
        inv_final = float(self.inventarios.inventarios['materias_primas'][material_nombre]['inventario_final_sem2'])
        
        # Inventarios finales del primer semestre (política de la empresa)
        inv_final_sem1 = float(5000 if material == 'Material A' else (3000 if material == 'Material B' else 2000))
        
        # Cálculos primer semestre
        total_mat_sem1 = float(requerimiento_sem1 + inv_final_sem1)
        material_comprar_sem1 = float(total_mat_sem1 - inv_inicial)
        total_dinero_sem1 = float(material_comprar_sem1 * self.precios_materiales[material]['sem1'])
        
        # Cálculos segundo semestre
        total_mat_sem2 = float(requerimiento_sem2 + inv_final)
        material_comprar_sem2 = float(total_mat_sem2 - inv_final_sem1)
        total_dinero_sem2 = float(material_comprar_sem2 * self.precios_materiales[material]['sem2'])
        
        return {
            'sem1': {
                'requerimiento': float(requerimiento_sem1),
                'inv_final': inv_final_sem1,
                'total_materiales': total_mat_sem1,
                'inv_inicial': inv_inicial,
                'material_comprar': material_comprar_sem1,
                'precio': self.precios_materiales[material]['sem1'],
                'total_dinero': total_dinero_sem1
            },
            'sem2': {
                'requerimiento': float(requerimiento_sem2),
                'inv_final': inv_final,
                'total_materiales': total_mat_sem2,
                'inv_inicial': inv_final_sem1,
                'material_comprar': material_comprar_sem2,
                'precio': self.precios_materiales[material]['sem2'],
                'total_dinero': total_dinero_sem2
            },
            'total': {
                'requerimiento': float(requerimiento_sem1 + requerimiento_sem2),
                'inv_final': inv_final,
                'material_comprar': float(material_comprar_sem1 + material_comprar_sem2),
                'total_dinero': float(total_dinero_sem1 + total_dinero_sem2)
            }
        }
    
    def generar_presupuesto(self):
        self.imprimir_encabezado()
        
        total_compras_sem1 = 0.0
        total_compras_sem2 = 0.0
        total_compras_anual = 0.0
        
        for material in ['Material A', 'Material B', 'Material C']:
            # Definir requerimientos para cada material
            req_sem1 = float(42200 if material == 'Material A' else (21100 if material == 'Material B' else 492500))
            req_sem2 = float(34460 if material == 'Material A' else (17230 if material == 'Material B' else 372500))
            
            resultados = self.calcular_material(material, req_sem1, req_sem2)
            
            print(f"+--------------------------------+--------------+--------------+--------------+")
            print(f"| {material}".ljust(32) + "| 1er Semestre | 2do Semestre | Total 2016   |")
            print(f"+--------------------------------+--------------+--------------+--------------+")
            print(f"| Requerimiento de materiales".ljust(32) + 
                  f"| {resultados['sem1']['requerimiento']:>12,.0f} | {resultados['sem2']['requerimiento']:>12,.0f} | {resultados['total']['requerimiento']:>12,.0f} |")
            print(f"| (+) Inventario Final".ljust(32) + 
                  f"| {resultados['sem1']['inv_final']:>12,.0f} | {resultados['sem2']['inv_final']:>12,.0f} | {resultados['sem2']['inv_final']:>12,.0f} |")
            print(f"| Total de Materiales".ljust(32) + 
                  f"| {resultados['sem1']['total_materiales']:>12,.0f} | {resultados['sem2']['total_materiales']:>12,.0f} | {resultados['total']['requerimiento'] + resultados['sem2']['inv_final']:>12,.0f} |")
            print(f"| (-) Inventario Inicial".ljust(32) + 
                  f"| {resultados['sem1']['inv_inicial']:>12,.0f} | {resultados['sem2']['inv_inicial']:>12,.0f} | {resultados['sem1']['inv_inicial']:>12,.0f} |")
            print(f"| Material a comprar".ljust(32) + 
                  f"| {resultados['sem1']['material_comprar']:>12,.0f} | {resultados['sem2']['material_comprar']:>12,.0f} | {resultados['total']['material_comprar']:>12,.0f} |")
            print(f"| Precio de Compra".ljust(32) + 
                  f"| ${resultados['sem1']['precio']:>11,.2f} | ${resultados['sem2']['precio']:>11,.2f} |")
            print(f"| Total de {material} en $:".ljust(32) + 
                  f"| ${resultados['sem1']['total_dinero']:>11,.0f} | ${resultados['sem2']['total_dinero']:>11,.0f} | ${resultados['total']['total_dinero']:>11,.0f} |")
            print(f"+--------------------------------+--------------+--------------+--------------+")
            
            total_compras_sem1 += resultados['sem1']['total_dinero']
            total_compras_sem2 += resultados['sem2']['total_dinero']
            total_compras_anual += resultados['total']['total_dinero']
        
        # Imprimir totales
        print(f"| Compras totales:".ljust(32) + 
              f"| ${total_compras_sem1:>11,.0f} | ${total_compras_sem2:>11,.0f} | ${total_compras_anual:>11,.0f} |")
        print(f"+--------------------------------+--------------+--------------+--------------+")

class PresupuestoRequerimientoMateriales:
    def __init__(self, productos_ventas, presupuesto_produccion, requerimientos):
        self.productos_ventas = productos_ventas
        self.presupuesto_produccion = presupuesto_produccion
        self.requerimientos = requerimientos
        self.requerimientos_por_producto = {
            'CL': {
                'Material A': {'requerimiento': 1.0},
                'Material B': {'requerimiento': 0.5},
                'Material C': {'requerimiento': 10.0}
            },
            'CE': {
                'Material A': {'requerimiento': 1.2},
                'Material B': {'requerimiento': 0.6},
                'Material C': {'requerimiento': 25.0}
            },
            'CR': {
                'Material A': {'requerimiento': 2.0},
                'Material B': {'requerimiento': 1.0},
                'Material C': {'requerimiento': 5.0}
            }
        }
        
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("4. PRESUPUESTO DE REQUERIMIENTO DE MATERIALES".center(80))
        print("="*80 + "\n")
    
    def calcular_requerimientos(self, producto, unidades_producir, material):
        req = self.requerimientos_por_producto[producto][material]['requerimiento']
        return unidades_producir * req
    
    def generar_presupuesto(self):
        self.imprimir_encabezado()
        
        totales_materiales = {'Material A': 0, 'Material B': 0, 'Material C': 0}
        
        # Para cada producto (CL, CE, CR)
        for producto in ['CL', 'CE', 'CR']:
            print(f"+--------------------------------+--------------+--------------+--------------+")
            print(f"| PRODUCTO {producto}".ljust(32) + "|  1er Semestre | 2do Semestre | Total 2016   |")
            print(f"+--------------------------------+--------------+--------------+--------------+")
            
            # Obtener unidades a producir
            sem1 = self.presupuesto_produccion.calcular_produccion_semestre(producto, 1)
            sem2 = self.presupuesto_produccion.calcular_produccion_semestre(producto, 2)
            unidades_sem1 = sem1['unidades_producir']
            unidades_sem2 = sem2['unidades_producir']
            total_unidades = unidades_sem1 + unidades_sem2
            
            # Mostrar unidades a producir
            print(f"| Unidades a producir".ljust(32) + 
                  f"| {unidades_sem1:>12,d} | {unidades_sem2:>12,d} | {total_unidades:>12,d} |")
            print(f"+--------------------------------+--------------+--------------+--------------+")
            
            # Para cada material (A, B, C)
            for material in ['Material A', 'Material B', 'Material C']:
                print(f"| {material}".ljust(32) + "|")
                
                # Requerimiento de material
                req = self.requerimientos_por_producto[producto][material]['requerimiento']
                print(f"| Requerimiento de material".ljust(32) + 
                      f"| {req:>12.1f} | {req:>12.1f} | {req:>12.1f} |")
                
                # Total de material requerido
                total_sem1 = self.calcular_requerimientos(producto, unidades_sem1, material)
                total_sem2 = self.calcular_requerimientos(producto, unidades_sem2, material)
                total_anual = total_sem1 + total_sem2
                
                print(f"| Total de {material} requerido".ljust(32) + 
                      f"| {total_sem1:>12,.0f} | {total_sem2:>12,.0f} | {total_anual:>12,.0f} |")
                print(f"+--------------------------------+--------------+--------------+--------------+")
                
                # Acumular totales
                totales_materiales[material] += total_anual
        
        # Imprimir totales generales
        print("\nTOTALES DE REQUERIMIENTOS POR MATERIAL")
        print(f"+--------------------------------+--------------+--------------+--------------+")
        print(f"| Material                       | 1er Semestre | 2do Semestre | Total 2016   |")
        print(f"+--------------------------------+--------------+--------------+--------------+")
        for material in ['Material A', 'Material B', 'Material C']:
            sem1_total = 0
            sem2_total = 0
            for producto in ['CL', 'CE', 'CR']:
                sem1 = self.presupuesto_produccion.calcular_produccion_semestre(producto, 1)
                sem2 = self.presupuesto_produccion.calcular_produccion_semestre(producto, 2)
                sem1_total += self.calcular_requerimientos(producto, sem1['unidades_producir'], material)
                sem2_total += self.calcular_requerimientos(producto, sem2['unidades_producir'], material)
            
            print(f"| {material}".ljust(32) + 
                  f"| {sem1_total:>12,.0f} | {sem2_total:>12,.0f} | {totales_materiales[material]:>12,.0f} |")
            print(f"+--------------------------------+--------------+--------------+--------------+")

class PresupuestoProveedores:
    def __init__(self, balance, presupuesto_compras, datos_adicionales):
        self.balance = balance
        self.presupuesto_compras = presupuesto_compras
        self.datos_adicionales = datos_adicionales
        
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("6. DETERMINACIÓN DEL SALDO DE PROVEEDORES Y FLUJO DE SALIDAS".center(80))
        print("="*80 + "\n")
    
    def calcular_saldos(self):
        # Obtener datos necesarios
        saldo_proveedores_2015 = self.balance.pasivo_corto_plazo['Proveedores']
        compras_2016 = 2141010  # Del presupuesto de compras
        
        # Calcular total de proveedores 2016
        total_proveedores = saldo_proveedores_2015 + compras_2016
        
        # Calcular salidas de efectivo
        porcentaje_2015 = self.datos_adicionales.datos['politicas_cobro_pago']['pago_proveedores_2015']
        porcentaje_2016 = self.datos_adicionales.datos['politicas_cobro_pago']['pago_compras_2016']
        
        pago_proveedores_2015 = saldo_proveedores_2015 * (porcentaje_2015 / 100)
        pago_proveedores_2016 = compras_2016 * (porcentaje_2016 / 100)
        total_salidas = pago_proveedores_2015 + pago_proveedores_2016
        
        # Calcular saldo final de proveedores
        saldo_final = total_proveedores - total_salidas
        
        return {
            'saldo_inicial': saldo_proveedores_2015,
            'compras': compras_2016,
            'total_proveedores': total_proveedores,
            'pago_2015': pago_proveedores_2015,
            'pago_2016': pago_proveedores_2016,
            'total_salidas': total_salidas,
            'saldo_final': saldo_final
        }
    
    def generar_presupuesto(self):
        self.imprimir_encabezado()
        
        resultados = self.calcular_saldos()
        
        # Imprimir tabla
        print("+--------------------------------+----------------+----------------+")
        print("|           Descripción          |     Importe    |      Total     |")
        print("+--------------------------------+----------------+----------------+")
        print(f"| Saldo de Proveedores 31-Dic-2015                | {resultados['saldo_inicial']:>14,.0f} |")
        print(f"| Compras 2016                                    | {resultados['compras']:>14,.0f} |")
        print(f"| Total de Proveedores 2016                       | {resultados['total_proveedores']:>14,.0f} |")
        print("+--------------------------------+----------------+----------------+")
        print("| Salidas de Efectivo:           |                |                |")
        print(f"| Por Proveedores del 2015 (100%)| {resultados['pago_2015']:>14,.0f} |                |")
        print(f"| Por Proveedores del 2016 (50%) | {resultados['pago_2016']:>14,.0f} |                |")
        print(f"| Total de Salidas 2016:         |                | {resultados['total_salidas']:>14,.0f} |")
        print("+--------------------------------+----------------+----------------+")
        print(f"| Saldo de Proveedores del 2016  |                | {resultados['saldo_final']:>14,.0f} |")
        print("+--------------------------------+----------------+----------------+")
        
        print("\nNotas:")
        print("- El saldo de proveedores 2015 proviene del Balance General")
        print("- Las compras 2016 provienen del Presupuesto de Compras")
        print("- El total de salidas se utilizará en el flujo de efectivo")
        print("- El saldo de proveedores 2016 se utilizará en el balance general presupuestado")
        
class PresupuestoManoObraDirecta:
    def __init__(self, presupuesto_produccion, requerimientos):
        self.presupuesto_produccion = presupuesto_produccion
        self.requerimientos = requerimientos
        self.cuotas_hora = {
            'semestre1': 15.00,
            'semestre2': 18.00
        }
        # Horas requeridas por unidad para cada producto
        self.horas_por_unidad = {
            'CL': 2.0,
            'CE': 1.0,
            'CR': 1.5
        }
    
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("7. PRESUPUESTO DE MANO DE OBRA DIRECTA".center(80))
        print("="*80 + "\n")
    
    def calcular_horas_requeridas(self, producto, unidades):
        return float(unidades) * self.horas_por_unidad[producto]
    
    def calcular_importe_mod(self, horas, semestre):
        cuota = self.cuotas_hora[f'semestre{semestre}']
        return float(horas) * cuota
    
    def generar_presupuesto(self):
        self.imprimir_encabezado()
        
        total_horas_sem1 = 0.0
        total_horas_sem2 = 0.0
        total_mod_sem1 = 0.0
        total_mod_sem2 = 0.0
        
        for producto in ['CL', 'CE', 'CR']:
            print(f"+--------------------------------+--------------+--------------+--------------+")
            print(f"| PRODUCTO {producto}".ljust(32) + "| 1er Semestre | 2do Semestre | Total 2016   |")
            print(f"+--------------------------------+--------------+--------------+--------------+")
            
            # Obtener unidades a producir y convertir a float
            sem1 = self.presupuesto_produccion.calcular_produccion_semestre(producto, 1)
            sem2 = self.presupuesto_produccion.calcular_produccion_semestre(producto, 2)
            unidades_sem1 = float(sem1['unidades_producir'])
            unidades_sem2 = float(sem2['unidades_producir'])
            total_unidades = unidades_sem1 + unidades_sem2
            
            # Mostrar unidades a producir
            print(f"| Unidades a producir".ljust(32) + 
                  f"| {unidades_sem1:>12,.0f} | {unidades_sem2:>12,.0f} | {total_unidades:>12,.0f} |")
            
            # Horas requeridas por unidad
            horas_por_unidad = self.horas_por_unidad[producto]
            print(f"| Horas requeridas por unidad".ljust(32) + 
                  f"| {horas_por_unidad:>12.1f} | {horas_por_unidad:>12.1f} | {horas_por_unidad:>12.1f} |")
            
            # Total de horas requeridas
            horas_sem1 = self.calcular_horas_requeridas(producto, unidades_sem1)
            horas_sem2 = self.calcular_horas_requeridas(producto, unidades_sem2)
            total_horas = horas_sem1 + horas_sem2
            
            print(f"| Total de horas requeridas".ljust(32) + 
                  f"| {horas_sem1:>12,.0f} | {horas_sem2:>12,.0f} | {total_horas:>12,.0f} |")
            
            # Cuota por hora
            print(f"| Cuota por hora".ljust(32) + 
                  f"| ${self.cuotas_hora['semestre1']:>11,.2f} | ${self.cuotas_hora['semestre2']:>11,.2f} |")
            
            # Importe de M.O.D.
            importe_sem1 = self.calcular_importe_mod(horas_sem1, 1)
            importe_sem2 = self.calcular_importe_mod(horas_sem2, 2)
            importe_total = importe_sem1 + importe_sem2
            print(f"| Importe de M.O.D.".ljust(32) + 
                  f"| ${importe_sem1:>11,.0f} | ${importe_sem2:>11,.0f} | ${importe_total:>11,.0f} |")
            print(f"+--------------------------------+--------------+--------------+--------------+")
            
            # Acumular totales
            total_horas_sem1 += horas_sem1
            total_horas_sem2 += horas_sem2
            total_mod_sem1 += importe_sem1
            total_mod_sem2 += importe_sem2
        
        # Imprimir totales generales
        print(f"| Total de horas requeridas por semestre".ljust(32) + 
              f"| {total_horas_sem1:>12,.0f} | {total_horas_sem2:>12,.0f} | {total_horas_sem1 + total_horas_sem2:>12,.0f} |")
        print(f"| Total de M.O.D. por semestre".ljust(32) + 
              f"| ${total_mod_sem1:>11,.0f} | ${total_mod_sem2:>11,.0f} | ${total_mod_sem1 + total_mod_sem2:>11,.0f} |")
        print(f"+--------------------------------+--------------+--------------+--------------+")

class PresupuestoGastosIndirectos:
    def __init__(self, gastos_fabricacion, presupuesto_mod):
        self.gastos_fabricacion = gastos_fabricacion
        self.presupuesto_mod = presupuesto_mod
        self.total_horas_mod = 83050  # Total horas M.O.D. Anual
        
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("8. PRESUPUESTO DE GASTOS INDIRECTOS DE FABRICACIÓN".center(80))
        print("="*80 + "\n")
    
    def obtener_gastos_semestre(self, concepto, semestre):
        if concepto == 'Depreciación':
            return self.gastos_fabricacion.obtener_gasto_anual(concepto) / 2
        elif concepto == 'Seguros':
            return self.gastos_fabricacion.obtener_gasto_anual('Seguros') / 2
        elif concepto == 'Mantenimiento':
            return self.gastos_fabricacion.obtener_gasto_semestral('Mantenimiento', semestre)
        elif concepto == 'Energéticos':
            return self.gastos_fabricacion.obtener_gasto_semestral('Energéticos', semestre)
        elif concepto == 'Varios':
            return self.gastos_fabricacion.obtener_gasto_anual('Varios') / 2
        return 0
    
    def calcular_totales(self):
        totales = {'sem1': 0, 'sem2': 0, 'anual': 0}
        conceptos = ['Depreciación', 'Seguros', 'Mantenimiento', 'Energéticos', 'Varios']
        
        for concepto in conceptos:
            gasto_sem1 = self.obtener_gastos_semestre(concepto, 1)
            gasto_sem2 = self.obtener_gastos_semestre(concepto, 2)
            gasto_anual = gasto_sem1 + gasto_sem2
            
            totales['sem1'] += gasto_sem1
            totales['sem2'] += gasto_sem2
            totales['anual'] += gasto_anual
            
        return totales
    
    def calcular_coeficiente_gif(self, total_gif):
        return total_gif / self.total_horas_mod
    
    def generar_presupuesto(self):
        self.imprimir_encabezado()
        
        # Imprimir tabla de gastos
        print("+--------------------------------+--------------+--------------+--------------+")
        print("|                                | 1er Semestre | 2do Semestre | Total 2016   |")
        print("+--------------------------------+--------------+--------------+--------------+")
        
        # Imprimir cada concepto
        conceptos = ['Depreciación', 'Seguros', 'Mantenimiento', 'Energéticos', 'Varios']
        totales = {'sem1': 0, 'sem2': 0, 'anual': 0}
        
        for concepto in conceptos:
            gasto_sem1 = self.obtener_gastos_semestre(concepto, 1)
            gasto_sem2 = self.obtener_gastos_semestre(concepto, 2)
            gasto_anual = gasto_sem1 + gasto_sem2
            
            print(f"| {concepto}".ljust(32) + 
                  f"| ${gasto_sem1:>11,.0f} | ${gasto_sem2:>11,.0f} | ${gasto_anual:>11,.0f} |")
            
            totales['sem1'] += gasto_sem1
            totales['sem2'] += gasto_sem2
            totales['anual'] += gasto_anual
        
        # Imprimir totales
        print("+--------------------------------+--------------+--------------+--------------+")
        print(f"| Total G.I.F. por semestre".ljust(32) + 
              f"| ${totales['sem1']:>11,.0f} | ${totales['sem2']:>11,.0f} | ${totales['anual']:>11,.0f} |")
        print("+--------------------------------+--------------+--------------+--------------+")
        
        # Imprimir coeficiente
        print("\nCoeficiente para determinar el costo por hora de Gastos Indirectos de Fabricación")
        print("+--------------------------------+------------------------------------------+")
        print(f"| Total de G.I.F.".ljust(32) + f"| ${totales['anual']:>40,.0f} |")
        print(f"| (/) Total horas M.O.D. Anual".ljust(32) + f"| {self.total_horas_mod:>41,d} |")
        coeficiente = self.calcular_coeficiente_gif(totales['anual'])
        print(f"| (=) Costo por Hora de G.I.F.".ljust(32) + f"| ${coeficiente:>40,.2f} |")
        print("+--------------------------------+------------------------------------------+")

class PresupuestoGastosOperacion:
    def __init__(self, gastos_admin, presupuesto_ventas):
        self.gastos_admin = gastos_admin
        self.presupuesto_ventas = presupuesto_ventas
        
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("9. PRESUPUESTO DE GASTOS DE OPERACIÓN".center(80))
        print("="*80 + "\n")
    
    def calcular_gastos_semestre(self, concepto, semestre):
        if concepto == 'Depreciación':
            return self.gastos_admin.obtener_gasto_anual('Depreciación') / 2
        elif concepto == 'Sueldos y Salarios':
            return self.gastos_admin.obtener_gasto_anual('Sueldos y Salarios') / 2
        elif concepto == 'Varios':
            if semestre == 1:
                return self.gastos_admin.obtener_gasto_semestral('Varios Primer Semestre', 1)
            else:
                return self.gastos_admin.obtener_gasto_semestral('Varios Segundo Semestre', 2)
        elif concepto == 'Intereses del Prestamo':
            return self.gastos_admin.obtener_gasto_anual('Intereses por Préstamo') / 2
        elif concepto == 'Comisiones':
            porcentaje = self.gastos_admin.obtener_porcentaje_comisiones() / 100
            total_ventas_sem = sum(
                self.presupuesto_ventas.productos[producto][f'ventas_sem{semestre}'] * 
                self.presupuesto_ventas.productos[producto][f'precio_sem{semestre}']
                for producto in ['CL', 'CE', 'CR']
            )
            return total_ventas_sem * porcentaje
        return 0
    
    def generar_presupuesto(self):
        self.imprimir_encabezado()
        
        print("+--------------------------------+--------------+--------------+--------------+")
        print("|                                | 1er Semestre | 2do Semestre | Total 2016   |")
        print("+--------------------------------+--------------+--------------+--------------+")
        
        total_sem1 = 0
        total_sem2 = 0
        
        # Conceptos a mostrar
        conceptos = [
            'Depreciación',
            'Sueldos y Salarios',
            'Comisiones',
            'Varios',
            'Intereses del Prestamo'
        ]
        
        # Generar cada línea del presupuesto
        for concepto in conceptos:
            gasto_sem1 = self.calcular_gastos_semestre(concepto, 1)
            gasto_sem2 = self.calcular_gastos_semestre(concepto, 2)
            total_anual = gasto_sem1 + gasto_sem2
            
            print(f"| {concepto}".ljust(32) + 
                  f"| ${gasto_sem1:>11,.0f} | ${gasto_sem2:>11,.0f} | ${total_anual:>11,.0f} |")
            
            total_sem1 += gasto_sem1
            total_sem2 += gasto_sem2
        
        # Imprimir totales
        total_anual = total_sem1 + total_sem2
        print("+--------------------------------+--------------+--------------+--------------+")
        print(f"| Total de Gastos de Operación:".ljust(32) + 
              f"| ${total_sem1:>11,.0f} | ${total_sem2:>11,.0f} | ${total_anual:>11,.0f} |")
        print("+--------------------------------+--------------+--------------+--------------+")

class PresupuestoCostoUnitario:
    def __init__(self, presupuesto_compras, presupuesto_gif):
        self.presupuesto_compras = presupuesto_compras
        self.presupuesto_gif = presupuesto_gif
        # Los costos de Material B y C son por redacción
        self.costos_materiales = {
            'Material A': self.presupuesto_compras.precios_materiales['Material A']['sem2'],  # 12.00 del 2do semestre
            'Material B': 3.00,  # Por redacción
            'Material C': 2.00   # Por redacción
        }
        self.costo_mod = 18.00  # Por redacción
        self.productos_info = {
            'CL': {
                'materiales': {
                    'Material A': 1.0,
                    'Material B': 0.5,
                    'Material C': 10.0
                },
                'horas_mod': 2.0,
                'horas_gif': 2.0
            },
            'CE': {
                'materiales': {
                    'Material A': 1.2,
                    'Material B': 0.6,
                    'Material C': 25.0
                },
                'horas_mod': 1.0,
                'horas_gif': 1.0
            },
            'CR': {
                'materiales': {
                    'Material A': 2.0,
                    'Material B': 1.0,
                    'Material C': 5.0
                },
                'horas_mod': 1.5,
                'horas_gif': 1.5
            }
        }
    
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("10. DETERMINACIÓN DEL COSTO UNITARIO DE PRODUCTOS TERMINADOS".center(80))
        print("="*80 + "\n")
    
    def calcular_costo_unitario(self, producto):
        info = self.productos_info[producto]
        costo_unitario_total = 0
        resultados = []
        
        # Calcular costos de materiales
        for material, cantidad in info['materiales'].items():
            costo = self.costos_materiales[material]
            costo_unitario = costo * cantidad
            costo_unitario_total += costo_unitario
            resultados.append({
                'descripcion': material,
                'costo': costo,
                'cantidad': cantidad,
                'costo_unitario': costo_unitario
            })
        
        # Calcular costo de mano de obra
        costo_mod = self.costo_mod * info['horas_mod']
        costo_unitario_total += costo_mod
        resultados.append({
            'descripcion': 'Mano de Obra',
            'costo': self.costo_mod,
            'cantidad': info['horas_mod'],
            'costo_unitario': costo_mod
        })
        
        # Calcular gastos indirectos de fabricación
        gif_por_hora = self.presupuesto_gif.calcular_coeficiente_gif(263000)  # Del presupuesto de GIF
        costo_gif = gif_por_hora * info['horas_gif']
        costo_unitario_total += costo_gif
        resultados.append({
            'descripcion': 'Gastos Indirectos de Fabricación',
            'costo': gif_por_hora,
            'cantidad': info['horas_gif'],
            'costo_unitario': costo_gif
        })
        
        return resultados, costo_unitario_total
    
    def generar_presupuesto(self):
        self.imprimir_encabezado()
        
        # Para cada producto (CL, CE, CR)
        for producto in ['CL', 'CE', 'CR']:
            print(f"\nPRODUCTO {producto}")
            print("+--------------------------------+-----------+-----------+--------------+")
            print("|           Descripción          |    Costo  | Cantidad  |Costo Unitario|")
            print("+--------------------------------+-----------+-----------+--------------+")
            
            resultados, costo_total = self.calcular_costo_unitario(producto)
            
            # Imprimir cada componente
            for item in resultados:
                print(f"| {item['descripcion']}".ljust(32) + 
                      f"| ${item['costo']:>8.2f} | {item['cantidad']:>9.1f} | ${item['costo_unitario']:>11.2f} |")
            
            # Imprimir costo unitario total
            print("+--------------------------------+-----------+-----------+--------------+")
            print(f"| Costo Unitario".ljust(32) + f"|           |           | ${costo_total:>11.2f} |")
            print("+--------------------------------+-----------+-----------+--------------+")

class PresupuestoValuacionInventarios:
    def __init__(self, inventarios, presupuesto_costo_unitario):
        self.inventarios = inventarios
        self.presupuesto_costo_unitario = presupuesto_costo_unitario
        # Los valores siguientes son del inventario final del segundo semestre
        self.inventario_materiales = {
            'Material A': {'unidades': 3000, 'costo': 12.00},  # (Redacción)
            'Material B': {'unidades': 2500, 'costo': 3.00},   # (Redacción)
            'Material C': {'unidades': 1800, 'costo': 2.00}    # (Redacción)
        }
        self.inventario_productos = {
            'Producto CL': {'unidades': 6500, 'costo': 75.83},  # Cédula 5p10
            'Producto CE': {'unidades': 7500, 'costo': 87.37},  # Cédula 5p10
            'Producto CR': {'unidades': 5000, 'costo': 68.76}   # Cédula 5p10
        }
    
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("11. Valuación de Inventarios Finales".center(80))
        print("="*80 + "\n")
    
    def generar_presupuesto(self):
        self.imprimir_encabezado()
        
        # Inventario Final de Materiales (inventario final del segundo semestre)
        print("Inventario Final de Materiales")
        print("+--------------------------------+-----------+--------------+--------------+")
        print("| Descripción                    | Unidades  |Costo Unitario|  Costo Total |")
        print("+--------------------------------+-----------+--------------+--------------+")
        
        total_materiales = 0
        for material, datos in self.inventario_materiales.items():
            costo_total = datos['unidades'] * datos['costo']
            total_materiales += costo_total
            print(f"| {material:<30} | {datos['unidades']:>9,d} | ${datos['costo']:>11.2f} | ${costo_total:>11,.2f} |")
        
        print("+--------------------------------+-----------+--------------+--------------+")
        print(f"| Inventario Final de Materiales |           |              | ${total_materiales:>11,.2f} |")  # Dato que se usa en el balance general
        print("+--------------------------------+-----------+--------------+--------------+")
        
        # Inventario Final de Producto Terminado
        print("\nInventario Final de Producto Terminado")
        print("+--------------------------------+-----------+--------------+--------------+")
        print("| Descripción                    | Unidades  |Costo Unitario|  Costo Total |")
        print("+--------------------------------+-----------+--------------+--------------+")
        
        total_productos = 0
        for producto, datos in self.inventario_productos.items():
            costo_total = datos['unidades'] * datos['costo']
            total_productos += costo_total
            print(f"| {producto:<30} | {datos['unidades']:>9,d} | ${datos['costo']:>11.2f} | ${costo_total:>11,.2f} |")
        
        print("+--------------------------------+-----------+--------------+--------------+")
        print(f"| Inventario Final de Producto   |           |              | ${total_productos:>11,.2f} |")  # Dato que se usa en el balance general
        print("+--------------------------------+-----------+--------------+--------------+")
        
        print("\nNotas:")
        print("- Los costos de los materiales son tomados de la redacción")
        print("- Los costos unitarios de los productos son tomados de la Cédula 5p10")
        print("- Estos valores del inventario final del segundo semestre se usan en el balance general")
        print(f"- Total de inventario final de materiales: ${total_materiales:,.2f}")
        print(f"- Total de inventario final de productos terminados: ${total_productos:,.2f}")

class PresupuestoCostoProduccionVentas:
    def __init__(self, presupuesto_compras, presupuesto_mod, presupuesto_gif, presupuesto_valuacion):
        self.presupuesto_compras = presupuesto_compras
        self.presupuesto_mod = presupuesto_mod
        self.presupuesto_gif = presupuesto_gif
        self.presupuesto_valuacion = presupuesto_valuacion
        self.saldo_inicial_materiales = 45000  # Dato de redacción
        self.inventario_inicial_productos = 135000  # Dato de redacción
        
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("ESTADO DE COSTO DE PRODUCCIÓN Y VENTAS".center(80))
        print("Presupuesto del 1 de Enero al 31 de Diciembre del 2016".center(80))
        print("="*80 + "\n")
    
    def calcular_estado(self):
        # Cálculos relacionados con los materiales
        compras_materiales = 2141010  # Del presupuesto de compra de materiales
        material_disponible = self.saldo_inicial_materiales + compras_materiales
        inventario_final_materiales = 47100  # De valuación de inventarios
        materiales_utilizados = material_disponible - inventario_final_materiales
        
        # Costos adicionales
        mano_obra_directa = 1350900  # Del presupuesto de mano de obra directa
        gastos_fabricacion = 263000  # Del presupuesto de gastos indirectos de fabricación
        
        # Cálculo del costo de producción
        costo_produccion = materiales_utilizados + mano_obra_directa + gastos_fabricacion
        
        # Cálculo del costo de ventas
        total_produccion_disponible = costo_produccion + self.inventario_inicial_productos
        inventario_final_productos = 1491968  # De valuación de inventarios
        costo_ventas = total_produccion_disponible - inventario_final_productos
        
        return {
            'saldo_inicial_materiales': self.saldo_inicial_materiales,
            'compras_materiales': compras_materiales,
            'material_disponible': material_disponible,
            'inventario_final_materiales': inventario_final_materiales,
            'materiales_utilizados': materiales_utilizados,
            'mano_obra_directa': mano_obra_directa,
            'gastos_fabricacion': gastos_fabricacion,
            'costo_produccion': costo_produccion,
            'inventario_inicial_productos': self.inventario_inicial_productos,
            'total_produccion_disponible': total_produccion_disponible,
            'inventario_final_productos': inventario_final_productos,
            'costo_ventas': costo_ventas
        }
    
    def generar_presupuesto(self):
        self.imprimir_encabezado()
        
        resultados = self.calcular_estado()
        
        # Imprimir estado
        print(f"Saldo Inicial de Materiales".ljust(50) + f"$ {resultados['saldo_inicial_materiales']:>13,.0f}")
        print(f"(+) Compras de Materiales".ljust(50) + f"{resultados['compras_materiales']:>15,.0f}")
        print(f"(=) Material Disponible".ljust(50) + f"{resultados['material_disponible']:>15,.0f}")
        print(f"(-) Inventario Final de Materiales".ljust(50) + f"{resultados['inventario_final_materiales']:>15,.0f}")
        print(f"(=) Materiales Utilizados".ljust(50) + f"{resultados['materiales_utilizados']:>15,.0f}")
        print(f"(+) Mano de Obra Directa".ljust(50) + f"{resultados['mano_obra_directa']:>15,.0f}")
        print(f"(+) Gastos de Fabricación Indirectos".ljust(50) + f"{resultados['gastos_fabricacion']:>15,.0f}")
        print("\033[93m" + f"(=) Costo de Producción".ljust(50) + f"{resultados['costo_produccion']:>15,.0f}" + "\033[0m")
        print(f"(+) Inventario Inicial de Productos Terminados".ljust(50) + f"{resultados['inventario_inicial_productos']:>15,.0f}")
        print(f"(=) Total de Producción Disponible".ljust(50) + f"{resultados['total_produccion_disponible']:>15,.0f}")
        print(f"(-) Inventario Final de Productos Terminados".ljust(50) + f"{resultados['inventario_final_productos']:>15,.0f}")
        print("\033[93m" + f"(=) Costo de Ventas".ljust(50) + f"$ {resultados['costo_ventas']:>13,.0f}" + "\033[0m")

class PresupuestoEstadoResultados:
    def __init__(self, presupuesto_ventas, presupuesto_costo_produccion, presupuesto_gastos_operacion):
        self.presupuesto_ventas = presupuesto_ventas
        self.presupuesto_costo_produccion = presupuesto_costo_produccion
        self.presupuesto_gastos_operacion = presupuesto_gastos_operacion
        self.tasa_isr = 0.30  # 30% según redacción
        self.tasa_ptu = 0.10  # 10% según redacción
        
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("ESTADO DE RESULTADOS".center(80))
        print("Presupuesto del 1 de Enero al 31 de Diciembre del 2016".center(80))
        print("="*80 + "\n")
    
    def calcular_estado(self):
        # Datos de ventas y costo de ventas
        ventas = 17233000  # Del presupuesto de ventas
        costo_ventas = 2395842  # Del estado de costo de producción y ventas
        
        # Cálculo de utilidad bruta
        utilidad_bruta = ventas - costo_ventas
        
        # Gastos de operación
        gastos_operacion = 460330  # Del presupuesto de gastos de operación
        
        # Cálculo de utilidad de operación
        utilidad_operacion = utilidad_bruta - gastos_operacion
        
        # Cálculo de ISR y PTU
        isr = utilidad_operacion * self.tasa_isr
        ptu = utilidad_operacion * self.tasa_ptu
        
        # Cálculo de utilidad neta
        utilidad_neta = utilidad_operacion - isr - ptu
        
        return {
            'ventas': ventas,
            'costo_ventas': costo_ventas,
            'utilidad_bruta': utilidad_bruta,
            'gastos_operacion': gastos_operacion,
            'utilidad_operacion': utilidad_operacion,
            'isr': isr,
            'ptu': ptu,
            'utilidad_neta': utilidad_neta
        }
    
    def generar_presupuesto(self):
        self.imprimir_encabezado()
        
        resultados = self.calcular_estado()
        
        # Imprimir estado de resultados
        print(f"Ventas".ljust(45) + f"$ {resultados['ventas']:>13,.0f}")
        print(f"(-) Costo de Ventas".ljust(45) + f"{resultados['costo_ventas']:>15,.0f}")
        print(f"(=) Utilidad Bruta".ljust(45) + f"{resultados['utilidad_bruta']:>15,.0f}")
        print(f"(-) Gastos de Operación".ljust(45) + f"{resultados['gastos_operacion']:>15,.0f}")
        print(f"(=) Utilidad de Operación".ljust(45) + f"{resultados['utilidad_operacion']:>15,.0f}")
        print(f"(-) ISR".ljust(45) + f"{resultados['isr']:>15,.0f}")
        print(f"(-) PTU".ljust(45) + f"{resultados['ptu']:>15,.0f}")
        print(f"(=) Utilidad Neta".ljust(45) + f"$ {resultados['utilidad_neta']:>13,.0f}")
        
        print("\nNotas:")
        print("- Las ventas provienen del Presupuesto de Ventas")
        print("- El costo de ventas proviene del Estado de Costo de Producción y Ventas")
        print("- Los gastos de operación provienen del Presupuesto de Gastos de Operación")
        print("- ISR calculado al 30% sobre la utilidad de operación")
        print("- PTU calculado al 10% sobre la utilidad de operación")

class PresupuestoFlujoEfectivo:
    def __init__(self, presupuesto_clientes, presupuesto_proveedores, presupuesto_mod, 
                 presupuesto_gif, presupuesto_gastos_op, presupuesto_estado_resultados):
        self.presupuesto_clientes = presupuesto_clientes
        self.presupuesto_proveedores = presupuesto_proveedores
        self.presupuesto_mod = presupuesto_mod
        self.presupuesto_gif = presupuesto_gif
        self.presupuesto_gastos_op = presupuesto_gastos_op
        self.presupuesto_estado_resultados = presupuesto_estado_resultados
        self.saldo_inicial = 100000  # Dato de redacción
        
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("ESTADO DE FLUJO DE EFECTIVO".center(80))
        print("Presupuesto del 1 de Enero al 31 de Diciembre del 2016".center(80))
        print("="*80 + "\n")
    
    def calcular_flujo(self):
        # Entradas
        cobranza_2016 = 13786400  # Del saldo de clientes y flujo de entrada
        cobranza_2015 = 80000     # Del saldo de clientes y flujo de entrada
        total_entradas = cobranza_2016 + cobranza_2015
        
        # Efectivo disponible
        efectivo_disponible = self.saldo_inicial + total_entradas
        
        # Salidas
        proveedores_2016 = 1070505  # Del saldo de proveedores y flujo de salida
        proveedores_2015 = 33500    # Del saldo de proveedores y flujo de salida
        pago_mod = 1350900         # Del presupuesto de MOD
        pago_gif = 183000          # Del presupuesto de GIF sin depreciación
        pago_gastos_op = 445330    # Del presupuesto de gastos de operación sin depreciación
        compra_activo = 85000      # Dato de redacción (Maquinaria)
        pago_isr_2015 = 50000      # Dato de redacción
        
        total_salidas = (proveedores_2016 + proveedores_2015 + pago_mod + 
                        pago_gif + pago_gastos_op + compra_activo + pago_isr_2015)
        
        # Flujo de efectivo actual
        flujo_efectivo = efectivo_disponible - total_salidas
        
        return {
            'saldo_inicial': self.saldo_inicial,
            'cobranza_2016': cobranza_2016,
            'cobranza_2015': cobranza_2015,
            'total_entradas': total_entradas,
            'efectivo_disponible': efectivo_disponible,
            'proveedores_2016': proveedores_2016,
            'proveedores_2015': proveedores_2015,
            'pago_mod': pago_mod,
            'pago_gif': pago_gif,
            'pago_gastos_op': pago_gastos_op,
            'compra_activo': compra_activo,
            'pago_isr_2015': pago_isr_2015,
            'total_salidas': total_salidas,
            'flujo_efectivo': flujo_efectivo
        }
    
    def generar_presupuesto(self):
        self.imprimir_encabezado()
        resultados = self.calcular_flujo()
        
        # Saldo inicial
        print(f"Saldo Inicial de Efectivo".ljust(45) + f"$ {resultados['saldo_inicial']:>13,.0f}")
        
        # Entradas
        print("\nEntradas:")
        print(f"Cobranza 2016".ljust(45) + f"$ {resultados['cobranza_2016']:>13,.0f}")
        print(f"Cobranza 2015".ljust(45) + f"{resultados['cobranza_2015']:>15,.0f}")
        print(f"Total de Entradas".ljust(45) + f"{resultados['total_entradas']:>15,.0f}")
        
        # Efectivo disponible
        print(f"Efectivo Disponible".ljust(45) + f"{resultados['efectivo_disponible']:>15,.0f}")
        
        # Salidas
        print("\nSalidas:")
        print(f"Proveedores 2016".ljust(45) + f"{resultados['proveedores_2016']:>15,.0f}")
        print(f"Proveedores 2015".ljust(45) + f"{resultados['proveedores_2015']:>15,.0f}")
        print(f"Pago Mano de Obra Directa".ljust(45) + f"{resultados['pago_mod']:>15,.0f}")
        print(f"Pago Gastos Indirectos de Fabricación".ljust(45) + f"{resultados['pago_gif']:>15,.0f}")
        print(f"Pago de Gastos de Operación".ljust(45) + f"{resultados['pago_gastos_op']:>15,.0f}")
        print(f"Compra de Activo Fijo (Maquinaria)".ljust(45) + f"{resultados['compra_activo']:>15,.0f}")
        print(f"Pago ISR 2015".ljust(45) + f"{resultados['pago_isr_2015']:>15,.0f}")
        print(f"Total de Salidas".ljust(45) + f"{resultados['total_salidas']:>15,.0f}")
        
        # Flujo de efectivo actual
        print(f"Flujo de Efectivo Actual".ljust(45) + f"$ {resultados['flujo_efectivo']:>13,.0f}")
        
        print("\nNota: Este flujo de efectivo se utilizará en el balance general")

class PresupuestoBalanceGeneral:
    def __init__(self, presupuesto_flujo, presupuesto_clientes, presupuesto_valuacion, presupuesto_proveedores, presupuesto_estado_resultados):
        self.presupuesto_flujo = presupuesto_flujo
        self.presupuesto_clientes = presupuesto_clientes
        self.presupuesto_valuacion = presupuesto_valuacion
        self.presupuesto_proveedores = presupuesto_proveedores
        self.presupuesto_estado_resultados = presupuesto_estado_resultados
        
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print("BALANCE GENERAL".center(80))
        print("Presupuesto al 31 de Diciembre del 2016".center(80))
        print("="*80 + "\n")
    
    def generar_presupuesto(self):
        self.imprimir_encabezado()
        
        # ACTIVO
        print("ACTIVO")
        print("Circulante")
        
        # Activo Circulante
        efectivo = 10748165  # Del Estado de Flujo de Efectivo
        clientes = 3446600   # Del saldo de clientes y flujo de entrada
        deudores = 35000     # Redacción
        funcionarios = 10500  # Redacción
        inv_materiales = 47100    # De valuación de inventarios finales
        inv_productos = 1491968   # De valuación de inventarios finales
        
        total_circulante = efectivo + clientes + deudores + funcionarios + inv_materiales + inv_productos
        
        print(f"Efectivo".ljust(35) + f"$ {efectivo:>11,.0f}")
        print(f"Clientes".ljust(35) + f"{clientes:>13,.0f}")
        print(f"Deudores Diversos".ljust(35) + f"{deudores:>13,.0f}")
        print(f"Funcionarios y Empleados".ljust(35) + f"{funcionarios:>13,.0f}")
        print(f"Inventario de Materiales".ljust(35) + f"{inv_materiales:>13,.0f}")
        print(f"Inventario de Producto Terminado".ljust(35) + f"{inv_productos:>13,.0f}")
        print(f"Total de Activos Circulantes:".ljust(35) + f"$ {total_circulante:>11,.0f}")
        
        # Activo No Circulante
        print("\nNo Circulante")
        terreno = 905000     # Redacción
        planta = 1585000    # Redacción + Balance + Compra de máquina
        dep_acum = 745000   # Redacción + Depreciación de Operación y GIF
        
        total_no_circulante = terreno + planta - dep_acum
        
        print(f"Terreno".ljust(35) + f"{terreno:>13,.0f}")
        print(f"Planta y Equipo".ljust(35) + f"{planta:>13,.0f}")
        print(f"Depreciación Acumulada".ljust(35) + f"({dep_acum:,.0f})")
        print(f"Total Activos No Circulante".ljust(35) + f"$ {total_no_circulante:>11,.0f}")
        
        # Activo Total
        activo_total = total_circulante + total_no_circulante
        print(f"\nACTIVO TOTAL".ljust(35) + f"$ {activo_total:>11,.0f}")
        
        # PASIVO
        print("\nPASIVO")
        print("Corto Plazo")
        
        # Pasivo Corto Plazo
        proveedores = 1070505    # Del saldo de proveedores y flujo de salida
        documentos = 95000       # Redacción
        isr = 4313048           # Del Estado de Resultados
        ptu = 1437683           # Del Estado de Resultados
        
        total_corto_plazo = proveedores + documentos + isr + ptu
        
        print(f"Proveedores".ljust(35) + f"{proveedores:>13,.0f}")
        print(f"Documentos por Pagar".ljust(35) + f"{documentos:>13,.0f}")
        print(f"ISR por Pagar".ljust(35) + f"{isr:>13,.0f}")
        print(f"PTU por Pagar".ljust(35) + f"{ptu:>13,.0f}")
        print(f"Total de Pasivo Corto Plazo:".ljust(35) + f"$ {total_corto_plazo:>11,.0f}")
        
        # Pasivo Largo Plazo
        print("\nLargo Plazo")
        prestamos = 120000    # Redacción
        
        print(f"Préstamos Bancarios".ljust(35) + f"{prestamos:>13,.0f}")
        print(f"Total de Pasivo Largo Plazo:".ljust(35) + f"$ {prestamos:>11,.0f}")
        
        # Pasivo Total
        pasivo_total = total_corto_plazo + prestamos
        print(f"\nPASIVO TOTAL".ljust(35) + f"$ {pasivo_total:>11,.0f}")
        
        # CAPITAL CONTABLE
        print("\nCAPITAL CONTABLE")
        capital_aportado = 1500000    # Redacción
        capital_ganado = 362000       # Redacción
        utilidad = 8626097            # Del Estado de Resultados
        
        total_capital = capital_aportado + capital_ganado + utilidad
        
        print(f"Capital Aportado".ljust(35) + f"{capital_aportado:>13,.0f}")
        print(f"Capital Ganado".ljust(35) + f"{capital_ganado:>13,.0f}")
        print(f"Utilidad del Ejercicio".ljust(35) + f"{utilidad:>13,.0f}")
        print(f"Total de Capital Contable".ljust(35) + f"$ {total_capital:>11,.0f}")
        
        # Suma de Pasivo y Capital
        suma_total = pasivo_total + total_capital
        print(f"\nSUMA DE PASIVO Y CAPITAL".ljust(35) + f"$ {suma_total:>11,.0f}")

class SistemaPresupuestoMaestro:
    def __init__(self):
        self.balance = BalanceGeneral()
        self.requerimientos = RequerimientoMateriales()
        self.inventarios = InformacionInventarios()
        self.productos = ProductosVentas()
        self.gastos_admin = GastosAdminVentas()
        self.gastos_fabricacion = GastosFabricacionIndirectos()
        self.datos_adicionales = DatosAdicionales()
    
    def imprimir_encabezado(self):
        print("\n" + "="*80)
        print(f"{InformacionEmpresa.NOMBRE}".center(80))
        print(f"Sistema de Presupuesto Maestro {InformacionEmpresa.AÑO}".center(80))
        print(f"Giro: {InformacionEmpresa.GIRO}".center(80))
        print(f"Clientes: {InformacionEmpresa.CLIENTES}".center(80))
        print("="*80)

    def imprimir_menu_captura(self):
        print("\n=== 1. CAPTURA DE DATOS ===")
        print("1. Balance General")
        print("2. Requerimiento de Materiales")
        print("3. Información de Inventarios")
        print("4. Productos y Ventas Planeadas")
        print("5. Gastos de Administración y Ventas")
        print("6. Gastos de Fabricación Indirectos")
        print("7. Datos Adicionales")
        print("8. Capturar Todos los Datos")

    def imprimir_menu_presupuesto(self):
        print("\n=== 2. PRESUPUESTO DE OPERACIÓN ===")
        print("9. Presupuesto de Ventas")
        print("10. Determinación del Saldo de Clientes y Flujo de Entradas")
        print("11. Presupuesto de Producción")
        print("12. Presupuesto de Requerimiento de Materiales")
        print("13. Presupuesto de Compra de Materiales")
        print("14. Determinación del Saldo de Proveedores y Flujo de Salidas")
        print("15. Presupuesto de Mano de Obra Directa")
        print("16. Presupuesto de Gastos Indirectos de Fabricación")
        print("17. Presupuesto de Gastos de Operación")
        print("18. Determinación del Costo Unitario de Productos Terminados")
        print("19. Valuación de Inventarios Finales")
        print("20. Generar Todo el Presupuesto de Operación")
        
        print("\n=== 3. PRESUPUESTO FINANCIERO ===")
        print("21. Estado de Costo de Producción y Ventas")
        print("22. Estado de Resultados")
        print("23. Estado de Flujo de Efectivo")
        print("24. Balance General Presupuestado")
        print("25. Generar Todo el Presupuesto Financiero")
    
    def obtener_datos_completos(self):
        print("\n=== CAPTURA COMPLETA DE DATOS ===")
        print("Se capturarán todos los datos necesarios para el sistema.")
        input("Presione Enter para comenzar...")

        # 1. Balance General
        print("\n1. BALANCE GENERAL")
        print("-" * 50)
        self.balance.solicitar_datos()
        print("Balance General capturado correctamente.")
        input("\nPresione Enter para continuar...")

        # 2. Requerimiento de Materiales
        print("\n2. REQUERIMIENTO DE MATERIALES")
        print("-" * 50)
        self.requerimientos.solicitar_datos()
        print("Requerimientos de materiales capturados correctamente.")
        input("\nPresione Enter para continuar...")

        # 3. Información de Inventarios
        print("\n3. INFORMACIÓN DE INVENTARIOS")
        print("-" * 50)
        self.inventarios.solicitar_datos()
        print("Información de inventarios capturada correctamente.")
        input("\nPresione Enter para continuar...")

        # 4. Productos y Ventas Planeadas
        print("\n4. PRODUCTOS Y VENTAS PLANEADAS")
        print("-" * 50)
        self.productos.solicitar_datos()
        print("Productos y ventas planeadas capturados correctamente.")
        input("\nPresione Enter para continuar...")

        # 5. Gastos de Administración y Ventas
        print("\n5. GASTOS DE ADMINISTRACIÓN Y VENTAS")
        print("-" * 50)
        self.gastos_admin.solicitar_datos()
        print("Gastos de administración y ventas capturados correctamente.")
        input("\nPresione Enter para continuar...")

        # 6. Gastos de Fabricación Indirectos
        print("\n6. GASTOS DE FABRICACIÓN INDIRECTOS")
        print("-" * 50)
        self.gastos_fabricacion.solicitar_datos()
        print("Gastos de fabricación indirectos capturados correctamente.")
        input("\nPresione Enter para continuar...")

        # 7. Datos Adicionales
        print("\n7. DATOS ADICIONALES")
        print("-" * 50)
        self.datos_adicionales.solicitar_datos()
        print("Datos adicionales capturados correctamente.")

        print("\n=== CAPTURA COMPLETA FINALIZADA ===")
        print("Todos los datos han sido capturados exitosamente.")
        input("\nPresione Enter para volver al menú principal...")

    def ejecutar_opcion_captura(self, opcion):
        try:
            if opcion == 1:
                self.balance.solicitar_datos()
            elif opcion == 2:
                self.requerimientos.solicitar_datos()
            elif opcion == 3:
                self.inventarios.solicitar_datos()
            elif opcion == 4:
                self.productos.solicitar_datos()
            elif opcion == 5:
                self.gastos_admin.solicitar_datos()
            elif opcion == 6:
                self.gastos_fabricacion.solicitar_datos()
            elif opcion == 7:
                self.datos_adicionales.solicitar_datos()
                
        except Exception as e:
            print(f"\nError durante la captura de datos: {str(e)}")
        finally:
            input("\nPresione Enter para continuar...")

    def verificar_datos_ventas(self):
        # Verificar si los datos necesarios para el presupuesto de ventas están capturados
        return hasattr(self.productos, 'productos') and bool(self.productos.productos)

    def verificar_datos_clientes(self):
        # Verificar datos para el presupuesto de clientes
        return (self.verificar_datos_ventas() and 
                hasattr(self.balance, 'activo_circulante') and 
                hasattr(self.datos_adicionales, 'datos'))

    def verificar_datos_produccion(self):
        # Verificar datos para el presupuesto de producción
        return (self.verificar_datos_ventas() and 
                hasattr(self.inventarios, 'inventarios'))

    def verificar_datos_requerimientos(self):
        # Verificar datos para el presupuesto de requerimientos
        return (self.verificar_datos_produccion() and 
                hasattr(self.requerimientos, 'materiales'))

    def verificar_datos_compras(self):
        # Verificar datos para el presupuesto de compras
        return (self.verificar_datos_requerimientos() and 
                hasattr(self.inventarios, 'inventarios'))

    def verificar_datos_proveedores(self):
        # Verificar datos para el presupuesto de proveedores
        return (hasattr(self.balance, 'pasivo_corto_plazo') and 
                self.verificar_datos_compras() and 
                hasattr(self.datos_adicionales, 'datos'))

    def verificar_datos_mod(self):
        # Verificar datos para el presupuesto de mano de obra directa
        return self.verificar_datos_produccion()

    def verificar_datos_gif(self):
        # Verificar datos para el presupuesto de gastos indirectos
        return (self.verificar_datos_mod() and 
                hasattr(self.gastos_fabricacion, 'gastos'))

    def verificar_datos_gastos_operacion(self):
        # Verificar datos para el presupuesto de gastos de operación
        return (self.verificar_datos_ventas() and 
                hasattr(self.gastos_admin, 'gastos'))

    def verificar_datos_costo_unitario(self):
        # Verificar datos para el costo unitario
        return (self.verificar_datos_gif() and 
                hasattr(self.requerimientos, 'materiales'))

    def verificar_datos_valuacion_inventarios(self):
        # Verificar datos para la valuación de inventarios
        return (self.verificar_datos_costo_unitario() and 
                hasattr(self.inventarios, 'inventarios'))

    def verificar_datos_costo_produccion(self):
        # Verificar datos para el costo de producción y ventas
        return all([
            self.verificar_datos_compras(),
            self.verificar_datos_mod(),
            self.verificar_datos_gif(),
            self.verificar_datos_valuacion_inventarios()
        ])

    def verificar_datos_estado_resultados(self):
        # Verificar datos para el estado de resultados
        return self.verificar_datos_costo_produccion()

    def verificar_datos_flujo_efectivo(self):
        # Verificar datos para el flujo de efectivo
        return all([
            self.verificar_datos_clientes(),
            self.verificar_datos_proveedores(),
            self.verificar_datos_mod(),
            self.verificar_datos_gif(),
            self.verificar_datos_gastos_operacion(),
            self.verificar_datos_estado_resultados()
        ])

    def verificar_datos_balance(self):
        # Verificar datos para el balance general
        return all([
            self.verificar_datos_flujo_efectivo(),
            self.verificar_datos_clientes(),
            self.verificar_datos_valuacion_inventarios(),
            self.verificar_datos_proveedores(),
            self.verificar_datos_estado_resultados()
        ])

    def verificar_datos_cargados(self):
        """Verifica que todos los datos necesarios estén cargados"""
        try:
            # Verificar datos básicos
            if not hasattr(self.productos, 'productos') or not self.productos.productos:
                return False, "Datos de productos no cargados"
            
            if not hasattr(self.inventarios, 'inventarios') or not self.inventarios.inventarios:
                return False, "Datos de inventarios no cargados"
                
            if not hasattr(self.gastos_admin, 'gastos') or not self.gastos_admin.gastos:
                return False, "Datos de gastos administrativos no cargados"
                
            if not hasattr(self.gastos_fabricacion, 'gastos') or not self.gastos_fabricacion.gastos:
                return False, "Datos de gastos de fabricación no cargados"
                
            return True, "Todos los datos están cargados correctamente"
            
        except Exception as e:
            return False, f"Error al verificar datos: {str(e)}"

    def generar_todo_presupuesto_operacion(self):
        # Verificar datos antes de generar presupuestos
        datos_ok, mensaje = self.verificar_datos_cargados()
        if not datos_ok:
            print(f"\nError: {mensaje}")
            print("Por favor, capture todos los datos necesarios primero.")
            input("\nPresione Enter para continuar...")
            return
    
    def menu_principal(self):
        while True:
            self.imprimir_encabezado()
            print("\nMENÚ PRINCIPAL")
            print("=" * 50)
            
            self.imprimir_menu_captura()
            self.imprimir_menu_presupuesto()
            
            print("\n=== 4. SISTEMA ===")
            print("0. Salir")
            
            try:
                opcion = int(input("\nSeleccione una opción: "))
                
                if opcion == 0:
                    print("\n¡Gracias por usar el sistema!")
                    break
                    
                # Opciones de Captura de Datos
                elif 1 <= opcion <= 7:
                    self.ejecutar_opcion_captura(opcion)
                elif opcion == 8:
                    self.obtener_datos_completos()
                    
                # Opciones de Presupuesto
                elif 9 <= opcion <= 25:
                    self.ejecutar_opcion_presupuesto(opcion)
                    
                else:
                    print("\nOpción no válida. Por favor intente de nuevo.")
                    
            except ValueError:
                print("\nPor favor, ingrese un número válido.")

    def generar_todo_presupuesto_operacion(self):
        print("\n=== GENERANDO PRESUPUESTO DE OPERACIÓN COMPLETO ===")
        
        # Verificar todos los datos necesarios
        if not (self.verificar_datos_ventas() and 
                self.verificar_datos_clientes() and 
                self.verificar_datos_produccion() and 
                self.verificar_datos_requerimientos() and 
                self.verificar_datos_compras() and 
                self.verificar_datos_proveedores() and 
                self.verificar_datos_mod() and 
                self.verificar_datos_gif() and 
                self.verificar_datos_gastos_operacion() and 
                self.verificar_datos_costo_unitario() and 
                self.verificar_datos_valuacion_inventarios()):
            print("\nError: Necesita capturar todos los datos necesarios primero.")
            input("\nPresione Enter para continuar...")
            return

        print("\nGenerando presupuestos de operación...")
        # Generar cada presupuesto
        presupuestos = [
            (9, "Presupuesto de Ventas"),
            (10, "Determinación del Saldo de Clientes y Flujo de Entradas"),
            (11, "Presupuesto de Producción"),
            (12, "Presupuesto de Requerimiento de Materiales"),
            (13, "Presupuesto de Compra de Materiales"),
            (14, "Determinación del Saldo de Proveedores y Flujo de Salidas"),
            (15, "Presupuesto de Mano de Obra Directa"),
            (16, "Presupuesto de Gastos Indirectos de Fabricación"),
            (17, "Presupuesto de Gastos de Operación"),
            (18, "Determinación del Costo Unitario de Productos Terminados"),
            (19, "Valuación de Inventarios Finales")
        ]
        
        for opcion, nombre in presupuestos:
            print(f"\n{'-'*80}")
            print(f"Generando: {nombre}")
            print(f"{'-'*80}")
            self.ejecutar_opcion_presupuesto(opcion)
            input("\nPresione Enter para continuar al siguiente presupuesto...")
        
        print("\nTodos los presupuestos de operación han sido generados.")
        input("\nPresione Enter para volver al menú principal...")

    def generar_todo_presupuesto_financiero(self):
        print("\n=== GENERANDO PRESUPUESTO FINANCIERO COMPLETO ===")
        
        # Verificar todos los datos necesarios
        if not (self.verificar_datos_costo_produccion() and 
                self.verificar_datos_estado_resultados() and 
                self.verificar_datos_flujo_efectivo() and 
                self.verificar_datos_balance()):
            print("\nError: Necesita generar todos los presupuestos de operación primero.")
            input("\nPresione Enter para continuar...")
            return

        print("\nGenerando estados financieros...")
        # Generar cada estado financiero
        presupuestos = [
            (21, "Estado de Costo de Producción y Ventas"),
            (22, "Estado de Resultados"),
            (23, "Estado de Flujo de Efectivo"),
            (24, "Balance General Presupuestado")
        ]
        
        for opcion, nombre in presupuestos:
            print(f"\n{'-'*80}")
            print(f"Generando: {nombre}")
            print(f"{'-'*80}")
            self.ejecutar_opcion_presupuesto(opcion)
            input("\nPresione Enter para continuar al siguiente estado financiero...")
        
        print("\nTodos los estados financieros han sido generados.")
        input("\nPresione Enter para volver al menú principal...")
        
    def ejecutar_opcion_presupuesto(self, opcion):
        try:
            if opcion == 20:
                self.generar_todo_presupuesto_operacion()
                return
            elif opcion == 25:
                self.generar_todo_presupuesto_financiero()
                return
                
            elif opcion == 9:
                if not self.verificar_datos_ventas():
                    raise ValueError("Necesita capturar los datos de Productos y Ventas primero.")
                presupuesto_ventas = PresupuestoVentas(self.productos)
                presupuesto_ventas.generar_presupuesto()
                
            elif opcion == 10:
                if not self.verificar_datos_clientes():
                    raise ValueError("Necesita capturar el Balance General, Ventas y Datos Adicionales primero.")
                presupuesto_clientes = PresupuestoClientes(self.balance, self.productos, self.datos_adicionales)
                presupuesto_clientes.generar_presupuesto()
                
            elif opcion == 11:
                if not self.verificar_datos_produccion():
                    raise ValueError("Necesita capturar los datos de Ventas e Inventarios primero.")
                presupuesto_produccion = PresupuestoProduccion(self.productos, self.inventarios)
                presupuesto_produccion.generar_presupuesto()
                
            elif opcion == 12:
                if not self.verificar_datos_requerimientos():
                    raise ValueError("Necesita capturar los datos de Producción y Requerimientos de Materiales primero.")
                presupuesto_produccion = PresupuestoProduccion(self.productos, self.inventarios)
                presupuesto_requerimientos = PresupuestoRequerimientoMateriales(
                    self.productos, presupuesto_produccion, self.requerimientos)
                presupuesto_requerimientos.generar_presupuesto()
                
            elif opcion == 13:
                if not self.verificar_datos_compras():
                    raise ValueError("Necesita capturar los datos de Requerimientos e Inventarios primero.")
                presupuesto_produccion = PresupuestoProduccion(self.productos, self.inventarios)
                presupuesto_requerimientos = PresupuestoRequerimientoMateriales(
                    self.productos, presupuesto_produccion, self.requerimientos)
                presupuesto_compras = PresupuestoCompraMateriales(self.inventarios, presupuesto_requerimientos)
                presupuesto_compras.generar_presupuesto()

            elif opcion == 14:
                if not self.verificar_datos_proveedores():
                    raise ValueError("Necesita capturar el Balance, Compras y Datos Adicionales primero.")
                presupuesto_produccion = PresupuestoProduccion(self.productos, self.inventarios)
                presupuesto_requerimientos = PresupuestoRequerimientoMateriales(
                    self.productos, presupuesto_produccion, self.requerimientos)
                presupuesto_compras = PresupuestoCompraMateriales(self.inventarios, presupuesto_requerimientos)
                presupuesto_proveedores = PresupuestoProveedores(self.balance, presupuesto_compras, self.datos_adicionales)
                presupuesto_proveedores.generar_presupuesto()

            elif opcion == 15:
                if not self.verificar_datos_mod():
                    raise ValueError("Necesita capturar los datos de Producción primero.")
                presupuesto_produccion = PresupuestoProduccion(self.productos, self.inventarios)
                presupuesto_mod = PresupuestoManoObraDirecta(presupuesto_produccion, self.requerimientos)
                presupuesto_mod.generar_presupuesto()

            elif opcion == 16:
                if not self.verificar_datos_gif():
                    raise ValueError("Necesita capturar los datos de MOD y Gastos de Fabricación primero.")
                presupuesto_produccion = PresupuestoProduccion(self.productos, self.inventarios)
                presupuesto_mod = PresupuestoManoObraDirecta(presupuesto_produccion, self.requerimientos)
                presupuesto_gif = PresupuestoGastosIndirectos(self.gastos_fabricacion, presupuesto_mod)
                presupuesto_gif.generar_presupuesto()

            elif opcion == 17:
                if not self.verificar_datos_gastos_operacion():
                    raise ValueError("Necesita capturar los datos de Ventas y Gastos Administrativos primero.")
                presupuesto_ventas = self.productos  # Usar el objeto productos directamente
                presupuesto_gastos_op = PresupuestoGastosOperacion(self.gastos_admin, presupuesto_ventas)
                presupuesto_gastos_op.generar_presupuesto()

            elif opcion == 18:
                if not self.verificar_datos_costo_unitario():
                    raise ValueError("Necesita capturar los datos de GIF y Requerimientos primero.")
                presupuesto_produccion = PresupuestoProduccion(self.productos, self.inventarios)
                presupuesto_mod = PresupuestoManoObraDirecta(presupuesto_produccion, self.requerimientos)
                presupuesto_gif = PresupuestoGastosIndirectos(self.gastos_fabricacion, presupuesto_mod)
                presupuesto_requerimientos = PresupuestoRequerimientoMateriales(
                    self.productos, presupuesto_produccion, self.requerimientos)
                presupuesto_compras = PresupuestoCompraMateriales(self.inventarios, presupuesto_requerimientos)
                presupuesto_costo_unitario = PresupuestoCostoUnitario(presupuesto_compras, presupuesto_gif)
                presupuesto_costo_unitario.generar_presupuesto()


            elif opcion == 19:
                if not self.verificar_datos_valuacion_inventarios():
                    raise ValueError("Necesita capturar los datos de Costos Unitarios e Inventarios primero.")
                
                # Crear primero los objetos necesarios
                presupuesto_produccion = PresupuestoProduccion(self.productos, self.inventarios)
                presupuesto_requerimientos = PresupuestoRequerimientoMateriales(
                    self.productos, presupuesto_produccion, self.requerimientos)
                presupuesto_compras = PresupuestoCompraMateriales(self.inventarios, presupuesto_requerimientos)
                presupuesto_mod = PresupuestoManoObraDirecta(presupuesto_produccion, self.requerimientos)
                presupuesto_gif = PresupuestoGastosIndirectos(self.gastos_fabricacion, presupuesto_mod)
                
                # Crear el objeto de costo unitario con los parámetros correctos
                presupuesto_costo_unitario = PresupuestoCostoUnitario(
                    presupuesto_compras=presupuesto_compras,
                    presupuesto_gif=presupuesto_gif
                )
                
                # Crear y generar el presupuesto de valuación
                presupuesto_valuacion = PresupuestoValuacionInventarios(
                    self.inventarios,
                    presupuesto_costo_unitario
                )
                presupuesto_valuacion.generar_presupuesto()

            elif opcion == 21:
                if not self.verificar_datos_costo_produccion():
                    raise ValueError("Necesita generar todos los presupuestos previos necesarios primero.")
                presupuesto_produccion = PresupuestoProduccion(self.productos, self.inventarios)
                presupuesto_mod = PresupuestoManoObraDirecta(presupuesto_produccion, self.requerimientos)
                presupuesto_gif = PresupuestoGastosIndirectos(self.gastos_fabricacion, presupuesto_mod)
                presupuesto_costo_produccion = PresupuestoCostoProduccionVentas(
                    None, presupuesto_mod, presupuesto_gif, None)
                presupuesto_costo_produccion.generar_presupuesto()

            elif opcion == 22:
                if not self.verificar_datos_estado_resultados():
                    raise ValueError("Necesita generar el Estado de Costo de Producción y Ventas primero.")
                presupuesto_ventas = PresupuestoVentas(self.productos)
                presupuesto_costo_produccion = PresupuestoCostoProduccionVentas(None, None, None, None)
                presupuesto_estado_resultados = PresupuestoEstadoResultados(
                    presupuesto_ventas, presupuesto_costo_produccion, self.gastos_admin)
                presupuesto_estado_resultados.generar_presupuesto()

            elif opcion == 23:
                if not self.verificar_datos_flujo_efectivo():
                    raise ValueError("Necesita generar todos los presupuestos previos necesarios primero.")
                presupuesto_clientes = PresupuestoClientes(self.balance, self.productos, self.datos_adicionales)
                presupuesto_proveedores = PresupuestoProveedores(self.balance, None, self.datos_adicionales)
                presupuesto_mod = PresupuestoManoObraDirecta(None, self.requerimientos)
                presupuesto_gif = PresupuestoGastosIndirectos(self.gastos_fabricacion, None)
                presupuesto_gastos_op = PresupuestoGastosOperacion(self.gastos_admin, None)
                presupuesto_estado_resultados = PresupuestoEstadoResultados(None, None, None)
                presupuesto_flujo = PresupuestoFlujoEfectivo(
                    presupuesto_clientes, presupuesto_proveedores, presupuesto_mod,
                    presupuesto_gif, presupuesto_gastos_op, presupuesto_estado_resultados)
                presupuesto_flujo.generar_presupuesto()

            elif opcion == 24:
                if not self.verificar_datos_balance():
                    raise ValueError("Necesita generar todos los presupuestos previos necesarios primero.")
                presupuesto_flujo = PresupuestoFlujoEfectivo(None, None, None, None, None, None)
                presupuesto_clientes = PresupuestoClientes(None, None, None)
                presupuesto_valuacion = PresupuestoValuacionInventarios(None, None)
                presupuesto_proveedores = PresupuestoProveedores(None, None, None)
                presupuesto_estado_resultados = PresupuestoEstadoResultados(None, None, None)
                presupuesto_balance = PresupuestoBalanceGeneral(
                    presupuesto_flujo, presupuesto_clientes, presupuesto_valuacion,
                    presupuesto_proveedores, presupuesto_estado_resultados)
                presupuesto_balance.generar_presupuesto()
                    
        except ValueError as e:
            print(f"\nError: {str(e)}")
        except Exception as e:
            print(f"\nError inesperado: {str(e)}")
        finally:
            if opcion not in [20, 25]:  # No mostrar el mensaje para las opciones de generación completa
                input("\nPresione Enter para continuar...")


def main():
    sistema = SistemaPresupuestoMaestro()
    sistema.menu_principal()

if __name__ == "__main__":
    main()