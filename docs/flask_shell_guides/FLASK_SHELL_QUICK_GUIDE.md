# 🐚 Flask Shell - Guía Rápida de Referencia

**Guía práctica para consultas diarias sin levantar el servidor**

---

## 🚀 Inicio Rápido

### Abrir Flask Shell
```bash
# Desde el directorio del proyecto
cd /home/jose/my_Works/my_projects/tax-calculator-pro

# Activar entorno y abrir shell
source taxapp_env/bin/activate
flask shell

# O usar el alias
taxshell
```

### Salir de Flask Shell
```python
exit()
# o presiona Ctrl+D
```

---

## 📦 Importar Modelos

```python
# Importar todos los modelos a la vez
from app.models import User, People, Property, Transaction, TaxCalculation

# O importar uno por uno según necesites
from app.models import User
from app.models import Property
```

---

## 📊 Consultas Básicas del Día a Día

### 👥 **USUARIOS**

```python
# Ver todos los usuarios
User.query.all()

# Contar usuarios
User.query.count()

# Buscar usuario por nombre
User.query.filter_by(username='jose').first()

# Ver solo admins
User.query.filter_by(is_admin=True).all()

# Ver usuarios activos
User.query.filter_by(is_active=True).all()

# Último usuario creado
User.query.order_by(User.created_at.desc()).first()

# Ver info de un usuario específico
user = User.query.get(1)  # Por ID
print(f"Usuario: {user.username}")
print(f"Admin: {user.is_admin}")
print(f"Último login: {user.last_login}")
print(f"Total logins: {user.login_count}")
```

### 👤 **PERSONAS**

```python
# Ver todas las personas
People.query.all()

# Contar personas
People.query.count()

# Buscar por NIF
People.query.filter_by(nif='12345678A').first()

# Buscar por nombre
People.query.filter(People.name.like('%José%')).all()

# Ver solo personas físicas
People.query.filter_by(person_type='Física').all()

# Ver solo personas jurídicas
People.query.filter_by(person_type='Jurídica').all()

# Últimas personas registradas
People.query.order_by(People.created_at.desc()).limit(5).all()
```

### 🏠 **PROPIEDADES**

```python
# Ver todas las propiedades
Property.query.all()

# Contar propiedades
Property.query.count()

# Buscar por referencia catastral
Property.query.filter_by(cadastral_reference='1234567VH5797S').first()

# Propiedades de Alfafar
Property.query.filter_by(town='Alfafar').all()

# Propiedades por rango de valor
Property.query.filter(
    Property.cadastral_value >= 50000,
    Property.cadastral_value <= 150000
).all()

# Propiedades más caras (top 10)
Property.query.order_by(Property.cadastral_value.desc()).limit(10).all()

# Propiedades más baratas (top 10)
Property.query.order_by(Property.cadastral_value.asc()).limit(10).all()

# Valor promedio de propiedades
from sqlalchemy import func
Property.query.with_entities(func.avg(Property.cadastral_value)).scalar()

# Buscar por dirección (parcial)
Property.query.filter(Property.address.like('%Calle Mayor%')).all()
```

### 💰 **TRANSACCIONES**

```python
# Ver todas las transacciones
Transaction.query.all()

# Contar transacciones
Transaction.query.count()

# Solo ventas
Transaction.query.filter_by(transaction_type='Venta').all()

# Solo herencias
Transaction.query.filter_by(transaction_type='Herencia').all()

# Transacciones de este año
from datetime import datetime
year = datetime.now().year
Transaction.query.filter(
    Transaction.transaction_date >= f'{year}-01-01'
).all()

# Transacciones por rango de valor
Transaction.query.filter(
    Transaction.transaction_value >= 100000
).all()

# Últimas 10 transacciones
Transaction.query.order_by(Transaction.transaction_date.desc()).limit(10).all()

# Transacciones de una propiedad específica
Transaction.query.filter_by(property_id=1).all()
```

---

## 🔗 Navegar entre Tablas Relacionadas

### Desde una Transacción

```python
# Obtener una transacción
trans = Transaction.query.first()

# Ver datos de la propiedad
trans.property.address
trans.property.cadastral_reference
trans.property.cadastral_value

# Ver vendedor (si es venta)
if trans.grantor:
    print(trans.grantor.name, trans.grantor.surname)

# Ver comprador (si es venta)
if trans.grantee:
    print(trans.grantee.name, trans.grantee.surname)

# Ver todas las transacciones de una propiedad
prop = trans.property
for t in prop.transactions:
    print(f"{t.transaction_type} - {t.transaction_date} - €{t.transaction_value}")
```

### Desde una Propiedad

```python
# Obtener una propiedad
prop = Property.query.first()

# Ver todas sus transacciones
prop.transactions

# Contar cuántas transacciones tiene
len(prop.transactions)

# Ver la última transacción
sorted(prop.transactions, key=lambda t: t.transaction_date, reverse=True)[0]
```

### Desde una Persona

```python
# Obtener una persona
person = People.query.first()

# Ver en qué transacciones ha participado como comprador
Transaction.query.filter_by(grantee_id=person.id).all()

# Ver en qué transacciones ha participado como vendedor
Transaction.query.filter_by(grantor_id=person.id).all()
```

---

## 🔢 Estadísticas Rápidas

```python
# Totales
print(f"Usuarios: {User.query.count()}")
print(f"Personas: {People.query.count()}")
print(f"Propiedades: {Property.query.count()}")
print(f"Transacciones: {Transaction.query.count()}")

# Desglose de transacciones
ventas = Transaction.query.filter_by(transaction_type='Venta').count()
herencias = Transaction.query.filter_by(transaction_type='Herencia').count()
print(f"Ventas: {ventas}")
print(f"Herencias: {herencias}")

# Valor total transaccionado
from sqlalchemy import func
total = Transaction.query.with_entities(
    func.sum(Transaction.transaction_value)
).scalar()
print(f"Valor total: €{total:,.2f}")

# Promedio de transacciones
avg = Transaction.query.with_entities(
    func.avg(Transaction.transaction_value)
).scalar()
print(f"Valor promedio: €{avg:,.2f}")
```

---

## 🛠️ Operaciones de Mantenimiento

### Verificar Datos

```python
# Ver registros duplicados (NIFs)
from sqlalchemy import func
duplicates = People.query.with_entities(
    People.nif,
    func.count(People.id)
).group_by(People.nif).having(func.count(People.id) > 1).all()

# Ver registros sin transacciones
props_without_trans = Property.query.filter(
    ~Property.id.in_([t.property_id for t in Transaction.query.all()])
).all()

# Ver transacciones con valores anormales
anomalies = Transaction.query.filter(
    Transaction.transaction_value <= 0
).all()
```

### Ver Estructura de Tabla

```python
# Ver columnas de un modelo
User.__table__.columns.keys()
Property.__table__.columns.keys()
Transaction.__table__.columns.keys()

# Ver relaciones
User.__mapper__.relationships.keys()
Transaction.__mapper__.relationships.keys()
```

---

## 💡 Trucos y Tips

### Formatear Salida

```python
# Ver datos de forma más legible
for user in User.query.all():
    print(f"ID: {user.id} | Usuario: {user.username} | Admin: {user.is_admin}")

# Con f-strings multilínea
for prop in Property.query.limit(5).all():
    print(f"""
    Dirección: {prop.address}
    Ref. Catastral: {prop.cadastral_reference}
    Valor: €{prop.cadastral_value:,.2f}
    {'─'*50}
    """)
```

### Exportar a Variables

```python
# Guardar consultas en variables para trabajar con ellas
admins = User.query.filter_by(is_admin=True).all()
propiedades_alfafar = Property.query.filter_by(town='Alfafar').all()
ventas_2024 = Transaction.query.filter(
    Transaction.transaction_date >= '2024-01-01'
).all()

# Ahora puedes trabajar con las variables sin hacer consultas repetidas
len(admins)
admins[0].username
```

### Debugging

```python
# Ver la consulta SQL que se ejecutará
query = User.query.filter_by(is_admin=True)
print(str(query))  # Muestra el SQL

# Verificar si existe un registro
user_exists = User.query.filter_by(username='jose').first() is not None
print(f"¿Usuario 'jose' existe? {user_exists}")

# Ver atributos de un objeto
user = User.query.first()
vars(user)  # Muestra todos los atributos
```

---

## ⚠️ Recordatorios Importantes

1. **No olvides el `.all()` o `.first()`**
   ```python
   # ❌ MAL - Devuelve un objeto Query
   users = User.query.filter_by(is_admin=True)
   
   # ✅ BIEN - Devuelve los datos
   users = User.query.filter_by(is_admin=True).all()
   ```

2. **Usa `.first()` en lugar de `.all()[0]`**
   ```python
   # ❌ Ineficiente y puede dar error si está vacío
   user = User.query.filter_by(username='jose').all()[0]
   
   # ✅ Mejor
   user = User.query.filter_by(username='jose').first()
   ```

3. **Verifica None antes de acceder a atributos**
   ```python
   user = User.query.filter_by(username='jose').first()
   if user:
       print(user.username)
   else:
       print("Usuario no encontrado")
   ```

4. **Usa `.count()` en lugar de `len(.all())`**
   ```python
   # ❌ Ineficiente - trae todos los datos a memoria
   total = len(User.query.all())
   
   # ✅ Eficiente - cuenta en la base de datos
   total = User.query.count()
   ```

---

## 🎯 Comandos Más Usados (Resumen)

```python
# Importar modelos
from app.models import User, People, Property, Transaction

# Ver todo
User.query.all()

# Contar
User.query.count()

# Buscar por campo
User.query.filter_by(username='jose').first()

# Buscar con condiciones
Property.query.filter(Property.cadastral_value > 100000).all()

# Ordenar
User.query.order_by(User.created_at.desc()).all()

# Limitar resultados
User.query.limit(10).all()

# Combinar operaciones
User.query.filter_by(is_admin=True).order_by(User.created_at.desc()).limit(5).all()

# Estadísticas
from sqlalchemy import func
User.query.with_entities(func.count()).scalar()
Property.query.with_entities(func.avg(Property.cadastral_value)).scalar()
```

---

## 📚 Recursos Adicionales

- **Archivo completo de ejemplos:** `docs/flask_shell_guides/ejemplo_consultas.py`
- **Script helper:** `docs/flask_shell_guides/shell_helper.py` (funciones predefinidas)
- **Guía de inicio:** `docs/flask_shell_guides/FLASK_SHELL_README.md`
- **Documentación Flask-SQLAlchemy:** https://flask-sqlalchemy.palletsprojects.com/

---

**💡 Tip Final:** Guarda esta guía cerca y ábrela en otra ventana mientras trabajas en Flask Shell para tener referencia rápida.

**Creado:** 7 de octubre de 2025  
**Actualizado:** 7 de octubre de 2025

