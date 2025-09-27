"""
TAX CALCULATOR PRO - DIAGRAMA DE ARQUITECTURA COMPLETA
=====================================================
Esquema visual del funcionamiento global de todas las configuraciones


1. PUNTO DE ENTRADA Y FLUJO PRINCIPAL
=====================================

Terminal: python run.py
         ↓
    run.py (3 líneas)
    ├── from app import create_app
    ├── app = create_app()  
    └── app.run(debug=True)
         ↓
    app/__init__.py (Fábrica de aplicación)
    ├── Importa Config desde config.py
    ├── Crea app = Flask(__name__)
    ├── Configura app.config.from_object(Config)
    ├── Inicializa db.init_app(app)
    ├── Configura CORS(app) con orígenes permitidos por env
    ├── Inicializa CSRFProtect + Flask-Limiter (rate limiting)
    ├── Inicia LoginManager (Flask-Login)
    ├── Añade cabeceras de seguridad + CSP en after_request
    ├── Importa routes desde routes.py
    └── Retorna app completa
         ↓
    APLICACIÓN FLASK FUNCIONANDO

    
2. SISTEMA DE CONFIGURACIÓN
===========================

.env file (variables de entorno)
├── SECRET_KEY=mi-clave-secreta
├── DEBUG=True
├── DATABASE_URL=sqlite:///database/app.db
└── MUNICIPALITY_NAME=Alfafar
         ↓
    load_dotenv() en config.py
         ↓  
    class Config:
    ├── SECRET_KEY = (obligatoria, sin fallback)
    ├── DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'  
    ├── SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///database/app.db')
    ├── CORS_ORIGINS = os.environ.get('CORS_ORIGINS', 'http://localhost:3000')
    ├── SECURITY_HEADERS_ENABLED = True
    └── MUNICIPALITY_NAME = os.environ.get('MUNICIPALITY_NAME', 'Alfafar')
         ↓
    Flask app en __init__.py
    └── app.config.from_object(Config)


3. COMPONENTES DE LA APLICACIÓN FLASK
=====================================

app/__init__.py (NÚCLEO)
├── db = SQLAlchemy()          # Base de datos
├── migrate = Migrate()        # Migraciones 
├── cors = CORS()              # Permisos web
├── csrf = CSRFProtect()       # Protección CSRF
├── limiter = Limiter(...)     # Rate limiting
├── login_manager = LoginManager() # Autenticación
└── create_app():
    ├── app = Flask(__name__)
    ├── app.config.from_object(Config)  ← Lee configuración
    ├── db.init_app(app)               ← Conecta base de datos
    ├── migrate.init_app(app, db)      ← Activa migraciones
    ├── CORS(app)                      ← Configura permisos web
    ├── csrf.init_app(app)             ← Activa CSRF
    ├── limiter.init_app(app)          ← Activa rate limiting
    ├── login_manager.init_app(app)    ← Activa autenticación
    ├── after_request: cabeceras de seguridad (CSP, X-Frame-Options, etc.)
    ├── from app import routes         ← Importa rutas web
    └── return app                     ← Devuelve app completa

    
4. ESTRUCTURA DE ARCHIVOS Y RESPONSABILIDADES
=============================================

tax-calculator-pro/
├── .env                    # Variables de entorno (secretos)
├── config.py              # Configuración de Flask 
├── run.py                 # Punto de entrada (ejecutor)
├── app/
│   ├── __init__.py       # Fábrica de aplicación (núcleo)
│   ├── models.py         # Modelos de base de datos
│   ├── routes.py         # Rutas web (URLs)
│   ├── services.py       # Lógica de negocio (cálculos IIVTNU)
│   └── legal_validator.py # Validación legal
├── database/
│   └── app.db            # Base de datos SQLite
└── data/
    └── *.json            # Datos sintéticos para pruebas

    
5. FLUJO DE DATOS COMPLETO
=========================

Usuario → Navegador → Flask Routes → Services → Models → Database
   ↑                                                        ↓
   ← ← ← ← ← Templates ← ← ← ← ← ← ← ← Results ← ← ← ← ← ← ←

DETALLE:
1. Usuario visita: http://localhost:5000/login o /register (CSRF activo; límites de tasa)
2. Autenticación: Flask-Login crea sesión segura (cookies HTTPOnly, SameSite=Lax)
3. Usuario autenticado accede a /dashboard, /calculator, /history (requiere login)
4. Admin accede a /admin, /admin/users (requiere rol admin)
5. Futuro: Services calculará IIVTNU, validará con legal_validator y persistirá resultados
6. Models: Consulta/guarda datos en base de datos  
7. Database: SQLite almacena usuarios y dominio IIVTNU
8. Templates: HTML con resultados
9. Usuario: Ve el resultado en su navegador


6. VENTAJAS DE ESTA ARQUITECTURA
===============================

✅ SEPARACIÓN DE RESPONSABILIDADES:
   - config.py → Solo configuración
   - run.py → Solo ejecución  
   - __init__.py → Solo montaje de componentes
   - models.py → Solo estructura de datos
   - routes.py → Solo rutas web
   - services.py → Solo lógica de negocio

✅ ESCALABILIDAD:
   - Fácil añadir nuevos modelos, rutas, servicios
   - Configuración flexible por entornos (.env)
   
✅ MANTENIMIENTO:
   - Cada archivo tiene una función específica
   - Fácil localizar problemas
   - Cambios aislados en componentes específicos

✅ SEGURIDAD:
   - Variables sensibles en .env (no en código)
   - CSRF + Rate limiting + Cabeceras de seguridad (CSP, X-Frame-Options, etc.)
   - Autenticación con Flask-Login y protección de rutas admin
   - Validación legal integrada (módulo preparado)
"""
