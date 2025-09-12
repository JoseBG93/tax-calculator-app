#!/usr/bin/env python3
import os
import subprocess
from anthropic import Anthropic

def get_changed_files():
    """Obtiene los archivos modificados en el commit/PR"""
    try:
        result = subprocess.run(
            ['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip().split('\n') if result.stdout.strip() else []
    except subprocess.CalledProcessError:
        return []

def main():
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ ANTHROPIC_API_KEY no encontrada")
        return
    
    client = Anthropic(api_key=api_key)
    changed_files = get_changed_files()
    
    if not changed_files:
        print("✅ No hay archivos modificados para revisar")
        return
    
    print(f"📋 Revisando {len(changed_files)} archivos modificados...")
    
    for file_path in changed_files:
        if os.path.exists(file_path) and file_path.endswith(('.py', '.js', '.yml', '.yaml')):
            print(f"🔍 Analizando: {file_path}")
            # Aquí podrías implementar la lógica de revisión específica

if __name__ == "__main__":
    main()