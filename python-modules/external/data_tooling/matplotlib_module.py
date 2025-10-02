#!/usr/bin/env python3
"""
MÓDULO EXTERNO: matplotlib
==========================

¿QUÉ ES?
Matplotlib es la librería fundamental para visualización de datos en Python.
Permite crear gráficos estáticos, animados e interactivos de alta calidad.

INSTALACIÓN:
pip install matplotlib

¿PARA QUÉ SIRVE?
- Crear gráficos de líneas, barras, scatter
- Histogramas y distribuciones
- Subplots y figuras complejas
- Personalización completa de gráficos
- Guardar gráficos en múltiples formatos
- Base para otras librerías de visualización

IMPORTANCIA: ⭐⭐⭐⭐⭐ (Esencial para visualización)
"""

def verificar_instalacion():
    """Verificar si matplotlib está instalado"""
    try:
        import matplotlib
        import matplotlib.pyplot as plt
        print("✅ Módulo 'matplotlib' instalado correctamente")
        print(f"📦 Versión: {matplotlib.__version__}")
        return True
    except ImportError:
        print("❌ Módulo 'matplotlib' no encontrado")
        print("💡 Para instalar: pip install matplotlib")
        return False

def ejemplo_matplotlib_basico():
    """Ejemplo básico de matplotlib"""
    
    print("=" * 50)
    print("📈 MÓDULO MATPLOTLIB - VISUALIZACIÓN")
    print("=" * 50)
    
    if not verificar_instalacion():
        return
    
    import matplotlib.pyplot as plt
    import numpy as np
    
    print("\n📝 Ejemplo básico de matplotlib:")
    print("""
import matplotlib.pyplot as plt
import numpy as np

# Datos para el gráfico
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crear gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title('Función Seno')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
    """)
    
    # Crear datos de ejemplo
    x = np.linspace(0, 10, 50)
    y = np.sin(x)
    
    # Crear gráfico (sin mostrar para no interrumpir el script)
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')
    plt.title('Función Seno', fontsize=14)
    plt.xlabel('X', fontsize=12)
    plt.ylabel('Y', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Guardar gráfico en lugar de mostrarlo
    plt.savefig('ejemplo_seno.png', dpi=150, bbox_inches='tight')
    plt.close()  # Cerrar para liberar memoria
    
    print("\n✅ Gráfico creado y guardado como 'ejemplo_seno.png'")
    print("   • Función seno con estilo personalizado")
    print("   • Grid semi-transparente")
    print("   • Labels y título")
    print("   • Leyenda incluida")

def ejemplo_matplotlib_tipos_graficos():
    """Ejemplo de diferentes tipos de gráficos"""
    
    print("\n" + "=" * 50)
    print("📊 TIPOS DE GRÁFICOS")
    print("=" * 50)
    
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Datos de ejemplo
    np.random.seed(42)
    
    # 1. GRÁFICO DE LÍNEAS
    print("\n1️⃣ GRÁFICO DE LÍNEAS:")
    
    x = np.linspace(0, 10, 20)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, 'o-', label='sin(x)', color='blue', linewidth=2)
    plt.plot(x, y2, 's--', label='cos(x)', color='red', linewidth=2)
    plt.title('Funciones Trigonométricas')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('lineas.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print("   ✅ Gráfico de líneas creado: lineas.png")
    
    # 2. GRÁFICO DE BARRAS
    print("\n2️⃣ GRÁFICO DE BARRAS:")
    
    categorias = ['Python', 'JavaScript', 'Java', 'C++', 'Go']
    valores = [45, 30, 25, 15, 10]
    colores = ['#3776ab', '#f7df1e', '#ed8b00', '#00599c', '#00add8']
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(categorias, valores, color=colores, alpha=0.8)
    plt.title('Popularidad de Lenguajes de Programación', fontsize=14)
    plt.xlabel('Lenguajes')
    plt.ylabel('Popularidad (%)')
    plt.xticks(rotation=45)
    
    # Agregar valores encima de las barras
    for bar, valor in zip(bars, valores):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{valor}%', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('barras.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print("   ✅ Gráfico de barras creado: barras.png")
    
    # 3. SCATTER PLOT
    print("\n3️⃣ SCATTER PLOT:")
    
    x = np.random.normal(50, 15, 100)
    y = np.random.normal(50, 15, 100)
    colores = np.random.rand(100)
    tamaños = np.random.randint(20, 200, 100)
    
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(x, y, c=colores, s=tamaños, alpha=0.6, cmap='viridis')
    plt.title('Scatter Plot con Colores y Tamaños Variables')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.colorbar(scatter, label='Color Scale')
    plt.grid(True, alpha=0.3)
    plt.savefig('scatter.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print("   ✅ Scatter plot creado: scatter.png")
    
    # 4. HISTOGRAMA
    print("\n4️⃣ HISTOGRAMA:")
    
    datos = np.random.normal(100, 15, 1000)
    
    plt.figure(figsize=(10, 6))
    n, bins, patches = plt.hist(datos, bins=30, alpha=0.7, color='skyblue', 
                               edgecolor='black', density=True)
    plt.title('Distribución Normal (μ=100, σ=15)')
    plt.xlabel('Valores')
    plt.ylabel('Densidad')
    plt.grid(True, alpha=0.3)
    
    # Agregar línea de distribución teórica
    x_teorico = np.linspace(datos.min(), datos.max(), 100)
    y_teorico = (1/(15*np.sqrt(2*np.pi))) * np.exp(-0.5*((x_teorico-100)/15)**2)
    plt.plot(x_teorico, y_teorico, 'r-', linewidth=2, label='Distribución teórica')
    plt.legend()
    
    plt.savefig('histograma.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print("   ✅ Histograma creado: histograma.png")

def ejemplo_matplotlib_subplots():
    """Ejemplo de subplots (múltiples gráficos)"""
    
    print("\n" + "=" * 50)
    print("🔲 SUBPLOTS - MÚLTIPLES GRÁFICOS")
    print("=" * 50)
    
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Datos
    x = np.linspace(0, 10, 100)
    
    # 1. SUBPLOTS BÁSICOS
    print("\n1️⃣ SUBPLOTS 2x2:")
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Dashboard de Funciones Matemáticas', fontsize=16)
    
    # Subplot 1: Seno
    axes[0, 0].plot(x, np.sin(x), 'b-')
    axes[0, 0].set_title('sin(x)')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Subplot 2: Coseno
    axes[0, 1].plot(x, np.cos(x), 'r-')
    axes[0, 1].set_title('cos(x)')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Subplot 3: Tangente
    y_tan = np.tan(x)
    y_tan[np.abs(y_tan) > 10] = np.nan  # Limitar valores extremos
    axes[1, 0].plot(x, y_tan, 'g-')
    axes[1, 0].set_title('tan(x)')
    axes[1, 0].set_ylim(-5, 5)
    axes[1, 0].grid(True, alpha=0.3)
    
    # Subplot 4: Exponencial
    axes[1, 1].plot(x, np.exp(x/5), 'm-')
    axes[1, 1].set_title('exp(x/5)')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('subplots.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print("   ✅ Subplots creados: subplots.png")
    
    # 2. SUBPLOTS CON DIFERENTES TAMAÑOS
    print("\n2️⃣ SUBPLOTS CON GRIDSPEC:")
    
    from matplotlib.gridspec import GridSpec
    
    fig = plt.figure(figsize=(12, 8))
    gs = GridSpec(3, 3, figure=fig)
    
    # Gráfico principal (ocupa 2x2)
    ax_main = fig.add_subplot(gs[0:2, 0:2])
    ax_main.plot(x, np.sin(x) + np.cos(x), 'purple', linewidth=3)
    ax_main.set_title('Gráfico Principal: sin(x) + cos(x)', fontsize=14)
    ax_main.grid(True, alpha=0.3)
    
    # Gráfico lateral derecho
    ax_right = fig.add_subplot(gs[0:2, 2])
    ax_right.hist(np.random.normal(0, 1, 1000), bins=20, orientation='horizontal', 
                  alpha=0.7, color='orange')
    ax_right.set_title('Histograma\nVertical')
    
    # Gráfico inferior
    ax_bottom = fig.add_subplot(gs[2, 0:2])
    ax_bottom.bar(['A', 'B', 'C', 'D'], [3, 7, 2, 5], color=['red', 'blue', 'green', 'orange'])
    ax_bottom.set_title('Gráfico de Barras')
    
    # Gráfico esquina
    ax_corner = fig.add_subplot(gs[2, 2])
    ax_corner.pie([30, 25, 25, 20], labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%')
    ax_corner.set_title('Pie Chart')
    
    plt.tight_layout()
    plt.savefig('gridspec.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print("   ✅ GridSpec layout creado: gridspec.png")

def ejemplo_matplotlib_personalizacion():
    """Ejemplo de personalización avanzada"""
    
    print("\n" + "=" * 50)
    print("🎨 PERSONALIZACIÓN AVANZADA")
    print("=" * 50)
    
    import matplotlib.pyplot as plt
    import numpy as np
    
    # 1. ESTILOS PREDEFINIDOS
    print("\n1️⃣ ESTILOS PREDEFINIDOS:")
    
    estilos_disponibles = ['default', 'classic', 'seaborn-v0_8', 'ggplot', 'dark_background']
    print(f"   📋 Estilos disponibles: {plt.style.available[:5]}...")
    
    # Usar estilo ggplot
    plt.style.use('ggplot')
    
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x) * np.exp(-x/10)
    y2 = np.cos(x) * np.exp(-x/10)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label='sin(x)·e^(-x/10)', linewidth=2)
    plt.plot(x, y2, label='cos(x)·e^(-x/10)', linewidth=2)
    plt.title('Funciones con Decaimiento Exponencial', fontsize=16)
    plt.xlabel('X', fontsize=12)
    plt.ylabel('Y', fontsize=12)
    plt.legend(fontsize=12)
    plt.savefig('estilo_ggplot.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    # Resetear estilo
    plt.style.use('default')
    
    print("   ✅ Gráfico con estilo ggplot: estilo_ggplot.png")
    
    # 2. PERSONALIZACIÓN MANUAL
    print("\n2️⃣ PERSONALIZACIÓN MANUAL:")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Datos
    x = np.linspace(0, 4*np.pi, 100)
    y = np.sin(x)
    
    # Gráfico principal
    line = ax.plot(x, y, linewidth=3, color='#2E86C1', alpha=0.8)
    
    # Personalizar ejes
    ax.set_facecolor('#F8F9FA')  # Color de fondo
    ax.spines['top'].set_visible(False)     # Quitar borde superior
    ax.spines['right'].set_visible(False)   # Quitar borde derecho
    ax.spines['left'].set_color('#34495E')  # Color borde izquierdo
    ax.spines['bottom'].set_color('#34495E') # Color borde inferior
    
    # Personalizar grid
    ax.grid(True, linestyle='--', alpha=0.6, color='#BDC3C7')
    
    # Títulos y labels
    ax.set_title('Función Seno Personalizada', fontsize=18, fontweight='bold', 
                color='#2C3E50', pad=20)
    ax.set_xlabel('X', fontsize=14, fontweight='bold', color='#34495E')
    ax.set_ylabel('Y', fontsize=14, fontweight='bold', color='#34495E')
    
    # Personalizar ticks
    ax.tick_params(colors='#34495E', labelsize=12)
    
    # Agregar anotación
    ax.annotate('Máximo local', xy=(np.pi/2, 1), xytext=(2, 1.2),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=12, color='red', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('personalizado.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print("   ✅ Gráfico personalizado: personalizado.png")

def ejemplo_matplotlib_con_datos():
    """Ejemplo con datos realistas simulados"""
    
    print("\n" + "=" * 50)
    print("📊 VISUALIZACIÓN CON DATOS REALISTAS")
    print("=" * 50)
    
    import matplotlib.pyplot as plt
    import numpy as np
    from datetime import datetime, timedelta
    
    # 1. DATOS DE SERIES TEMPORALES
    print("\n1️⃣ SERIE TEMPORAL:")
    
    # Generar 30 días de datos
    fechas = [datetime.now() - timedelta(days=x) for x in range(30, 0, -1)]
    notas_por_dia = np.random.poisson(3, 30) + np.random.normal(0, 0.5, 30)
    notas_por_dia = np.maximum(notas_por_dia, 0)  # No valores negativos
    
    plt.figure(figsize=(12, 6))
    plt.plot(fechas, notas_por_dia, 'o-', linewidth=2, markersize=6, 
             color='#3498DB', markerfacecolor='#E74C3C')
    plt.title('Notas Creadas por Día (Últimos 30 días)', fontsize=14, fontweight='bold')
    plt.xlabel('Fecha')
    plt.ylabel('Número de Notas')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    # Agregar línea de tendencia
    x_num = range(len(fechas))
    z = np.polyfit(x_num, notas_por_dia, 1)
    p = np.poly1d(z)
    plt.plot(fechas, p(x_num), "--", alpha=0.8, color='red', 
             label=f'Tendencia (pendiente: {z[0]:.2f})')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('serie_temporal.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print("   ✅ Serie temporal creada: serie_temporal.png")
    
    # 2. ANÁLISIS DE CATEGORÍAS
    print("\n2️⃣ ANÁLISIS DE CATEGORÍAS:")
    
    categorias = ['Trabajo', 'Personal', 'Estudio', 'Ideas', 'Recordatorios']
    cantidades = [45, 32, 28, 15, 25]
    colores = ['#E74C3C', '#3498DB', '#2ECC71', '#F39C12', '#9B59B6']
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Gráfico de barras
    bars = ax1.bar(categorias, cantidades, color=colores, alpha=0.8)
    ax1.set_title('Notas por Categoría', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Cantidad de Notas')
    ax1.set_xlabel('Categorías')
    
    # Agregar valores en las barras
    for bar, cantidad in zip(bars, cantidades):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{cantidad}', ha='center', va='bottom', fontweight='bold')
    
    # Gráfico circular
    wedges, texts, autotexts = ax2.pie(cantidades, labels=categorias, colors=colores,
                                      autopct='%1.1f%%', startangle=90)
    ax2.set_title('Distribución por Categoría', fontsize=14, fontweight='bold')
    
    # Personalizar texto del pie chart
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    plt.tight_layout()
    plt.savefig('categorias.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print("   ✅ Análisis de categorías: categorias.png")

def integracion_con_tax_calculator_pro():
    """Ejemplo de integración con proyecto tax-calculator-pro"""
    
    print("\n" + "=" * 50)
    print("🗂️ INTEGRACIÓN CON NOTESASSISTANT")
    print("=" * 50)
    
    import matplotlib.pyplot as plt
    import numpy as np
    from datetime import datetime, timedelta
    
    print("💡 Dashboards visuales para tu proyecto de notas:")
    
    # 1. DASHBOARD DE PRODUCTIVIDAD
    print("\n1️⃣ DASHBOARD DE PRODUCTIVIDAD:")
    
    # Simular datos de productividad
    dias_semana = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
    notas_semana = [5, 7, 4, 8, 6, 3, 2]
    horas_dia = list(range(24))
    notas_por_hora = np.random.poisson(0.5, 24)
    notas_por_hora[8:18] += np.random.poisson(1, 10)  # Más activo durante día
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Dashboard de Productividad - tax-calculator-pro', fontsize=16, fontweight='bold')
    
    # Notas por día de la semana
    bars1 = ax1.bar(dias_semana, notas_semana, color='#3498DB', alpha=0.8)
    ax1.set_title('Notas por Día de la Semana')
    ax1.set_ylabel('Número de Notas')
    for bar, valor in zip(bars1, notas_semana):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{valor}', ha='center', va='bottom', fontweight='bold')
    
    # Notas por hora del día
    ax2.plot(horas_dia, notas_por_hora, 'o-', color='#E74C3C', linewidth=2)
    ax2.set_title('Actividad por Hora del Día')
    ax2.set_xlabel('Hora')
    ax2.set_ylabel('Notas Promedio')
    ax2.grid(True, alpha=0.3)
    ax2.set_xticks(range(0, 24, 4))
    
    # Longitud de notas (histograma)
    longitudes = np.random.lognormal(4, 0.5, 200)
    ax3.hist(longitudes, bins=20, alpha=0.7, color='#2ECC71', edgecolor='black')
    ax3.set_title('Distribución de Longitud de Notas')
    ax3.set_xlabel('Caracteres')
    ax3.set_ylabel('Frecuencia')
    ax3.axvline(np.mean(longitudes), color='red', linestyle='--', 
                label=f'Media: {np.mean(longitudes):.0f}')
    ax3.legend()
    
    # Categorías (pie chart)
    categorias = ['Trabajo', 'Personal', 'Estudio', 'Ideas']
    valores = [40, 30, 20, 10]
    colores = ['#F39C12', '#9B59B6', '#1ABC9C', '#E67E22']
    ax4.pie(valores, labels=categorias, colors=colores, autopct='%1.1f%%', startangle=90)
    ax4.set_title('Distribución por Categoría')
    
    plt.tight_layout()
    plt.savefig('dashboard_productividad.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print("   ✅ Dashboard creado: dashboard_productividad.png")
    
    # 2. ANÁLISIS TEMPORAL AVANZADO
    print("\n2️⃣ ANÁLISIS TEMPORAL AVANZADO:")
    
    # Generar 90 días de datos con tendencias
    fechas = [datetime.now() - timedelta(days=x) for x in range(90, 0, -1)]
    tendencia = np.linspace(2, 4, 90)  # Tendencia creciente
    ruido = np.random.normal(0, 0.5, 90)
    estacionalidad = np.sin(np.arange(90) * 2 * np.pi / 7) * 0.5  # Patrón semanal
    notas_diarias = np.maximum(tendencia + ruido + estacionalidad, 0)
    
    # Calcular media móvil
    ventana = 7
    media_movil = np.convolve(notas_diarias, np.ones(ventana)/ventana, mode='same')
    
    plt.figure(figsize=(15, 8))
    
    # Gráfico principal
    plt.subplot(2, 1, 1)
    plt.plot(fechas, notas_diarias, 'o-', alpha=0.6, color='lightblue', 
             markersize=4, label='Datos diarios')
    plt.plot(fechas, media_movil, '-', linewidth=3, color='darkblue', 
             label=f'Media móvil ({ventana} días)')
    plt.title('Evolución Temporal de Creación de Notas (90 días)', fontsize=14, fontweight='bold')
    plt.ylabel('Notas por Día')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    
    # Análisis por mes
    plt.subplot(2, 1, 2)
    meses = ['Mes 1', 'Mes 2', 'Mes 3']
    notas_mes1 = notas_diarias[:30].sum()
    notas_mes2 = notas_diarias[30:60].sum()
    notas_mes3 = notas_diarias[60:].sum()
    totales_mes = [notas_mes1, notas_mes2, notas_mes3]
    
    bars = plt.bar(meses, totales_mes, color=['#FF6B6B', '#4ECDC4', '#45B7D1'], alpha=0.8)
    plt.title('Total de Notas por Mes')
    plt.ylabel('Total de Notas')
    
    for bar, total in zip(bars, totales_mes):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{total:.0f}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('analisis_temporal.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print("   ✅ Análisis temporal: analisis_temporal.png")
    
    print("\n🎯 Funciones útiles para tu proyecto:")
    print("""
def create_productivity_dashboard(note_data):
    '''Crear dashboard de productividad'''
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    # ... código del dashboard
    return fig

def plot_note_trends(dates, counts):
    '''Graficar tendencias temporales'''
    plt.figure(figsize=(12, 6))
    plt.plot(dates, counts, 'o-')
    # ... agregar media móvil, tendencias
    
def visualize_categories(categories, counts):
    '''Visualizar distribución de categorías'''
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.bar(categories, counts)
    ax2.pie(counts, labels=categories)
    return fig
    """)

def casos_uso_comunes():
    """Casos de uso más comunes de matplotlib"""
    
    print("\n" + "=" * 50)
    print("🎯 CASOS DE USO COMUNES")
    print("=" * 50)
    
    print("1. Gráfico de líneas:")
    print("   plt.plot(x, y)")
    print("   plt.title('Título')")
    print("   plt.show()")
    
    print("\n2. Gráfico de barras:")
    print("   plt.bar(categorias, valores)")
    print("   plt.xlabel('X'), plt.ylabel('Y')")
    
    print("\n3. Histograma:")
    print("   plt.hist(datos, bins=20)")
    print("   plt.hist(datos, density=True)  # Normalizado")
    
    print("\n4. Scatter plot:")
    print("   plt.scatter(x, y, c=colores, s=tamaños)")
    print("   plt.colorbar()  # Barra de colores")
    
    print("\n5. Subplots:")
    print("   fig, axes = plt.subplots(2, 2)")
    print("   axes[0, 0].plot(x, y)")
    
    print("\n6. Personalización:")
    print("   plt.style.use('ggplot')")
    print("   plt.figure(figsize=(10, 6))")
    print("   plt.grid(True, alpha=0.3)")
    
    print("\n7. Guardar gráficos:")
    print("   plt.savefig('grafico.png', dpi=300)")
    print("   plt.savefig('grafico.pdf')  # Formato vectorial")

if __name__ == "__main__":
    # Ejecutar todos los ejemplos
    ejemplo_matplotlib_basico()
    ejemplo_matplotlib_tipos_graficos()
    ejemplo_matplotlib_subplots()
    ejemplo_matplotlib_personalizacion()
    ejemplo_matplotlib_con_datos()
    casos_uso_comunes()
    integracion_con_tax_calculator_pro()
    
    print("\n" + "=" * 50)
    print("✅ RESUMEN DEL MÓDULO matplotlib")
    print("=" * 50)
    print("🔧 Usos principales:")
    print("   • Gráficos de líneas, barras, scatter")
    print("   • Histogramas y distribuciones")
    print("   • Subplots y figuras complejas")
    print("   • Personalización completa")
    print("   • Múltiples formatos de salida")
    print("   • Dashboards y reportes visuales")
    print("\n📚 Documentación oficial:")
    print("   https://matplotlib.org/")
    print("\n💡 Consejo: matplotlib es la base de visualización")
    print("   Aprende matplotlib y podrás usar seaborn, plotly, etc.")
    
    # Limpiar archivos temporales creados
    import os
    archivos_temp = ['ejemplo_seno.png', 'lineas.png', 'barras.png', 'scatter.png', 
                     'histograma.png', 'subplots.png', 'gridspec.png', 'estilo_ggplot.png',
                     'personalizado.png', 'serie_temporal.png', 'categorias.png',
                     'dashboard_productividad.png', 'analisis_temporal.png']
    
    for archivo in archivos_temp:
        if os.path.exists(archivo):
            os.remove(archivo)
    
    print("\n🧹 Archivos temporales limpiados") 