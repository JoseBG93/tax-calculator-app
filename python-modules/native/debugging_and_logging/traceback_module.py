#!/usr/bin/env python3
"""
MÓDULO NATIVO: traceback
========================

¿QUÉ ES?
El módulo 'traceback' proporciona utilidades para imprimir, formatear y 
manipular tracebacks (trazas de pila) de Python.

¿PARA QUÉ SIRVE?
- Obtener información detallada de errores
- Formatear tracebacks para logging
- Debugging y diagnóstico de problemas
- Crear mensajes de error personalizados
- Extraer información específica de excepciones

IMPORTANCIA: ⭐⭐⭐⭐⭐ (Muy importante para debugging)
"""

import traceback
import sys
import logging
from datetime import datetime

def ejemplo_traceback_basico():
    """Ejemplo básico de cómo usar traceback"""
    
    print("=" * 50)
    print("🔍 MÓDULO TRACEBACK - RASTREO DE ERRORES")
    print("=" * 50)
    
    def funcion_con_error():
        """Función que genera un error intencionalmente"""
        numero = 10
        resultado = numero / 0  # ← Error: División por cero
        return resultado
    
    def funcion_que_llama():
        """Función que llama a otra función con error"""
        print("   📞 Llamando a función_con_error()...")
        return funcion_con_error()
    
    def funcion_principal():
        """Función principal que inicia la cadena"""
        print("   🚀 Iniciando función_principal()...")
        return funcion_que_llama()
    
    # 1. EJEMPLO DE TRACEBACK BÁSICO
    print("\n1️⃣ EJEMPLO DE TRACEBACK BÁSICO:")
    
    try:
        funcion_principal()
    except Exception as e:
        print(f"   ❌ Error capturado: {e}")
        print(f"   📍 Tipo de error: {type(e).__name__}")
        
        print("\n   📋 TRACEBACK COMPLETO:")
        print("   " + "─" * 45)
        
        # Formatear traceback como string
        tb_lines = traceback.format_exc().split('\n')
        for line in tb_lines:
            print(f"   {line}")
        
        print("   " + "─" * 45)

def ejemplo_traceback_detallado():
    """Ejemplo detallado de información de traceback"""
    
    print("\n" + "=" * 50)
    print("📊 INFORMACIÓN DETALLADA DE TRACEBACK")
    print("=" * 50)
    
    def nivel_3():
        """Función nivel 3 - donde ocurre el error"""
        datos = {'nombre': 'Juan', 'edad': 30}
        return datos['profesion']  # ← Error: Clave no existe
    
    def nivel_2():
        """Función nivel 2 - llamada intermedia"""
        return nivel_3()
    
    def nivel_1():
        """Función nivel 1 - primera llamada"""
        return nivel_2()
    
    try:
        nivel_1()
    except Exception as e:
        print(f"🔍 ANÁLISIS DETALLADO DEL ERROR:")
        print(f"   Error: {e}")
        print(f"   Tipo: {type(e).__name__}")
        
        # Obtener información detallada del traceback
        exc_type, exc_value, exc_traceback = sys.exc_info()
        
        print(f"\n📋 INFORMACIÓN DE LA EXCEPCIÓN:")
        print(f"   Tipo de excepción: {exc_type.__name__}")
        print(f"   Valor: {exc_value}")
        
        # Extraer información del traceback
        print(f"\n🔗 CADENA DE LLAMADAS:")
        tb_list = traceback.extract_tb(exc_traceback)
        
        for i, frame in enumerate(tb_list):
            print(f"   [{i+1}] Archivo: {frame.filename}")
            print(f"       Función: {frame.name}")
            print(f"       Línea: {frame.lineno}")
            print(f"       Código: {frame.line}")
            print()

def ejemplo_traceback_personalizado():
    """Ejemplo de traceback personalizado para logging"""
    
    print("\n" + "=" * 50)
    print("🎨 TRACEBACK PERSONALIZADO")
    print("=" * 50)
    
    # Configurar logging
    logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    logger = logging.getLogger(__name__)
    
    def operacion_riesgosa():
        """Función que puede fallar"""
        archivos = ['archivo1.txt', 'archivo2.txt']
        for archivo in archivos:
            if archivo == 'archivo2.txt':
                raise FileNotFoundError(f"No se pudo encontrar {archivo}")
        return True
    
    def procesar_datos():
        """Función que procesa datos y maneja errores"""
        try:
            operacion_riesgosa()
        except FileNotFoundError as e:
            # Capturar información detallada del error
            error_info = {
                'timestamp': datetime.now().isoformat(),
                'error_type': type(e).__name__,
                'error_message': str(e),
                'function': 'procesar_datos',
                'traceback': traceback.format_exc()
            }
            
            # Log personalizado
            logger.error(f"Error en procesamiento de datos: {e}")
            logger.error(f"Traceback:\n{traceback.format_exc()}")
            
            print("   🚨 ERROR PROCESANDO DATOS:")
            print(f"   Timestamp: {error_info['timestamp']}")
            print(f"   Tipo: {error_info['error_type']}")
            print(f"   Mensaje: {error_info['error_message']}")
            print(f"   Función: {error_info['function']}")
            
            return error_info
    
    resultado = procesar_datos()
    if resultado:
        print(f"\n   📝 Información del error guardada para análisis")

def ejemplo_traceback_filtrado():
    """Ejemplo de cómo filtrar y limpiar tracebacks"""
    
    print("\n" + "=" * 50)
    print("🧹 TRACEBACK FILTRADO Y LIMPIO")
    print("=" * 50)
    
    def mi_funcion_especial():
        """Función de mi aplicación"""
        return int("no_es_numero")  # Error de conversión
    
    def helper_interno():
        """Función helper interna"""
        return mi_funcion_especial()
    
    def api_publica():
        """API pública de mi aplicación"""
        return helper_interno()
    
    try:
        api_publica()
    except ValueError as e:
        print("   📋 TRACEBACK COMPLETO:")
        print("   " + "─" * 40)
        tb_lines = traceback.format_exc().split('\n')
        for line in tb_lines:
            print(f"   {line}")
        
        print("\n   🎯 TRACEBACK FILTRADO (solo mi código):")
        print("   " + "─" * 40)
        
        # Filtrar solo líneas que contienen mi código
        tb_list = traceback.extract_tb(sys.exc_info()[2])
        for frame in tb_list:
            if '03_traceback_module.py' in frame.filename:
                print(f"   📍 {frame.name}() línea {frame.lineno}")
                print(f"      Código: {frame.line}")
        
        print(f"   ❌ Error final: {e}")

def ejemplo_traceback_stack_completo():
    """Ejemplo de obtener stack trace completo sin excepción"""
    
    print("\n" + "=" * 50)
    print("📚 STACK TRACE COMPLETO (sin error)")
    print("=" * 50)
    
    def funcion_a():
        """Función A"""
        print("   📍 Ejecutando función_a")
        funcion_b()
    
    def funcion_b():
        """Función B"""
        print("   📍 Ejecutando función_b")
        funcion_c()
    
    def funcion_c():
        """Función C"""
        print("   📍 Ejecutando función_c")
        
        # Obtener stack trace actual (sin error)
        print(f"\n   🔍 STACK TRACE ACTUAL:")
        stack = traceback.extract_stack()
        
        for i, frame in enumerate(stack[-4:]):  # Últimas 4 llamadas
            print(f"   [{i+1}] {frame.name}() en línea {frame.lineno}")
            print(f"       Código: {frame.line}")
    
    print("   🚀 Iniciando cadena de llamadas...")
    funcion_a()

def herramientas_debugging():
    """Herramientas útiles para debugging con traceback"""
    
    print("\n" + "=" * 50)
    print("🛠️ HERRAMIENTAS DE DEBUGGING")
    print("=" * 50)
    
    def crear_mensaje_error_completo(e):
        """Crear mensaje de error completo para debugging"""
        
        error_info = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'error_type': type(e).__name__,
            'error_message': str(e),
            'traceback_formatted': traceback.format_exc(),
            'stack_summary': traceback.extract_tb(sys.exc_info()[2])
        }
        
        return error_info
    
    def ejemplo_con_error_completo():
        """Ejemplo que genera error para mostrar debugging completo"""
        lista = [1, 2, 3]
        return lista[10]  # Error: índice fuera de rango
    
    try:
        ejemplo_con_error_completo()
    except Exception as e:
        info = crear_mensaje_error_completo(e)
        
        print(f"   🕒 Timestamp: {info['timestamp']}")
        print(f"   🔴 Error: {info['error_type']}: {info['error_message']}")
        
        print(f"\n   📋 Stack summary:")
        for i, frame in enumerate(info['stack_summary']):
            print(f"   [{i+1}] {frame.name}() - línea {frame.lineno}")
        
        print(f"\n   💡 SUGERENCIAS DE DEBUGGING:")
        if "IndexError" in info['error_type']:
            print("   • Verificar el tamaño de la lista")
            print("   • Usar len() para validar índices")
            print("   • Considerar usar try/except para índices dinámicos")
        
        print(f"\n   🔧 Para reproducir:")
        print(f"   • Ejecutar: python {__file__}")
        print(f"   • Función: {info['stack_summary'][-1].name}")
        print(f"   • Línea: {info['stack_summary'][-1].lineno}")

def casos_uso_comunes():
    """Casos de uso más comunes del módulo traceback"""
    
    print("\n" + "=" * 50)
    print("🎯 CASOS DE USO COMUNES")
    print("=" * 50)
    
    print("1. Logging de errores con traceback completo:")
    print("   try:")
    print("       operacion_riesgosa()")
    print("   except Exception as e:")
    print("       logger.error(f'Error: {e}')")
    print("       logger.error(f'Traceback:\\n{traceback.format_exc()}')")
    
    print("\n2. Obtener información específica del error:")
    print("   exc_type, exc_value, exc_traceback = sys.exc_info()")
    print("   tb_list = traceback.extract_tb(exc_traceback)")
    print("   last_frame = tb_list[-1]")
    print("   print(f'Error en {last_frame.filename}:{last_frame.lineno}')")
    
    print("\n3. Crear mensajes de error user-friendly:")
    print("   try:")
    print("       procesar_archivo()")
    print("   except FileNotFoundError:")
    print("       print('Error: Archivo no encontrado')")
    print("       if DEBUG:")
    print("           print(traceback.format_exc())")
    
    print("\n4. Debugging en desarrollo:")
    print("   import traceback")
    print("   traceback.print_stack()  # Mostrar stack actual")
    
    print("\n5. Formatear traceback para APIs:")
    print("   error_response = {")
    print("       'error': str(e),")
    print("       'traceback': traceback.format_exc() if DEBUG else None")
    print("   }")

if __name__ == "__main__":
    # Ejecutar todos los ejemplos
    ejemplo_traceback_basico()
    ejemplo_traceback_detallado()
    ejemplo_traceback_personalizado()
    ejemplo_traceback_filtrado()
    ejemplo_traceback_stack_completo()
    herramientas_debugging()
    casos_uso_comunes()
    
    print("\n" + "=" * 50)
    print("✅ RESUMEN DEL MÓDULO traceback")
    print("=" * 50)
    print("🔧 Usos principales:")
    print("   • Obtener información detallada de errores")
    print("   • Formatear tracebacks para logging")
    print("   • Debugging y diagnóstico de problemas")
    print("   • Crear mensajes de error informativos")
    print("   • Extraer información específica de excepciones")
    print("\n📚 Documentación oficial:")
    print("   https://docs.python.org/3/library/traceback.html")
    print("\n💡 Consejo: Usar traceback.format_exc() es la forma más común")
    print("   de obtener el traceback completo como string para logging.") 