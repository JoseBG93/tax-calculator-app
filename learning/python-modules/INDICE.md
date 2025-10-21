# 📋 Índice Global — python_modules (Nativos + Externos)

Este índice relaciona todos los módulos y documentación disponibles bajo `python_modules/`, agrupados por dominio. Úsalo como mapa maestro para navegar rápido a cualquier tema.

---

## 📚 Documentación por área
- Nativos: `native/README.md` · `native/INDICE.md`
- Externos: `external/README.md` · `external/INDICE.md` · `external/requirements_external.txt`

---

## 🐍 Biblioteca estándar (native/)

### Runtime y sistema
- `native/runtime_and_system/sys_module.py`
  - Argumentos de línea de comandos, `sys.path`, flujos estándar, salida/errores
- `native/runtime_and_system/os_module.py`
  - Sistema de archivos, rutas, variables de entorno, permisos, organizador de archivos

### Debugging y logging
- `native/debugging_and_logging/traceback_module.py`
  - Trazas de error básicas/avanzadas, formatos, filtrado, stack sin excepción
- `native/debugging_and_logging/logging_module.py`
  - Configuración básica/avanzada, múltiples handlers, filtros, rotación, formateo

### Formatos de datos
- `native/data_formats/json_module.py`
  - JSON en memoria y archivos, manejo de errores, encoders/decoders personalizados, config manager

---

## 🌐 Ecosistema externo (external/)

### Backend core
- `external/backend_core/requests_module.py`
  - HTTP (GET/POST/PUT/PATCH/DELETE), headers, autenticación, sesiones, descargas, manejo de errores
- `external/backend_core/pytest_module.py`
  - Tests, fixtures, parametrización, mocking, cobertura, CLI, estructura de proyecto
- `external/backend_core/flask_module.py`
  - Rutas, templates, API REST, formularios, sesiones, middleware, errores, integración de proyecto
- `external/backend_core/sqlalchemy_module.py`
  - Modelos, CRUD, relaciones, consultas avanzadas, servicios, migraciones e integración

### Scraping e imágenes
- `external/scraping_and_images/beautifulsoup_module.py`
  - Parsing HTML/XML, selectores, scraping con `requests`, extracción estructurada
- `external/scraping_and_images/pillow_module.py`
  - Creación/edición de imágenes, filtros, metadatos, utilidades (thumbnails, avatares)

### Data tooling
- `external/data_tooling/numpy_module.py`
  - Arrays, vectorización, broadcasting, álgebra lineal y estadísticas
- `external/data_tooling/pandas_module.py`
  - IO (CSV/JSON/Excel), selección, limpieza, groupby/agg, stats y reportes
- `external/data_tooling/matplotlib_module.py`
  - Tipos de gráficos, subplots, estilos, dashboards y guardado de figuras
- `external/data_tooling/scikit_learn_module.py`
  - ML clásico: clasificación, regresión, clustering, preprocessing, validación y pipelines

---

## 🧭 Rutas de navegación rápida
- Web/API: `requests` → `flask` → `sqlalchemy` → `pytest`
- Datos/Análisis: `numpy` → `pandas` → `matplotlib`
- ML clásico: `numpy` → `pandas` → `scikit_learn`
- Observabilidad: `traceback` → `logging`

---

## 🔧 Ejecución rápida
- Nativos: ejecutar directamente cualquier `*.py` dentro de `native/`
- Externos: crear venv y `pip install -r external/requirements_external.txt` antes de ejecutar `*.py`

---

## 🗂️ Mantenibilidad
Cada vez que agregues un nuevo módulo:
1) Colócalo en la subcarpeta adecuada
2) Actualiza su README/INDICE de área
3) Añádelo en este índice global y en `python_modules/README.md`

---

Última actualización: sincronizado con los contenidos detectados en `native/` y `external/`.
