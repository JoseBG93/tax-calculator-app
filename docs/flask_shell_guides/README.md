# 🐚 Flask Shell Guides - Documentación Completa

Este directorio contiene toda la documentación y herramientas para trabajar con Flask Shell y realizar consultas rápidas a la base de datos sin levantar el servidor.

---

## 📁 Contenido del Directorio

| Archivo | Descripción | Para |
|---------|-------------|------|
| **FLASK_SHELL_README.md** | Guía de inicio rápido | Empezar |
| **FLASK_SHELL_QUICK_GUIDE.md** | Referencia completa con todos los ejemplos | Consultar |
| **shell_helper.py** | Script con 40+ funciones predefinidas | Usar |
| **ejemplo_consultas.py** | Ejemplos detallados de SQLAlchemy | Aprender |

---

## 🚀 Inicio Rápido

### 1. Lee el README primero
```bash
cat docs/flask_shell_guides/FLASK_SHELL_README.md
```

### 2. Abre Flask Shell con helper
```bash
taxshell-helper

# Dentro del shell:
>>> help()          # Ver todas las funciones
>>> stats()         # Ver estadísticas
>>> last_users(5)   # Últimos 5 usuarios
```

### 3. Consulta la guía cuando necesites
```bash
# Abre en tu editor favorito
nano docs/flask_shell_guides/FLASK_SHELL_QUICK_GUIDE.md
```

---

## 📖 Orden de Lectura Recomendado

Para **aprender desde cero:**

1. **`FLASK_SHELL_README.md`** → Empieza aquí
2. **`FLASK_SHELL_QUICK_GUIDE.md`** → Referencia completa
3. **`ejemplo_consultas.py`** → Ejemplos detallados
4. **`shell_helper.py`** → Ver código de las funciones

Para **uso diario:**

1. **`taxshell-helper`** → Comando directo
2. **`FLASK_SHELL_QUICK_GUIDE.md`** → Tener abierto como referencia

---

## 🎯 Comandos Disponibles

Desde cualquier ubicación en terminal:

```bash
# Flask Shell con funciones helper precargadas (recomendado)
taxshell-helper

# Flask Shell limpio (para consultas personalizadas)
taxshell

# Ver ayuda de todos los comandos
taxhelp
```

---

## 🛠️ Personalización

### Añadir tus propias funciones

Edita `shell_helper.py` y añade al final (antes del mensaje de inicio):

```python
def my_custom_function():
    """Tu función personalizada"""
    # Tu código aquí
    pass
```

Guarda y la próxima vez que ejecutes `taxshell-helper` estará disponible.

---

## 💡 Tips

1. **Mantén abierta la guía** mientras trabajas en Flask Shell
2. **Usa `help()`** dentro del shell para recordar funciones
3. **Combina** funciones helper con consultas SQLAlchemy directas
4. **No necesitas levantar el servidor** para hacer consultas

---

## 🔗 Enlaces Útiles

- **Proyecto principal:** `../../README.md`
- **Documentación general:** `../`
- **SQLAlchemy Docs:** https://docs.sqlalchemy.org/
- **Flask-SQLAlchemy:** https://flask-sqlalchemy.palletsprojects.com/

---

**Ubicación:** `/docs/flask_shell_guides/`  
**Proyecto:** Tax Calculator Pro  
**Creado:** 7 de octubre de 2025  
**Autor:** José

