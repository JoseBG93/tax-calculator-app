#!/usr/bin/env python
"""
Secure superadmin bootstrap/maintenance for Tax Calculator Pro.

Features:
- Detect configured superadmin by ID (preferred) or username from app config
- Create superadmin if missing
- Interactively change superadmin username and/or password (with validation)
- Ensure superadmin has is_admin/is_active = True

Usage:
    export SECRET_KEY=...            # required for app to load
    # optional but recommended for stability across username changes:
    # export SUPERADMIN_USER_ID="1"
    # or fallback:
    # export SUPERADMIN_USERNAME="jose"
    python create_admin.py
"""

import sys
import getpass
from typing import Optional

from app import create_app, db
from app.models import User
from app.security_validations import (
    validate_and_sanitize_username,
    validate_password,
)


def _prompt_yes_no(message: str) -> bool:
    while True:
        resp = input(f"{message} (s/n): ").strip().lower()
        if resp in ("s", "si", "sí", "y", "yes"):  # support ES + EN
            return True
        if resp in ("n", "no"):  # negative
            return False
        print("↩️  Answer with 's' or 'n'.")


def _prompt_new_username(current_username: str) -> Optional[str]:
    raw = input(
        f"  New username (leave empty to keep '{current_username}'): "
    ).strip()
    if not raw:
        return None
    ok, sanitized, msg = validate_and_sanitize_username(raw)
    if not ok:
        print(f"❌ Username inválido: {msg}")
        return None
    return sanitized


def _prompt_new_password() -> Optional[str]:
    pwd = getpass.getpass("Nueva contraseña (dejar vacío para no cambiar): ")
    if not pwd:
        return None
    ok, msg = validate_password(pwd)
    if not ok:
        print(f"❌ {msg}")
        return None
    confirm = getpass.getpass("Confirmar nueva contraseña: ")
    if pwd != confirm:
        print("❌ Las contraseñas no coinciden")
        return None
    return pwd


def _find_superadmin(app) -> Optional[User]:
    """Find superadmin by configured ID (preferred) or username."""
    user_id = app.config.get("SUPERADMIN_USER_ID")
    username = app.config.get("SUPERADMIN_USERNAME")
    if user_id:
        try:
            user = User.query.get(int(user_id))
            if user:
                return user
        except Exception:
            pass
    if username:
        return User.query.filter_by(username=username).first()
    return None


def create_or_update_superadmin():
    app = create_app()
    with app.app_context():
        user = _find_superadmin(app)

        if user is None:
            print("ℹ️  No existe superadmin según configuración.")
            # Offer to create
            if not _prompt_yes_no("¿Quieres crear el superadministrador ahora?"):
                print("⏹️  Operación cancelada.")
                return

            # Suggest configured username as default
            suggested_username = app.config.get("SUPERADMIN_USERNAME", "admin")
            entered = input(
                f"Nombre de usuario superadmin (Enter para '{suggested_username}'): "
            ).strip()
            new_username = entered or suggested_username
            ok, sanitized, msg = validate_and_sanitize_username(new_username)
            if not ok:
                print(f"❌ Username inválido: {msg}")
                return
            if User.query.filter_by(username=sanitized).first():
                print("❌ Ese nombre de usuario ya existe.")
                return

            new_password = None
            while new_password is None:
                new_password = _prompt_new_password()

            user = User(username=sanitized)
            user.set_password(new_password)
            user.is_admin = True
            user.is_active = True
            try:
                db.session.add(user)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(f"❌ Error creando superadmin: {e}")
                return

            print("✅ Superadmin creado correctamente.")
            print("👉 Recomendado: exporta SUPERADMIN_USER_ID con tu ID para mayor seguridad.")
            print("   Ejemplo: export SUPERADMIN_USER_ID=\"%s\"" % user.id)
            return

        # If we are here, superadmin exists
        print(
            f"Encontrado superadmin: id={user.id}, username='{user.username}', is_admin={user.is_admin}, is_active={user.is_active}"
        )

        # Ensure flags
        changed_flags = False
        if not user.is_admin:
            user.is_admin = True
            changed_flags = True
        if not user.is_active:
            user.is_active = True
            changed_flags = True
        if changed_flags:
            try:
                db.session.commit()
                print("🔒 Flags de superadmin asegurados (is_admin/is_active).")
            except Exception as e:
                db.session.rollback()
                print(f"❌ Error actualizando flags: {e}")
                return

        # Offer changes
        if _prompt_yes_no("¿Quieres cambiar el nombre de usuario del superadmin?"):
            new_un = _prompt_new_username(user.username)
            if new_un:
                if User.query.filter_by(username=new_un).first() and new_un != user.username:
                    print("❌ Username ya en uso.")
                else:
                    user.username = new_un
                    try:
                        db.session.commit()
                        print("✅ Username actualizado.")
                    except Exception as e:
                        db.session.rollback()
                        print(f"❌ Error actualizando username: {e}")
                        return
                    # Warn if relying on username-based superadmin
                    if not app.config.get("SUPERADMIN_USER_ID"):
                        print("⚠️  Estás usando SUPERADMIN_USERNAME. Actualiza la variable de entorno")
                        print("    para coincidir con el nuevo nombre o define SUPERADMIN_USER_ID.")

        if _prompt_yes_no("¿Quieres cambiar la contraseña del superadmin?"):
            # Ask for current password for verification
            current_pwd = getpass.getpass("Introduce la contraseña actual: ")
            if not user.check_password(current_pwd):
                print("❌ La contraseña actual no es correcta.")
                return
            new_pwd = None
            while new_pwd is None:
                new_pwd = _prompt_new_password()
            user.set_password(new_pwd)
            try:
                db.session.commit()
                print("✅ Contraseña actualizada.")
            except Exception as e:
                db.session.rollback()
                print(f"❌ Error actualizando contraseña: {e}")
                return

        print("🎯 Operación completada.")


if __name__ == '__main__':
    try:
        create_or_update_superadmin()
    except RuntimeError as e:
        # Common cause: missing SECRET_KEY in environment
        print(f"❌ Error al iniciar la app: {e}")
        print("💡 Asegúrate de exportar SECRET_KEY antes de ejecutar este script.")
        sys.exit(1)