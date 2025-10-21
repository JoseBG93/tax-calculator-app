# 🏛️ Guía del Panel de Administración Web

## 📋 **Índice**
1. [¿Qué es el Panel de Administración?](#qué-es)
2. [Cómo Acceder](#cómo-acceder)
3. [Funcionalidades Principales](#funcionalidades)
4. [Operaciones CRUD](#operaciones-crud)
5. [Seguridad](#seguridad)
6. [Solución de Problemas](#solución-problemas)

---

## 🎯 **¿Qué es el Panel de Administración?** {#qué-es}

El **Panel de Administración Web** es una interfaz visual completa que te permite:
- ✅ **Ver** todos los registros de tus tablas
- ✅ **Crear** nuevos registros (personas, propiedades, transacciones, etc.)
- ✅ **Editar** registros existentes
- ✅ **Eliminar** registros
- ✅ **Buscar** y **filtrar** datos
- ✅ **Exportar** datos (CSV, Excel)

**Todo desde tu navegador**, sin necesidad de usar la terminal.

---

## 🔐 **Cómo Acceder** {#cómo-acceder}

> **Requisitos Previos:** Asegúrate de tener el entorno virtual creado y la base de datos inicializada

---

### **📦 Paso 1: Arrancar el Servidor**

Desde el directorio raíz del proyecto:

```bash
# Activate the virtual environment
source taxapp_env/bin/activate

# Run the Flask development server
python run.py
```

> 💡 **Nota:** Si acabas de clonar el repositorio, primero navega al directorio:
> ```bash
> cd tax-calculator-pro
> ```

**Salida esperada:**
```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

---

### **🔑 Paso 2: Iniciar Sesión**

1. **Abre tu navegador** y navega a:
   ```
   http://localhost:5000
   ```

2. **Ingresa tus credenciales** de administrador:
   
   | Campo       | Valor              |
   |-------------|--------------------|
   | Usuario     | `tu_usuario_admin` |
   | Contraseña  | `tu_contraseña`    |

3. Haz clic en **"Login"** o presiona `Enter`

> ⚠️ **Importante:** Solo usuarios con `is_admin=True` pueden acceder al panel

---

### **⚙️ Paso 3: Acceder al Panel de Administración**

Una vez autenticado, tienes **dos opciones**:

#### **Opción A: URL Directa**
```
http://localhost:5000/admin
```

#### **Opción B: Navegación**
- Busca el enlace **"Admin Panel"** en la barra de navegación
- Haz clic para acceder directamente

**Pantalla esperada:**

Verás el dashboard principal con las siguientes secciones:
- 👥 **Usuarios** (Admin Users)
- 🧑‍💼 **Personas** (Admin People)
- 🏠 **Propiedades** (Admin Properties)
- 📄 **Transacciones** (Admin Transactions)
- 💰 **Cálculos Fiscales** (Admin Tax Calculations)

---

## ⚙️ **Funcionalidades Principales** {#funcionalidades}

### **📊 Vista de Lista**

Cada tabla tiene su propia vista de lista con:
- **Columnas configuradas** para mostrar información relevante
- **Búsqueda** en tiempo real (campos configurados)
- **Filtros** por fecha, tipo, valor, etc.
- **Paginación** automática (25 registros por página)
- **Ordenación** por columna (clic en encabezado)

### **🔍 Búsqueda Avanzada**

Puedes buscar en:
- **Usuarios:** por username
- **Personas:** por NIF, nombre, apellidos
- **Propiedades:** por referencia catastral, dirección
- **Transacciones:** por tipo, fecha, valor
- **Cálculos Fiscales:** por tipo de gravamen, fecha

### **🎯 Filtros Rápidos**

Cada tabla tiene filtros específicos:
- **Usuarios:** es_admin, is_active, fecha_creación
- **Personas:** tipo_persona, fecha_creación
- **Propiedades:** municipio, valor_catastral, fecha_creación
- **Transacciones:** tipo_transacción, fecha, valor
- **Cálculos:** tipo_gravamen, fecha_creación

---

## 📝 **Operaciones CRUD** {#operaciones-crud}

### **1️⃣ CREATE - Crear Nuevo Registro**

1. Selecciona la tabla deseada del menú lateral
2. Clic en botón **"Create"** (arriba a la derecha)
3. Rellena el formulario con los datos
4. Clic en **"Save"**

**Ejemplo:** Crear una nueva persona
```
- NIF: 12345678A
- Nombre: Juan
- Apellidos: García López
- Tipo: Física
- Dirección: Calle Mayor, 1
```

### **2️⃣ READ - Ver/Consultar Registros**

1. Selecciona la tabla del menú lateral
2. Visualiza todos los registros en formato tabla
3. Usa búsqueda/filtros para encontrar específicos
4. Clic en el "ojo" 👁️ para ver detalles completos

### **3️⃣ UPDATE - Editar Registro**

1. Localiza el registro en la lista
2. Clic en el icono de **"Editar"** ✏️
3. Modifica los campos necesarios
4. Clic en **"Save"**

**Nota:** Algunos campos pueden estar protegidos (ej: ID, password)

### **4️⃣ DELETE - Eliminar Registro**

1. Localiza el registro en la lista
2. Clic en el icono de **"Eliminar"** 🗑️
3. Confirma la eliminación

**⚠️ ADVERTENCIA:** La eliminación es permanente.

---

## 🔒 **Seguridad** {#seguridad}

### **Control de Acceso**

El panel de administración está **protegido** con dos capas de seguridad:

1. **Autenticación:** Solo usuarios con sesión iniciada pueden acceder
2. **Autorización:** Solo usuarios con `is_admin=True` pueden ver el panel

### **¿Quién Puede Acceder?**

Solo los usuarios con permisos de administrador pueden acceder al panel:
- ✅ **Usuarios admin:** `is_admin=True` → Acceso completo al panel
- ❌ **Usuarios normales:** `is_admin=False` → Sin acceso al panel

### **¿Qué Pasa si Intento Acceder sin Permisos?**

- Si **NO estás autenticado** → Redirección a `/login`
- Si **NO eres admin** → Redirección a página principal

### **Campos Protegidos**

Por seguridad, algunos campos están **ocultos** o **protegidos**:
- **Password de usuarios:** NO visible ni editable desde el panel
- **IDs:** Generados automáticamente, no editables
- **Fechas automáticas:** `created_at`, `updated_at` se gestionan automáticamente

---

## 🔧 **Solución de Problemas** {#solución-problemas}

### **❌ Error: "Forbidden - No tienes acceso"**

**Causa:** Tu usuario no tiene `is_admin=True`

**Solución:** Actualizar tu usuario en la base de datos:

```bash
flask shell
```

```python
from app.models import User
user = User.query.filter_by(username='tu_usuario').first()
user.is_admin = True
db.session.commit()
exit()
```

### **❌ Error: "404 Not Found" al acceder a /admin**

**Causa:** Flask-Admin no se inicializó correctamente

**Solución:**
1. Verifica que el archivo `app/admin.py` existe
2. Verifica que `init_admin(app)` se llama en `app/__init__.py`
3. Reinicia el servidor

### **❌ No Veo Mis Tablas en el Panel**

**Causa:** Los modelos no se registraron correctamente

**Solución:**
Verifica en `app/admin.py` que todas las líneas `admin.add_view(...)` están presentes.

### **❌ Error al Guardar Datos**

**Posibles causas:**
- Campo obligatorio vacío (`nullable=False`)
- Valor duplicado en campo único (`unique=True`)
- Tipo de dato incorrecto (texto en campo numérico)

**Solución:** Revisa el mensaje de error y ajusta los datos.

---

## 📚 **Tablas Disponibles en el Panel**

| Tabla | URL | Descripción |
|-------|-----|-------------|
| **Usuarios** | `/admin/admin_users/` | Gestión de usuarios del sistema |
| **Personas** | `/admin/admin_people/` | Personas físicas/jurídicas en transacciones |
| **Propiedades** | `/admin/admin_properties/` | Inmuebles y propiedades |
| **Transacciones** | `/admin/admin_transactions/` | Compraventas, herencias, etc. |
| **Cálculos Fiscales** | `/admin/admin_taxcalculations/` | Cálculos del IIVTNU |

---

## 🎨 **Personalización Futura**

El panel de administración es **completamente personalizable**. Puedes:

- ✅ Cambiar colores y estilos (archivo `custom_base.html`)
- ✅ Añadir columnas calculadas
- ✅ Crear formularios personalizados
- ✅ Añadir validaciones personalizadas
- ✅ Exportar a PDF, Excel, CSV
- ✅ Crear dashboards con estadísticas
- ✅ Añadir gráficos y visualizaciones

**Archivo de configuración:** `app/admin.py`

---

## 📞 **Recursos Adicionales**

- **Documentación Flask-Admin:** https://flask-admin.readthedocs.io/
- **Ejemplos de personalización:** Ver comentarios en `app/admin.py`
- **Soporte SQLAlchemy:** https://docs.sqlalchemy.org/

---

**Fecha:** 2 de octubre de 2025  
**Proyecto:** Tax Calculator Pro - IIVTNU Alfafar  
**Autor:** Jose - Inspección Tributaria Alfafar

