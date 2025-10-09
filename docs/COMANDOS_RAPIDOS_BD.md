# 🚀 COMANDOS RÁPIDOS PARA CONSULTAR LA BASE DE DATOS

## 📊 MÉTODO 1: SQLite CLI (SQL Directo)

### Entrar a la base de datos
```bash
cd /home/jose/my_Works/my_projects/tax-calculator-pro
sqlite3 database/app.db
```

### Comandos dentro de SQLite

#### Configuración visual (ejecutar al entrar)
```sql
.headers on          -- Mostrar nombres de columnas
.mode column         -- Formato de tabla legible
.width 5 15 10 10    -- Ancho de columnas (ajustar según necesidad)
```

#### Ver todas las tablas
```sql
.tables
```

#### Ver estructura de una tabla
```sql
.schema user
.schema people
.schema property
```

#### CONSULTAS RÁPIDAS - Usuarios

```sql
-- Ver TODOS los usuarios
SELECT id, username, is_admin, is_active FROM user;

-- Contar usuarios totales
SELECT COUNT(*) as total_usuarios FROM user;

-- Ver solo administradores
SELECT id, username, last_login, login_count 
FROM user 
WHERE is_admin = 1;

-- Ver usuarios activos
SELECT id, username, created_at 
FROM user 
WHERE is_active = 1;

-- Ver usuarios inactivos
SELECT id, username, is_admin 
FROM user 
WHERE is_active = 0;

-- Ver último login de todos
SELECT username, last_login, login_count 
FROM user 
ORDER BY last_login DESC;

-- Ver usuarios creados recientemente (últimos 5)
SELECT id, username, created_at 
FROM user 
ORDER BY created_at DESC 
LIMIT 5;
```

#### CONSULTAS RÁPIDAS - Personas

```sql
-- Contar personas registradas
SELECT COUNT(*) as total_personas FROM people;

-- Ver todas las personas
SELECT id, first_name, last_name, document_id, email FROM people;

-- Buscar persona por DNI
SELECT * FROM people WHERE document_id = '12345678A';

-- Buscar persona por nombre
SELECT * FROM people WHERE first_name LIKE '%Jose%';
```

#### CONSULTAS RÁPIDAS - Propiedades

```sql
-- Contar propiedades
SELECT COUNT(*) as total_propiedades FROM property;

-- Ver propiedades con sus dueños
SELECT p.id, p.cadastral_reference, pe.first_name, pe.last_name
FROM property p
JOIN people pe ON p.owner_id = pe.id;

-- Propiedades por referencia catastral
SELECT * FROM property WHERE cadastral_reference = '1234567890';
```

#### CONSULTAS RÁPIDAS - Transacciones

```sql
-- Contar transacciones
SELECT COUNT(*) as total_transacciones FROM transaction;

-- Ver últimas 10 transacciones
SELECT id, property_id, transaction_type, transaction_date, declared_value
FROM transaction
ORDER BY transaction_date DESC
LIMIT 10;

-- Transacciones de un tipo específico
SELECT * FROM transaction WHERE transaction_type = 'sale';
```

#### CONSULTAS RÁPIDAS - Cálculos Fiscales

```sql
-- Contar cálculos realizados
SELECT COUNT(*) as total_calculos FROM tax_calculation;

-- Ver últimos cálculos con detalles
SELECT id, transaction_id, tax_amount, created_at
FROM tax_calculation
ORDER BY created_at DESC
LIMIT 10;
```

#### Salir de SQLite
```sql
.quit
```

---

## 🐍 MÉTODO 2: Flask Shell (Python + ORM)

### Entrar al shell de Flask
```bash
cd /home/jose/my_Works/my_projects/tax-calculator-pro
source taxapp_env/bin/activate
flask shell
```

### Comandos dentro de Flask Shell

#### Importar modelos (ejecutar al entrar)
```python
from app.models import User, People, Property, Transaction, TaxCalculation
from app import db
```

#### Consultas con SQLAlchemy ORM

```python
# ====================
# USUARIOS
# ====================

# Contar usuarios
User.query.count()

# Ver todos los usuarios
users = User.query.all()
for u in users:
    print(f"{u.id}: {u.username} - Admin: {u.is_admin}")

# Buscar usuario por nombre
user = User.query.filter_by(username='Josh93').first()
print(f"ID: {user.id}, Admin: {user.is_admin}")

# Solo administradores
admins = User.query.filter_by(is_admin=True).all()
print(f"Total admins: {len(admins)}")

# Usuarios activos
active = User.query.filter_by(is_active=True).count()
print(f"Usuarios activos: {active}")

# Últimos 5 usuarios registrados
recent = User.query.order_by(User.created_at.desc()).limit(5).all()
for u in recent:
    print(f"{u.username} - Creado: {u.created_at}")

# ====================
# PERSONAS
# ====================

# Contar personas
People.query.count()

# Ver todas
people = People.query.all()
for p in people:
    print(f"{p.id}: {p.first_name} {p.last_name} - DNI: {p.document_id}")

# Buscar por DNI
person = People.query.filter_by(document_id='12345678A').first()

# Buscar por nombre (parcial)
results = People.query.filter(People.first_name.like('%Jose%')).all()

# ====================
# PROPIEDADES
# ====================

# Contar propiedades
Property.query.count()

# Ver todas con dueño
properties = Property.query.join(People).all()
for prop in properties:
    print(f"{prop.cadastral_reference} - Dueño: {prop.owner.first_name}")

# ====================
# TRANSACCIONES
# ====================

# Últimas 10 transacciones
transactions = Transaction.query.order_by(Transaction.transaction_date.desc()).limit(10).all()
for t in transactions:
    print(f"ID: {t.id} - Tipo: {t.transaction_type} - Valor: {t.declared_value}")

# ====================
# CÁLCULOS FISCALES
# ====================

# Contar cálculos
TaxCalculation.query.count()

# Últimos cálculos
calculations = TaxCalculation.query.order_by(TaxCalculation.created_at.desc()).limit(5).all()
```

#### Salir del Flask Shell
```python
exit()
```

---

## ⚡ MÉTODO 3: Comandos de Una Línea (One-Liners)

### Comandos SQLite de una línea (sin entrar al shell)

```bash
# Contar usuarios
sqlite3 database/app.db "SELECT COUNT(*) FROM user;"

# Ver todos los usuarios
sqlite3 database/app.db "SELECT id, username, is_admin FROM user;"

# Ver solo admins
sqlite3 database/app.db "SELECT username FROM user WHERE is_admin=1;"

# Contar personas
sqlite3 database/app.db "SELECT COUNT(*) FROM people;"

# Ver último login de todos
sqlite3 database/app.db "SELECT username, last_login FROM user ORDER BY last_login DESC;"

# Estadísticas rápidas
sqlite3 database/app.db "SELECT 
    (SELECT COUNT(*) FROM user) as usuarios,
    (SELECT COUNT(*) FROM people) as personas,
    (SELECT COUNT(*) FROM property) as propiedades,
    (SELECT COUNT(*) FROM transaction) as transacciones;"
```

### Comandos Flask de una línea

```bash
# Contar usuarios (desde terminal, sin entrar al shell)
cd /home/jose/my_Works/my_projects/tax-calculator-pro && \
source taxapp_env/bin/activate && \
flask shell -c "from app.models import User; print(f'Total usuarios: {User.query.count()}')"

# Ver admins
flask shell -c "from app.models import User; [print(f'{u.username}') for u in User.query.filter_by(is_admin=True).all()]"
```

---

## 🎯 MÉTODO 4: Crear Alias Personalizados en Bash

### Agregar al archivo ~/.bashrc

```bash
# Alias para tax-calculator-pro database
alias taxdb='sqlite3 /home/jose/my_Works/my_projects/tax-calculator-pro/database/app.db'
alias taxusers='sqlite3 /home/jose/my_Works/my_projects/tax-calculator-pro/database/app.db "SELECT id, username, is_admin, is_active FROM user;"'
alias taxcount='sqlite3 /home/jose/my_Works/my_projects/tax-calculator-pro/database/app.db "SELECT (SELECT COUNT(*) FROM user) as usuarios, (SELECT COUNT(*) FROM people) as personas, (SELECT COUNT(*) FROM property) as propiedades;"'
alias taxadmins='sqlite3 /home/jose/my_Works/my_projects/tax-calculator-pro/database/app.db "SELECT username, is_admin, last_login FROM user WHERE is_admin=1;"'
```

### Después de agregar los alias:
```bash
source ~/.bashrc
```

### Uso de los alias:
```bash
taxdb        # Abre la BD en modo interactivo
taxusers     # Lista todos los usuarios
taxcount     # Muestra conteo de registros
taxadmins    # Lista solo administradores

---

## 💡 RECOMENDACIONES

1. **Para consultas rápidas diarias** → Usa alias de bash
2. **Para exploración de datos** → Usa SQLite CLI con `.mode column`
3. **Para lógica compleja con Python** → Usa Flask Shell
4. **Para scripts automatizados** → Usa Python (como list_users.py)

---

## 🔒 NOTA DE SEGURIDAD

⚠️ **Las contraseñas están hasheadas y NUNCA se deben ver en texto plano.**

Si intentas ver contraseñas:
```sql
SELECT password FROM user;
-- Verás algo como: pbkdf2:sha256:600000$abc123...
```

Esto es **correcto y seguro**. Para cambiar contraseñas usa `change_password.py`.
