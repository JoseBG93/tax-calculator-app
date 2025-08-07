# ========================================
# TAX CALCULATOR PRO - EXPLICACIÓN DETALLADA DE DEPENDENCIAS
# ========================================



## DEPENDENCIAS BÁSICAS

### 1. FLASK (Framework Web)
**Versión:** 2.3.3

**ARCHIVOS RELACIONADOS:**
- `app/routes.py` → Define las rutas HTTP (URLs) que maneja tu aplicación
- `app/__init__.py` → Inicializa la aplicación Flask y configura el blueprint
- `run.py` → Punto de entrada que inicia el servidor Flask

**CARPETAS RELACIONADAS:**
- `templates/` → Es la carpeta donde Flask busca los archivos de plantillas HTML 
que utiliza para generar las páginas web que se muestran al usuario. 
Cuando defines una ruta que devuelve `render_template('archivo.html')`, Flask busca ese archivo dentro de `templates/`.
- `static/` → Es la carpeta donde Flask almacena y entrega automáticamente archivos estáticos,
 como hojas de estilo CSS, archivos JavaScript y todo tipo de imágenes. 
 Por ejemplo, si tienes un archivo `style.css` dentro de `static/`, puedes enlazarlo en tus plantillas HTML y Flask lo servirá 
 directamente al navegador sin que tengas que programar nada extra.

**FUNCIONALIDAD DETALLADA:**
Flask es el corazón de tu aplicación web. Cuando un usuario visita tu sitio, Flask recibe la petición HTTP, 
ejecuta el código Python correspondiente a esa URL, y devuelve una respuesta (HTML, JSON, etc.). 
Es como un "director de tráfico" que decide qué hacer con cada petición. 
Flask es minimalista pero potente, perfecto para aprender conceptos web sin complicaciones innecesarias.



### 2. FLASK-SQLALCHEMY (Base de Datos)
**Versión:** 3.0.5

**ARCHIVOS RELACIONADOS:**
- `app/models.py` → Define las clases Python que se convierten en tablas SQL
- `app/__init__.py` → Configura la conexión a la base de datos
- `config.py` → Define la URL de la base de datos (SQLite/PostgreSQL)

**CARPETAS RELACIONADAS:**
- `database/` → Aquí se almacena el archivo SQLite de la base de datos

**FUNCIONALIDAD DETALLADA:**
SQLAlchemy es un ORM (Object-Relational Mapping) que te permite trabajar con bases de datos usando código Python 
en lugar de SQL puro. En lugar de escribir "CREATE TABLE users", defines una clase Python `User` 
y SQLAlchemy crea automáticamente la tabla. Esto hace que tu código sea más limpio, más seguro (evita inyección SQL) 
y más fácil de mantener.



### 3. FLASK-CORS (Comunicación Frontend-Backend)
**Versión:** 4.0.0

**ARCHIVOS RELACIONADOS:**
- `app/__init__.py` → Configura CORS para permitir peticiones desde el frontend

**CARPETAS RELACIONADAS:**
- `static/` → Permite que el frontend (HTML/CSS/JS) se comunique con el backend

**FUNCIONALIDAD DETALLADA:**
Por defecto, los navegadores bloquean por seguridad las peticiones HTTP que provienen de un dominio diferente al del backend 
(por ejemplo, si tu frontend está en `localhost:3000` y tu backend en `localhost:5000`).  
CORS (Cross-Origin Resource Sharing) es una extensión que actúa como mecanismo de seguridad implementado 
en los navegadores web. Su función es controlar qué sitios web (dominios) pueden comunicarse, a través de una API, 
con tu backend. Pero además, Flask-CORS configura automáticamente los encabezados ("headers") necesarios 
a las respuestas de tu API para que el navegador permita estas peticiones "cruzadas". Así, tu frontend y backend 
pueden comunicarse sin problemas durante el desarrollo y en producción, siempre que configures correctamente los orígenes permitidos. 



### 4. FLASK-MIGRATE (Gestión de Base de Datos)
**Versión:** 4.0.5

**ARCHIVOS RELACIONADOS:**
- `app/models.py` → Aquí defines las clases que representan las tablas de la base de datos. Cuando modificas estas clases 
(por ejemplo, añades o cambias un campo), Flask-Migrate detecta esos cambios para generar los scripts de migración necesarios.
- `database/` → Esta carpeta guarda los archivos de migración generados automáticamente. Cada archivo representa un "paso" 
en la evolución de la estructura de la base de datos, permitiendo actualizarla o retroceder a versiones anteriores 
de forma controlada.

**CARPETAS RELACIONADAS:**
- `database/` → Contiene archivos de migración y control de versiones

**FUNCIONALIDAD DETALLADA:**
Flask-Migrate te permite hacer cambios en la estructura de tu base de datos de forma controlada. Si, por ejemplo, 
añades un nuevo campo a un modelo, Flask-Migrate genera automáticamente un script SQL que actualiza la base de datos 
sin perder datos. Es como un "control de versiones" para tu base de datos, esencial para desarrollo en equipo 
y despliegue en producción.



### 5. PANDAS (Manipulación de Datos)
**Versión:** 2.1.4

**ARCHIVOS RELACIONADOS:**
- `app/services.py` → Procesa y analiza los datos de los documentos sintéticos
- `app/utils.py` → Funciones auxiliares para manipulación de datos
- `data/` → Lee los 33 archivos JSON de documentos sintéticos

**CARPETAS RELACIONADAS:**
- `data/` → Contiene todos los archivos JSON que Pandas leerá y procesará

**FUNCIONALIDAD DETALLADA:**
Pandas es la biblioteca más importante para análisis de datos en Python. Convierte tus archivos JSON en "DataFrames" (tablas)
que puedes manipular fácilmente. Puedes filtrar datos, hacer cálculos estadísticos, agrupar información, y exportar resultados. 
Es fundamental para procesar tus documentos sintéticos y preparar los datos para modelos de IA.



### 6. NUMPY (Cálculos Numéricos)
**Versión:** 1.25.2

**ARCHIVOS RELACIONADOS:**
- `app/services.py` → Realiza cálculos fiscales complejos y operaciones matemáticas

**FUNCIONALIDAD DETALLADA:**
NumPy es la base de toda la computación científica en Python. Proporciona arrays multidimensionales y operaciones matemáticas 
muy rápidas. Es la base sobre la que se construyen Pandas y Scikit-learn. Para tu proyecto, será esencial para cálculos fiscales 
complejos, análisis estadístico de datos tributarios, y optimización de rendimiento.



### 7. MARSHMALLOW (Validación de Datos)
**Versión:** 3.20.1

**ARCHIVOS RELACIONADOS:**
- `app/models.py` → Define esquemas de validación para los datos de entrada
- `app/routes.py` → Valida automáticamente los datos que llegan por HTTP

**FUNCIONALIDAD DETALLADA:**
Marshmallow convierte datos JSON en objetos Python y viceversa, validando automáticamente que los datos tengan el formato correcto. 
Si alguien envía datos malformados a tu API, Marshmallow los rechaza antes de que lleguen a tu lógica de negocio. 
Esto hace tu aplicación más robusta y segura.



### 8. PYTHON-DOTENV (Configuración Segura)
**Versión:** 1.0.0

**ARCHIVOS RELACIONADOS:**
- `config.py` → Lee variables de entorno para configurar la aplicación
- `.env` → Archivo (no subir a Git) con claves secretas y configuración

**FUNCIONALIDAD DETALLADA:**
Python-dotenv lee un archivo `.env` que contiene variables de entorno como claves de API, contraseñas de base de datos, etc. 
Esto es crucial para seguridad: nunca hardcodeas información sensible en tu código. 
Diferentes entornos (desarrollo, producción) pueden tener diferentes archivos `.env`.



### 9. REQUESTS (Comunicación con APIs Externas)
**Versión:** 2.31.0

**ARCHIVOS RELACIONADOS:**
- `app/services.py` → Hace peticiones a APIs externas (OpenAI, sistemas municipales)

**FUNCIONALIDAD DETALLADA:**
Requests es la biblioteca estándar para hacer peticiones HTTP en Python. Te permite conectar tu aplicación con servicios 
externos como OpenAI para explicaciones de IA, APIs de sistemas municipales, o cualquier servicio web. Es esencial 
para la integración con sistemas externos.




## HERRAMIENTAS DE DESARROLLO

### 10. PYTEST (Testing)
**Versión:** 7.4.3

**ARCHIVOS RELACIONADOS:**
- `tests/` → Carpeta con archivos de pruebas unitarias y de integración

**FUNCIONALIDAD DETALLADA:**
Pytest es el framework de testing más popular en Python. Te permite escribir pruebas que verifican que tu código funciona
correctamente. Las pruebas se ejecutan automáticamente y te avisan si algo se rompe. Es esencial para desarrollo profesional
y mantener la calidad del código.



### 11. PYTEST-FLASK (Testing para Flask)
**Versión:** 1.3.0

**ARCHIVOS RELACIONADOS:**
- `tests/` → Pruebas específicas para endpoints de Flask

**FUNCIONALIDAD DETALLADA:**
Pytest-flask proporciona herramientas específicas para probar aplicaciones Flask. Te permite simular peticiones HTTP 
a tus endpoints y verificar que devuelven las respuestas correctas. Es crucial para asegurar que tu API funciona 
correctamente.



### 12. BLACK (Formateo de Código)
**Versión:** 23.11.0

**ARCHIVOS RELACIONADOS:**
- Todos los archivos `.py` del proyecto

**FUNCIONALIDAD DETALLADA:**
Black formatea automáticamente tu código Python siguiendo un estilo consistente. Elimina debates sobre formato de código 
y hace que el código sea más legible. Se ejecuta automáticamente y reformatea todo el código según estándares profesionales.



### 13. FLAKE8 (Análisis de Código)
**Versión:** 6.1.0

**ARCHIVOS RELACIONADOS:**
- Todos los archivos `.py` del proyecto

**FUNCIONALIDAD DETALLADA:**
Flake8 es un linter, es decir, una herramienta automática que revisa tu código fuente para detectar errores, 
problemas de estilo y complejidad. Un linter te ayuda a identificar malas prácticas, errores comunes y a mantener 
un estilo de código consistente antes de ejecutar el programa.
Te avisa de problemas antes de que ejecutes el código, ayudando a mantener alta calidad y detectando errores.



### 14. ISORT (Ordenamiento de Imports)
**Versión:** 5.12.0

**ARCHIVOS RELACIONADOS:**
- Todos los archivos `.py` del proyecto

**FUNCIONALIDAD DETALLADA:**
Isort organiza automáticamente las líneas de importación en tus archivos Python. Agrupa imports por tipo 
(bibliotecas estándar, terceros, locales) y los ordena alfabéticamente. Hace el código más limpio y profesional.



### 15. MYPY (Verificación de Tipos)
**Versión:** 1.7.1

**ARCHIVOS RELACIONADOS:**
- Todos los archivos `.py` del proyecto

**FUNCIONALIDAD DETALLADA:**
Mypy verifica tipos estáticos en tu código Python. Te avisa si pasas un string donde esperas un número, por ejemplo. 
Esto detecta errores antes de ejecutar el código y hace el código más robusto y fácil de mantener.




## DEPENDENCIAS FUTURAS (Fase 2-4)

### 16. SCIKIT-LEARN (Machine Learning)
**Versión:** 1.3.2

**ARCHIVOS RELACIONADOS:**
- `app/services.py` → Modelos de IA para clasificación y detección de anomalías

**FUNCIONALIDAD DETALLADA:**
Scikit-learn es la biblioteca más popular para machine learning en Python. Te permitirá crear modelos que clasifiquen 
automáticamente tipos de documentos, detecten anomalías en datos fiscales, y predigan valores basándose en patrones históricos.



### 17. MATPLOTLIB (Visualización)
**Versión:** 3.8.2

**ARCHIVOS RELACIONADOS:**
- `static/js/` → Genera gráficos para el frontend

**FUNCIONALIDAD DETALLADA:**
Matplotlib es la biblioteca fundamental para crear gráficos en Python. Te permitirá visualizar datos fiscales,
crear gráficos de evolución de impuestos, y generar reportes visuales para análisis de datos.



### 18. SEABORN (Visualización Avanzada)
**Versión:** 0.13.0

**ARCHIVOS RELACIONADOS:**
- `static/js/` → Gráficos estadísticos avanzados

**FUNCIONALIDAD DETALLADA:**
Seaborn se construye sobre Matplotlib y proporciona gráficos estadísticos más avanzados y atractivos. 
Perfecto para análisis de datos tributarios y presentaciones profesionales.



### 19. OPENAI (IA Externa)
**Versión:** 1.3.7

**ARCHIVOS RELACIONADOS:**
- `app/services.py` → Integración con OpenAI para explicaciones inteligentes

**FUNCIONALIDAD DETALLADA:**
OpenAI te permitirá integrar IA externa para generar explicaciones automáticas de cálculos fiscales, 
responder preguntas sobre impuestos, y proporcionar asistencia inteligente a los usuarios.



### 20. REPORTLAB (Generación de PDFs)
**Versión:** 4.0.7

**ARCHIVOS RELACIONADOS:**
- `app/services.py` → Genera reportes en PDF

**FUNCIONALIDAD DETALLADA:**
ReportLab te permite generar documentos PDF profesionales automáticamente. Perfecto para crear reportes fiscales, 
liquidaciones, y documentación oficial.



### 21. FLASK-JWT-EXTENDED (Autenticación)
**Versión:** 4.5.3

**ARCHIVOS RELACIONADOS:**
- `app/__init__.py` → Configuración de autenticación
- `app/routes.py` → Protección de endpoints

**FUNCIONALIDAD DETALLADA:**
JWT (JSON Web Tokens) proporciona autenticación segura para tu API. Los usuarios se identifican una vez 
y reciben un token que usan para acceder a recursos protegidos sin volver a identificarse.



### 22. CRYPTOGRAPHY (Encriptación)
**Versión:** 41.0.8

**ARCHIVOS RELACIONADOS:**
- `app/services.py` → Encriptación de datos sensibles

**FUNCIONALIDAD DETALLADA:**
Cryptography proporciona funciones de encriptación y desencriptación para proteger datos sensibles como información personal
de contribuyentes, claves de API, y datos confidenciales del sistema.




# ========================================
# RESUMEN DE INTEGRACIÓN EN EL PROYECTO
# ========================================

## FLUJO DE DATOS:
1. **Frontend (HTML/CSS/JS)** → Flask (routes.py) → Servicios (services.py) → Base de datos (models.py)
2. **Datos JSON** → Pandas (services.py) → Análisis → Resultados
3. **APIs externas** → Requests (services.py) → Procesamiento → Respuesta

## ARQUITECTURA:
- **Flask** maneja las peticiones web
- **SQLAlchemy** gestiona la base de datos
- **Pandas** procesa los datos sintéticos
- **Herramientas de desarrollo** mantienen la calidad del código
- **Dependencias futuras** añadirán IA y funcionalidades avanzadas

## BENEFICIOS PARA TU APRENDIZAJE:
- **Stack moderno** usado en empresas reales
- **Herramientas profesionales** que verás en el mercado laboral
- **Arquitectura escalable** que puedes expandir
- **Buenas prácticas** desde el principio