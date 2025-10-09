# 🐚 Flask Shell - Guía de Inicio Rápido

**Consultas rápidas a tu base de datos sin levantar el servidor**

---

## 📚 Archivos Disponibles

| Archivo | Descripción | Uso |
|---------|-------------|-----|
| **FLASK_SHELL_QUICK_GUIDE.md** | Guía de referencia completa con ejemplos | Referencia |
| **shell_helper.py** | Funciones predefinidas para consultas rápidas | Cargar en shell |
| **ejemplo_consultas.py** | Ejemplos detallados de consultas SQLAlchemy | Aprendizaje |

---

## 🚀 Inicio Rápido

### Opción 1: Flask Shell Limpio

```bash
# Desde cualquier lugar
taxshell

# Dentro del shell
>>> from app.models import User, Property, Transaction
>>> User.query.count()
>>> Property.query.all()
```

### Opción 2: Flask Shell con Helper (Recomendado)

```bash
# Desde cualquier lugar - Helper ya cargado
taxshell-helper

# Las funciones ya están disponibles
>>> stats()              # Ver estadísticas generales
>>> last_users(5)        # Últimos 5 usuarios
>>> find_property('Calle Mayor')
>>> help()               # Ver todas las funciones
```

### Opción 3: Cargar Helper Manualmente

```bash
taxshell

# Dentro del shell
>>> exec(open('docs/flask_shell_guides/shell_helper.py').read())
>>> stats()
```

---

## ⚡ Funciones Más Útiles (con helper cargado)

```python
# Estadísticas rápidas
stats()                  # Completas
quick_stats()            # Una línea

# Listar datos
all_users()
all_people()
all_properties()
all_transactions()

# Buscar
find_user('jose')
find_person('García')
find_property('Calle')
search_all('término')    # Busca en todo

# Top 10
expensive_properties()
cheap_properties()
last_transactions(10)

# Filtros específicos
sales()                  # Solo ventas
inheritances()           # Solo herencias
transactions_this_year()
property_transactions(1) # Por ID de propiedad

# Ayuda
help()                   # Lista todas las funciones
```

---

## 📖 Consultas SQLAlchemy Directas

```python
# Importar modelos
from app.models import User, People, Property, Transaction

# Consultas básicas
User.query.all()                              # Todos
User.query.count()                            # Contar
User.query.get(1)                             # Por ID
User.query.filter_by(username='jose').first() # Buscar

# Consultas avanzadas
Property.query.filter(
    Property.cadastral_value > 100000
).all()

User.query.order_by(User.created_at.desc()).limit(10).all()

# Estadísticas
from sqlalchemy import func
Property.query.with_entities(func.avg(Property.cadastral_value)).scalar()
```

---

## 💡 Tips Rápidos

1. **Para consultas simples → usa helper:**
   ```python
   stats()
   last_users(5)
   ```

2. **Para consultas complejas → usa SQLAlchemy directo:**
   ```python
   Property.query.filter(
       Property.cadastral_value.between(50000, 150000)
   ).order_by(Property.address).all()
   ```

3. **Para aprender → consulta los archivos de ejemplo:**
   - `FLASK_SHELL_QUICK_GUIDE.md` → Referencia rápida
   - `ejemplo_consultas.py` → Ejemplos detallados

---

## 🎯 Casos de Uso Comunes

### Ver resumen del día
```bash
taxshell-helper
>>> quick_stats()
>>> last_transactions(10)
```

### Buscar una propiedad
```bash
taxshell-helper
>>> find_property('Calle Mayor')
>>> # O más específico:
>>> Property.query.filter_by(cadastral_reference='1234567VH5797S').first()
```

### Ver actividad de un usuario
```bash
taxshell-helper
>>> find_user('jose')
```

### Auditar transacciones del año
```bash
taxshell-helper
>>> transactions_this_year()
```

### Ver propiedades en rango de precio
```bash
taxshell-helper
>>> properties_by_value(50000, 150000)
```

---

## 📋 Comandos de Terminal

```bash
# Abrir shell normal
taxshell

# Abrir shell con helper
taxshell-helper

# Ver ayuda de comandos tax
taxhelp

# Listar usuarios (sin shell)
taxlist

# Gestionar usuarios (sin shell)
taxpasswd
taxadmin
```

---

## 🔧 Personalización

Puedes añadir tus propias funciones al archivo `docs/flask_shell_guides/shell_helper.py`:

```python
def my_custom_query():
    """Tu consulta personalizada"""
    # Tu código aquí
    pass
```

Después de editar, recarga el helper:
```python
>>> exec(open('docs/flask_shell_guides/shell_helper.py').read())
```

---

## ⚠️ Recordatorios

- ✅ Flask Shell **NO levanta el servidor** - solo accede a la BD
- ✅ Es perfecto para consultas rápidas del día a día
- ✅ Los cambios en la BD son reales (ten cuidado)
- ✅ Para operaciones complejas mejor usar el admin panel web

---

## 📚 Documentación Adicional

- **SQLAlchemy:** https://docs.sqlalchemy.org/
- **Flask-SQLAlchemy:** https://flask-sqlalchemy.palletsprojects.com/
- **Flask Shell:** https://flask.palletsprojects.com/en/latest/shell/

---

**Creado:** 7 de octubre de 2025  
**Proyecto:** Tax Calculator Pro  
**Autor:** José

