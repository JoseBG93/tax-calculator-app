#!/usr/bin/env python3
"""
MÓDULO NATIVO: logging
======================

¿QUÉ ES?
El módulo 'logging' proporciona un sistema flexible y potente para registrar 
eventos en aplicaciones Python. Es como un "diario" para tu programa.

¿PARA QUÉ SIRVE?
- Registrar información sobre el funcionamiento del programa
- Debugging y diagnóstico de problemas
- Monitoreo de aplicaciones en producción
- Auditoría de operaciones
- Seguimiento de errores y excepciones

IMPORTANCIA: ⭐⭐⭐⭐⭐ (Muy importante para desarrollo profesional)
"""

import logging
import sys
import os
from datetime import datetime
import traceback

def ejemplo_logging_basico():
    """Ejemplo básico de logging"""
    
    print("=" * 50)
    print("📝 MÓDULO LOGGING - REGISTRO DE EVENTOS")
    print("=" * 50)
    
    # 1. CONFIGURACIÓN BÁSICA
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    logger = logging.getLogger(__name__)
    
    print("\n1️⃣ NIVELES DE LOGGING:")
    print("   DEBUG < INFO < WARNING < ERROR < CRITICAL")
    
    # 2. EJEMPLOS DE CADA NIVEL
    print("\n   📋 Ejemplos de cada nivel:")
    
    logger.debug("🔍 DEBUG: Información detallada para debugging")
    logger.info("ℹ️ INFO: Información general del programa")
    logger.warning("⚠️ WARNING: Algo inesperado pero no crítico")
    logger.error("❌ ERROR: Error que no detiene el programa")
    logger.critical("🚨 CRITICAL: Error crítico que puede detener el programa")
    
    print("\n   💡 Solo se muestran INFO y superiores (configuración actual)")

def ejemplo_logging_configuracion():
    """Ejemplo de configuración avanzada de logging"""
    
    print("\n" + "=" * 50)
    print("⚙️ CONFIGURACIÓN AVANZADA DE LOGGING")
    print("=" * 50)
    
    # 1. CONFIGURACIÓN DETALLADA
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
        handlers=[
            logging.FileHandler('app.log'),  # Archivo
            logging.StreamHandler(sys.stdout)  # Consola
        ]
    )
    
    # 2. LOGGER PERSONALIZADO
    logger = logging.getLogger('mi_aplicacion')
    
    print("\n📋 FORMATO DETALLADO:")
    print("   %(asctime)s - Fecha y hora")
    print("   %(name)s - Nombre del logger")
    print("   %(levelname)s - Nivel del mensaje")
    print("   %(funcName)s - Nombre de la función")
    print("   %(lineno)d - Número de línea")
    print("   %(message)s - Mensaje")
    
    print("\n📝 EJEMPLO DE LOGGING DETALLADO:")
    
    def operacion_importante():
        """Función que realiza una operación importante"""
        logger.info("Iniciando operación importante")
        
        try:
            # Simular trabajo
            logger.debug("Procesando datos...")
            resultado = 42 / 1
            logger.info(f"Operación completada. Resultado: {resultado}")
            return resultado
        except Exception as e:
            logger.error(f"Error en operación: {e}")
            raise
    
    def funcion_principal():
        """Función principal de la aplicación"""
        logger.info("Aplicación iniciada")
        
        try:
            resultado = operacion_importante()
            logger.info(f"Aplicación terminada exitosamente. Resultado: {resultado}")
        except Exception as e:
            logger.critical(f"Error crítico en aplicación: {e}")
            logger.critical(f"Traceback:\n{traceback.format_exc()}")
    
    funcion_principal()

def ejemplo_logging_archivos():
    """Ejemplo de logging a archivos"""
    
    print("\n" + "=" * 50)
    print("📁 LOGGING A ARCHIVOS")
    print("=" * 50)
    
    # 1. CONFIGURACIÓN PARA ARCHIVOS
    print("🔧 Configuración de archivos de log:")
    
    # Logger para aplicación general
    app_logger = logging.getLogger('app')
    app_logger.setLevel(logging.INFO)
    
    # Logger para errores específicos
    error_logger = logging.getLogger('errors')
    error_logger.setLevel(logging.ERROR)
    
    # 2. HANDLERS ESPECÍFICOS
    
    # Handler para archivo general
    app_handler = logging.FileHandler('aplicacion.log')
    app_handler.setLevel(logging.INFO)
    app_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    app_handler.setFormatter(app_formatter)
    
    # Handler para archivo de errores
    error_handler = logging.FileHandler('errores.log')
    error_handler.setLevel(logging.ERROR)
    error_formatter = logging.Formatter('%(asctime)s - CRITICAL - %(message)s\n%(pathname)s:%(lineno)d\n')
    error_handler.setFormatter(error_formatter)
    
    # Handler para consola
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    
    # 3. AGREGAR HANDLERS A LOGGERS
    app_logger.addHandler(app_handler)
    app_logger.addHandler(console_handler)
    
    error_logger.addHandler(error_handler)
    error_logger.addHandler(console_handler)
    
    print(f"   📄 Archivo general: aplicacion.log")
    print(f"   📄 Archivo errores: errores.log")
    print(f"   📺 Consola: para monitoreo en tiempo real")
    
    # 4. EJEMPLOS DE USO
    print("\n📝 Ejemplos de logging a archivos:")
    
    def procesar_usuario(user_id):
        """Procesar información de usuario"""
        app_logger.info(f"Procesando usuario {user_id}")
        
        if user_id == 999:
            error_msg = f"Usuario {user_id} no encontrado"
            app_logger.error(error_msg)
            error_logger.error(f"USER_NOT_FOUND: {error_msg}")
            return False
        
        app_logger.info(f"Usuario {user_id} procesado exitosamente")
        return True
    
    # Procesar algunos usuarios
    usuarios = [123, 456, 999, 789]
    for user_id in usuarios:
        procesar_usuario(user_id)
    
    print(f"\n📊 Resultados guardados en:")
    print(f"   aplicacion.log - Registro general")
    print(f"   errores.log - Solo errores críticos")

def ejemplo_logging_formato_personalizado():
    """Ejemplo de formatos personalizados de logging"""
    
    print("\n" + "=" * 50)
    print("🎨 FORMATOS PERSONALIZADOS DE LOGGING")
    print("=" * 50)
    
    # 1. DIFERENTES FORMATOS
    formatos = {
        'simple': '%(levelname)s - %(message)s',
        'detallado': '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
        'produccion': '%(asctime)s | %(levelname)8s | %(name)s | %(message)s',
        'json_like': '{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}',
        'desarrollo': '🐍 %(asctime)s [%(levelname)s] %(funcName)s() → %(message)s'
    }
    
    print("📋 Formatos disponibles:")
    for nombre, formato in formatos.items():
        print(f"   {nombre}: {formato}")
    
    # 2. CONFIGURAR LOGGER CON FORMATO PERSONALIZADO
    def crear_logger_con_formato(nombre, formato):
        """Crear logger con formato específico"""
        logger = logging.getLogger(nombre)
        logger.setLevel(logging.DEBUG)
        
        # Limpiar handlers existentes
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
        
        # Crear nuevo handler
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(formato)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger
    
    # 3. EJEMPLOS DE CADA FORMATO
    print("\n📝 Ejemplos de cada formato:")
    
    def operacion_demo():
        """Operación de demostración"""
        mensaje = "Operación de demostración ejecutada"
        
        for nombre, formato in formatos.items():
            print(f"\n   🎯 Formato '{nombre}':")
            logger = crear_logger_con_formato(f"demo_{nombre}", formato)
            logger.info(mensaje)

    operacion_demo()

def ejemplo_logging_filtros():
    """Ejemplo de filtros de logging"""
    
    print("\n" + "=" * 50)
    print("🔍 FILTROS DE LOGGING")
    print("=" * 50)
    
    # 1. FILTRO PERSONALIZADO
    class FiltroSensible(logging.Filter):
        """Filtro para ocultar información sensible"""
        
        def filter(self, record):
            # No registrar mensajes con información sensible
            mensaje = record.getMessage()
            palabras_prohibidas = ['password', 'secret', 'token']
            
            for palabra in palabras_prohibidas:
                if palabra.lower() in mensaje.lower():
                    record.msg = mensaje.replace(palabra, '***CENSURADO***')
            
            return True
    
    # 2. FILTRO POR NIVEL
    class FiltroPorModulo(logging.Filter):
        """Filtro por módulo específico"""
        
        def __init__(self, modulo):
            self.modulo = modulo
        
        def filter(self, record):
            return record.name.startswith(self.modulo)
    
    # 3. CONFIGURAR LOGGER CON FILTROS
    logger = logging.getLogger('sistema_seguro')
    logger.setLevel(logging.DEBUG)
    
    # Crear handler
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # Agregar filtros
    handler.addFilter(FiltroSensible())
    logger.addHandler(handler)
    
    print("🔒 Ejemplo de filtro de información sensible:")
    
    def login_usuario(username, password):
        """Simular login de usuario"""
        logger.info(f"Intento de login para usuario: {username}")
        logger.debug(f"Validando password: {password}")  # Será censurado
        logger.info("Login exitoso")
    
    def obtener_token(secret_key):
        """Simular obtención de token"""
        logger.info("Generando token de acceso")
        logger.debug(f"Usando secret key: {secret_key}")  # Será censurado
        logger.info("Token generado exitosamente")
    
    # Ejemplos
    login_usuario("juan123", "mi_password_secreto")
    obtener_token("super_secret_key_123")

def ejemplo_logging_rotativo():
    """Ejemplo de logging rotativo"""
    
    print("\n" + "=" * 50)
    print("🔄 LOGGING ROTATIVO")
    print("=" * 50)
    
    from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
    
    # 1. ROTACIÓN POR TAMAÑO
    print("📏 Rotación por tamaño:")
    
    logger_size = logging.getLogger('rotativo_size')
    logger_size.setLevel(logging.INFO)
    
    # Handler que rota cuando el archivo alcanza 1KB
    size_handler = RotatingFileHandler(
        'app_rotativo.log',
        maxBytes=1024,  # 1KB
        backupCount=3   # Mantener 3 archivos de backup
    )
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    size_handler.setFormatter(formatter)
    logger_size.addHandler(size_handler)
    
    print(f"   📄 Archivo principal: app_rotativo.log")
    print(f"   📄 Archivos backup: app_rotativo.log.1, app_rotativo.log.2, app_rotativo.log.3")
    print(f"   📏 Tamaño máximo: 1KB por archivo")
    
    # 2. ROTACIÓN POR TIEMPO
    print(f"\n⏰ Rotación por tiempo:")
    
    logger_time = logging.getLogger('rotativo_time')
    logger_time.setLevel(logging.INFO)
    
    # Handler que rota cada día a medianoche
    time_handler = TimedRotatingFileHandler(
        'app_diario.log',
        when='midnight',
        interval=1,
        backupCount=7  # Mantener 7 días de logs
    )
    
    time_handler.setFormatter(formatter)
    logger_time.addHandler(time_handler)
    
    print(f"   📄 Archivo principal: app_diario.log")
    print(f"   📄 Archivos backup: app_diario.log.2024-01-01, app_diario.log.2024-01-02, etc.")
    print(f"   ⏰ Rotación: Cada día a medianoche")
    
    # 3. EJEMPLO DE USO
    print(f"\n📝 Ejemplo de logs rotativos:")
    
    def generar_logs_ejemplo():
        """Generar algunos logs para demostrar rotación"""
        for i in range(20):
            mensaje = f"Mensaje de ejemplo #{i+1} - " + "A" * 50  # Mensaje largo
            logger_size.info(mensaje)
            logger_time.info(f"Log diario #{i+1}")
    
    generar_logs_ejemplo()
    
    print(f"   ✅ Logs generados. Revisar archivos app_rotativo.log* y app_diario.log*")

def casos_uso_comunes():
    """Casos de uso más comunes del módulo logging"""
    
    print("\n" + "=" * 50)
    print("🎯 CASOS DE USO COMUNES")
    print("=" * 50)
    
    print("1. Configuración básica para desarrollo:")
    print("   logging.basicConfig(")
    print("       level=logging.DEBUG,")
    print("       format='%(asctime)s - %(levelname)s - %(message)s'")
    print("   )")
    
    print("\n2. Logging con archivos separados:")
    print("   # Logger para aplicación")
    print("   app_logger = logging.getLogger('app')")
    print("   app_handler = logging.FileHandler('app.log')")
    print("   app_logger.addHandler(app_handler)")
    
    print("\n3. Logging de errores con traceback:")
    print("   try:")
    print("       operacion_riesgosa()")
    print("   except Exception as e:")
    print("       logger.error(f'Error: {e}')")
    print("       logger.error(traceback.format_exc())")
    
    print("\n4. Logging condicional (debug vs producción):")
    print("   if DEBUG:")
    print("       logger.debug('Información detallada')")
    print("   else:")
    print("       logger.info('Información general')")
    
    print("\n5. Logging con contexto:")
    print("   def procesar_pedido(pedido_id):")
    print("       logger.info(f'Procesando pedido {pedido_id}')")
    print("       # ... lógica ...")
    print("       logger.info(f'Pedido {pedido_id} procesado')")
    
    print("\n6. Logging para APIs:")
    print("   @app.route('/api/users')")
    print("   def get_users():")
    print("       logger.info(f'API llamada: GET /api/users')")
    print("       # ... lógica ...")
    print("       logger.info(f'API respuesta: {len(users)} usuarios')")

def ejemplo_logging_completo():
    """Ejemplo completo de sistema de logging"""
    
    print("\n" + "=" * 50)
    print("💡 EJEMPLO COMPLETO: SISTEMA DE LOGGING")
    print("=" * 50)
    
    def configurar_logging():
        """Configurar sistema completo de logging"""
        
        # 1. CONFIGURACIÓN PRINCIPAL
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('sistema_completo.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        # 2. LOGGERS ESPECIALIZADOS
        loggers = {
            'auth': logging.getLogger('sistema.auth'),
            'db': logging.getLogger('sistema.database'),
            'api': logging.getLogger('sistema.api'),
            'security': logging.getLogger('sistema.security')
        }
        
        # 3. CONFIGURAR NIVELES
        loggers['security'].setLevel(logging.WARNING)  # Solo warnings y errores
        
        return loggers
    
    def simular_aplicacion():
        """Simular funcionamiento de aplicación completa"""
        
        loggers = configurar_logging()
        
        # Simular operaciones
        loggers['auth'].info("Usuario admin iniciando sesión")
        loggers['db'].info("Conectando a base de datos")
        loggers['api'].info("API endpoint /users llamado")
        
        # Simular warning
        loggers['security'].warning("Intento de acceso no autorizado detectado")
        
        # Simular error
        try:
            # Simular error de base de datos
            raise ConnectionError("No se pudo conectar a la base de datos")
        except Exception as e:
            loggers['db'].error(f"Error de conexión: {e}")
            loggers['db'].error(traceback.format_exc())
        
        loggers['auth'].info("Sesión de usuario terminada")
        
        print(f"\n   📄 Logs guardados en: sistema_completo.log")
        print(f"   📊 Revisar archivo para ver logs estructurados")
    
    simular_aplicacion()

if __name__ == "__main__":
    # Ejecutar todos los ejemplos
    ejemplo_logging_basico()
    ejemplo_logging_configuracion()
    ejemplo_logging_archivos()
    ejemplo_logging_formato_personalizado()
    ejemplo_logging_filtros()
    ejemplo_logging_rotativo()
    casos_uso_comunes()
    ejemplo_logging_completo()
    
    print("\n" + "=" * 50)
    print("✅ RESUMEN DEL MÓDULO logging")
    print("=" * 50)
    print("🔧 Usos principales:")
    print("   • Registrar eventos y actividades del programa")
    print("   • Debugging y diagnóstico de problemas")
    print("   • Monitoreo de aplicaciones en producción")
    print("   • Auditoría y seguimiento de operaciones")
    print("   • Manejo profesional de errores")
    print("\n📚 Documentación oficial:")
    print("   https://docs.python.org/3/library/logging.html")
    print("\n💡 Consejo: Usar logging en lugar de print() para aplicaciones serias")
    print("   logging es más flexible, configurable y profesional.") 