#!/usr/bin/env python3
"""
MÓDULO NATIVO: json
===================

¿QUÉ ES?
El módulo 'json' proporciona funciones para trabajar con el formato JSON 
(JavaScript Object Notation). JSON es un formato de intercambio de datos 
ligero y fácil de leer.

¿PARA QUÉ SIRVE?
- Serializar datos Python a formato JSON
- Deserializar datos JSON a objetos Python
- Comunicación con APIs web
- Almacenamiento de configuraciones
- Intercambio de datos entre sistemas

IMPORTANCIA: ⭐⭐⭐⭐⭐ (Muy importante para APIs y datos)
"""

import json
import os
from datetime import datetime
from collections import OrderedDict

def ejemplo_json_basico():
    """Ejemplo básico de uso del módulo json"""
    
    print("=" * 50)
    print("📄 MÓDULO JSON - MANEJO DE DATOS JSON")
    print("=" * 50)
    
    # 1. DATOS PYTHON → JSON (SERIALIZACIÓN)
    print("\n1️⃣ SERIALIZACIÓN: Python → JSON")
    
    datos_python = {
        "nombre": "Juan Pérez",
        "edad": 30,
        "activo": True,
        "salario": 45000.50,
        "skills": ["Python", "JavaScript", "SQL"],
        "direccion": {
            "ciudad": "Madrid",
            "codigo_postal": "28001"
        },
        "proyectos": None
    }
    
    # Convertir a JSON string
    json_string = json.dumps(datos_python)
    print(f"   Python dict: {datos_python}")
    print(f"   JSON string: {json_string}")
    
    # 2. JSON → DATOS PYTHON (DESERIALIZACIÓN)
    print("\n2️⃣ DESERIALIZACIÓN: JSON → Python")
    
    json_texto = '''
    {
        "producto": "Laptop",
        "precio": 899.99,
        "disponible": true,
        "categorias": ["electrónicos", "computadoras"],
        "especificaciones": {
            "ram": "16GB",
            "almacenamiento": "512GB SSD"
        }
    }
    '''
    
    # Convertir JSON a Python dict
    datos_recuperados = json.loads(json_texto)
    print(f"   JSON texto: {json_texto.strip()}")
    print(f"   Python dict: {datos_recuperados}")
    
    # 3. TIPOS DE DATOS COMPATIBLES
    print("\n3️⃣ TIPOS DE DATOS COMPATIBLES:")
    print("   Python → JSON:")
    print("   dict → object")
    print("   list, tuple → array")
    print("   str → string")
    print("   int, float → number")
    print("   True → true")
    print("   False → false")
    print("   None → null")

def ejemplo_json_archivos():
    """Ejemplo de lectura y escritura de archivos JSON"""
    
    print("\n" + "=" * 50)
    print("📁 JSON CON ARCHIVOS")
    print("=" * 50)
    
    # 1. ESCRIBIR JSON A ARCHIVO
    print("\n1️⃣ ESCRIBIR JSON A ARCHIVO:")
    
    datos_usuario = {
        "usuarios": [
            {
                "id": 1,
                "nombre": "Ana García",
                "email": "ana@example.com",
                "registro": "2024-01-15",
                "configuracion": {
                    "tema": "oscuro",
                    "notificaciones": True,
                    "idioma": "es"
                }
            },
            {
                "id": 2,
                "nombre": "Carlos López",
                "email": "carlos@example.com",
                "registro": "2024-01-16",
                "configuracion": {
                    "tema": "claro",
                    "notificaciones": False,
                    "idioma": "es"
                }
            }
        ],
        "metadatos": {
            "version": "1.0",
            "created_at": datetime.now().isoformat(),
            "total_users": 2
        }
    }
    
    # Guardar en archivo
    archivo_salida = "usuarios.json"
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(datos_usuario, f, indent=2, ensure_ascii=False)
    
    print(f"   ✅ Datos guardados en: {archivo_salida}")
    print(f"   📊 Contenido: {len(datos_usuario['usuarios'])} usuarios")
    
    # 2. LEER JSON DESDE ARCHIVO
    print("\n2️⃣ LEER JSON DESDE ARCHIVO:")
    
    try:
        with open(archivo_salida, 'r', encoding='utf-8') as f:
            datos_cargados = json.load(f)
        
        print(f"   ✅ Datos cargados desde: {archivo_salida}")
        print(f"   📊 Usuarios encontrados: {len(datos_cargados['usuarios'])}")
        
        # Mostrar información de cada usuario
        for usuario in datos_cargados['usuarios']:
            print(f"   👤 {usuario['nombre']} ({usuario['email']})")
            print(f"      Tema: {usuario['configuracion']['tema']}")
    
    except FileNotFoundError:
        print(f"   ❌ Error: Archivo {archivo_salida} no encontrado")
    except json.JSONDecodeError as e:
        print(f"   ❌ Error al parsear JSON: {e}")
    
    # 3. OPCIONES DE FORMATEO
    print("\n3️⃣ OPCIONES DE FORMATEO:")
    
    datos_ejemplo = {"a": 1, "b": [2, 3], "c": {"d": 4}}
    
    print("   Compacto:")
    print(f"   {json.dumps(datos_ejemplo, separators=(',', ':'))}")
    
    print("   Formateado:")
    print(f"   {json.dumps(datos_ejemplo, indent=2)}")
    
    print("   Ordenado por claves:")
    print(f"   {json.dumps(datos_ejemplo, indent=2, sort_keys=True)}")

def ejemplo_json_manejo_errores():
    """Ejemplo de manejo de errores con JSON"""
    
    print("\n" + "=" * 50)
    print("🚨 MANEJO DE ERRORES JSON")
    print("=" * 50)
    
    # 1. JSON MALFORMADO
    print("\n1️⃣ JSON MALFORMADO:")
    
    json_malformado = '''
    {
        "nombre": "Juan",
        "edad": 30,
        "activo": True,  // Comentario no válido en JSON
        "extra": ,       // Coma sin valor
    }
    '''
    
    try:
        datos = json.loads(json_malformado)
        print(f"   ✅ JSON parseado correctamente")
    except json.JSONDecodeError as e:
        print(f"   ❌ Error de JSON: {e}")
        print(f"   📍 Línea: {e.lineno}, Columna: {e.colno}")
        print(f"   💡 Mensaje: {e.msg}")
    
    # 2. TIPOS NO SERIALIZABLES
    print("\n2️⃣ TIPOS NO SERIALIZABLES:")
    
    from datetime import datetime
    
    datos_con_fecha = {
        "evento": "Reunión",
        "fecha": datetime.now(),  # datetime no es serializable por defecto
        "participantes": ["Ana", "Carlos"]
    }
    
    try:
        json_string = json.dumps(datos_con_fecha)
        print(f"   ✅ JSON creado correctamente")
    except TypeError as e:
        print(f"   ❌ Error de tipo: {e}")
        print(f"   💡 Solución: Convertir datetime a string")
        
        # Solución: convertir datetime a string
        datos_corregidos = {
            "evento": "Reunión",
            "fecha": datetime.now().isoformat(),  # Convertir a string
            "participantes": ["Ana", "Carlos"]
        }
        
        json_string = json.dumps(datos_corregidos)
        print(f"   ✅ JSON corregido: {json_string}")
    
    # 3. ARCHIVO NO ENCONTRADO
    print("\n3️⃣ ARCHIVO NO ENCONTRADO:")
    
    try:
        with open("archivo_inexistente.json", 'r') as f:
            datos = json.load(f)
    except FileNotFoundError:
        print(f"   ❌ Archivo no encontrado")
        print(f"   💡 Solución: Verificar ruta o crear archivo por defecto")
        
        # Crear archivo por defecto
        datos_default = {"mensaje": "Archivo creado por defecto"}
        with open("archivo_inexistente.json", 'w') as f:
            json.dump(datos_default, f, indent=2)
        print(f"   ✅ Archivo creado con datos por defecto")

def ejemplo_json_personalizado():
    """Ejemplo de serialización personalizada"""
    
    print("\n" + "=" * 50)
    print("🎨 SERIALIZACIÓN PERSONALIZADA")
    print("=" * 50)
    
    # 1. ENCODER PERSONALIZADO
    print("\n1️⃣ ENCODER PERSONALIZADO:")
    
    class DateTimeEncoder(json.JSONEncoder):
        """Encoder personalizado para datetime"""
        
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            return super().default(obj)
    
    # Datos con datetime
    evento = {
        "nombre": "Conferencia Python",
        "fecha_inicio": datetime(2024, 3, 15, 9, 0),
        "fecha_fin": datetime(2024, 3, 15, 17, 0),
        "lugar": "Madrid",
        "asistentes": 150
    }
    
    # Serializar con encoder personalizado
    json_evento = json.dumps(evento, cls=DateTimeEncoder, indent=2)
    print(f"   📅 Evento serializado:")
    print(f"   {json_evento}")
    
    # 2. DECODER PERSONALIZADO
    print("\n2️⃣ DECODER PERSONALIZADO:")
    
    def datetime_decoder(dct):
        """Decoder personalizado para datetime"""
        for key, value in dct.items():
            if key.endswith('_inicio') or key.endswith('_fin'):
                try:
                    dct[key] = datetime.fromisoformat(value)
                except (ValueError, TypeError):
                    pass  # Mantener valor original si no es datetime
        return dct
    
    # Deserializar con decoder personalizado
    evento_recuperado = json.loads(json_evento, object_hook=datetime_decoder)
    print(f"   📅 Evento deserializado:")
    print(f"   Fecha inicio: {evento_recuperado['fecha_inicio']} (tipo: {type(evento_recuperado['fecha_inicio'])})")
    print(f"   Fecha fin: {evento_recuperado['fecha_fin']} (tipo: {type(evento_recuperado['fecha_fin'])})")
    
    # 3. PRESERVAR ORDEN CON ORDEREDDICT
    print("\n3️⃣ PRESERVAR ORDEN CON ORDEREDDICT:")
    
    json_ordenado = '{"z": 1, "a": 2, "m": 3}'
    
    # Cargar como OrderedDict
    datos_ordenados = json.loads(json_ordenado, object_pairs_hook=OrderedDict)
    print(f"   📊 Datos ordenados: {datos_ordenados}")
    print(f"   🔑 Claves en orden: {list(datos_ordenados.keys())}")

def ejemplo_json_apis():
    """Ejemplo de JSON para APIs"""
    
    print("\n" + "=" * 50)
    print("🌐 JSON PARA APIs")
    print("=" * 50)
    
    # 1. ESTRUCTURA DE RESPUESTA API
    print("\n1️⃣ ESTRUCTURA DE RESPUESTA API:")
    
    def crear_respuesta_api(success=True, data=None, message="", status_code=200):
        """Crear respuesta estándar de API"""
        respuesta = {
            "success": success,
            "status_code": status_code,
            "timestamp": datetime.now().isoformat(),
            "message": message,
            "data": data
        }
        return respuesta
    
    # Respuesta exitosa
    usuarios_data = [
        {"id": 1, "nombre": "Ana", "activo": True},
        {"id": 2, "nombre": "Carlos", "activo": False}
    ]
    
    respuesta_exitosa = crear_respuesta_api(
        success=True,
        data=usuarios_data,
        message="Usuarios obtenidos correctamente",
        status_code=200
    )
    
    print(f"   ✅ Respuesta exitosa:")
    print(f"   {json.dumps(respuesta_exitosa, indent=2)}")
    
    # Respuesta de error
    respuesta_error = crear_respuesta_api(
        success=False,
        data=None,
        message="Usuario no encontrado",
        status_code=404
    )
    
    print(f"\n   ❌ Respuesta de error:")
    print(f"   {json.dumps(respuesta_error, indent=2)}")
    
    # 2. VALIDACIÓN DE DATOS DE ENTRADA
    print("\n2️⃣ VALIDACIÓN DE DATOS DE ENTRADA:")
    
    def validar_datos_usuario(json_data):
        """Validar datos de usuario desde JSON"""
        errores = []
        
        # Campos requeridos
        campos_requeridos = ['nombre', 'email', 'edad']
        for campo in campos_requeridos:
            if campo not in json_data:
                errores.append(f"Campo '{campo}' es requerido")
        
        # Validaciones específicas
        if 'email' in json_data:
            if '@' not in json_data['email']:
                errores.append("Email debe contener @")
        
        if 'edad' in json_data:
            if not isinstance(json_data['edad'], int) or json_data['edad'] < 0:
                errores.append("Edad debe ser un número entero positivo")
        
        return errores
    
    # Datos válidos
    datos_validos = {
        "nombre": "María González",
        "email": "maria@example.com",
        "edad": 28
    }
    
    errores = validar_datos_usuario(datos_validos)
    if errores:
        print(f"   ❌ Errores en datos válidos: {errores}")
    else:
        print(f"   ✅ Datos válidos: {json.dumps(datos_validos)}")
    
    # Datos inválidos
    datos_invalidos = {
        "nombre": "Pedro",
        "email": "pedro-sin-arroba",
        "edad": "veintiocho"  # Debería ser número
    }
    
    errores = validar_datos_usuario(datos_invalidos)
    if errores:
        print(f"   ❌ Errores encontrados: {errores}")

def ejemplo_json_configuracion():
    """Ejemplo de uso de JSON para configuración"""
    
    print("\n" + "=" * 50)
    print("⚙️ JSON PARA CONFIGURACIÓN")
    print("=" * 50)
    
    # 1. ARCHIVO DE CONFIGURACIÓN
    print("\n1️⃣ ARCHIVO DE CONFIGURACIÓN:")
    
    configuracion_app = {
        "app": {
            "name": "Notes Assistant",
            "version": "1.0.0",
            "debug": True,
            "port": 8000
        },
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "notes_db",
            "user": "admin",
            "password": "secret123"
        },
        "logging": {
            "level": "INFO",
            "file": "app.log",
            "max_size": "10MB",
            "backup_count": 5
        },
        "features": {
            "authentication": True,
            "encryption": False,
            "api_rate_limit": 1000
        }
    }
    
    # Guardar configuración
    with open("config.json", 'w') as f:
        json.dump(configuracion_app, f, indent=2)
    
    print(f"   ✅ Configuración guardada en: config.json")
    
    # 2. CARGAR Y USAR CONFIGURACIÓN
    print("\n2️⃣ CARGAR Y USAR CONFIGURACIÓN:")
    
    class ConfigManager:
        """Gestor de configuración"""
        
        def __init__(self, config_file="config.json"):
            self.config_file = config_file
            self.config = self.load_config()
        
        def load_config(self):
            """Cargar configuración desde archivo"""
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except FileNotFoundError:
                print(f"   ⚠️ Archivo de configuración no encontrado, usando defaults")
                return self.get_default_config()
            except json.JSONDecodeError as e:
                print(f"   ❌ Error en archivo de configuración: {e}")
                return self.get_default_config()
        
        def get_default_config(self):
            """Configuración por defecto"""
            return {
                "app": {"name": "App", "debug": False, "port": 8000},
                "database": {"host": "localhost", "port": 5432},
                "logging": {"level": "INFO"}
            }
        
        def get(self, key, default=None):
            """Obtener valor de configuración"""
            keys = key.split('.')
            value = self.config
            
            for k in keys:
                if isinstance(value, dict) and k in value:
                    value = value[k]
                else:
                    return default
            
            return value
    
    # Usar configuración
    config = ConfigManager()
    
    print(f"   📱 Nombre de app: {config.get('app.name')}")
    print(f"   🐛 Debug mode: {config.get('app.debug')}")
    print(f"   🌐 Puerto: {config.get('app.port')}")
    print(f"   📊 Nivel de logging: {config.get('logging.level')}")
    print(f"   🔐 Autenticación: {config.get('features.authentication')}")
    print(f"   📨 Rate limit: {config.get('features.api_rate_limit')}")

def casos_uso_comunes():
    """Casos de uso más comunes del módulo json"""
    
    print("\n" + "=" * 50)
    print("🎯 CASOS DE USO COMUNES")
    print("=" * 50)
    
    print("1. Guardar datos en archivo:")
    print("   data = {'users': [{'name': 'Ana', 'id': 1}]}")
    print("   with open('data.json', 'w') as f:")
    print("       json.dump(data, f, indent=2)")
    
    print("\n2. Cargar datos desde archivo:")
    print("   with open('data.json', 'r') as f:")
    print("       data = json.load(f)")
    
    print("\n3. Convertir dict a JSON string:")
    print("   json_string = json.dumps(data, indent=2)")
    
    print("\n4. Parsear JSON string:")
    print("   data = json.loads(json_string)")
    
    print("\n5. Respuesta de API:")
    print("   response = {")
    print("       'success': True,")
    print("       'data': users,")
    print("       'message': 'Success'")
    print("   }")
    print("   return json.dumps(response)")
    
    print("\n6. Configuración de aplicación:")
    print("   config = {")
    print("       'database': {'host': 'localhost'},")
    print("       'debug': True")
    print("   }")
    print("   with open('config.json', 'w') as f:")
    print("       json.dump(config, f)")
    
    print("\n7. Logging estructurado:")
    print("   log_entry = {")
    print("       'timestamp': datetime.now().isoformat(),")
    print("       'level': 'ERROR',")
    print("       'message': 'Database connection failed'")
    print("   }")
    print("   print(json.dumps(log_entry))")

if __name__ == "__main__":
    # Ejecutar todos los ejemplos
    ejemplo_json_basico()
    ejemplo_json_archivos()
    ejemplo_json_manejo_errores()
    ejemplo_json_personalizado()
    ejemplo_json_apis()
    ejemplo_json_configuracion()
    casos_uso_comunes()
    
    # Limpiar archivos temporales
    archivos_temporales = ['usuarios.json', 'archivo_inexistente.json', 'config.json']
    for archivo in archivos_temporales:
        if os.path.exists(archivo):
            os.remove(archivo)
    
    print("\n" + "=" * 50)
    print("✅ RESUMEN DEL MÓDULO json")
    print("=" * 50)
    print("🔧 Usos principales:")
    print("   • Serializar datos Python a JSON")
    print("   • Deserializar JSON a datos Python")
    print("   • Comunicación con APIs web")
    print("   • Almacenamiento de configuraciones")
    print("   • Intercambio de datos entre sistemas")
    print("\n📚 Documentación oficial:")
    print("   https://docs.python.org/3/library/json.html")
    print("\n💡 Consejo: JSON es el estándar para intercambio de datos en web")
    print("   Siempre manejar errores JSONDecodeError en aplicaciones reales.") 