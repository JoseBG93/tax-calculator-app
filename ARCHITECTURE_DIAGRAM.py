"""
TAX CALCULATOR PRO - DIAGRAMA DE ARQUITECTURA COMPLETA
=====================================================
Esquema visual del funcionamiento global de todas las configuraciones


1. PUNTO DE ENTRADA Y FLUJO PRINCIPAL
=====================================

Terminal: python run.py
         ↓
    run.py
    ├── from app import create_app
    ├── app = create_app()
    ├── os.environ['FLASK_ENV'] = 'development'
    ├── template_files = glob('app/templates/*.html')  ← autoreload
    └── app.run(debug=True, use_reloader=True, extra_files=template_files,
                host='127.0.0.1', port=${PORT|5000})
         ↓
    app/__init__.py (Fábrica de aplicación)
    ├── Jinja: app.jinja_env.autoescape = True 
    ├── app.config.from_object('config.Config')
    ├── db.init_app(app) + migrate.init_app(app, db)
    ├── CORS(app, resources={"/*": {"origins": CORS_ORIGINS}})
    ├── csrf.init_app(app) + limiter.init_app(app)
    ├── login_manager.init_app(app); login_view = 'login'
    ├── after_request: cabeceras seguridad + CSP + HSTS (condicional)
    ├── @login_manager.user_loader: carga User por id
    ├── import app.routes as routes; routes.register_routes(app)
    └── return app
         ↓
    APLICACIÓN FLASK FUNCIONANDO

    
2. SISTEMA DE CONFIGURACIÓN
===========================

.env file (variables de entorno)
├── SECRET_KEY=<obligatoria>
├── DEBUG=True
├── DATABASE_URL=sqlite:///database/app.db
├── CORS_ORIGINS=http://localhost:3000[,https://...]
└── (ver claves opcionales abajo)
         ↓
    load_dotenv() en config.py
         ↓  
    class Config:
    ├── SECRET_KEY = _require_secret_key()  ← exige variable o lanza error
    ├── DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
    ├── SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///database/app.db')
    ├── SQLALCHEMY_TRACK_MODIFICATIONS = False
    ├── CORS_ORIGINS = os.environ.get('CORS_ORIGINS', 'http://localhost:3000').split(',')
    ├── SECURITY_HEADERS_ENABLED = os.environ.get('SECURITY_HEADERS_ENABLED','True').lower()=='true'
    ├── SESSION_COOKIE_SECURE/HTTPONLY/SAMESITE ('Lax')
    ├── WTF_CSRF_ENABLED = True; WTF_CSRF_TIME_LIMIT = 3600
    ├── RATELIMIT_STORAGE_URI = 'memory://'; RATELIMIT_DEFAULT = '100 per hour'
    ├── UPLOAD_FOLDER, MAX_CONTENT_LENGTH, ALLOWED_EXTENSIONS
    ├── SPACY_MODEL = 'es_core_news_md'
    └── Marco legal IIVTNU: referencias, topes y defaults municipales
         ↓
    Flask app en __init__.py
    └── app.config.from_object('config.Config')


3. COMPONENTES DE LA APLICACIÓN FLASK
=====================================

app/__init__.py (NÚCLEO)
├── db = SQLAlchemy()                    # Base de datos
├── migrate = Migrate()                  # Migraciones 
├── login_manager = LoginManager()       # Autenticación
├── csrf = CSRFProtect()                 # Protección CSRF
├── limiter = Limiter(key_func=get_remote_address,
│                    default_limits=["100 per hour"]) # Rate limiting
├── CORS (flask_cors)                    # Permisos web
└── create_app():
    ├── app = Flask(__name__)
    ├── app.jinja_env.autoescape = True
    ├── app.config.from_object('config.Config')
    ├── db.init_app(app); migrate.init_app(app, db)
    ├── CORS(app, resources={"/*": {"origins": CORS_ORIGINS}})
    ├── csrf.init_app(app); limiter.init_app(app)
    ├── login_manager.init_app(app); login_view = 'login'
    ├── after_request: X-Frame-Options, X-Content-Type-Options, XSS, CSP, HSTS
    ├── @login_manager.user_loader → User.query.get(id)
    ├── import app.routes as routes; routes.register_routes(app)
    └── return app

    
4. ESTRUCTURA DE ARCHIVOS Y RESPONSABILIDADES
=============================================

tax-calculator-pro/
├── .env                       # Variables de entorno (secretos)
├── config.py                  # Configuración de Flask
├── run.py                     # Punto de entrada (servidor dev)
├── app/
│   ├── __init__.py            # Fábrica de aplicación (núcleo)
│   ├── models.py              # Modelos de base de datos
│   ├── routes.py              # Rutas web (auth, admin, vistas)
│   ├── security_validations.py# Validaciones y decoradores (admin/superadmin)
│   ├── services.py            # Lógica IIVTNU (pendiente)
│   ├── legal_validator.py     # Marco legal IIVTNU
│   ├── templates/             # HTML Jinja2 (index, login, register, admin, ...)
│   └── static/                # CSS/JS/imagenes (p.ej. css/register.css)
├── database/
│   └── app.db                 # Base de datos SQLite
├── data/                      # Casos de prueba IIVTNU
├── docs/                      # Documentación legal y normativa
├── dependencies/              # requirements.txt (dependencias fijadas)
├── tests/                     # Pytest (p.ej. tests/test_cors.py)
└── README.md                  # Guía del proyecto

    
5. FLUJO DE DATOS COMPLETO
==========================

Usuario → Navegador → Flask Routes → Services → Models → Database
   ↑                                                        ↓
   ← ← ← ← ← Templates ← ← ← ← ← ← ← ← Results ← ← ← ← ← ← ←

DETALLE:
1. Usuario visita: http://localhost:5000/index | /login | /register (CSRF activo; rate limit en login/registro)
2. Autenticación: Flask-Login crea sesión (cookies HTTPOnly, SameSite='Lax')
3. Rutas protegidas: /dashboard, /calculator, /history (requieren login)
4. Área admin:
   ├─ /admin (admin_required)
   ├─ /admin/users (superadmin_required)
   └─ /admin/settings (superadmin_required)
5. Services (pendiente): cálculo IIVTNU y validación con legal_validator
6. Models: consulta/guardado en base de datos
7. Database: SQLite para desarrollo
8. Templates: vistas HTML renderizadas con Jinja2
9. Seguridad HTTP: CORS restringido a orígenes configurados; CSP estricta; HSTS si cookie secure


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
   - CSRF + Rate limiting + Cabeceras de seguridad (CSP, X-Frame-Options, HSTS cond.)
   - Autenticación con Flask-Login y protección de rutas admin/superadmin
   - Validación legal integrada (módulo preparado)


7. ESTADO ACTUAL DEL PROYECTO
=============================

✅ Núcleo Flask operativo (Factory Pattern) con CORS, CSRF, rate limiting y cabeceras de seguridad
✅ Autenticación y administración básica (dashboard, gestión de usuarios, ajustes)
✅ Modelos de base de datos listos; plantillas base disponibles
🔄 Lógica de negocio IIVTNU en `app/services.py` pendiente de implementación
🔄 Integración del validador legal en flujo de cálculo pendiente
"""
