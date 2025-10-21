"""
GUÍA COMPLETA DE DECORADORES EN PYTHON - BLOQUE 5
DECORADORES PARA FLASK - MUY IMPORTANTES PARA NUESTRO PROYECTO WEB
Tax Calculator Pro - Referencia para José
"""

from functools import wraps

print("="*80)
print("BLOQUE 5: DECORADORES PARA FLASK - APLICACIÓN WEB")
print("="*80)

# ============================================================================
# 5. DECORADORES PARA FLASK - MUY IMPORTANTES PARA NUESTRO PROYECTO WEB
# ============================================================================

print("\n5. Decoradores para Flask - Para nuestra aplicación web")
print("-" * 60)

# Simulación de decoradores Flask (sin importar Flask para esta demo)
def route(path):
    """
    FUNCIÓN QUE CREA DECORADORES PARA RUTAS WEB
    
    ¿QUÉ HACE?
    • Esta función crea decoradores personalizados para cada dirección web
    • Cuando escribes @route("/calcular"), Python llama a route("/calcular")
    • La función route() devuelve un decorador específico para esa ruta
    
    PARÁMETROS:
    • path: La dirección web que quieres crear (ej: "/calcular", "/admin", "/")
    
    FLUJO COMPLETO:
    1. Usuario escribe @route("/calcular") 
    2. Python ejecuta route("/calcular") 
    3. route() devuelve un decorador personalizado
    4. Ese decorador se aplica a la función que viene después
    """
    def decorator(func):
        """
        DECORADOR PERSONALIZADO PARA ESTA RUTA ESPECÍFICA
        
        ¿QUÉ HACE?
        • Recibe la función Python (ej: calcular_impuesto) como parámetro
        • Crea una versión "mejorada" (wrapper) de esa función
        • La función mejorada incluye funcionalidades extra de Flask
        
        PARÁMETROS:
        • func: La función original (ej: calcular_impuesto, panel_admin)
        
        FLUJO:
        1. @route("/calcular") crea este decorador
        2. Python pasa calcular_impuesto() como 'func' 
        3. decorator() crea una versión mejorada (wrapper)
        4. Devuelve el wrapper que reemplaza a la función original
        """
        @wraps(func)  # Preserva nombre y documentación de la función original
        def wrapper(*args, **kwargs):
            """
            FUNCIÓN MEJORADA QUE REEMPLAZA A LA ORIGINAL
            
            ¿QUÉ HACE?
            • Se ejecuta cada vez que un usuario visita la ruta web
            • Contiene la función original + funcionalidades extra de Flask
            • Devuelve el resultado al navegador del usuario
            
            PARÁMETROS:
            • *args, **kwargs: Acepta cualquier combinación de argumentos
              para que funcione con cualquier tipo de función
            
            FLUJO CUANDO USUARIO VISITA LA WEB:
            1. Usuario escribe: www.tuapp.com/calcular
            2. Flask ejecuta wrapper() correspondiente a esa ruta
            3. wrapper() ejecuta la función original (calcular_impuesto)
            4. wrapper() devuelve el resultado ("IIVTNU: 3500€")
            5. Usuario ve el resultado en su navegador
            """
            print(f"🌐 PASO 1: Ruta registrada: {path} -> {func.__name__}")
            # Ejecutamos la función original y devolvemos su resultado
            return func(*args, **kwargs)  # ← ESTO es lo que ve el usuario final
        
        # CREACIÓN DE ATRIBUTOS PERSONALIZADOS PARA FLASK
        # Flask guarda internamente qué ruta corresponde a qué función
        wrapper._route_path = path  # ← AÑADIMOS una propiedad nueva a la función wrapper
        
        # ¿QUÉ SIGNIFICA wrapper._route_path = path?
        # • wrapper: La función mejorada que creamos
        # • _route_path: Nombre de atributo INVENTADO (como "_animales" o "_comida")
        # • path: El valor que le asignamos (ej: "/calcular", "/admin")
        #
        # Es exactamente igual que hacer:
        # mi_funcion._animales = "Mi animal preferido es el perro"
        # mi_funcion._comida = "Me gusta la pizza"
        #
        # EJEMPLO PRÁCTICO:
        # Si escribes @route("/calcular"), entonces:
        # wrapper._route_path = "/calcular"
        #
        # Ahora puedes hacer: print(wrapper._route_path) → "/calcular"
        #
        # ¿POR QUÉ FLASK USA ESTE NOMBRE ESPECÍFICO?
        # Flask "escucha" nombres específicos como códigos secretos:
        # • _route_path → Flask dice: "¡Ah, esto es una ruta!"
        # • _mi_etiqueta → Flask dice: "¿Qué es esto? No lo entiendo"
        #
        # OTROS ATRIBUTOS QUE FLASK "ESCUCHA":
        # wrapper.methods = ["GET", "POST"]     # Métodos HTTP permitidos
        # wrapper.endpoint = "calcular"         # Nombre interno de la ruta  
        # wrapper.__name__ = "calcular_impuesto" # Nombre de función (con @wraps)
        # wrapper.required_auth = True          # Requiere autenticación
        #
        # ATRIBUTOS QUE PUEDES INVENTAR (Flask los ignora):
        # wrapper._descripcion = "Calcula impuestos"
        # wrapper._autor = "José"
        # wrapper._version = "1.0"
        
        return wrapper  # ← Devolvemos la función MEJORADA (con extras de Flask)
    
    return decorator  # ← Devolvemos el decorador personalizado para esta ruta

def require_auth(func):
    """
    DECORADOR DE AUTENTICACIÓN - "PORTERO DE SEGURIDAD"
    
    ¿QUÉ HACE?
    • Protege el acceso a rutas/direcciones web específicas
    • Se ejecuta CADA VEZ que un usuario intenta acceder a una función protegida
    • Verifica si el usuario tiene permisos antes de ejecutar la función original
    • Es como un portero que pregunta "¿Quién eres?" antes de dejarte pasar
    
    ¿CUÁNDO SE EJECUTA?
    • CADA VEZ que un usuario visita una ruta protegida
    • ANTES de ejecutar la función original (ej: calcular_impuesto)
    • Si hay autenticación → continúa a la función original
    • Si no hay autenticación → bloquea el acceso
    
    DIFERENCIA CON @route():
    • @route("/admin"): Crea la dirección web
    • @require_auth: Protege el acceso a esa dirección
    
    EJEMPLO EN TU PROYECTO:
    Sin protección:  Cualquiera puede calcular impuestos
    Con protección:  Solo funcionarios del Ayuntamiento pueden acceder
    """
    @wraps(func)  # Preserva nombre y documentación de la función original
    def wrapper(*args, **kwargs):
        """
        WRAPPER QUE ACTÚA COMO PORTERO DE SEGURIDAD
        
        FLUJO CUANDO UN USUARIO INTENTA ACCEDER:
        1. Usuario visita: www.tuapp.com/admin
        2. Flask ejecuta primero este wrapper (portero)
        3. Wrapper verifica: "¿Tienes permisos para entrar?"
        4. Si SÍ → ejecuta la función original (admin_configuracion)
        5. Si NO → bloquea acceso y muestra error "Acceso denegado"
        
        EN UNA APLICACIÓN REAL VERIFICARÍA:
        • Token de sesión del usuario
        • Credenciales (usuario/contraseña)
        • Roles y permisos específicos
        • Certificados de funcionario
        """
        # En una app real, verificaría el token/sesión del usuario
        print(f"🔐 PASO 2: Verificando autenticación para acceder a {func.__name__}")
        
        # AQUÍ IRÍA LA LÓGICA REAL DE AUTENTICACIÓN:
        # if not usuario_autenticado():
        #     return {"error": "Acceso denegado - Se requiere autenticación"}
        # if not usuario_tiene_permisos():
        #     return {"error": "Acceso denegado - Permisos insuficientes"}
        
        # Si llega aquí, el usuario está autenticado → ejecutar función original
        return func(*args, **kwargs)
    
    return wrapper

def validate_json_input(func):
    """Decorador para validar entrada JSON en APIs
    
    EXPLICACIÓN EDUCATIVA:
    Este es el tercer decorador que estamos viendo. Su función es validar
    que los datos que llegan a nuestra función estén en formato JSON correcto.
    
    En una aplicación real de IIVTNU, validaría que el cliente envíe datos como:
    {
        "valor_catastral": 150000,
        "fecha_anterior": "2020-01-15",
        "fecha_actual": "2024-08-20"
    }
    
    Si los datos no están en formato JSON o faltan campos, el decorador
    devolvería un error SIN ejecutar la función principal.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"✅ PASO 3: Validando JSON de entrada para {func.__name__}")
        # En una app real, aquí habría código como:
        # if not request.is_json:
        #     return {"error": "Los datos deben estar en formato JSON"}
        # if "valor_catastral" not in request.json:
        #     return {"error": "Falta el valor catastral"}
        
        return func(*args, **kwargs)
    return wrapper

# ========================================================================
# EXPLICACIÓN DETALLADA: ORDEN DE APLICACIÓN VS ORDEN DE EJECUCIÓN
# ========================================================================

"""
CONCEPTO CLAVE: Los decoradores tienen DOS órdenes diferentes:

1. ORDEN DE APLICACIÓN (cuando Python carga el archivo)
2. ORDEN DE EJECUCIÓN (cuando llega una petición web)

SON ÓRDENES OPUESTOS - esto es lo que confunde a todo el mundo.

EJEMPLO PRÁCTICO CON NUESTROS DECORADORES:
"""

# Ejemplos de uso en rutas Flask
@route('/api/calcular-iivtnu')    # 3º SE APLICA (último en envolver)
@require_auth                     # 2º SE APLICA 
@validate_json_input             # 1º SE APLICA (primero en envolver)
def api_calcular_iivtnu():
    """Endpoint API para calcular IIVTNU
    
    ORDEN DE APLICACIÓN (cuando Python carga este archivo):
    --------------------------------------------------------
    1º. Python ve @validate_json_input y hace:
        api_calcular_iivtnu = validate_json_input(api_calcular_iivtnu)
        
    2º. Python ve @require_auth y hace:
        api_calcular_iivtnu = require_auth(api_calcular_iivtnu)
        
    3º. Python ve @route('/api/calcular-iivtnu') y hace:
        api_calcular_iivtnu = route('/api/calcular-iivtnu')(api_calcular_iivtnu)
    
    Resultado: Como MUÑECAS RUSAS:
    route(require_auth(validate_json_input(función_original)))
    
    
    ORDEN DE EJECUCIÓN (cuando el usuario visita /api/calcular-iivtnu):
    ------------------------------------------------------------------
    1º. Se ejecuta @route: "¿La URL es correcta?" ✓
    2º. Se ejecuta @require_auth: "¿Está autenticado?" ✓  
    3º. Se ejecuta @validate_json_input: "¿El JSON es válido?" ✓
    4º. FINALMENTE se ejecuta la función api_calcular_iivtnu()
    
    ¡EL ORDEN DE EJECUCIÓN ES INVERSO AL ORDEN DE APLICACIÓN!
    
    ANALOGÍA: Es como vestirse en invierno:
    - APLICACIÓN: Primero camiseta, luego jersey, luego abrigo
    - EJECUCIÓN: La gente ve primero el abrigo, luego el jersey, luego la camiseta
    """
    print("🎯 PASO 4: Ejecutando función principal api_calcular_iivtnu()")
    return {"mensaje": "Cálculo IIVTNU realizado correctamente"}

@route('/admin/configuracion')
@require_auth
def admin_configuracion():
    """Panel de administración"""
    return {"mensaje": "Panel de administración cargado"}

# Simular llamadas
print("Simulando llamadas a endpoints:")
api_calcular_iivtnu()
admin_configuracion()

print("\n🎯 RESUMEN BLOQUE 5:")
print("✅ Decoradores Flask: @route crea direcciones web")
print("✅ @require_auth protege el acceso (autenticación)")
print("✅ @validate_json_input valida datos de entrada")
print("✅ ORDEN: Aplicación (abajo→arriba) vs Ejecución (arriba→abajo)")
print("✅ Como muñecas rusas: se aplican al revés de como se ejecutan")