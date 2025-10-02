# 🐍 python_modules — Guía General (Nativos + Externos)

## 📖 ¿Qué es esta carpeta?
Conjunto unificado de módulos de Python educativos y ejecutables, organizados en dos áreas:
- `native/` — Módulos nativos de la biblioteca estándar de Python
- `external/` — Módulos externos (instalables con pip)

Incluye ejemplos paso a paso, casos de uso reales y recomendaciones de mejores prácticas. Cada archivo `.py` se puede ejecutar directamente para ver los ejemplos en acción.

---

## 📁 Estructura de alto nivel
```
python_modules/
├── native/    # Módulos estándar de Python (sin instalación adicional)
└── external/  # Módulos de terceros (requieren instalación)
```

- Documentación por área:
  - Nativos: ver `native/README.md` y `native/INDICE.md`
  - Externos: ver `external/README.md` y `external/INDICE.md`

---

## 📦 Catálogo completo de módulos incluidos

### Nativos (standard library)
- `native/runtime_and_system/sys_module.py` — Información del intérprete, argumentos CLI, `sys.path`, flujos estándar
- `native/runtime_and_system/os_module.py` — Sistema de archivos, rutas, variables de entorno, permisos
- `native/debugging_and_logging/traceback_module.py` — Trazas de error, formatos, filtrado y stack sin excepción
- `native/debugging_and_logging/logging_module.py` — Configuración básica/avanzada, formatos, filtros, rotación
- `native/data_formats/json_module.py` — Serialización JSON, archivos, validación, configuración de apps

### Externos (terceros)
- `external/backend_core/requests_module.py` — HTTP (GET/POST/PUT/PATCH/DELETE), headers, auth, sesiones, descargas
- `external/backend_core/pytest_module.py` — Testing, fixtures, parametrización, mocking, cobertura y CLI
- `external/backend_core/flask_module.py` — Microframework web, rutas, templates, API REST, sesiones y errores
- `external/backend_core/sqlalchemy_module.py` — ORM, modelos, CRUD, relaciones, consultas y migraciones
- `external/scraping_and_images/beautifulsoup_module.py` — Parsing HTML/XML, selectores, scraping con requests
- `external/scraping_and_images/pillow_module.py` — Imágenes: abrir, transformar, filtros, metadata, dibujos
- `external/data_tooling/numpy_module.py` — Arrays, vectorización, broadcasting, álgebra lineal, estadísticas
- `external/data_tooling/pandas_module.py` — DataFrames/Series, IO (CSV/JSON/Excel), limpieza, groupby, merges
- `external/data_tooling/matplotlib_module.py` — Gráficos (líneas, barras, hist, scatter), subplots, estilos
- `external/data_tooling/scikit_learn_module.py` — ML clásico: clasificación, regresión, clustering, pipelines

---

## 🚀 Cómo ejecutar los ejemplos

### Nativos (no requieren instalación)
```bash
# Desde python_modules/native/<subcarpeta>
python json_module.py
python logging_module.py
```

### Externos (crear entorno y instalar)
```bash
cd external
python -m venv venv && source venv/bin/activate
pip install -r requirements_external.txt

# Ejecutar cualquiera de los módulos
python backend_core/requests_module.py
python data_tooling/pandas_module.py
```

Consejo: también puedes instalar módulos individuales con `pip install <paquete>` si prefieres no instalar todo.

---

## 🎓 Rutas de aprendizaje recomendadas
- Desarrollo web (backend): `requests` → `flask` → `sqlalchemy` → `pytest`
- Análisis de datos: `numpy` → `pandas` → `matplotlib` → `pytest`
- Machine Learning clásico: `numpy` → `pandas` → `scikit-learn` → `matplotlib`
- Debugging y observabilidad: `traceback` → `logging` (y aplicar en todos los proyectos)

Cada ruta tiene ejemplos ejecutables dentro de los propios módulos.

---

## 🔗 Integración con proyectos (ejemplos comunes)
- API + persistencia: `flask` + `sqlalchemy` + `pytest`
- Data pipeline: `requests` + `beautifulsoup4` + `pandas` + `matplotlib`
- Utilidades base: `os` + `sys` + `json` + `logging` + `traceback`

---

## 🛡️ Mejores prácticas transversales
- Usar entornos virtuales (`venv`/`conda`) para externos
- Fijar versiones en `requirements.txt` para reproducibilidad
- Añadir tests con `pytest` y cobertura
- Manejar errores con `try/except`, `traceback.format_exc()` y `logging`
- Separar configuración en JSON (y validarla)

---

## 📚 Referencias locales
- Nativos: `native/README.md` · `native/INDICE.md`
- Externos: `external/README.md` · `external/INDICE.md` · `external/requirements_external.txt`

Si añades nuevos módulos, recuerda actualizar también `python_modules/INDICE.md` (índice global) y mantener esta guía.


