#!/bin/bash
# ==============================================================================
# ALIAS PERSONALIZADOS PARA TAX-CALCULATOR-PRO
# ==============================================================================
#
# Archivo específico con todos los alias y funciones del proyecto Tax Calculator Pro
#
# INSTALACIÓN:
#   Opción 1 (Recomendada): Añadir al final de ~/.bashrc:
#     source /home/user/tax-calculator-pro/bash_aliases.sh
#
#   Opción 2: Usar directamente cuando trabajes en este proyecto:
#     source bash_aliases.sh
#
# COMANDOS DISPONIBLES:
#   taxhelp      → Ver todos los comandos disponibles
#   taxusers     → Ver todos los usuarios
#   taxrun       → Ejecutar la aplicación
#
# ==============================================================================

# ==============================================================================
# CONFIGURACIÓN DE VARIABLES
# ==============================================================================

# Ruta base del proyecto Tax-Calculator-Pro
export TAX_CALC_DIR="/home/jose/my_Works/my_projects/tax-calculator-pro"
export TAX_DB="$TAX_CALC_DIR/database/app.db"

# ==============================================================================
# ALIAS PARA CONSULTAS DE BASE DE DATOS
# ==============================================================================

# Abrir base de datos en modo interactivo con formato legible
alias taxdb='sqlite3 -header -column '"$TAX_DB"

# Ver todos los usuarios
alias taxusers='sqlite3 -header -column '"$TAX_DB"' "SELECT id, username, is_admin as admin, is_active as activo, login_count as logins FROM user;"'

# Ver solo administradores
alias taxadmins='sqlite3 -header -column '"$TAX_DB"' "SELECT id, username, last_login, login_count FROM user WHERE is_admin=1;"'

# Ver estadísticas generales
alias taxcount='sqlite3 -header -column '"$TAX_DB"' "SELECT (SELECT COUNT(*) FROM user) as Usuarios, (SELECT COUNT(*) FROM people) as Personas, (SELECT COUNT(*) FROM property) as Propiedades, (SELECT COUNT(*) FROM [transaction]) as Transacciones, (SELECT COUNT(*) FROM tax_calculation) as Calculos;"'

# Ver usuarios activos
alias taxactive='sqlite3 -header -column '"$TAX_DB"' "SELECT id, username, last_login FROM user WHERE is_active=1;"'

# Ver usuarios inactivos
alias taxinactive='sqlite3 -header -column '"$TAX_DB"' "SELECT id, username FROM user WHERE is_active=0;"'

# Ver todas las tablas de la base de datos
alias taxtables='sqlite3 '"$TAX_DB"' ".tables"'

# Ver estructura de la tabla user
alias taxschema='sqlite3 '"$TAX_DB"' ".schema user"'

# ==============================================================================
# ALIAS PARA SCRIPTS PYTHON
# ==============================================================================

# Activar entorno virtual + listar usuarios
alias taxlist='cd '"$TAX_CALC_DIR"' && source taxapp_env/bin/activate && python list_users.py'

# Activar entorno virtual + cambiar contraseña
alias taxpasswd='cd '"$TAX_CALC_DIR"' && source taxapp_env/bin/activate && python change_password.py'

# Activar entorno virtual + gestionar admin
alias taxadmin='cd '"$TAX_CALC_DIR"' && source taxapp_env/bin/activate && python create_admin.py'

# Activar entorno virtual + abrir Flask shell
alias taxshell='cd '"$TAX_CALC_DIR"' && source taxapp_env/bin/activate && flask shell'

# Activar entorno virtual + abrir Flask shell con helper precargado
alias taxshell-helper='cd '"$TAX_CALC_DIR"' && source taxapp_env/bin/activate && flask shell --command="exec(open(\"docs/flask_shell_guides/shell_helper.py\").read())"'

# Activar entorno virtual
alias taxenv='cd '"$TAX_CALC_DIR"' && source taxapp_env/bin/activate'

# Ejecutar la aplicación
alias taxrun='cd '"$TAX_CALC_DIR"' && source taxapp_env/bin/activate && python run.py'

# ==============================================================================
# ALIAS DE NAVEGACIÓN
# ==============================================================================

# Nota: Usa 'taxapp' para ir al directorio del proyecto (definido en ~/.bash_aliases)

# ==============================================================================
# FUNCIONES DE BÚSQUEDA Y GESTIÓN DE USUARIOS
# ==============================================================================

# Buscar usuario por nombre
# Uso: taxfind 'username'
taxfind() {
    if [ -z "$1" ]; then
        echo "❌ Uso: taxfind <nombre_usuario>"
        return 1
    fi
    sqlite3 -header -column "$TAX_DB" "SELECT id, username, is_admin, is_active, last_login FROM user WHERE username LIKE '%$1%';"
}

# Ver información completa de un usuario por ID
# Uso: taxuser 2
taxuser() {
    if [ -z "$1" ]; then
        echo "❌ Uso: taxuser <user_id>"
        return 1
    fi
    sqlite3 -header -column "$TAX_DB" "SELECT * FROM user WHERE id=$1;"
}

# ==============================================================================
# AYUDA RÁPIDA
# ==============================================================================

# Mostrar todos los comandos específicos del proyecto
alias taxhelp='echo "
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 COMANDOS DISPONIBLES TAX-CALCULATOR-PRO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 CONSULTAS BASE DE DATOS:
  taxdb          - Abrir BD en modo interactivo
  taxusers       - Ver todos los usuarios
  taxadmins      - Ver solo administradores
  taxactive      - Ver usuarios activos
  taxinactive    - Ver usuarios inactivos
  taxcount       - Estadísticas generales
  taxtables      - Ver todas las tablas
  taxschema      - Ver estructura tabla user
  taxfind <user> - Buscar usuario por nombre
  taxuser <id>   - Ver info completa de usuario

🐍 SCRIPTS PYTHON:
  taxlist         - Listar usuarios (script Python)
  taxpasswd       - Cambiar contraseña
  taxadmin        - Gestionar superadmin
  taxshell        - Abrir Flask Shell (limpio)
  taxshell-helper - Abrir Flask Shell con funciones helper precargadas
  taxrun          - Ejecutar aplicación

📁 NAVEGACIÓN:
  taxapp         - Ir al directorio del proyecto (alias general en ~/.bash_aliases)

❓ AYUDA GENERAL:
  taxhelp        - Mostrar esta ayuda
  myaliases      - Ver TODOS tus alias organizados

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"'

# ==============================================================================
# MENSAJE DE CONFIRMACIÓN DE CARGA
# ==============================================================================

echo ""
echo "✅ Alias de Tax Calculator Pro cargados correctamente!"
echo "💡 Ejecuta 'taxhelp' para ver todos los comandos disponibles"
echo ""
