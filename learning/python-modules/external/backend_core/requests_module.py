#!/usr/bin/env python3
"""
MÓDULO EXTERNO: requests
========================

¿QUÉ ES?
El módulo 'requests' es la librería HTTP más popular de Python. Hace que 
enviar peticiones HTTP sea extremadamente simple y human-friendly.

INSTALACIÓN:
pip install requests

¿PARA QUÉ SIRVE?
- Hacer peticiones HTTP (GET, POST, PUT, DELETE)
- Consumir APIs REST
- Descargar archivos
- Web scraping básico
- Autenticación HTTP
- Manejo de cookies y sesiones

IMPORTANCIA: ⭐⭐⭐⭐⭐ (Esencial para web y APIs)
"""

# NOTA IMPORTANTE: Este módulo requiere instalación
# pip install requests

def verificar_instalacion():
    """Verificar si requests está instalado"""
    try:
        import requests
        print("✅ Módulo 'requests' instalado correctamente")
        print(f"📦 Versión: {requests.__version__}")
        return True
    except ImportError:
        print("❌ Módulo 'requests' no encontrado")
        print("💡 Para instalar: pip install requests")
        return False

def ejemplo_requests_basico():
    """Ejemplo básico de uso del módulo requests"""
    
    print("=" * 50)
    print("🌐 MÓDULO REQUESTS - HTTP PARA HUMANOS")
    print("=" * 50)
    
    if not verificar_instalacion():
        return
    
    import requests
    
    # 1. GET REQUEST BÁSICO
    print("\n1️⃣ GET REQUEST BÁSICO:")
    
    try:
        # Hacer petición GET a una API pública
        url = "https://httpbin.org/get"
        response = requests.get(url)
        
        print(f"   🎯 URL: {url}")
        print(f"   📊 Status Code: {response.status_code}")
        print(f"   ✅ Exitoso: {response.ok}")
        print(f"   📝 Texto respuesta (primeros 100 chars): {response.text[:100]}...")
        
    except requests.RequestException as e:
        print(f"   ❌ Error en petición: {e}")
    
    # 2. TRABAJAR CON JSON
    print("\n2️⃣ TRABAJAR CON JSON:")
    
    try:
        # API que devuelve JSON
        url = "https://jsonplaceholder.typicode.com/posts/1"
        response = requests.get(url)
        
        if response.ok:
            # Convertir respuesta a JSON automáticamente
            data = response.json()
            print(f"   📄 Post ID: {data['id']}")
            print(f"   📝 Título: {data['title']}")
            print(f"   👤 User ID: {data['userId']}")
            print(f"   📄 Contenido: {data['body'][:50]}...")
        
    except requests.RequestException as e:
        print(f"   ❌ Error: {e}")
    except ValueError:
        print(f"   ❌ Respuesta no es JSON válido")
    
    # 3. HEADERS Y USER AGENT
    print("\n3️⃣ HEADERS Y USER AGENT:")
    
    headers = {
        'User-Agent': 'Mi App de Notas/1.0',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    try:
        url = "https://httpbin.org/headers"
        response = requests.get(url, headers=headers)
        
        if response.ok:
            data = response.json()
            print(f"   📋 Headers enviados:")
            for header, value in headers.items():
                print(f"      {header}: {value}")
            
            print(f"   📋 Headers recibidos por el servidor:")
            received_headers = data['headers']
            for key, value in list(received_headers.items())[:3]:
                print(f"      {key}: {value}")
        
    except requests.RequestException as e:
        print(f"   ❌ Error: {e}")

def ejemplo_requests_metodos_http():
    """Ejemplo de diferentes métodos HTTP"""
    
    print("\n" + "=" * 50)
    print("🔀 MÉTODOS HTTP CON REQUESTS")
    print("=" * 50)
    
    import requests
    
    # URL base para testing
    base_url = "https://jsonplaceholder.typicode.com"
    
    # 1. GET - Obtener datos
    print("\n1️⃣ GET - OBTENER DATOS:")
    
    try:
        response = requests.get(f"{base_url}/posts", params={'_limit': 3})
        
        if response.ok:
            posts = response.json()
            print(f"   📊 Obtenidos {len(posts)} posts")
            for post in posts:
                print(f"   📄 Post {post['id']}: {post['title'][:30]}...")
        
    except requests.RequestException as e:
        print(f"   ❌ Error GET: {e}")
    
    # 2. POST - Crear datos
    print("\n2️⃣ POST - CREAR DATOS:")
    
    nuevo_post = {
        "title": "Mi nueva nota",
        "body": "Contenido de mi nota creada con requests",
        "userId": 1
    }
    
    try:
        response = requests.post(f"{base_url}/posts", json=nuevo_post)
        
        if response.ok:
            created_post = response.json()
            print(f"   ✅ Post creado con ID: {created_post['id']}")
            print(f"   📝 Título: {created_post['title']}")
        
    except requests.RequestException as e:
        print(f"   ❌ Error POST: {e}")
    
    # 3. PUT - Actualizar datos completos
    print("\n3️⃣ PUT - ACTUALIZAR DATOS COMPLETOS:")
    
    post_actualizado = {
        "id": 1,
        "title": "Nota actualizada completamente",
        "body": "Contenido completamente nuevo",
        "userId": 1
    }
    
    try:
        response = requests.put(f"{base_url}/posts/1", json=post_actualizado)
        
        if response.ok:
            updated_post = response.json()
            print(f"   ✅ Post actualizado ID: {updated_post['id']}")
            print(f"   📝 Nuevo título: {updated_post['title']}")
        
    except requests.RequestException as e:
        print(f"   ❌ Error PUT: {e}")
    
    # 4. PATCH - Actualización parcial
    print("\n4️⃣ PATCH - ACTUALIZACIÓN PARCIAL:")
    
    actualizacion_parcial = {
        "title": "Solo cambio el título"
    }
    
    try:
        response = requests.patch(f"{base_url}/posts/1", json=actualizacion_parcial)
        
        if response.ok:
            patched_post = response.json()
            print(f"   ✅ Post actualizado parcialmente")
            print(f"   📝 Nuevo título: {patched_post['title']}")
        
    except requests.RequestException as e:
        print(f"   ❌ Error PATCH: {e}")
    
    # 5. DELETE - Eliminar datos
    print("\n5️⃣ DELETE - ELIMINAR DATOS:")
    
    try:
        response = requests.delete(f"{base_url}/posts/1")
        
        if response.ok:
            print(f"   ✅ Post eliminado exitosamente")
            print(f"   📊 Status code: {response.status_code}")
        
    except requests.RequestException as e:
        print(f"   ❌ Error DELETE: {e}")

def ejemplo_requests_manejo_errores():
    """Ejemplo de manejo de errores con requests"""
    
    print("\n" + "=" * 50)
    print("🚨 MANEJO DE ERRORES CON REQUESTS")
    print("=" * 50)
    
    import requests
    from requests.exceptions import ConnectionError, Timeout, RequestException
    
    # 1. URL INEXISTENTE
    print("\n1️⃣ URL INEXISTENTE:")
    
    try:
        response = requests.get("https://sitio-que-no-existe-12345.com", timeout=5)
        print(f"   ✅ Respuesta: {response.status_code}")
    except ConnectionError:
        print(f"   ❌ Error de conexión: No se pudo conectar al servidor")
    except Timeout:
        print(f"   ❌ Error de timeout: La petición tardó demasiado")
    except RequestException as e:
        print(f"   ❌ Error general: {e}")
    
    # 2. STATUS CODE DE ERROR
    print("\n2️⃣ STATUS CODE DE ERROR:")
    
    try:
        # Esta URL devuelve 404
        response = requests.get("https://httpbin.org/status/404")
        
        print(f"   📊 Status code: {response.status_code}")
        
        # Verificar si la respuesta es exitosa
        if response.ok:
            print(f"   ✅ Petición exitosa")
        else:
            print(f"   ❌ Petición falló")
            
        # Lanzar excepción si hay error
        response.raise_for_status()
        
    except requests.HTTPError as e:
        print(f"   🚨 HTTP Error: {e}")
    except RequestException as e:
        print(f"   ❌ Error general: {e}")
    
    # 3. TIMEOUT PERSONALIZADO
    print("\n3️⃣ TIMEOUT PERSONALIZADO:")
    
    try:
        # URL que tarda en responder
        response = requests.get("https://httpbin.org/delay/2", timeout=1)
        print(f"   ✅ Respuesta rápida: {response.status_code}")
    except Timeout:
        print(f"   ⏰ Timeout: La petición tardó más de 1 segundo")
    except RequestException as e:
        print(f"   ❌ Error: {e}")
    
    # 4. FUNCIÓN HELPER PARA PETICIONES SEGURAS
    def peticion_segura(url, method='GET', **kwargs):
        """Función helper para hacer peticiones seguras"""
        try:
            response = requests.request(method, url, timeout=10, **kwargs)
            response.raise_for_status()
            return response
        except ConnectionError:
            print(f"   ❌ No se pudo conectar a {url}")
            return None
        except Timeout:
            print(f"   ⏰ Timeout al conectar a {url}")
            return None
        except requests.HTTPError as e:
            print(f"   🚨 HTTP Error {e.response.status_code}: {e}")
            return None
        except RequestException as e:
            print(f"   ❌ Error inesperado: {e}")
            return None
    
    print("\n4️⃣ FUNCIÓN HELPER SEGURA:")
    
    # Usar función helper
    response = peticion_segura("https://httpbin.org/get")
    if response:
        print(f"   ✅ Petición exitosa: {response.status_code}")

def ejemplo_requests_autenticacion():
    """Ejemplo de autenticación con requests"""
    
    print("\n" + "=" * 50)
    print("🔐 AUTENTICACIÓN CON REQUESTS")
    print("=" * 50)
    
    import requests
    from requests.auth import HTTPBasicAuth
    
    # 1. AUTENTICACIÓN BÁSICA
    print("\n1️⃣ AUTENTICACIÓN BÁSICA:")
    
    try:
        # Usar httpbin para probar autenticación
        username = "usuario_test"
        password = "password_test"
        
        # Método 1: Usando HTTPBasicAuth
        response = requests.get(
            f"https://httpbin.org/basic-auth/{username}/{password}",
            auth=HTTPBasicAuth(username, password)
        )
        
        if response.ok:
            data = response.json()
            print(f"   ✅ Autenticación exitosa")
            print(f"   👤 Usuario autenticado: {data['user']}")
        
    except requests.RequestException as e:
        print(f"   ❌ Error de autenticación: {e}")
    
    # 2. AUTENTICACIÓN CON TOKEN
    print("\n2️⃣ AUTENTICACIÓN CON TOKEN:")
    
    # Simular token de API
    api_token = "mi_token_secreto_123"
    
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    
    try:
        # Usar httpbin para verificar headers
        response = requests.get("https://httpbin.org/bearer", headers=headers)
        
        if response.ok:
            data = response.json()
            print(f"   ✅ Token enviado correctamente")
            print(f"   🔑 Token: {data['token'][:20]}...")
        
    except requests.RequestException as e:
        print(f"   ❌ Error con token: {e}")
    
    # 3. API KEY EN PARÁMETROS
    print("\n3️⃣ API KEY EN PARÁMETROS:")
    
    api_key = "mi_api_key_123"
    
    params = {
        'api_key': api_key,
        'format': 'json'
    }
    
    try:
        response = requests.get("https://httpbin.org/get", params=params)
        
        if response.ok:
            data = response.json()
            print(f"   ✅ API key enviada en parámetros")
            print(f"   🔗 URL final: {data['url']}")
        
    except requests.RequestException as e:
        print(f"   ❌ Error con API key: {e}")

def ejemplo_requests_sesiones():
    """Ejemplo de sesiones con requests"""
    
    print("\n" + "=" * 50)
    print("🍪 SESIONES Y COOKIES CON REQUESTS")
    print("=" * 50)
    
    import requests
    
    # 1. USANDO SESIONES
    print("\n1️⃣ USANDO SESIONES:")
    
    # Crear sesión
    session = requests.Session()
    
    # Configurar headers por defecto para toda la sesión
    session.headers.update({
        'User-Agent': 'Mi App de Notas/1.0',
        'Accept': 'application/json'
    })
    
    try:
        # Primera petición con la sesión
        response1 = session.get("https://httpbin.org/cookies/set/session_id/abc123")
        print(f"   🍪 Primera petición: {response1.status_code}")
        
        # Segunda petición - mantiene cookies automáticamente
        response2 = session.get("https://httpbin.org/cookies")
        
        if response2.ok:
            data = response2.json()
            print(f"   🍪 Cookies mantenidas: {data['cookies']}")
    
    except requests.RequestException as e:
        print(f"   ❌ Error en sesión: {e}")
    finally:
        session.close()
    
    # 2. MANEJO MANUAL DE COOKIES
    print("\n2️⃣ MANEJO MANUAL DE COOKIES:")
    
    cookies = {
        'usuario_id': '12345',
        'preferencias': 'tema_oscuro'
    }
    
    try:
        response = requests.get("https://httpbin.org/cookies", cookies=cookies)
        
        if response.ok:
            data = response.json()
            print(f"   🍪 Cookies enviadas: {data['cookies']}")
    
    except requests.RequestException as e:
        print(f"   ❌ Error con cookies: {e}")

def ejemplo_requests_descarga_archivos():
    """Ejemplo de descarga de archivos con requests"""
    
    print("\n" + "=" * 50)
    print("📥 DESCARGA DE ARCHIVOS CON REQUESTS")
    print("=" * 50)
    
    import requests
    import os
    
    # 1. DESCARGA SIMPLE
    print("\n1️⃣ DESCARGA SIMPLE:")
    
    try:
        # URL de archivo pequeño para probar
        url = "https://httpbin.org/json"
        response = requests.get(url)
        
        if response.ok:
            # Guardar contenido
            with open("archivo_descargado.json", 'w') as f:
                f.write(response.text)
            
            print(f"   ✅ Archivo descargado: archivo_descargado.json")
            print(f"   📊 Tamaño: {len(response.content)} bytes")
    
    except requests.RequestException as e:
        print(f"   ❌ Error en descarga: {e}")
    
    # 2. DESCARGA CON PROGRESO (para archivos grandes)
    print("\n2️⃣ DESCARGA CON STREAMING:")
    
    try:
        url = "https://httpbin.org/stream/10"
        
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            
            total_size = len(response.content) if hasattr(response, 'content') else 0
            downloaded = 0
            
            with open("archivo_stream.txt", 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
            
            print(f"   ✅ Descarga streaming completada")
            print(f"   📊 Bytes descargados: {downloaded}")
    
    except requests.RequestException as e:
        print(f"   ❌ Error en streaming: {e}")
    
    # Limpiar archivos de prueba
    for archivo in ["archivo_descargado.json", "archivo_stream.txt"]:
        if os.path.exists(archivo):
            os.remove(archivo)
            print(f"   🗑️ Archivo temporal eliminado: {archivo}")

def ejemplo_requests_api_real():
    """Ejemplo práctico con API real"""
    
    print("\n" + "=" * 50)
    print("🌍 EJEMPLO PRÁCTICO CON API REAL")
    print("=" * 50)
    
    import requests
    
    # Usando JSONPlaceholder - API gratuita para testing
    
    # 1. OBTENER LISTA DE USUARIOS
    print("\n1️⃣ OBTENER USUARIOS:")
    
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        
        if response.ok:
            users = response.json()
            print(f"   👥 Total usuarios: {len(users)}")
            
            for user in users[:3]:  # Solo primeros 3
                print(f"   👤 {user['name']} ({user['email']})")
                print(f"      🏢 Empresa: {user['company']['name']}")
    
    except requests.RequestException as e:
        print(f"   ❌ Error obteniendo usuarios: {e}")
    
    # 2. CREAR SIMULACIÓN DE CLASE API CLIENT
    class NotesAPIClient:
        """Cliente para API de notas"""
        
        def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
            self.base_url = base_url
            self.session = requests.Session()
            self.session.headers.update({
                'Content-Type': 'application/json',
                'User-Agent': 'NotesApp/1.0'
            })
        
        def get_posts(self, limit=5):
            """Obtener posts (notas)"""
            try:
                response = self.session.get(
                    f"{self.base_url}/posts",
                    params={'_limit': limit}
                )
                response.raise_for_status()
                return response.json()
            except requests.RequestException as e:
                print(f"Error obteniendo posts: {e}")
                return []
        
        def create_post(self, title, body, user_id=1):
            """Crear nuevo post"""
            try:
                data = {
                    'title': title,
                    'body': body,
                    'userId': user_id
                }
                response = self.session.post(f"{self.base_url}/posts", json=data)
                response.raise_for_status()
                return response.json()
            except requests.RequestException as e:
                print(f"Error creando post: {e}")
                return None
        
        def close(self):
            """Cerrar sesión"""
            self.session.close()
    
    # 3. USAR CLIENTE API
    print("\n2️⃣ USAR CLIENTE API:")
    
    client = NotesAPIClient()
    
    try:
        # Obtener posts existentes
        posts = client.get_posts(3)
        print(f"   📄 Posts obtenidos: {len(posts)}")
        
        for post in posts:
            print(f"   📝 {post['title'][:40]}...")
        
        # Crear nuevo post
        new_post = client.create_post(
            title="Mi nota desde Python",
            body="Esta nota fue creada usando requests en Python"
        )
        
        if new_post:
            print(f"   ✅ Post creado con ID: {new_post['id']}")
            print(f"   📝 Título: {new_post['title']}")
    
    finally:
        client.close()

def casos_uso_comunes():
    """Casos de uso más comunes del módulo requests"""
    
    print("\n" + "=" * 50)
    print("🎯 CASOS DE USO COMUNES")
    print("=" * 50)
    
    print("1. Consumir API REST:")
    print("   response = requests.get('https://api.ejemplo.com/datos')")
    print("   data = response.json()")
    
    print("\n2. Enviar datos a API:")
    print("   data = {'nombre': 'Juan', 'email': 'juan@email.com'}")
    print("   response = requests.post('https://api.ejemplo.com/users', json=data)")
    
    print("\n3. Autenticación con token:")
    print("   headers = {'Authorization': 'Bearer mi_token'}")
    print("   response = requests.get(url, headers=headers)")
    
    print("\n4. Descargar archivo:")
    print("   response = requests.get('https://ejemplo.com/archivo.pdf')")
    print("   with open('archivo.pdf', 'wb') as f:")
    print("       f.write(response.content)")
    
    print("\n5. Manejo de errores:")
    print("   try:")
    print("       response = requests.get(url, timeout=10)")
    print("       response.raise_for_status()")
    print("   except requests.RequestException as e:")
    print("       print(f'Error: {e}')")
    
    print("\n6. Usar sesión para múltiples peticiones:")
    print("   session = requests.Session()")
    print("   session.headers.update({'User-Agent': 'Mi App'})")
    print("   response1 = session.get(url1)")
    print("   response2 = session.get(url2)")

def integracion_con_tax_calculator_pro():
    """Ejemplo de integración con proyecto tax-calculator-pro"""
    
    print("\n" + "=" * 50)
    print("🗂️ INTEGRACIÓN CON NOTESASSISTANT")
    print("=" * 50)
    
    print("💡 Posibles usos de requests en tu proyecto de notas:")
    
    print("\n1. Backup en la nube:")
    print("   # Subir notas a servicio en la nube")
    print("   def backup_notes(notes):")
    print("       response = requests.post(")
    print("           'https://mi-backup-service.com/upload',")
    print("           json={'notes': notes},")
    print("           headers={'Authorization': 'Bearer ' + api_key}")
    print("       )")
    
    print("\n2. Sincronización entre dispositivos:")
    print("   # Obtener notas desde servidor")
    print("   def sync_notes():")
    print("       response = requests.get(")
    print("           'https://mi-api.com/notes',")
    print("           headers={'User-ID': user_id}")
    print("       )")
    print("       return response.json() if response.ok else []")
    
    print("\n3. Integración con servicios externos:")
    print("   # Enviar nota a Slack, Discord, etc.")
    print("   def share_note_to_slack(note_content):")
    print("       payload = {'text': note_content}")
    print("       requests.post(slack_webhook_url, json=payload)")
    
    print("\n4. Importar desde otros servicios:")
    print("   # Importar notas desde Notion, Google Keep, etc.")
    print("   def import_from_service(api_endpoint):")
    print("       response = requests.get(api_endpoint)")
    print("       external_notes = response.json()")
    print("       # Convertir a formato local")

if __name__ == "__main__":
    # Ejecutar todos los ejemplos
    ejemplo_requests_basico()
    ejemplo_requests_metodos_http()
    ejemplo_requests_manejo_errores()
    ejemplo_requests_autenticacion()
    ejemplo_requests_sesiones()
    ejemplo_requests_descarga_archivos()
    ejemplo_requests_api_real()
    casos_uso_comunes()
    integracion_con_tax_calculator_pro()
    
    print("\n" + "=" * 50)
    print("✅ RESUMEN DEL MÓDULO requests")
    print("=" * 50)
    print("🔧 Usos principales:")
    print("   • Hacer peticiones HTTP de forma simple")
    print("   • Consumir APIs REST")
    print("   • Descargar archivos desde internet")
    print("   • Web scraping básico")
    print("   • Autenticación HTTP")
    print("   • Manejo de sesiones y cookies")
    print("\n📚 Documentación oficial:")
    print("   https://docs.python-requests.org/")
    print("\n💡 Consejo: requests es el estándar para HTTP en Python")
    print("   Casi todos los proyectos Python web lo usan.") 