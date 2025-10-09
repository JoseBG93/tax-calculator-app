#!/usr/bin/env python3
"""
FLASK SHELL HELPER - Funciones Útiles para Consultas Rápidas
==============================================================

Este archivo contiene funciones predefinidas para hacer consultas comunes
de manera más rápida y sencilla desde Flask Shell.

USO:
----
1. Abrir Flask Shell:
   $ flask shell

2. Cargar este archivo:
   >>> exec(open('docs/flask_shell_guides/shell_helper.py').read())

3. Usar las funciones:
   >>> stats()              # Ver estadísticas generales
   >>> last_users(5)        # Ver últimos 5 usuarios
   >>> find_property('Calle Mayor')  # Buscar propiedad

CREADO: 7 de octubre de 2025
"""

from app.models import User, People, Property, Transaction, TaxCalculation
from sqlalchemy import func, desc
from datetime import datetime
from tabulate import tabulate  # pip install tabulate (si no lo tienes)

# ==============================================================================
# 📊 ESTADÍSTICAS GENERALES
# ==============================================================================

def stats():
    """Muestra estadísticas generales de la base de datos"""
    print("\n" + "="*60)
    print("📊 ESTADÍSTICAS GENERALES DE LA BASE DE DATOS")
    print("="*60)
    
    # Totales
    total_users = User.query.count()
    total_people = People.query.count()
    total_properties = Property.query.count()
    total_transactions = Transaction.query.count()
    
    print(f"\n📦 TOTALES:")
    print(f"  👥 Usuarios:      {total_users}")
    print(f"  👤 Personas:      {total_people}")
    print(f"  🏠 Propiedades:   {total_properties}")
    print(f"  💰 Transacciones: {total_transactions}")
    
    # Desglose de usuarios
    admins = User.query.filter_by(is_admin=True).count()
    active = User.query.filter_by(is_active=True).count()
    print(f"\n👥 USUARIOS:")
    print(f"  🔑 Administradores: {admins}")
    print(f"  ✅ Activos:         {active}")
    print(f"  ❌ Inactivos:       {total_users - active}")
    
    # Desglose de personas
    fisicas = People.query.filter_by(person_type='Física').count()
    juridicas = People.query.filter_by(person_type='Jurídica').count()
    print(f"\n👤 PERSONAS:")
    print(f"  🧑 Físicas:   {fisicas}")
    print(f"  🏢 Jurídicas: {juridicas}")
    
    # Desglose de transacciones
    if total_transactions > 0:
        ventas = Transaction.query.filter_by(transaction_type='Venta').count()
        herencias = Transaction.query.filter_by(transaction_type='Herencia').count()
        
        # Valores totales
        total_value = Transaction.query.with_entities(
            func.sum(Transaction.transaction_value)
        ).scalar() or 0
        
        avg_value = Transaction.query.with_entities(
            func.avg(Transaction.transaction_value)
        ).scalar() or 0
        
        print(f"\n💰 TRANSACCIONES:")
        print(f"  🏪 Ventas:    {ventas}")
        print(f"  🏛️  Herencias: {herencias}")
        print(f"  💵 Valor total:    €{total_value:,.2f}")
        print(f"  📊 Valor promedio: €{avg_value:,.2f}")
    
    print("\n" + "="*60 + "\n")


def quick_stats():
    """Versión corta de estadísticas (una línea por tipo)"""
    print(f"👥 Users: {User.query.count()} | "
          f"👤 People: {People.query.count()} | "
          f"🏠 Props: {Property.query.count()} | "
          f"💰 Trans: {Transaction.query.count()}")


# ==============================================================================
# 👥 FUNCIONES PARA USUARIOS
# ==============================================================================

def all_users():
    """Lista todos los usuarios con su información básica"""
    users = User.query.all()
    print(f"\n📋 USUARIOS ({len(users)} total):\n")
    for u in users:
        admin_badge = "🔑" if u.is_admin else "  "
        active_badge = "✅" if u.is_active else "❌"
        print(f"  {admin_badge} {active_badge} [{u.id}] {u.username} "
              f"(logins: {u.login_count}, último: {u.last_login or 'nunca'})")
    print()


def last_users(n=5):
    """Muestra los últimos N usuarios creados"""
    users = User.query.order_by(desc(User.created_at)).limit(n).all()
    print(f"\n🆕 ÚLTIMOS {n} USUARIOS:\n")
    for u in users:
        print(f"  [{u.id}] {u.username} - Creado: {u.created_at}")
    print()


def admins():
    """Lista todos los administradores"""
    admin_users = User.query.filter_by(is_admin=True).all()
    print(f"\n🔑 ADMINISTRADORES ({len(admin_users)} total):\n")
    for u in admin_users:
        status = "✅ Activo" if u.is_active else "❌ Inactivo"
        print(f"  [{u.id}] {u.username} - {status}")
    print()


def find_user(username):
    """Busca un usuario por nombre (búsqueda parcial)"""
    users = User.query.filter(User.username.like(f'%{username}%')).all()
    if users:
        print(f"\n🔍 RESULTADOS PARA '{username}':\n")
        for u in users:
            print(f"  [{u.id}] {u.username}")
            print(f"      Admin: {u.is_admin} | Activo: {u.is_active}")
            print(f"      Último login: {u.last_login or 'nunca'}")
            print(f"      Total logins: {u.login_count}\n")
    else:
        print(f"❌ No se encontraron usuarios con '{username}'")
    return users


# ==============================================================================
# 👤 FUNCIONES PARA PERSONAS
# ==============================================================================

def all_people():
    """Lista todas las personas"""
    people = People.query.all()
    print(f"\n📋 PERSONAS ({len(people)} total):\n")
    for p in people:
        tipo_emoji = "🧑" if p.person_type == 'Física' else "🏢"
        print(f"  {tipo_emoji} [{p.id}] {p.name} {p.surname} - NIF: {p.nif}")
    print()


def last_people(n=5):
    """Muestra las últimas N personas registradas"""
    people = People.query.order_by(desc(People.created_at)).limit(n).all()
    print(f"\n🆕 ÚLTIMAS {n} PERSONAS:\n")
    for p in people:
        print(f"  [{p.id}] {p.name} {p.surname} - {p.nif}")
    print()


def find_person(search):
    """Busca personas por nombre, apellido o NIF"""
    people = People.query.filter(
        (People.name.like(f'%{search}%')) |
        (People.surname.like(f'%{search}%')) |
        (People.nif.like(f'%{search}%'))
    ).all()
    
    if people:
        print(f"\n🔍 RESULTADOS PARA '{search}':\n")
        for p in people:
            print(f"  [{p.id}] {p.name} {p.surname}")
            print(f"      NIF: {p.nif}")
            print(f"      Tipo: {p.person_type}")
            print(f"      Dirección: {p.notification_address}\n")
    else:
        print(f"❌ No se encontraron personas con '{search}'")
    return people


# ==============================================================================
# 🏠 FUNCIONES PARA PROPIEDADES
# ==============================================================================

def all_properties():
    """Lista todas las propiedades"""
    props = Property.query.all()
    print(f"\n📋 PROPIEDADES ({len(props)} total):\n")
    for p in props:
        print(f"  🏠 [{p.id}] {p.address}")
        print(f"      Ref: {p.cadastral_reference} | Valor: €{p.cadastral_value:,.2f}\n")


def last_properties(n=5):
    """Muestra las últimas N propiedades registradas"""
    props = Property.query.order_by(desc(Property.created_at)).limit(n).all()
    print(f"\n🆕 ÚLTIMAS {n} PROPIEDADES:\n")
    for p in props:
        print(f"  [{p.id}] {p.address} - €{p.cadastral_value:,.2f}")
    print()


def find_property(search):
    """Busca propiedades por dirección o referencia catastral"""
    props = Property.query.filter(
        (Property.address.like(f'%{search}%')) |
        (Property.cadastral_reference.like(f'%{search}%'))
    ).all()
    
    if props:
        print(f"\n🔍 RESULTADOS PARA '{search}':\n")
        for p in props:
            print(f"  🏠 [{p.id}] {p.address}")
            print(f"      Municipio: {p.town}")
            print(f"      Ref. Catastral: {p.cadastral_reference}")
            print(f"      Valor: €{p.cadastral_value:,.2f}")
            print(f"      Transacciones: {len(p.transactions)}\n")
    else:
        print(f"❌ No se encontraron propiedades con '{search}'")
    return props


def expensive_properties(n=10):
    """Muestra las N propiedades más caras"""
    props = Property.query.order_by(desc(Property.cadastral_value)).limit(n).all()
    print(f"\n💎 TOP {n} PROPIEDADES MÁS CARAS:\n")
    for i, p in enumerate(props, 1):
        print(f"  {i}. [{p.id}] {p.address}")
        print(f"      Valor: €{p.cadastral_value:,.2f}\n")


def cheap_properties(n=10):
    """Muestra las N propiedades más baratas"""
    props = Property.query.order_by(Property.cadastral_value).limit(n).all()
    print(f"\n💸 TOP {n} PROPIEDADES MÁS BARATAS:\n")
    for i, p in enumerate(props, 1):
        print(f"  {i}. [{p.id}] {p.address}")
        print(f"      Valor: €{p.cadastral_value:,.2f}\n")


def properties_by_value(min_value, max_value):
    """Busca propiedades en un rango de valores"""
    props = Property.query.filter(
        Property.cadastral_value >= min_value,
        Property.cadastral_value <= max_value
    ).all()
    
    print(f"\n🏠 PROPIEDADES ENTRE €{min_value:,.2f} Y €{max_value:,.2f}:\n")
    print(f"📊 Total encontradas: {len(props)}\n")
    
    for p in props:
        print(f"  [{p.id}] {p.address} - €{p.cadastral_value:,.2f}")
    print()
    return props


# ==============================================================================
# 💰 FUNCIONES PARA TRANSACCIONES
# ==============================================================================

def all_transactions():
    """Lista todas las transacciones"""
    trans = Transaction.query.all()
    print(f"\n📋 TRANSACCIONES ({len(trans)} total):\n")
    for t in trans:
        tipo_emoji = "🏪" if t.transaction_type == 'Venta' else "🏛️"
        print(f"  {tipo_emoji} [{t.id}] {t.transaction_type} - €{t.transaction_value:,.2f}")
        print(f"      Fecha: {t.transaction_date}")
        print(f"      Propiedad: {t.property.address}\n")


def last_transactions(n=10):
    """Muestra las últimas N transacciones"""
    trans = Transaction.query.order_by(desc(Transaction.transaction_date)).limit(n).all()
    print(f"\n🆕 ÚLTIMAS {n} TRANSACCIONES:\n")
    for t in trans:
        tipo_emoji = "🏪" if t.transaction_type == 'Venta' else "🏛️"
        print(f"  {tipo_emoji} [{t.id}] {t.transaction_type}")
        print(f"      Valor: €{t.transaction_value:,.2f}")
        print(f"      Fecha: {t.transaction_date}")
        print(f"      Propiedad: {t.property.address}\n")


def sales():
    """Lista todas las ventas"""
    ventas = Transaction.query.filter_by(transaction_type='Venta').all()
    print(f"\n🏪 VENTAS ({len(ventas)} total):\n")
    for v in ventas:
        print(f"  [{v.id}] €{v.transaction_value:,.2f} - {v.transaction_date}")
        print(f"      Propiedad: {v.property.address}")
        if v.grantor:
            print(f"      Vendedor: {v.grantor.name} {v.grantor.surname}")
        if v.grantee:
            print(f"      Comprador: {v.grantee.name} {v.grantee.surname}")
        print()


def inheritances():
    """Lista todas las herencias"""
    herencias = Transaction.query.filter_by(transaction_type='Herencia').all()
    print(f"\n🏛️ HERENCIAS ({len(herencias)} total):\n")
    for h in herencias:
        print(f"  [{h.id}] €{h.transaction_value:,.2f} - {h.transaction_date}")
        print(f"      Propiedad: {h.property.address}")
        if h.decedent:
            print(f"      Causante: {h.decedent.name} {h.decedent.surname}")
        if h.heir:
            print(f"      Heredero: {h.heir.name} {h.heir.surname}")
        print()


def transactions_this_year():
    """Muestra transacciones del año actual"""
    year = datetime.now().year
    trans = Transaction.query.filter(
        Transaction.transaction_date >= f'{year}-01-01'
    ).all()
    
    print(f"\n📅 TRANSACCIONES DE {year} ({len(trans)} total):\n")
    for t in trans:
        tipo_emoji = "🏪" if t.transaction_type == 'Venta' else "🏛️"
        print(f"  {tipo_emoji} [{t.id}] {t.transaction_type} - €{t.transaction_value:,.2f}")
        print(f"      Fecha: {t.transaction_date}\n")
    
    if trans:
        total_value = sum(t.transaction_value for t in trans)
        print(f"💰 Valor total: €{total_value:,.2f}")
    print()
    return trans


def property_transactions(property_id):
    """Muestra todas las transacciones de una propiedad"""
    prop = Property.query.get(property_id)
    if not prop:
        print(f"❌ No existe propiedad con ID {property_id}")
        return
    
    print(f"\n🏠 TRANSACCIONES DE: {prop.address}")
    print(f"📍 Referencia: {prop.cadastral_reference}\n")
    
    if prop.transactions:
        for t in sorted(prop.transactions, key=lambda x: x.transaction_date):
            tipo_emoji = "🏪" if t.transaction_type == 'Venta' else "🏛️"
            print(f"  {tipo_emoji} {t.transaction_type}")
            print(f"      Fecha: {t.transaction_date}")
            print(f"      Valor: €{t.transaction_value:,.2f}\n")
    else:
        print("  ℹ️  No hay transacciones registradas para esta propiedad\n")


# ==============================================================================
# 🔍 FUNCIONES DE BÚSQUEDA AVANZADA
# ==============================================================================

def search_all(term):
    """Busca un término en usuarios, personas y propiedades"""
    print(f"\n🔍 BÚSQUEDA GLOBAL: '{term}'\n")
    print("="*60)
    
    # Buscar en usuarios
    users = User.query.filter(User.username.like(f'%{term}%')).all()
    if users:
        print(f"\n👥 USUARIOS ({len(users)}):")
        for u in users:
            print(f"  • {u.username}")
    
    # Buscar en personas
    people = People.query.filter(
        (People.name.like(f'%{term}%')) |
        (People.surname.like(f'%{term}%')) |
        (People.nif.like(f'%{term}%'))
    ).all()
    if people:
        print(f"\n👤 PERSONAS ({len(people)}):")
        for p in people:
            print(f"  • {p.name} {p.surname} - {p.nif}")
    
    # Buscar en propiedades
    props = Property.query.filter(
        (Property.address.like(f'%{term}%')) |
        (Property.cadastral_reference.like(f'%{term}%'))
    ).all()
    if props:
        print(f"\n🏠 PROPIEDADES ({len(props)}):")
        for p in props:
            print(f"  • {p.address}")
    
    if not users and not people and not props:
        print("\n❌ No se encontraron resultados")
    
    print("\n" + "="*60 + "\n")


# ==============================================================================
# 📋 FUNCIONES DE LISTADO
# ==============================================================================

def help():
    """Muestra todas las funciones disponibles"""
    print("""
╔════════════════════════════════════════════════════════════════╗
║         🐚 FUNCIONES DISPONIBLES EN SHELL HELPER              ║
╚════════════════════════════════════════════════════════════════╝

📊 ESTADÍSTICAS:
  stats()                    - Estadísticas completas
  quick_stats()              - Estadísticas en una línea

👥 USUARIOS:
  all_users()                - Lista todos los usuarios
  last_users(n)              - Últimos N usuarios
  admins()                   - Lista administradores
  find_user('nombre')        - Buscar usuario

👤 PERSONAS:
  all_people()               - Lista todas las personas
  last_people(n)             - Últimas N personas
  find_person('término')     - Buscar persona

🏠 PROPIEDADES:
  all_properties()           - Lista todas las propiedades
  last_properties(n)         - Últimas N propiedades
  find_property('término')   - Buscar propiedad
  expensive_properties(n)    - Top N más caras
  cheap_properties(n)        - Top N más baratas
  properties_by_value(min,max) - Buscar por rango de valor

💰 TRANSACCIONES:
  all_transactions()         - Lista todas las transacciones
  last_transactions(n)       - Últimas N transacciones
  sales()                    - Solo ventas
  inheritances()             - Solo herencias
  transactions_this_year()   - Transacciones del año actual
  property_transactions(id)  - Transacciones de una propiedad

🔍 BÚSQUEDA:
  search_all('término')      - Busca en todas las tablas

❓ AYUDA:
  help()                     - Muestra este mensaje

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 TIP: Puedes combinar con consultas directas de SQLAlchemy
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)


# ==============================================================================
# 🎯 MENSAJE DE INICIO
# ==============================================================================

print("\n" + "="*70)
print("✅ Shell Helper cargado correctamente!")
print("="*70)
print("\n💡 Escribe 'help()' para ver todas las funciones disponibles")
print("💡 Escribe 'stats()' para ver estadísticas generales")
print("💡 Escribe 'quick_stats()' para un resumen rápido\n")

