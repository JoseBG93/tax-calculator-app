#!/usr/bin/env python3
"""
MÓDULO NATIVO: sys
================

¿QUÉ ES?
El módulo 'sys' significa "system" y proporciona acceso a variables y funciones 
que interactúan estrechamente con el intérprete de Python.

¿PARA QUÉ SIRVE?
- Obtener información del sistema Python
- Manipular el path de búsqueda de módulos
- Controlar la entrada/salida estándar
- Obtener argumentos de línea de comandos
- Controlar el comportamiento del intérprete

IMPORTANCIA: ⭐⭐⭐⭐⭐ (Muy importante)
"""

import sys

def ejemplos_sys():
    """Ejemplos prácticos del módulo sys"""
    
    print("=" * 50)
    print("🐍 MÓDULO SYS - INFORMACIÓN DEL SISTEMA")
    print("=" * 50)
    
    # 1. INFORMACIÓN DE VERSIÓN
    print("\n1️⃣ INFORMACIÓN DE VERSIÓN:")
    print(f"   Versión Python: {sys.version}")
    print(f"   Versión corta: {sys.version_info}")
    print(f"   Versión mayor: {sys.version_info.major}")
    print(f"   Versión menor: {sys.version_info.minor}")
    
    # 2. INFORMACIÓN DE PLATAFORMA
    print("\n2️⃣ INFORMACIÓN DE PLATAFORMA:")
    print(f"   Plataforma: {sys.platform}")
    print(f"   Arquitectura: {sys.maxsize > 2**32 and '64-bit' or '32-bit'}")
    
    # 3. RUTAS DE BÚSQUEDA (MUY IMPORTANTE)
    print("\n3️⃣ RUTAS DE BÚSQUEDA DE MÓDULOS:")
    print("   Python busca módulos en estas rutas:")
    for i, ruta in enumerate(sys.path[:5]):  # Solo primeras 5 rutas
        print(f"   [{i}] {ruta}")
    print(f"   ... y {len(sys.path) - 5} rutas más")

    """Path es una lista de directorios que Python busca para importar módulos.
    Es importante para importar módulos desde otros directorios.
    Por ejemplo, si tenemos un módulo en el directorio "mi_modulo",
    podemos agregarlo a sys.path para importarlo desde cualquier otro directorio.
    """
    # 4. ARGUMENTOS DE LÍNEA DE COMANDOS
    print("\n4️⃣ ARGUMENTOS DE LÍNEA DE COMANDOS:")
    print(f"   Archivo ejecutado: {sys.argv[0]}")
    print(f"   Todos los argumentos: {sys.argv}")
    print("   💡 Ejemplo: python script.py arg1 arg2")
    print("       sys.argv = ['script.py', 'arg1', 'arg2']")
    """
    sys.argv es una lista de argumentos que se pasan al script cuando se ejecuta.
    El primer elemento es el nombre del script.
    Los siguientes elementos son los argumentos que se pasan al script.
    """
    
    # 5. ENTRADA/SALIDA ESTÁNDAR
    print("\n5️⃣ ENTRADA/SALIDA ESTÁNDAR:")
    print("   stdin (entrada): Para leer input del usuario")
    print("   stdout (salida): Para print() normal")
    print("   stderr (error): Para mensajes de error")
    print(f"   Ejemplo: sys.stderr.write('Error!\\n')")
    
    # 6. TAMAÑO DE OBJETOS
    print("\n6️⃣ TAMAÑO DE OBJETOS:")
    ejemplo_lista = [1, 2, 3, 4, 5]
    ejemplo_string = "Hola mundo"
    print(f"   Lista {ejemplo_lista}: {sys.getsizeof(ejemplo_lista)} bytes")
    print(f"   String '{ejemplo_string}': {sys.getsizeof(ejemplo_string)} bytes")
    """
    sys.getsizeof() es una función que devuelve el tamaño en bytes de un objeto.
    Es útil para saber cuánto memoria ocupa un objeto.
    """
    
    # 7. SALIR DEL PROGRAMA
    print("\n7️⃣ CONTROL DEL PROGRAMA:")
    print("   sys.exit(0)  # Salir con código 0 (éxito)")
    print("   sys.exit(1)  # Salir con código 1 (error)")
    print("   💡 No ejecutamos sys.exit() aquí para no terminar el script")

def ejemplo_manipular_path():
    """Ejemplo de cómo manipular sys.path (como en run.py)"""
    
    print("\n" + "=" * 50)
    print("🛠️ EJEMPLO PRÁCTICO: MANIPULAR sys.path")
    print("=" * 50)
    
    # Guardar estado original
    path_original = sys.path.copy()
    
    print(f"Path original tiene {len(path_original)} rutas")
    
    # Agregar nueva ruta al inicio (como en run.py)
    nueva_ruta = "/mi/proyecto/src"
    sys.path.insert(0, nueva_ruta)
    
    print(f"➕ Agregamos '{nueva_ruta}' al inicio")
    print(f"   Ahora sys.path[0] = {sys.path[0]}")
    
    # Verificar si una ruta existe
    if nueva_ruta in sys.path:
        print("✅ La nueva ruta está en sys.path")
    
    # Restaurar estado original
    sys.path = path_original
    print("🔄 Restauramos sys.path original")

def ejemplo_argumentos_linea_comandos():
    """Ejemplo de cómo usar argumentos de línea de comandos"""
    
    print("\n" + "=" * 50)  
    print("💬 EJEMPLO: ARGUMENTOS DE LÍNEA DE COMANDOS")
    print("=" * 50)
    
    print("Argumentos recibidos:")
    for i, arg in enumerate(sys.argv):
        if i == 0:
            print(f"   Programa: {arg}")
        else:
            print(f"   Argumento {i}: {arg}")
    
    # Ejemplo de cómo procesar argumentos
    if len(sys.argv) > 1:
        print(f"\n🎯 Procesando argumentos:")
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"   Procesando argumento {i}: {arg}")
    else:
        print("\n💡 Para probar argumentos, ejecuta:")
        print("   python 01_sys_module.py arg1 arg2 arg3")

def ejemplo_salida_error():
    """Ejemplo de usar stderr para mensajes de error"""
    
    print("\n" + "=" * 50)
    print("🚨 EJEMPLO: SALIDA DE ERROR")
    print("=" * 50)
    
    # Salida normal (stdout)
    print("✅ Mensaje normal (stdout)")
    
    # Salida de error (stderr)
    sys.stderr.write("⚠️ Mensaje de error (stderr)\n")
    
    # Diferencia práctica:
    # stdout se puede redirigir: python script.py > output.txt
    # stderr NO se redirige: python script.py > output.txt (errores se ven en pantalla)
    
    print("💡 Diferencia práctica:")
    print("   stdout: Para salida normal del programa")
    print("   stderr: Para errores y mensajes de debug")

# CASOS DE USO COMUNES EN TUS PROYECTOS
def casos_uso_comunes():
    """Casos de uso más comunes del módulo sys"""
    
    print("\n" + "=" * 50)
    print("🎯 CASOS DE USO COMUNES")
    print("=" * 50)
    
    print("1. Verificar versión Python:")
    print("   if sys.version_info >= (3, 8):")
    print("       # Código para Python 3.8+")
    
    print("\n2. Agregar ruta para imports:")
    print("   sys.path.insert(0, '/ruta/a/mi/modulo')")
    print("   from mi_modulo import mi_funcion")
    
    print("\n3. Salir con código específico:")
    print("   if error_critico:")
    print("       sys.exit(1)  # Salir con error")
    
    print("\n4. Obtener argumentos:")
    print("   if len(sys.argv) < 2:")
    print("       print('Uso: python script.py <archivo>')")
    print("       sys.exit(1)")
    
    print("\n5. Redirigir salida:")
    print("   sys.stdout = open('output.txt', 'w')")
    print("   print('Esto va al archivo')  # Se guarda en archivo")

if __name__ == "__main__":
    # Ejecutar todos los ejemplos
    ejemplos_sys()
    ejemplo_manipular_path()
    ejemplo_argumentos_linea_comandos()
    ejemplo_salida_error()
    casos_uso_comunes()
    
    print("\n" + "=" * 50)
    print("✅ RESUMEN DEL MÓDULO sys")
    print("=" * 50)
    print("🔧 Usos principales:")
    print("   • Información del sistema Python")
    print("   • Manipular rutas de búsqueda de módulos")
    print("   • Procesar argumentos de línea de comandos")
    print("   • Controlar entrada/salida estándar")
    print("   • Salir del programa con códigos específicos")
    print("\n📚 Documentación oficial:")
    print("   https://docs.python.org/3/library/sys.html") 