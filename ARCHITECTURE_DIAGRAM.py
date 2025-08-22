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
    ├── Configura CORS(app)
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
    ├── SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback')
    ├── DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'  
    ├── SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///database/app.db')
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
└── create_app():
    ├── app = Flask(__name__)
    ├── app.config.from_object(Config)  ← Lee configuración
    ├── db.init_app(app)               ← Conecta base de datos
    ├── migrate.init_app(app, db)      ← Activa migraciones
    ├── CORS(app)                      ← Configura permisos web
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
│   ├── models.py         # Modelos de base de datos ← PRÓXIMO PASO
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
1. Usuario visita: http://localhost:5000/calcular
2. Flask routes.py: @app.route('/calcular') → función calcular_iivtnu()
3. Services: Lógica de cálculo del impuesto
4. Models: Consulta/guarda datos en base de datos  
5. Database: SQLite almacena personas, propiedades, transmisiones
6. Templates: HTML con resultados
7. Usuario: Ve el resultado en su navegador


6. PRÓXIMOS PASOS - MODELS.PY
=============================

app/models.py definirá:

Person (Personas)
├── id, nif, nombre, tipo_persona
├── Relación: Una persona puede tener múltiples transmisiones

Property (Propiedades)  
├── id, referencia_catastral, valor_actual, direccion
├── Relación: Una propiedad puede tener múltiples transmisiones

Transmission (Transmisiones)
├── id, fecha_transmision, tipo_transmision
├── Relación: person_id (transmitente), person_id (adquirente), property_id
├── Relación: Una transmisión genera un cálculo fiscal

TaxCalculation (Cálculos IIVTNU)
├── id, base_imponible, cuota_integra, cuota_liquida
├── Relación: transmission_id (cada cálculo pertenece a una transmisión)


7. VENTAJAS DE ESTA ARQUITECTURA
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
   - Configuración centralizada
   - Validación legal integrada
"""
