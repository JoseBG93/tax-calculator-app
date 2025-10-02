#!/usr/bin/env python3
"""
MÓDULO EXTERNO: pillow (PIL)
============================

¿QUÉ ES?
Pillow es la librería estándar de Python para procesamiento de imágenes.
Es un fork mejorado de PIL (Python Imaging Library).

INSTALACIÓN:
pip install pillow

¿PARA QUÉ SIRVE?
- Abrir, manipular y guardar imágenes
- Redimensionar y recortar imágenes
- Aplicar filtros y efectos
- Conversión entre formatos
- Dibujar sobre imágenes
- Extraer metadatos

IMPORTANCIA: ⭐⭐⭐⭐⭐ (Esencial para imágenes)
"""

def verificar_instalacion():
    """Verificar si pillow está instalado"""
    try:
        from PIL import Image
        print("✅ Módulo 'pillow' instalado correctamente")
        print(f"📦 Versión de PIL: {Image.__version__}")
        return True
    except ImportError:
        print("❌ Módulo 'pillow' no encontrado")
        print("💡 Para instalar: pip install pillow")
        return False

def ejemplo_pillow_basico():
    """Ejemplo básico de uso de pillow"""
    
    print("=" * 50)
    print("🖼️ MÓDULO PILLOW - PROCESAMIENTO DE IMÁGENES")
    print("=" * 50)
    
    if not verificar_instalacion():
        return
    
    print("\n📝 Ejemplo básico de Pillow:")
    print("""
from PIL import Image, ImageDraw, ImageFont
import os

# Crear imagen simple
img = Image.new('RGB', (300, 200), color='lightblue')
img.save('imagen_simple.png')

# Abrir imagen existente
try:
    img = Image.open('imagen_simple.png')
    print(f"Formato: {img.format}")
    print(f"Tamaño: {img.size}")
    print(f"Modo: {img.mode}")
except FileNotFoundError:
    print("Imagen no encontrada")

# Redimensionar imagen
img_redimensionada = img.resize((150, 100))
img_redimensionada.save('imagen_pequena.png')

# Convertir formato
img.save('imagen_convertida.jpg', 'JPEG')
    """)
    
    from PIL import Image, ImageDraw
    
    # Crear imagen de ejemplo
    img = Image.new('RGB', (200, 100), color='lightgreen')
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), "¡Hola Pillow!", fill='black')
    img.save('ejemplo_pillow.png')
    
    print("\n✅ Imagen de ejemplo creada: ejemplo_pillow.png")
    print("   • Tamaño: 200x100 pixels")
    print("   • Color de fondo: verde claro")
    print("   • Texto: '¡Hola Pillow!'")
    
    # Limpiar archivo temporal
    if os.path.exists('ejemplo_pillow.png'):
        os.remove('ejemplo_pillow.png')

def ejemplo_pillow_manipulacion():
    """Ejemplo de manipulación de imágenes"""
    
    print("\n" + "=" * 50)
    print("🎨 MANIPULACIÓN DE IMÁGENES")
    print("=" * 50)
    
    print("📝 Operaciones comunes:")
    print("""
from PIL import Image, ImageFilter, ImageEnhance

# Crear imagen base
img = Image.new('RGB', (400, 300), color='white')

# Aplicar filtros
img_blur = img.filter(ImageFilter.BLUR)
img_sharpen = img.filter(ImageFilter.SHARPEN)
img_edge = img.filter(ImageFilter.FIND_EDGES)

# Ajustar brillo y contraste
enhancer = ImageEnhance.Brightness(img)
img_bright = enhancer.enhance(1.5)  # 50% más brillante

enhancer = ImageEnhance.Contrast(img)
img_contrast = enhancer.enhance(2.0)  # Doble contraste

# Rotar imagen
img_rotated = img.rotate(45, expand=True)

# Recortar imagen
box = (50, 50, 200, 150)  # (left, top, right, bottom)
img_cropped = img.crop(box)

# Voltear imagen
img_flipped_h = img.transpose(Image.FLIP_LEFT_RIGHT)
img_flipped_v = img.transpose(Image.FLIP_TOP_BOTTOM)
    """)
    
    print("\n✅ Operaciones disponibles:")
    print("   • Filtros: BLUR, SHARPEN, EDGE_ENHANCE")
    print("   • Mejoras: Brillo, Contraste, Color")
    print("   • Transformaciones: Rotar, Voltear, Recortar")
    print("   • Redimensionamiento: resize(), thumbnail()")

def ejemplo_pillow_dibujo():
    """Ejemplo de dibujo sobre imágenes"""
    
    print("\n" + "=" * 50)
    print("✏️ DIBUJAR SOBRE IMÁGENES")
    print("=" * 50)
    
    print("📝 Crear gráficos simples:")
    print("""
from PIL import Image, ImageDraw, ImageFont

# Crear lienzo
img = Image.new('RGB', (400, 300), color='white')
draw = ImageDraw.Draw(img)

# Dibujar formas
draw.rectangle([50, 50, 150, 100], fill='red', outline='black')
draw.ellipse([200, 50, 300, 150], fill='blue', outline='navy')
draw.line([50, 200, 350, 200], fill='green', width=3)

# Dibujar texto
draw.text((50, 250), "Hola Pillow!", fill='black')

# Intentar usar fuente personalizada
try:
    font = ImageFont.truetype('arial.ttf', 20)
    draw.text((200, 250), "¡Con fuente!", fill='purple', font=font)
except OSError:
    draw.text((200, 250), "¡Sin fuente!", fill='purple')

img.save('dibujo_ejemplo.png')
    """)
    
    print("\n✅ Funciones de dibujo:")
    print("   • rectangle(): Rectángulos")
    print("   • ellipse(): Círculos y elipses")
    print("   • line(): Líneas")
    print("   • text(): Texto")
    print("   • polygon(): Polígonos")
    print("   • arc(): Arcos")

def ejemplo_pillow_metadatos():
    """Ejemplo de trabajo con metadatos"""
    
    print("\n" + "=" * 50)
    print("📊 METADATOS DE IMÁGENES")
    print("=" * 50)
    
    print("📝 Extraer información:")
    print("""
from PIL import Image
from PIL.ExifTags import TAGS

# Crear imagen con información
img = Image.new('RGB', (200, 100), color='yellow')
img.save('test_meta.jpg', 'JPEG', quality=95)

# Abrir y analizar
img = Image.open('test_meta.jpg')

print(f"Archivo: test_meta.jpg")
print(f"Formato: {img.format}")
print(f"Tamaño: {img.size}")
print(f"Modo: {img.mode}")

# Obtener EXIF data (si existe)
exif_data = img._getexif()
if exif_data:
    for tag_id, value in exif_data.items():
        tag = TAGS.get(tag_id, tag_id)
        print(f"{tag}: {value}")
else:
    print("No hay datos EXIF")

# Información del archivo
import os
file_size = os.path.getsize('test_meta.jpg')
print(f"Tamaño archivo: {file_size} bytes")
    """)
    
    print("\n✅ Información disponible:")
    print("   • Formato de archivo")
    print("   • Dimensiones (ancho x alto)")
    print("   • Modo de color (RGB, RGBA, L, etc.)")
    print("   • Datos EXIF (cámara, fecha, etc.)")
    print("   • Tamaño de archivo")

def integracion_con_tax_calculator_pro():
    """Ejemplo de integración con proyecto tax-calculator-pro"""
    
    print("\n" + "=" * 50)
    print("🗂️ INTEGRACIÓN CON NOTESASSISTANT")
    print("=" * 50)
    
    print("💡 Posibles usos en tu proyecto:")
    
    print("\n📝 1. Generar miniaturas para attachments:")
    print("""
def create_thumbnail(image_path, size=(100, 100)):
    '''Crear miniatura de imagen'''
    try:
        with Image.open(image_path) as img:
            img.thumbnail(size)
            thumbnail_path = f"{image_path}_thumb.jpg"
            img.save(thumbnail_path, 'JPEG')
            return thumbnail_path
    except Exception as e:
        print(f"Error creando miniatura: {e}")
        return None
    """)
    
    print("\n📝 2. Generar avatares para usuarios:")
    print("""
def create_avatar(initials, size=(64, 64), bg_color='lightblue'):
    '''Crear avatar con iniciales'''
    img = Image.new('RGB', size, color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Calcular posición centrada del texto
    text_width = draw.textsize(initials)[0]
    text_height = draw.textsize(initials)[1]
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    
    draw.text((x, y), initials, fill='white')
    return img
    """)
    
    print("\n📝 3. Procesar imágenes en notas:")
    print("""
def process_note_image(image_path):
    '''Procesar imagen adjunta a nota'''
    try:
        with Image.open(image_path) as img:
            # Redimensionar si es muy grande
            if img.size[0] > 800 or img.size[1] > 600:
                img.thumbnail((800, 600))
            
            # Convertir a RGB si es necesario
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Guardar versión optimizada
            optimized_path = f"{image_path}_optimized.jpg"
            img.save(optimized_path, 'JPEG', quality=85)
            
            return optimized_path
    except Exception as e:
        print(f"Error procesando imagen: {e}")
        return None
    """)
    
    print("\n📝 4. Crear reportes visuales:")
    print("""
def create_note_stats_chart(stats_data):
    '''Crear gráfico simple de estadísticas'''
    img = Image.new('RGB', (400, 300), color='white')
    draw = ImageDraw.Draw(img)
    
    # Título
    draw.text((150, 20), "Estadísticas de Notas", fill='black')
    
    # Datos de ejemplo
    y_pos = 60
    for category, count in stats_data.items():
        draw.text((50, y_pos), f"{category}: {count}", fill='blue')
        y_pos += 30
    
    return img
    """)
    
    print("\n🎯 Casos de uso:")
    print("   • Procesar imágenes adjuntas")
    print("   • Crear miniaturas automáticas")
    print("   • Generar avatares de usuario")
    print("   • Optimizar imágenes para web")
    print("   • Crear reportes visuales")
    print("   • Aplicar marca de agua")

def casos_uso_comunes():
    """Casos de uso más comunes de pillow"""
    
    print("\n" + "=" * 50)
    print("🎯 CASOS DE USO COMUNES")
    print("=" * 50)
    
    print("1. Abrir y guardar imagen:")
    print("   img = Image.open('foto.jpg')")
    print("   img.save('nueva_foto.png')")
    
    print("\n2. Redimensionar:")
    print("   img = img.resize((200, 200))")
    print("   img.thumbnail((100, 100))  # Mantiene proporción")
    
    print("\n3. Aplicar filtros:")
    print("   img = img.filter(ImageFilter.BLUR)")
    print("   img = img.filter(ImageFilter.SHARPEN)")
    
    print("\n4. Rotar y voltear:")
    print("   img = img.rotate(90)")
    print("   img = img.transpose(Image.FLIP_LEFT_RIGHT)")
    
    print("\n5. Dibujar texto:")
    print("   draw = ImageDraw.Draw(img)")
    print("   draw.text((10, 10), 'Hola', fill='black')")
    
    print("\n6. Crear imagen nueva:")
    print("   img = Image.new('RGB', (300, 200), color='red')")

if __name__ == "__main__":
    # Ejecutar todos los ejemplos
    ejemplo_pillow_basico()
    ejemplo_pillow_manipulacion()
    ejemplo_pillow_dibujo()
    ejemplo_pillow_metadatos()
    casos_uso_comunes()
    integracion_con_tax_calculator_pro()
    
    print("\n" + "=" * 50)
    print("✅ RESUMEN DEL MÓDULO pillow")
    print("=" * 50)
    print("🔧 Usos principales:")
    print("   • Abrir, manipular y guardar imágenes")
    print("   • Redimensionar y recortar")
    print("   • Aplicar filtros y efectos")
    print("   • Dibujar sobre imágenes")
    print("   • Convertir entre formatos")
    print("   • Extraer metadatos")
    print("\n📚 Documentación oficial:")
    print("   https://pillow.readthedocs.io/")
    print("\n💡 Consejo: Pillow es la librería estándar")
    print("   para imágenes en Python.") 