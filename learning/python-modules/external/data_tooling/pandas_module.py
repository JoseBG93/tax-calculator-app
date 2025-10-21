#!/usr/bin/env python3
"""
MÓDULO EXTERNO: pandas
======================

¿QUÉ ES?
El módulo 'pandas' es la librería más poderosa para análisis y manipulación 
de datos en Python. Proporciona estructuras de datos fáciles de usar.

INSTALACIÓN:
pip install pandas

¿PARA QUÉ SIRVE?
- Leer/escribir archivos CSV, Excel, JSON
- Manipular datos tabulares (como Excel)
- Análisis estadístico básico
- Limpieza y transformación de datos
- Agrupación y agregación
- Merge y joins de datos

IMPORTANCIA: ⭐⭐⭐⭐⭐ (Esencial para datos)
"""

def verificar_instalacion():
    """Verificar si pandas está instalado"""
    try:
        import pandas as pd
        print("✅ Módulo 'pandas' instalado correctamente")
        print(f"📦 Versión: {pd.__version__}")
        return True
    except ImportError:
        print("❌ Módulo 'pandas' no encontrado")
        print("💡 Para instalar: pip install pandas")
        return False

def ejemplo_pandas_basico():
    """Ejemplo básico de uso del módulo pandas"""
    
    print("=" * 50)
    print("📊 MÓDULO PANDAS - ANÁLISIS DE DATOS")
    print("=" * 50)
    
    if not verificar_instalacion():
        return
    
    import pandas as pd
    
    # 1. CREAR SERIES (1 DIMENSIÓN)
    print("\n1️⃣ CREAR SERIES:")
    
    # Serie simple
    numeros = pd.Series([1, 2, 3, 4, 5])
    print(f"   📊 Serie de números:")
    print(f"   {numeros}")
    
    # Serie con índice personalizado
    notas = pd.Series([8.5, 9.0, 7.5, 8.0], index=['Ana', 'Luis', 'María', 'Pedro'])
    print(f"\n   📊 Serie con índice personalizado:")
    print(f"   {notas}")
    
    # 2. CREAR DATAFRAME (2 DIMENSIONES - TABLA)
    print("\n2️⃣ CREAR DATAFRAME:")
    
    # DataFrame desde diccionario
    datos = {
        'nombre': ['Ana', 'Luis', 'María', 'Pedro'],
        'edad': [25, 30, 28, 35],
        'ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla'],
        'nota': [8.5, 9.0, 7.5, 8.0]
    }
    
    df = pd.DataFrame(datos)
    print(f"   📊 DataFrame creado:")
    print(f"{df}")
    
    # 3. INFORMACIÓN BÁSICA DEL DATAFRAME
    print("\n3️⃣ INFORMACIÓN BÁSICA:")
    
    print(f"   📏 Dimensiones: {df.shape}")
    print(f"   📋 Columnas: {list(df.columns)}")
    print(f"   🔢 Tipos de datos:")
    print(f"{df.dtypes}")
    
    # 4. ESTADÍSTICAS BÁSICAS
    print("\n4️⃣ ESTADÍSTICAS BÁSICAS:")
    
    print(f"   📊 Descripción estadística:")
    print(f"{df.describe()}")

def ejemplo_pandas_lectura_archivos():
    """Ejemplo de lectura de archivos con pandas"""
    
    print("\n" + "=" * 50)
    print("📁 LECTURA DE ARCHIVOS CON PANDAS")
    print("=" * 50)
    
    import pandas as pd
    import os
    
    # 1. CREAR ARCHIVO CSV DE PRUEBA
    print("\n1️⃣ CREAR ARCHIVO CSV DE PRUEBA:")
    
    # Datos de ejemplo para notas
    datos_notas = {
        'id': [1, 2, 3, 4, 5],
        'titulo': ['Reunión proyecto', 'Lista compras', 'Ideas app', 'Recordatorio', 'Notas estudio'],
        'contenido': ['Discutir avances', 'Leche, pan, huevos', 'Funciones nuevas', 'Llamar al médico', 'Capítulo 3'],
        'fecha': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19'],
        'prioridad': ['Alta', 'Media', 'Alta', 'Baja', 'Media']
    }
    
    df_notas = pd.DataFrame(datos_notas)
    
    # Guardar en CSV
    df_notas.to_csv('notas_ejemplo.csv', index=False)
    print(f"   ✅ Archivo CSV creado: notas_ejemplo.csv")
    
    # 2. LEER ARCHIVO CSV
    print("\n2️⃣ LEER ARCHIVO CSV:")
    
    try:
        # Leer CSV completo
        df_leido = pd.read_csv('notas_ejemplo.csv')
        print(f"   📊 Datos leídos del CSV:")
        print(f"{df_leido}")
        
        # Leer con parámetros específicos
        df_limitado = pd.read_csv('notas_ejemplo.csv', usecols=['titulo', 'prioridad'])
        print(f"\n   📊 Solo columnas específicas:")
        print(f"{df_limitado}")
        
    except FileNotFoundError:
        print(f"   ❌ Archivo no encontrado")
    
    # 3. GUARDAR EN DIFERENTES FORMATOS
    print("\n3️⃣ GUARDAR EN DIFERENTES FORMATOS:")
    
    # Guardar en JSON
    df_notas.to_json('notas_ejemplo.json', orient='records', indent=2)
    print(f"   ✅ Guardado en JSON: notas_ejemplo.json")
    
    # Guardar en Excel (requiere openpyxl)
    try:
        df_notas.to_excel('notas_ejemplo.xlsx', index=False)
        print(f"   ✅ Guardado en Excel: notas_ejemplo.xlsx")
    except ImportError:
        print(f"   ⚠️ Excel no disponible (instalar: pip install openpyxl)")
    
    # 4. LEER JSON
    print("\n4️⃣ LEER JSON:")
    
    try:
        df_desde_json = pd.read_json('notas_ejemplo.json')
        print(f"   📊 Datos leídos desde JSON:")
        print(f"{df_desde_json.head()}")
    except ValueError as e:
        print(f"   ❌ Error leyendo JSON: {e}")
    
    # Limpiar archivos temporales
    archivos_temp = ['notas_ejemplo.csv', 'notas_ejemplo.json', 'notas_ejemplo.xlsx']
    for archivo in archivos_temp:
        if os.path.exists(archivo):
            os.remove(archivo)
            print(f"   🗑️ Archivo temporal eliminado: {archivo}")

def ejemplo_pandas_manipulacion():
    """Ejemplo de manipulación de datos con pandas"""
    
    print("\n" + "=" * 50)
    print("🔧 MANIPULACIÓN DE DATOS CON PANDAS")
    print("=" * 50)
    
    import pandas as pd
    
    # Datos de ejemplo más completos
    datos = {
        'id': [1, 2, 3, 4, 5, 6, 7, 8],
        'titulo': ['Reunión', 'Compras', 'Ideas', 'Recordatorio', 'Estudio', 'Trabajo', 'Personal', 'Urgente'],
        'categoria': ['Trabajo', 'Personal', 'Trabajo', 'Personal', 'Estudio', 'Trabajo', 'Personal', 'Trabajo'],
        'prioridad': ['Alta', 'Media', 'Alta', 'Baja', 'Media', 'Alta', 'Baja', 'Alta'],
        'completada': [True, False, False, True, False, True, False, False],
        'fecha': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19', '2024-01-20', '2024-01-21', '2024-01-22']
    }
    
    df = pd.DataFrame(datos)
    
    # 1. FILTRADO DE DATOS
    print("\n1️⃣ FILTRADO DE DATOS:")
    
    # Filtrar por prioridad alta
    alta_prioridad = df[df['prioridad'] == 'Alta']
    print(f"   📊 Notas de prioridad alta:")
    print(f"{alta_prioridad[['titulo', 'prioridad']]}")
    
    # Filtrar por múltiples condiciones
    trabajo_no_completado = df[(df['categoria'] == 'Trabajo') & (df['completada'] == False)]
    print(f"\n   📊 Trabajo no completado:")
    print(f"{trabajo_no_completado[['titulo', 'categoria', 'completada']]}")
    
    # 2. SELECCIÓN DE COLUMNAS
    print("\n2️⃣ SELECCIÓN DE COLUMNAS:")
    
    # Seleccionar columnas específicas
    resumen = df[['titulo', 'prioridad', 'completada']]
    print(f"   📊 Resumen (solo columnas importantes):")
    print(f"{resumen}")
    
    # 3. ORDENACIÓN
    print("\n3️⃣ ORDENACIÓN:")
    
    # Ordenar por prioridad y fecha
    df_ordenado = df.sort_values(['prioridad', 'fecha'], ascending=[False, True])
    print(f"   📊 Ordenado por prioridad y fecha:")
    print(f"{df_ordenado[['titulo', 'prioridad', 'fecha']]}")
    
    # 4. AGRUPACIÓN
    print("\n4️⃣ AGRUPACIÓN:")
    
    # Agrupar por categoría
    por_categoria = df.groupby('categoria').size()
    print(f"   📊 Notas por categoría:")
    print(f"{por_categoria}")
    
    # Agrupar por prioridad y ver completadas
    por_prioridad = df.groupby('prioridad')['completada'].sum()
    print(f"\n   📊 Completadas por prioridad:")
    print(f"{por_prioridad}")

def ejemplo_pandas_estadisticas():
    """Ejemplo de análisis estadístico con pandas"""
    
    print("\n" + "=" * 50)
    print("📈 ANÁLISIS ESTADÍSTICO CON PANDAS")
    print("=" * 50)
    
    import pandas as pd
    import numpy as np
    
    # Crear datos de ejemplo con números
    np.random.seed(42)  # Para resultados reproducibles
    
    datos_numericos = {
        'usuario_id': range(1, 101),
        'notas_creadas': np.random.randint(1, 50, 100),
        'tiempo_promedio': np.random.normal(5, 2, 100),  # minutos
        'calificacion': np.random.randint(1, 6, 100),
        'mes': np.random.choice(['Enero', 'Febrero', 'Marzo'], 100)
    }
    
    df_stats = pd.DataFrame(datos_numericos)
    
    # 1. ESTADÍSTICAS DESCRIPTIVAS
    print("\n1️⃣ ESTADÍSTICAS DESCRIPTIVAS:")
    
    print(f"   📊 Descripción completa:")
    print(f"{df_stats.describe()}")
    
    # 2. ESTADÍSTICAS POR COLUMNA
    print("\n2️⃣ ESTADÍSTICAS POR COLUMNA:")
    
    print(f"   📊 Promedio de notas creadas: {df_stats['notas_creadas'].mean():.2f}")
    print(f"   📊 Mediana de tiempo: {df_stats['tiempo_promedio'].median():.2f} min")
    print(f"   📊 Desviación estándar calificación: {df_stats['calificacion'].std():.2f}")
    print(f"   📊 Valor máximo notas: {df_stats['notas_creadas'].max()}")
    print(f"   📊 Valor mínimo notas: {df_stats['notas_creadas'].min()}")
    
    # 3. CORRELACIONES
    print("\n3️⃣ CORRELACIONES:")
    
    # Correlación entre columnas numéricas
    correlaciones = df_stats[['notas_creadas', 'tiempo_promedio', 'calificacion']].corr()
    print(f"   📊 Matriz de correlaciones:")
    print(f"{correlaciones}")
    
    # 4. AGRUPACIÓN CON ESTADÍSTICAS
    print("\n4️⃣ AGRUPACIÓN CON ESTADÍSTICAS:")
    
    # Estadísticas por mes
    stats_por_mes = df_stats.groupby('mes').agg({
        'notas_creadas': ['mean', 'sum', 'count'],
        'tiempo_promedio': ['mean', 'std'],
        'calificacion': ['mean', 'max', 'min']
    })
    
    print(f"   📊 Estadísticas por mes:")
    print(f"{stats_por_mes}")

def ejemplo_pandas_limpieza():
    """Ejemplo de limpieza de datos con pandas"""
    
    print("\n" + "=" * 50)
    print("🧹 LIMPIEZA DE DATOS CON PANDAS")
    print("=" * 50)
    
    import pandas as pd
    import numpy as np
    
    # Crear datos "sucios" con problemas comunes
    datos_sucios = {
        'id': [1, 2, 3, 4, 5, 6, 7, 8],
        'titulo': ['  Reunión  ', 'COMPRAS', 'ideas', '', 'Estudio', 'Trabajo', None, 'URGENTE'],
        'prioridad': ['Alta', 'media', 'ALTA', 'baja', 'Media', 'alta', 'Alta', 'MEDIA'],
        'fecha': ['2024-01-15', '2024/01/16', '15-01-2024', '2024-01-18', '', '2024-01-20', None, '2024-01-22'],
        'valor': [100, 200, None, 150, 0, 300, 250, np.nan]
    }
    
    df_sucio = pd.DataFrame(datos_sucios)
    
    print("\n1️⃣ DATOS ORIGINALES (SUCIOS):")
    print(f"{df_sucio}")
    print(f"\n   📊 Información sobre valores nulos:")
    print(f"{df_sucio.isnull().sum()}")
    
    # 2. LIMPIEZA PASO A PASO
    print("\n2️⃣ LIMPIEZA PASO A PASO:")
    
    # Copia para trabajar
    df_limpio = df_sucio.copy()
    
    # Limpiar espacios en blanco
    df_limpio['titulo'] = df_limpio['titulo'].str.strip()
    print(f"   ✅ Espacios en blanco eliminados")
    
    # Normalizar texto (todo minúsculas)
    df_limpio['prioridad'] = df_limpio['prioridad'].str.lower().str.capitalize()
    print(f"   ✅ Texto normalizado")
    
    # Manejar valores nulos en título
    df_limpio['titulo'] = df_limpio['titulo'].fillna('Sin título')
    df_limpio['titulo'] = df_limpio['titulo'].replace('', 'Sin título')
    print(f"   ✅ Valores nulos en título manejados")
    
    # Manejar valores nulos en valor (rellenar con media)
    media_valor = df_limpio['valor'].mean()
    df_limpio['valor'] = df_limpio['valor'].fillna(media_valor)
    print(f"   ✅ Valores nulos en valor rellenados con media: {media_valor:.2f}")
    
    # 3. RESULTADO FINAL
    print("\n3️⃣ DATOS LIMPIOS:")
    print(f"{df_limpio}")
    
    # 4. VALIDACIÓN DE LIMPIEZA
    print("\n4️⃣ VALIDACIÓN:")
    print(f"   📊 Valores nulos restantes: {df_limpio.isnull().sum().sum()}")
    print(f"   📊 Valores únicos en prioridad: {df_limpio['prioridad'].unique()}")

def casos_uso_comunes():
    """Casos de uso más comunes del módulo pandas"""
    
    print("\n" + "=" * 50)
    print("🎯 CASOS DE USO COMUNES")
    print("=" * 50)
    
    print("1. Leer archivo CSV:")
    print("   df = pd.read_csv('archivo.csv')")
    print("   print(df.head())")
    
    print("\n2. Filtrar datos:")
    print("   df_filtrado = df[df['columna'] > 100]")
    print("   df_multiple = df[(df['col1'] > 50) & (df['col2'] == 'valor')]")
    
    print("\n3. Agrupar y resumir:")
    print("   resumen = df.groupby('categoria').sum()")
    print("   stats = df.groupby('grupo').agg({'col1': 'mean', 'col2': 'count'})")
    
    print("\n4. Operaciones con fechas:")
    print("   df['fecha'] = pd.to_datetime(df['fecha'])")
    print("   df['año'] = df['fecha'].dt.year")
    
    print("\n5. Guardar resultados:")
    print("   df.to_csv('resultado.csv', index=False)")
    print("   df.to_excel('resultado.xlsx', index=False)")
    
    print("\n6. Manejo de valores nulos:")
    print("   df.dropna()  # Eliminar filas con nulos")
    print("   df.fillna(0)  # Rellenar nulos con 0")

def integracion_con_tax_calculator_pro():
    """Ejemplo de integración con proyecto tax-calculator-pro"""
    
    print("\n" + "=" * 50)
    print("🗂️ INTEGRACIÓN CON NOTESASSISTANT")
    print("=" * 50)
    
    print("💡 Posibles usos de pandas en tu proyecto de notas:")
    
    print("\n1. Análisis de notas:")
    print("   # Leer notas desde CSV")
    print("   df_notas = pd.read_csv('notas.csv')")
    print("   print(f'Total notas: {len(df_notas)}')")
    print("   print(f'Notas por categoría: {df_notas.groupby(\"categoria\").size()}')")
    
    print("\n2. Reportes automáticos:")
    print("   # Generar reporte mensual")
    print("   df_notas['fecha'] = pd.to_datetime(df_notas['fecha'])")
    print("   df_notas['mes'] = df_notas['fecha'].dt.month")
    print("   reporte = df_notas.groupby('mes').size()")
    
    print("\n3. Backup y export:")
    print("   # Exportar notas a Excel")
    print("   df_notas.to_excel('backup_notas.xlsx', index=False)")
    print("   # Exportar por categoría")
    print("   for cat in df_notas['categoria'].unique():")
    print("       df_cat = df_notas[df_notas['categoria'] == cat]")
    print("       df_cat.to_csv(f'notas_{cat}.csv', index=False)")
    
    print("\n4. Búsqueda avanzada:")
    print("   # Buscar en contenido de notas")
    print("   def buscar_notas(df, termino):")
    print("       return df[df['contenido'].str.contains(termino, case=False, na=False)]")
    
    print("\n5. Estadísticas de uso:")
    print("   # Análisis de patrones")
    print("   df_notas['longitud'] = df_notas['contenido'].str.len()")
    print("   print(f'Longitud promedio: {df_notas[\"longitud\"].mean():.2f}')")
    print("   print(f'Nota más larga: {df_notas[\"longitud\"].max()}')")

if __name__ == "__main__":
    # Ejecutar todos los ejemplos
    ejemplo_pandas_basico()
    ejemplo_pandas_lectura_archivos()
    ejemplo_pandas_manipulacion()
    ejemplo_pandas_estadisticas()
    ejemplo_pandas_limpieza()
    casos_uso_comunes()
    integracion_con_tax_calculator_pro()
    
    print("\n" + "=" * 50)
    print("✅ RESUMEN DEL MÓDULO pandas")
    print("=" * 50)
    print("🔧 Usos principales:")
    print("   • Leer/escribir archivos CSV, Excel, JSON")
    print("   • Manipular datos tabulares")
    print("   • Análisis estadístico")
    print("   • Limpieza de datos")
    print("   • Agrupación y agregación")
    print("   • Filtrado y selección")
    print("\n📚 Documentación oficial:")
    print("   https://pandas.pydata.org/docs/")
    print("\n💡 Consejo: pandas es Excel pero programático")
    print("   Si usas Excel, pandas será tu mejor amigo.") 