"""
GUÍA COMPLETA DE DECORADORES EN PYTHON - BLOQUE 4
DECORADORES PERSONALIZADOS - PARA FUNCIONALIDADES ESPECÍFICAS
Tax Calculator Pro - Referencia para José
"""

from functools import wraps
import time
from datetime import datetime

print("="*80)
print("BLOQUE 4: DECORADORES PERSONALIZADOS")
print("="*80)

# ============================================================================
# 4. DECORADORES PERSONALIZADOS - PARA FUNCIONALIDADES ESPECÍFICAS
# ============================================================================
#
# CONCEPTO FUNDAMENTAL: ¿QUÉ ES UN DECORADOR PERSONALIZADO?
# Un decorador es una FUNCIÓN que contiene otra FUNCIÓN dentro (wrapper)
# y que puede aplicarse a otras funciones para "mejorarlas" automáticamente.
#
# ESTRUCTURA BÁSICA - PATRÓN DE 3 PARTES:
# 1. FUNCIÓN EXTERNA (el decorador): Recibe la función original como parámetro
# 2. FUNCIÓN INTERNA (el wrapper): Contiene la función original + extras
# 3. RETURN: Devuelve la función wrapper (mejorada), no la ejecuta
#
# def mi_decorador(funcion_original):        # ← FUNCIÓN EXTERNA (decorador)
#     def wrapper(*args, **kwargs):          # ← FUNCIÓN INTERNA (wrapper)
#         # EXTRAS antes de la función original
#         resultado = funcion_original(*args, **kwargs)  # ← Ejecuta función original
#         # EXTRAS después de la función original
#         return resultado                   # ← Return #1: devuelve resultado (número/dato)
#     return wrapper                         # ← Return #2: devuelve función wrapper
#
# CONCEPTO CLAVE - MODIFICACIÓN IRREVERSIBLE:
# • Cuando aplicas @mi_decorador a una función, la función original "desaparece"
# • El nombre de la función ahora apunta al wrapper (función mejorada)
# • La función original sigue existiendo DENTRO del wrapper, pero ya no puedes acceder directamente
# • Es como cambiar un coche básico por uno con extras: funciona igual pero con mejoras automáticas
#
# EJEMPLO REAL DE TRANSFORMACIÓN:
# @mi_decorador
# def vender_bocadillo():     # ← Esta función se TRANSFORMA
#     return 3.50
# 
# # A partir de aquí:
# vender_bocadillo() → NO ejecuta la función original directamente
# vender_bocadillo() → ejecuta el wrapper que contiene: extras + función original + más extras
#
# ¿POR QUÉ NECESITAMOS EL WRAPPER?
# PROBLEMA: Si el decorador devuelve directamente el resultado (número), 
# la función se convierte en un número y no puedes llamarla más veces.
# SOLUCIÓN: El wrapper mantiene la función "ejecutable" pero con extras automáticos.
#
# ANALOGÍA SIMPLE:
# • Función original = regalo
# • Wrapper = papel de regalo con extras (instrucciones, garantía, accesorios)
# • Sigues teniendo un "regalo" que puedes "abrir" (ejecutar) cuando quieras
# • Pero ahora incluye extras automáticamente cada vez que lo abres
#
# ¿QUÉ ES @wraps Y POR QUÉ ES ESENCIAL?
# @wraps preserva la IDENTIDAD de la función original (nombre y documentación)
# Sin @wraps: func.__name__ = "wrapper" (confuso para debugging)
# Con @wraps: func.__name__ = "nombre_original" (fácil identificación)
#
# POSICIÓN CORRECTA DE @wraps - MUY IMPORTANTE:
# @wraps debe ir DENTRO del decorador, ANTES del wrapper, NUNCA fuera
#
# ✅ CORRECTO:
# def mi_decorador(func):                    # ← DECORADOR (función externa)
#     @wraps(func)                           # ← @wraps VA AQUÍ (antes del wrapper)
#     def wrapper(*args, **kwargs):          # ← WRAPPER (función interna)
#         return func(*args, **kwargs)
#     return wrapper
#
# ❌ INCORRECTO - Fuera del decorador:
# @wraps(algo)  # ← ERROR: ¿wraps de qué?
# def mi_decorador(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper
#
# ❌ INCORRECTO - Después del wrapper:
# def mi_decorador(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     @wraps(func)  # ← ERROR: ya es tarde
#     return wrapper
#
# REGLA SIMPLE: @wraps va inmediatamente ANTES de la definición del wrapper, DENTRO del decorador
# RAZÓN: @wraps es un decorador que se aplica AL wrapper para preservar la identidad de func
#
# ¿QUÉ SON *args y **kwargs? - EXPLICACIÓN CLARA Y DEFINITIVA
# Son la forma de hacer que el wrapper funcione con CUALQUIER función, sin importar sus parámetros
#
# CONCEPTO CLAVE: La diferencia NO es el tipo de dato, es CÓMO pasas los argumentos
#
# LA FUNCIÓN SIEMPRE TIENE LOS MISMOS PARÁMETROS:
# def calcular(valor1, valor2, municipio):  # ← Estos parámetros nunca cambian
#     return f"{valor1}, {valor2}, {municipio}"
#
# FORMA 1 - ARGUMENTOS POSICIONALES (*args):
# • Se pasan por POSICIÓN (orden): calcular(100000, 80000, "Alfafar")
# • Python asigna por orden: primer argumento → primer parámetro, etc.
# • args = (100000, 80000, "Alfafar") ← TUPLA con valores en orden
#
# FORMA 2 - ARGUMENTOS CON NOMBRE (**kwargs):
# • Se pasan con NOMBRE=VALOR: calcular(valor1=100000, valor2=80000, municipio="Alfafar")
# • Python asigna por nombre específico: valor1=100000, valor2=80000, etc.
# • kwargs = {"valor1": 100000, "valor2": 80000, "municipio": "Alfafar"} ← DICCIONARIO
#
# FORMA 3 - MIXTA (ambos):
# • calcular("José", edad=30, ciudad="Alfafar")
# • args = ("José",) ← primer argumento por posición
# • kwargs = {"edad": 30, "ciudad": "Alfafar"} ← resto con nombre
#
# EJEMPLO PRÁCTICO - MISMA FUNCIÓN, DIFERENTES FORMAS DE LLAMARLA:
# def saludar(nombre, edad, ciudad):
#     print(f"Hola {nombre}, tienes {edad} años y vives en {ciudad}")
#
# # Todas estas llamadas hacen EXACTAMENTE lo mismo:
# saludar("José", 30, "Alfafar")                    # Por posición (*args)
# saludar(nombre="José", edad=30, ciudad="Alfafar") # Por nombre (**kwargs)
# saludar("José", edad=30, ciudad="Alfafar")        # Mixta (args + kwargs)
# saludar(ciudad="Alfafar", nombre="José", edad=30) # Por nombre en diferente orden
#
# ¿CUÁNDO USAR CADA UNA?
# • POSICIONALES (args): Pocos parámetros simples → calcular(100000, 80000, "Alfafar")
# • CON NOMBRE (kwargs): Muchos parámetros o necesitas claridad → configurar(host="localhost", puerto=8080, ssl=True)
# • REGLA: Si vas en orden, usa posicionales. Si necesitas claridad o cambiar orden, usa nombres.
#
# ¿POR QUÉ NECESITAMOS *args y **kwargs EN WRAPPERS?
# PROBLEMA: ¿Cómo hacer UN wrapper que funcione con TODAS estas funciones?
# def func_sin_params():
#     return "sin parámetros"
# def func_con_posicionales(a, b, c):
#     return a + b + c
# def func_con_nombres(nombre, edad, ciudad="Valencia"):
#     return f"{nombre} tiene {edad} años"
#
# SOLUCIÓN MALA - Un wrapper específico para cada función:
# def wrapper1():                                    # Solo para func_sin_params
#     return func_sin_params()
# def wrapper2(a, b, c):                            # Solo para func_con_posicionales
#     return func_con_posicionales(a, b, c)
# def wrapper3(nombre, edad, ciudad="Valencia"):     # Solo para func_con_nombres
#     return func_con_nombres(nombre, edad, ciudad)
#
# SOLUCIÓN BUENA - UN wrapper universal:
# def wrapper(*args, **kwargs):  # ← Acepta CUALQUIER combinación de argumentos
#     return func(*args, **kwargs)  # ← Pasa TODO sin modificar a la función original
#
# ¿CÓMO FUNCIONA EL WRAPPER UNIVERSAL?
# wrapper()                        # args=(), kwargs={} → func_sin_params()
# wrapper(1, 2, 3)                 # args=(1,2,3), kwargs={} → func_con_posicionales(1, 2, 3)
# wrapper("José", edad=30, ciudad="Alfafar")  # args=("José",), kwargs={"edad":30, "ciudad":"Alfafar"}
#
# ¡ES COMO UNA CAJA UNIVERSAL QUE ACEPTA CUALQUIER COSA Y LA PASA INTACTA!
#
# ¿QUÉ SIGNIFICA global EN LOS DECORADORES?
# global le dice a Python: "Esta variable NO es local de la función, es global del programa"
#
# PROBLEMA sin global:
# caja_total = 0.0  # Variable global
# def wrapper():
#     caja_total += precio  # ❌ ERROR: Python piensa que es variable local
# 
# SOLUCIÓN con global:
# caja_total = 0.0  # Variable global
# def wrapper():
#     global caja_total     # ← "Esta variable es la global, no crees una local"
#     caja_total += precio  # ✅ Funciona: modifica la variable global
#
# EJEMPLO SIMPLE:
# contador = 0  # Variable global
# def incrementar():
#     global contador  # Sin esto, Python crearía una variable local "contador"
#     contador += 1    # Modifica la variable global
# incrementar()
# print(contador)  # 1
#
# RAZÓN en decoradores: Queremos que variables como caja_total se mantengan 
# entre diferentes llamadas a la función, acumulando datos de todas las ejecuciones
#
# VENTAJAS DE DECORADORES PERSONALIZADOS:
# • CÓDIGO LIMPIO: Cada función se enfoca solo en su trabajo específico
# • SIN REPETICIÓN: No duplicas código de validación/logging en cada función
# • MANTENIMIENTO FÁCIL: Cambios en el decorador afectan todas las funciones automáticamente
# • ESCALABILIDAD: Añadir nuevas funciones es súper fácil (solo añades @decorador)
#
# PERFECTO PARA IIVTNU: Validar datos fiscales, registrar cálculos, medir tiempos
# ============================================================================

print("\n4. Decoradores personalizados - Para nuestro proyecto")
print("-" * 60)

# EJEMPLO PRÁCTICO COMPLETO: Sistema de ventas automático
print("\n🏪 EJEMPLO REAL: Sistema de registro automático de ventas")
print("=" * 50)

# Base de datos simulada
registro_ventas = []
caja_total = 0.0

def registrar_venta(operacion_de_venta):
    """
    DECORADOR REAL que mejora cualquier función de venta
    
    RECIBE: operacion_de_venta (función original que solo vende)
    DEVUELVE: wrapper (función mejorada que vende + registra automáticamente)
    
    El wrapper incluye: registro, tickets, actualización de caja, logging
    """
    @wraps(operacion_de_venta)  # Preserva nombre y documentación original
    def wrapper():
        """
        WRAPPER - Función mejorada que reemplaza a la original
        
        Hace TODO lo que hacía la función original + extras automáticos
        """
        global caja_total
        
        # EXTRA 1: Logging antes de la venta
        print(f"[SISTEMA] Iniciando venta: {operacion_de_venta.__name__}")
        
        # FUNCIÓN ORIGINAL: Se ejecuta aquí (devuelve precio)
        precio = operacion_de_venta()
        
        # EXTRA 2: Registro automático en base de datos
        registro_ventas.append({
            'producto': operacion_de_venta.__name__.replace('vender_', ''),
            'precio': precio,
            'hora': datetime.now().strftime("%H:%M:%S")
        })
        
        # EXTRA 3: Actualizar caja automáticamente
        caja_total += precio
        
        # EXTRA 4: Ticket automático
        print(f"[TICKET] Producto: {operacion_de_venta.__name__.replace('vender_', '').title()}")
        print(f"[TICKET] Precio: {precio}€")
        print(f"[SISTEMA] ✓ Venta registrada automáticamente")
        
        return precio  # Devuelve lo mismo que la función original
    
    return wrapper  # Devuelve la función wrapper (mejorada)

# APLICAMOS EL DECORADOR: Transformación irreversible
@registrar_venta
def vender_cafe():
    """Prepara y vende un café"""  # Esta documentación se preserva gracias a @wraps
    print("  ☕ Preparando café...")
    return 1.20

@registrar_venta
def vender_bocadillo():
    """Prepara y vende un bocadillo"""
    print("  🥪 Preparando bocadillo...")
    return 3.50

# DEMOSTRACIÓN: Las funciones ahora son "mejoradas"
print("\n📋 DEMOSTRACIÓN DE TRANSFORMACIÓN:")
print(f"Nombre de vender_cafe: {vender_cafe.__name__}")  # Gracias a @wraps: "vender_cafe"
print(f"Documentación: {vender_cafe.__doc__}")  # Gracias a @wraps: se preserva

print("\n💰 SIMULACIÓN DE VENTAS:")
print("-" * 30)

print("\n🕐 08:30 - Primera venta del día:")
precio1 = vender_cafe()  # Ejecuta wrapper: extras + función original + más extras
print(f"Cliente paga: {precio1}€")

print("\n🕐 09:15 - Segunda venta:")
precio2 = vender_bocadillo()  # Cada llamada ejecuta todos los extras automáticamente
print(f"Cliente paga: {precio2}€")

print("\n🕐 10:00 - Tercera venta:")
precio3 = vender_cafe()  # Los extras se ejecutan CADA VEZ, no solo una vez
print(f"Cliente paga: {precio3}€")

print("\n📊 RESULTADO DEL SISTEMA AUTOMÁTICO:")
print("=" * 40)
print("Registro de ventas (automático):")
for i, venta in enumerate(registro_ventas, 1):
    print(f"  {i}. {venta['hora']} | {venta['producto'].title()} | {venta['precio']}€")
print(f"\n💰 Total en caja: {caja_total}€")
print(f"📈 Ventas realizadas: {len(registro_ventas)}")

print("\n🎯 CONCEPTO CLAVE DEMOSTRADO:")
print("-" * 40)
print("✅ vender_cafe() sigue siendo una FUNCIÓN (puedes llamarla múltiples veces)")
print("✅ Pero ahora ES el wrapper, no la función original")
print("✅ Cada llamada ejecuta: extras + función original + más extras")
print("✅ Sin duplicar código: cada función de venta tiene solo 2 líneas")
print("✅ Mantenimiento fácil: cambios en @registrar_venta afectan todas las ventas")

print("\n🔍 VERIFICACIÓN TÉCNICA:")
print("-" * 30)
print("¿Las funciones originales desaparecieron? SÍ")
print("¿Ahora son funciones wrapper? SÍ")
print("¿Siguen funcionando igual para el usuario? SÍ")
print("¿Tienen extras automáticos? SÍ")
print("¿Es irreversible sin técnicas especiales? SÍ")

def validar_parametros_iivtnu(func):
    """Decorador que valida parámetros de cálculos IIVTNU"""
    @wraps(func)  # Preserva el nombre y documentación de la función original
    def wrapper(*args, **kwargs):
        # Validación antes de ejecutar la función
        if 'valor_actual' in kwargs and kwargs['valor_actual'] <= 0:
            raise ValueError("El valor actual debe ser positivo")
        if 'valor_anterior' in kwargs and kwargs['valor_anterior'] <= 0:
            raise ValueError("El valor anterior debe ser positivo")
        
        print(f"✓ Validación exitosa para {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"✓ Cálculo completado: {resultado}")
        return resultado
    return wrapper

def medir_tiempo_calculo(func):
    """Decorador que mide el tiempo de ejecución de cálculos"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"⏱️  {func.__name__} ejecutado en {fin-inicio:.4f} segundos")
        return resultado
    return wrapper

def log_calculo_tributario(func):
    """Decorador que registra todos los cálculos realizados"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"📊 [{timestamp}] Iniciando cálculo: {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"📊 [{timestamp}] Finalizado cálculo: {func.__name__} -> {resultado}")
        return resultado
    return wrapper

# Ejemplos de uso de decoradores personalizados
@validar_parametros_iivtnu
@medir_tiempo_calculo
@log_calculo_tributario
def calcular_base_imponible(valor_actual: float, valor_anterior: float, coeficiente: float) -> float:
    """Calcula la base imponible del IIVTNU"""
    incremento = valor_actual - valor_anterior
    return incremento * (coeficiente / 100)

# Ejemplo de ejecución
try:
    resultado = calcular_base_imponible(valor_actual=100000, valor_anterior=80000, coeficiente=15.5)
    print(f"Resultado final: {resultado}")
except ValueError as e:
    print(f"❌ Error de validación: {e}")

print("\n🎯 RESUMEN BLOQUE 4:")
print("✅ Decoradores personalizados = funciones que mejoran otras funciones")
print("✅ Estructura: decorador(función_original) → wrapper → return wrapper")
print("✅ @wraps preserva identidad de la función original")
print("✅ *args, **kwargs hacen el wrapper universal")
print("✅ Perfecto para validación, logging, medición de tiempo")