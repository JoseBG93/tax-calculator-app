#!/usr/bin/env python3
"""
MÓDULO EXTERNO: flask
=====================

¿QUÉ ES?
El módulo 'flask' es un micro framework web minimalista y flexible 
para crear aplicaciones web y APIs de forma rápida y simple.

INSTALACIÓN:
pip install flask

¿PARA QUÉ SIRVE?
- Crear aplicaciones web simples
- Desarrollar APIs REST
- Servir contenido HTML/JSON
- Routing de URLs
- Manejar peticiones HTTP
- Sesiones y cookies

IMPORTANCIA: ⭐⭐⭐⭐⭐ (Esencial para web)
"""

def verificar_instalacion():
    """Verificar si flask está instalado"""
    try:
        import flask
        print("✅ Módulo 'flask' instalado correctamente")
        print(f"📦 Versión: {flask.__version__}")
        return True
    except ImportError:
        print("❌ Módulo 'flask' no encontrado")
        print("💡 Para instalar: pip install flask")
        return False

def ejemplo_flask_basico():
    """Ejemplo básico de uso del módulo flask"""
    
    print("=" * 50)
    print("🌍 MÓDULO FLASK - WEB FRAMEWORK")
    print("=" * 50)
    
    if not verificar_instalacion():
        return
    
    print("\n📝 Ejemplo básico de Flask:")
    print("""
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola desde Flask!"

@app.route('/about')
def about():
    return "Acerca de mi aplicación"

if __name__ == '__main__':
    app.run(debug=True)
    """)
    
    print("\n🚀 Para ejecutar:")
    print("   python app.py")
    print("   # Abrir http://localhost:5000")
    
    print("\n✅ Conceptos clave:")
    print("   • Flask(__name__): Crear aplicación")
    print("   • @app.route(): Decorador para rutas")
    print("   • app.run(): Ejecutar servidor")
    print("   • debug=True: Modo desarrollo")

def ejemplo_flask_api():
    """Ejemplo de API REST con Flask"""
    
    print("\n" + "=" * 50)
    print("🔌 API REST CON FLASK")
    print("=" * 50)
    
    print("📝 Ejemplo de API para notas:")
    print("""
# notes_api.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulación de base de datos
notes = [
    {"id": 1, "title": "Nota 1", "content": "Contenido 1"},
    {"id": 2, "title": "Nota 2", "content": "Contenido 2"}
]

@app.route('/api/notes', methods=['GET'])
def get_notes():
    '''Obtener todas las notas'''
    return jsonify(notes)

@app.route('/api/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    '''Obtener nota específica'''
    note = next((n for n in notes if n['id'] == note_id), None)
    if note:
        return jsonify(note)
    return jsonify({"error": "Nota no encontrada"}), 404

@app.route('/api/notes', methods=['POST'])
def create_note():
    '''Crear nueva nota'''
    data = request.get_json()
    
    if not data or not data.get('title'):
        return jsonify({"error": "Título requerido"}), 400
    
    new_note = {
        "id": len(notes) + 1,
        "title": data['title'],
        "content": data.get('content', '')
    }
    notes.append(new_note)
    return jsonify(new_note), 201

@app.route('/api/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    '''Actualizar nota'''
    note = next((n for n in notes if n['id'] == note_id), None)
    if not note:
        return jsonify({"error": "Nota no encontrada"}), 404
    
    data = request.get_json()
    note.update(data)
    return jsonify(note)

@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    '''Eliminar nota'''
    global notes
    notes = [n for n in notes if n['id'] != note_id]
    return jsonify({"message": "Nota eliminada"})

if __name__ == '__main__':
    app.run(debug=True)
    """)
    
    print("\n🧪 Probar API con curl:")
    print("   # GET todas las notas")
    print("   curl http://localhost:5000/api/notes")
    print("   # POST nueva nota")
    print("   curl -X POST -H 'Content-Type: application/json' \\")
    print("        -d '{\"title\":\"Nueva nota\",\"content\":\"Contenido\"}' \\")
    print("        http://localhost:5000/api/notes")
    
    print("\n✅ Métodos HTTP:")
    print("   • GET: Obtener datos")
    print("   • POST: Crear datos")
    print("   • PUT: Actualizar datos")
    print("   • DELETE: Eliminar datos")

def ejemplo_flask_templates():
    """Ejemplo de templates HTML con Flask"""
    
    print("\n" + "=" * 50)
    print("🎨 TEMPLATES HTML CON FLASK")
    print("=" * 50)
    
    print("📝 Estructura de archivos:")
    print("""
proyecto/
├── app.py
└── templates/
    ├── base.html
    ├── index.html
    └── notes.html
    """)
    
    print("\n📝 Ejemplo con templates:")
    print("""
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Mi App de Notas')

@app.route('/notes')
def notes():
    notes_list = [
        {'title': 'Nota 1', 'content': 'Contenido 1'},
        {'title': 'Nota 2', 'content': 'Contenido 2'}
    ]
    return render_template('notes.html', notes=notes_list)

<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <nav>
        <a href="/">Inicio</a>
        <a href="/notes">Notas</a>
    </nav>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>

<!-- templates/index.html -->
{% extends "base.html" %}
{% block content %}
<h1>Bienvenido a {{ title }}</h1>
<p>Esta es tu aplicación de notas</p>
{% endblock %}

<!-- templates/notes.html -->
{% extends "base.html" %}
{% block content %}
<h1>Mis Notas</h1>
{% for note in notes %}
<div>
    <h3>{{ note.title }}</h3>
    <p>{{ note.content }}</p>
</div>
{% endfor %}
{% endblock %}
    """)
    
    print("\n✅ Conceptos de templates:")
    print("   • render_template(): Renderizar HTML")
    print("   • {{ variable }}: Mostrar variable")
    print("   • {% for %}: Loop en template")
    print("   • {% extends %}: Herencia de templates")
    print("   • {% block %}: Bloques de contenido")

def ejemplo_flask_formularios():
    """Ejemplo de formularios con Flask"""
    
    print("\n" + "=" * 50)
    print("📝 FORMULARIOS CON FLASK")
    print("=" * 50)
    
    print("📝 Manejo de formularios:")
    print("""
# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        if title:
            note = {
                'id': len(notes) + 1,
                'title': title,
                'content': content
            }
            notes.append(note)
            return redirect(url_for('index'))
        else:
            return render_template('add.html', error='Título requerido')
    
    return render_template('add.html')

<!-- templates/add.html -->
<form method="POST">
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
    
    <label>Título:</label>
    <input type="text" name="title" required>
    
    <label>Contenido:</label>
    <textarea name="content"></textarea>
    
    <button type="submit">Agregar Nota</button>
</form>
    """)
    
    print("\n✅ Conceptos de formularios:")
    print("   • request.method: Método HTTP")
    print("   • request.form: Datos del formulario")
    print("   • redirect(): Redireccionar")
    print("   • url_for(): Generar URL")

def ejemplo_flask_avanzado():
    """Ejemplo avanzado con Flask"""
    
    print("\n" + "=" * 50)
    print("🚀 FLASK AVANZADO")
    print("=" * 50)
    
    print("📝 Funciones avanzadas:")
    print("""
# app.py
from flask import Flask, session, g, before_request
import sqlite3

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

# Configuración de base de datos
DATABASE = 'notes.db'

def get_db():
    '''Obtener conexión a base de datos'''
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_db(exception):
    '''Cerrar conexión a base de datos'''
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.before_request
def before_request():
    '''Ejecutar antes de cada petición'''
    g.user = session.get('user_id')

@app.route('/login', methods=['POST'])
def login():
    session['user_id'] = request.form['username']
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
    """)
    
    print("\n✅ Conceptos avanzados:")
    print("   • session: Manejo de sesiones")
    print("   • g: Contexto global")
    print("   • before_request: Middleware")
    print("   • errorhandler: Manejo de errores")
    print("   • teardown_appcontext: Limpieza")

def integracion_con_tax_calculator_pro():
    """Ejemplo de integración con proyecto tax-calculator-pro"""
    
    print("\n" + "=" * 50)
    print("🗂️ INTEGRACIÓN CON NOTESASSISTANT")
    print("=" * 50)
    
    print("💡 Agregar web interface a tu proyecto:")
    
    print("\n📝 Estructura propuesta:")
    print("""
tax-calculator-pro/
├── src/
│   ├── models/
│   ├── services/
│   └── utils/
├── web/
│   ├── app.py              # Aplicación Flask
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── notes.py        # Rutas para notas
│   │   └── api.py          # API REST
│   └── templates/
│       ├── base.html
│       ├── index.html
│       └── notes.html
└── run_web.py              # Script para ejecutar web
    """)
    
    print("\n📝 Ejemplo de integración:")
    print("""
# web/app.py
from flask import Flask
from src.services.note_service import NoteService

app = Flask(__name__)
note_service = NoteService()

@app.route('/')
def index():
    notes = note_service.get_all_notes()
    return render_template('index.html', notes=notes)

@app.route('/api/notes')
def api_notes():
    notes = note_service.get_all_notes()
    return jsonify([note.to_dict() for note in notes])

# run_web.py
from web.app import app

if __name__ == '__main__':
    print("🌍 Iniciando servidor web...")
    print("📍 Dirección: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
    """)
    
    print("\n🎯 Casos de uso:")
    print("   • Interface web para gestionar notas")
    print("   • API REST para acceso programático")
    print("   • Dashboard con estadísticas")
    print("   • Búsqueda y filtrado visual")
    print("   • Backup y export desde web")
    print("   • Colaboración multi-usuario")
    
    print("\n🚀 Comandos:")
    print("   python run_web.py")
    print("   # Abrir http://localhost:5000")

def casos_uso_comunes():
    """Casos de uso más comunes del módulo flask"""
    
    print("\n" + "=" * 50)
    print("🎯 CASOS DE USO COMUNES")
    print("=" * 50)
    
    print("1. Aplicación web simple:")
    print("   app = Flask(__name__)")
    print("   @app.route('/')")
    print("   def home(): return 'Hola mundo'")
    
    print("\n2. API REST:")
    print("   @app.route('/api/data', methods=['GET', 'POST'])")
    print("   def api_data(): return jsonify({'data': 'valor'})")
    
    print("\n3. Templates HTML:")
    print("   @app.route('/page')")
    print("   def page(): return render_template('page.html', data=data)")
    
    print("\n4. Formularios:")
    print("   @app.route('/form', methods=['POST'])")
    print("   def form(): title = request.form['title']")
    
    print("\n5. Sesiones:")
    print("   session['user'] = 'username'")
    print("   user = session.get('user')")
    
    print("\n6. Manejo de errores:")
    print("   @app.errorhandler(404)")
    print("   def not_found(error): return 'Página no encontrada', 404")

if __name__ == "__main__":
    # Ejecutar todos los ejemplos
    ejemplo_flask_basico()
    ejemplo_flask_api()
    ejemplo_flask_templates()
    ejemplo_flask_formularios()
    ejemplo_flask_avanzado()
    casos_uso_comunes()
    integracion_con_tax_calculator_pro()
    
    print("\n" + "=" * 50)
    print("✅ RESUMEN DEL MÓDULO flask")
    print("=" * 50)
    print("🔧 Usos principales:")
    print("   • Crear aplicaciones web rápidas")
    print("   • Desarrollar APIs REST")
    print("   • Servir templates HTML")
    print("   • Manejar formularios")
    print("   • Gestionar sesiones")
    print("   • Routing de URLs")
    print("\n📚 Documentación oficial:")
    print("   https://flask.palletsprojects.com/")
    print("\n💡 Consejo: Flask es simple pero poderoso")
    print("   Perfecto para prototipos y aplicaciones pequeñas.") 