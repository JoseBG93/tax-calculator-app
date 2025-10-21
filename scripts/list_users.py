#!/usr/bin/env python
"""
SCRIPT PARA LISTAR USUARIOS
============================

Este script muestra TODOS los usuarios registrados en el sistema,
incluyendo cuáles son administradores.

USO:
    python list_users.py

IMPORTANTE:
- Puedes ver los NOMBRES DE USUARIO
- NO puedes ver las contraseñas (están hasheadas por seguridad)
- Si olvidaste tu contraseña, usa change_password.py para cambiarla

FECHA: 5 de octubre de 2025
"""

from app import create_app, db
from app.models import User
from datetime import datetime

def list_all_users():
    """
    Lista todos los usuarios del sistema con su información básica.
    """
    
    print("\n" + "="*70)
    print("👥 LISTADO DE USUARIOS - Tax Calculator Pro")
    print("="*70 + "\n")
    
    # Crear contexto de aplicación
    app = create_app()
    
    with app.app_context():
        # Obtener TODOS los usuarios ordenados por fecha de creación
        users = User.query.order_by(User.created_at.desc()).all()
        
        if not users:
            print("⚠️  No hay usuarios registrados en el sistema.")
            return
        
        print(f"📊 Total de usuarios: {len(users)}\n")
        
        # Contadores
        admin_count = sum(1 for u in users if u.is_admin)
        active_count = sum(1 for u in users if u.is_active)
        
        print(f"   🔑 Administradores: {admin_count}")
        print(f"   ✅ Cuentas activas: {active_count}")
        print(f"   ❌ Cuentas inactivas: {len(users) - active_count}")
        print("\n" + "-"*70 + "\n")
        
        # Listar cada usuario
        for idx, user in enumerate(users, 1):
            # Badges
            admin_badge = "🔑 ADMIN" if user.is_admin else "👤 USER"
            status_badge = "✅ Activo" if user.is_active else "❌ Inactivo"
            
            print(f"{idx}. {user.username}")
            print(f"   ID: {user.id}")
            print(f"   Rol: {admin_badge}")
            print(f"   Estado: {status_badge}")
            print(f"   Creado: {user.created_at.strftime('%d/%m/%Y %H:%M')}")
            
            if user.last_login:
                print(f"   Último login: {user.last_login.strftime('%d/%m/%Y %H:%M')}")
                print(f"   Logins totales: {user.login_count}")
            else:
                print(f"   Último login: Nunca")
            
            print()
        
        print("-"*70)
        print("\n💡 RECORDATORIOS:")
        print("   • Las CONTRASEÑAS están encriptadas y NO se pueden ver")
        print("   • Si olvidaste tu contraseña, usa: python change_password.py")
        print("   • Para gestionar admin, usa: python create_admin.py")
        print("\n")

if __name__ == "__main__":
    try:
        list_all_users()
    except KeyboardInterrupt:
        print("\n\n⚠️  Script interrumpido.")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        print("\n💡 Asegúrate de que:")
        print("   1. La base de datos existe (instance/app.db)")
        print("   2. La variable SECRET_KEY está configurada")
