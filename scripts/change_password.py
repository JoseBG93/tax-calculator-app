"""
SCRIPT DE CAMBIO DE CONTRASEÑA
===============================

Este script te permite cambiar la contraseña de cualquier usuario de forma segura.

USO:
    python change_password.py

FECHA: 2 de octubre de 2025
"""

from app import create_app, db
from app.models import User
import getpass

def change_user_password():
    """
    Cambia la contraseña de un usuario de forma interactiva.
    
    PROCESO:
    1. Solicita el nombre de usuario
    2. Busca el usuario en la base de datos
    3. Solicita la nueva contraseña (sin mostrarla en pantalla)
    4. Confirma la nueva contraseña
    5. Actualiza la contraseña en la base de datos
    """
    
    print("\n" + "="*60)
    print("🔐 CAMBIO DE CONTRASEÑA - Tax Calculator Pro")
    print("="*60 + "\n")
    
    # Solicitar nombre de usuario
    username = input("Nombre de usuario: ").strip()
    
    if not username:
        print("❌ Error: Debes proporcionar un nombre de usuario.")
        return
    
    # Crear contexto de aplicación
    app = create_app()
    
    with app.app_context():
        # Buscar usuario
        user = User.query.filter_by(username=username).first()
        
        if not user:
            print(f"\n❌ Error: Usuario '{username}' no encontrado en la base de datos.")
            print("\n💡 Usuarios disponibles:")
            all_users = User.query.all()
            for u in all_users:
                admin_badge = "🔑 [ADMIN]" if u.is_admin else ""
                print(f"   - {u.username} {admin_badge}")
            return
        
        # Mostrar información del usuario
        print(f"\n✅ Usuario encontrado: {user.username}")
        print(f"   Es administrador: {'Sí' if user.is_admin else 'No'}")
        print(f"   Cuenta activa: {'Sí' if user.is_active else 'No'}")
        
        # Solicitar nueva contraseña (sin mostrarla en pantalla)
        print("\n📝 Introduce la nueva contraseña:")
        print("   (Los caracteres NO se mostrarán por seguridad)")
        
        try:
            new_password = getpass.getpass("Nueva contraseña: ")
            confirm_password = getpass.getpass("Confirma contraseña: ")
        except KeyboardInterrupt:
            print("\n\n⚠️ Operación cancelada por el usuario.")
            return
        
        # Verificar que las contraseñas coincidan
        if new_password != confirm_password:
            print("\n❌ Error: Las contraseñas no coinciden.")
            return
        
        # Verificar longitud mínima
        if len(new_password) < 4:
            print("\n❌ Error: La contraseña debe tener al menos 4 caracteres.")
            return
        
        # Cambiar la contraseña
        user.set_password(new_password)
        
        # Guardar en la base de datos
        try:
            db.session.commit()
            print("\n" + "="*60)
            print("✅ ¡CONTRASEÑA CAMBIADA EXITOSAMENTE!")
            print("="*60)
            print(f"\n👤 Usuario: {user.username}")
            print(f"🔐 Nueva contraseña: {'*' * len(new_password)} ({len(new_password)} caracteres)")
            print(f"\n💡 Ahora puedes iniciar sesión en:")
            print(f"   http://localhost:5000/login")
            print(f"   Username: {user.username}")
            print(f"   Password: (tu nueva contraseña)")
            
            if user.is_admin:
                print(f"\n🏛️ Como administrador, también puedes acceder a:")
                print(f"   http://localhost:5000/admin")
            
        except Exception as e:
            db.session.rollback()
            print(f"\n❌ Error al guardar en la base de datos: {e}")
            return

if __name__ == "__main__":
    try:
        change_user_password()
    except KeyboardInterrupt:
        print("\n\n⚠️ Script interrumpido.")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")

