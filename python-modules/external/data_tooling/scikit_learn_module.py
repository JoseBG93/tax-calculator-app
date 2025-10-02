#!/usr/bin/env python3
"""
MÓDULO EXTERNO: scikit-learn
============================

¿QUÉ ES?
Scikit-learn es LA librería de machine learning más popular de Python.
Proporciona algoritmos listos para usar con API consistente y simple.

INSTALACIÓN:
pip install scikit-learn

¿PARA QUÉ SIRVE?
- Clasificación (predecir categorías)
- Regresión (predecir valores numéricos)
- Clustering (agrupar datos similares)
- Preprocessing (preparar datos)
- Model selection (elegir mejor modelo)
- Métricas de evaluación

IMPORTANCIA: ⭐⭐⭐⭐⭐ (Esencial para ML)
"""

def verificar_instalacion():
    """Verificar si scikit-learn está instalado"""
    try:
        import sklearn
        print("✅ Módulo 'scikit-learn' instalado correctamente")
        print(f"📦 Versión: {sklearn.__version__}")
        return True
    except ImportError:
        print("❌ Módulo 'scikit-learn' no encontrado")
        print("💡 Para instalar: pip install scikit-learn")
        return False

def ejemplo_sklearn_basico():
    """Ejemplo básico de scikit-learn"""
    
    print("=" * 50)
    print("🤖 MÓDULO SCIKIT-LEARN - MACHINE LEARNING")
    print("=" * 50)
    
    if not verificar_instalacion():
        return
    
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, r2_score
    
    print("\n📝 Ejemplo básico de regresión lineal:")
    print("""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Crear datos
X = np.random.rand(100, 1) * 10
y = 2 * X.ravel() + 1 + np.random.randn(100) * 2

# 2. Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. Crear y entrenar modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 4. Hacer predicciones
y_pred = modelo.predict(X_test)

# 5. Evaluar
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
    """)
    
    # Ejecutar ejemplo
    np.random.seed(42)
    
    # 1. Crear datos sintéticos
    X = np.random.rand(100, 1) * 10  # Features (variables independientes)
    y = 2 * X.ravel() + 1 + np.random.randn(100) * 2  # Target (variable dependiente)
    
    # 2. Dividir datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Crear y entrenar modelo
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    
    # 4. Hacer predicciones
    y_pred = modelo.predict(X_test)
    
    # 5. Evaluar modelo
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print("\n✅ Resultados del modelo:")
    print(f"   📊 Datos de entrenamiento: {len(X_train)} muestras")
    print(f"   📊 Datos de prueba: {len(X_test)} muestras")
    print(f"   📈 Coeficiente (pendiente): {modelo.coef_[0]:.2f}")
    print(f"   📈 Intercepto: {modelo.intercept_:.2f}")
    print(f"   📊 Error cuadrático medio: {mse:.2f}")
    print(f"   📊 R² Score: {r2:.3f}")
    
    print("\n💡 Interpretación:")
    print(f"   • El modelo explica {r2*100:.1f}% de la varianza")
    print(f"   • Ecuación: y = {modelo.coef_[0]:.2f}x + {modelo.intercept_:.2f}")

def ejemplo_sklearn_clasificacion():
    """Ejemplo de clasificación con scikit-learn"""
    
    print("\n" + "=" * 50)
    print("🎯 CLASIFICACIÓN CON SCIKIT-LEARN")
    print("=" * 50)
    
    import numpy as np
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
    
    # 1. CREAR DATASET SINTÉTICO
    print("\n1️⃣ CREAR DATASET:")
    
    X, y = make_classification(
        n_samples=1000,      # 1000 muestras
        n_features=20,       # 20 características
        n_informative=15,    # 15 características útiles
        n_redundant=5,       # 5 características redundantes
        n_classes=3,         # 3 clases
        random_state=42
    )
    
    print(f"   📊 Shape de X: {X.shape}")
    print(f"   📊 Shape de y: {y.shape}")
    print(f"   📊 Clases únicas: {np.unique(y)}")
    print(f"   📊 Distribución de clases: {np.bincount(y)}")
    
    # 2. DIVIDIR DATOS
    print("\n2️⃣ DIVIDIR DATOS:")
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"   📈 Entrenamiento: {X_train.shape[0]} muestras")
    print(f"   📈 Prueba: {X_test.shape[0]} muestras")
    
    # 3. ENTRENAR MÚLTIPLES MODELOS
    print("\n3️⃣ ENTRENAR MODELOS:")
    
    modelos = {
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
        'SVM': SVC(random_state=42)
    }
    
    resultados = {}
    
    for nombre, modelo in modelos.items():
        # Entrenar
        modelo.fit(X_train, y_train)
        
        # Predecir
        y_pred = modelo.predict(X_test)
        
        # Evaluar
        accuracy = accuracy_score(y_test, y_pred)
        resultados[nombre] = accuracy
        
        print(f"   🤖 {nombre}: {accuracy:.3f} accuracy")
    
    # 4. MEJOR MODELO
    mejor_modelo = max(resultados, key=resultados.get)
    print(f"\n🏆 Mejor modelo: {mejor_modelo} ({resultados[mejor_modelo]:.3f})")
    
    # 5. ANÁLISIS DETALLADO DEL MEJOR MODELO
    print("\n4️⃣ ANÁLISIS DETALLADO:")
    
    modelo_final = modelos[mejor_modelo]
    y_pred_final = modelo_final.predict(X_test)
    
    print("   📊 Classification Report:")
    print(classification_report(y_test, y_pred_final, target_names=['Clase 0', 'Clase 1', 'Clase 2']))
    
    print("   📊 Confusion Matrix:")
    cm = confusion_matrix(y_test, y_pred_final)
    print(cm)

def ejemplo_sklearn_preprocessing():
    """Ejemplo de preprocessing de datos"""
    
    print("\n" + "=" * 50)
    print("🛠️ PREPROCESSING DE DATOS")
    print("=" * 50)
    
    import numpy as np
    import pandas as pd
    from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.impute import SimpleImputer
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline
    
    # 1. CREAR DATOS CON PROBLEMAS COMUNES
    print("\n1️⃣ DATOS CON PROBLEMAS TÍPICOS:")
    
    np.random.seed(42)
    
    # Datos simulados con diferentes escalas y valores faltantes
    datos = {
        'edad': np.random.randint(18, 80, 100),
        'salario': np.random.normal(50000, 15000, 100),
        'experiencia': np.random.exponential(5, 100),
        'categoria': np.random.choice(['A', 'B', 'C'], 100),
        'tiene_coche': np.random.choice([True, False], 100)
    }
    
    df = pd.DataFrame(datos)
    
    # Introducir valores faltantes
    df.loc[np.random.choice(df.index, 10), 'salario'] = np.nan
    df.loc[np.random.choice(df.index, 5), 'experiencia'] = np.nan
    
    print(f"   📊 Shape original: {df.shape}")
    print(f"   📊 Valores faltantes por columna:")
    print(df.isnull().sum())
    print(f"   📊 Tipos de datos:")
    print(df.dtypes)
    
    # 2. MANEJO DE VALORES FALTANTES
    print("\n2️⃣ MANEJO DE VALORES FALTANTES:")
    
    # Imputar valores faltantes
    imputer_num = SimpleImputer(strategy='mean')
    df[['salario', 'experiencia']] = imputer_num.fit_transform(df[['salario', 'experiencia']])
    
    print(f"   ✅ Valores faltantes después de imputación:")
    print(df.isnull().sum())
    
    # 3. ESCALADO DE CARACTERÍSTICAS NUMÉRICAS
    print("\n3️⃣ ESCALADO DE CARACTERÍSTICAS:")
    
    # Antes del escalado
    print(f"   📊 Estadísticas antes del escalado:")
    print(df[['edad', 'salario', 'experiencia']].describe())
    
    # StandardScaler (media=0, std=1)
    scaler = StandardScaler()
    df_scaled = df.copy()
    df_scaled[['edad', 'salario', 'experiencia']] = scaler.fit_transform(
        df[['edad', 'salario', 'experiencia']]
    )
    
    print(f"   📊 Estadísticas después del escalado:")
    print(df_scaled[['edad', 'salario', 'experiencia']].describe())
    
    # 4. CODIFICACIÓN DE VARIABLES CATEGÓRICAS
    print("\n4️⃣ CODIFICACIÓN CATEGÓRICAS:")
    
    # Label Encoding para variables binarias
    le = LabelEncoder()
    df_scaled['tiene_coche_encoded'] = le.fit_transform(df_scaled['tiene_coche'])
    
    # One-Hot Encoding para variables categóricas
    encoder = OneHotEncoder(sparse_output=False, drop='first')
    categoria_encoded = encoder.fit_transform(df[['categoria']])
    categoria_columns = [f'categoria_{cat}' for cat in encoder.categories_[0][1:]]
    
    for i, col in enumerate(categoria_columns):
        df_scaled[col] = categoria_encoded[:, i]
    
    print(f"   ✅ Columnas después de encoding:")
    print(list(df_scaled.columns))
    
    # 5. PIPELINE COMPLETO
    print("\n5️⃣ PIPELINE COMPLETO:")
    
    # Crear pipeline que hace todo automáticamente
    numeric_features = ['edad', 'salario', 'experiencia']
    categorical_features = ['categoria']
    
    # Pipeline para features numéricas
    numeric_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])
    
    # Pipeline para features categóricas
    categorical_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('encoder', OneHotEncoder(drop='first', sparse_output=False))
    ])
    
    # Combinar pipelines
    preprocessor = ColumnTransformer([
        ('num', numeric_pipeline, numeric_features),
        ('cat', categorical_pipeline, categorical_features)
    ])
    
    # Aplicar preprocessing
    X_processed = preprocessor.fit_transform(df[numeric_features + categorical_features])
    
    print(f"   ✅ Shape después del preprocessing: {X_processed.shape}")
    print(f"   ✅ Pipeline creado y aplicado exitosamente")

def ejemplo_sklearn_clustering():
    """Ejemplo de clustering (aprendizaje no supervisado)"""
    
    print("\n" + "=" * 50)
    print("🔍 CLUSTERING - APRENDIZAJE NO SUPERVISADO")
    print("=" * 50)
    
    import numpy as np
    from sklearn.datasets import make_blobs
    from sklearn.cluster import KMeans, DBSCAN
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import silhouette_score, adjusted_rand_score
    
    # 1. CREAR DATOS PARA CLUSTERING
    print("\n1️⃣ CREAR DATOS:")
    
    X, y_true = make_blobs(
        n_samples=300,
        centers=4,
        cluster_std=0.6,
        random_state=42
    )
    
    print(f"   📊 Datos creados: {X.shape}")
    print(f"   📊 Clusters reales: {len(np.unique(y_true))}")
    
    # 2. K-MEANS CLUSTERING
    print("\n2️⃣ K-MEANS CLUSTERING:")
    
    # Probar diferentes números de clusters
    silhouette_scores = []
    K_range = range(2, 8)
    
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(X)
        silhouette = silhouette_score(X, labels)
        silhouette_scores.append(silhouette)
        print(f"   🔢 K={k}: Silhouette Score = {silhouette:.3f}")
    
    # Mejor K según silhouette score
    mejor_k = K_range[np.argmax(silhouette_scores)]
    print(f"   🏆 Mejor K: {mejor_k} (Score: {max(silhouette_scores):.3f})")
    
    # 3. CLUSTERING FINAL
    print("\n3️⃣ CLUSTERING FINAL:")
    
    kmeans_final = KMeans(n_clusters=mejor_k, random_state=42, n_init=10)
    labels_kmeans = kmeans_final.fit_predict(X)
    
    # DBSCAN como alternativa
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    dbscan = DBSCAN(eps=0.3, min_samples=5)
    labels_dbscan = dbscan.fit_predict(X_scaled)
    
    print(f"   📊 K-Means clusters encontrados: {len(np.unique(labels_kmeans))}")
    print(f"   📊 DBSCAN clusters encontrados: {len(np.unique(labels_dbscan[labels_dbscan != -1]))}")
    print(f"   📊 DBSCAN outliers: {np.sum(labels_dbscan == -1)}")
    
    # 4. EVALUACIÓN
    print("\n4️⃣ EVALUACIÓN:")
    
    # Comparar con clusters reales (si los conocemos)
    ari_kmeans = adjusted_rand_score(y_true, labels_kmeans)
    ari_dbscan = adjusted_rand_score(y_true, labels_dbscan)
    
    print(f"   📊 K-Means ARI: {ari_kmeans:.3f}")
    print(f"   📊 DBSCAN ARI: {ari_dbscan:.3f}")
    
    # Silhouette scores
    sil_kmeans = silhouette_score(X, labels_kmeans)
    sil_dbscan = silhouette_score(X, labels_dbscan) if len(np.unique(labels_dbscan)) > 1 else 0
    
    print(f"   📊 K-Means Silhouette: {sil_kmeans:.3f}")
    print(f"   📊 DBSCAN Silhouette: {sil_dbscan:.3f}")

def ejemplo_sklearn_validacion():
    """Ejemplo de validación de modelos"""
    
    print("\n" + "=" * 50)
    print("✅ VALIDACIÓN DE MODELOS")
    print("=" * 50)
    
    import numpy as np
    from sklearn.datasets import make_classification
    from sklearn.model_selection import cross_val_score, GridSearchCV, validation_curve
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    from sklearn.model_selection import train_test_split
    
    # 1. CREAR DATOS
    print("\n1️⃣ PREPARAR DATOS:")
    
    X, y = make_classification(
        n_samples=1000,
        n_features=20,
        n_informative=15,
        n_classes=2,
        random_state=42
    )
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"   📊 Datos de entrenamiento: {X_train.shape}")
    print(f"   📊 Datos de prueba: {X_test.shape}")
    
    # 2. VALIDACIÓN CRUZADA
    print("\n2️⃣ VALIDACIÓN CRUZADA:")
    
    modelo = RandomForestClassifier(random_state=42)
    
    # Cross-validation con diferentes métricas
    cv_scores = cross_val_score(modelo, X_train, y_train, cv=5)
    cv_precision = cross_val_score(modelo, X_train, y_train, cv=5, scoring='precision')
    cv_recall = cross_val_score(modelo, X_train, y_train, cv=5, scoring='recall')
    cv_f1 = cross_val_score(modelo, X_train, y_train, cv=5, scoring='f1')
    
    print(f"   📊 Accuracy CV: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")
    print(f"   📊 Precision CV: {cv_precision.mean():.3f} ± {cv_precision.std():.3f}")
    print(f"   📊 Recall CV: {cv_recall.mean():.3f} ± {cv_recall.std():.3f}")
    print(f"   📊 F1 CV: {cv_f1.mean():.3f} ± {cv_f1.std():.3f}")
    
    # 3. GRID SEARCH PARA HIPERPARÁMETROS
    print("\n3️⃣ GRID SEARCH:")
    
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5, 10]
    }
    
    grid_search = GridSearchCV(
        RandomForestClassifier(random_state=42),
        param_grid,
        cv=3,  # Reducido para velocidad
        scoring='accuracy',
        n_jobs=-1
    )
    
    grid_search.fit(X_train, y_train)
    
    print(f"   🏆 Mejores parámetros: {grid_search.best_params_}")
    print(f"   📊 Mejor score CV: {grid_search.best_score_:.3f}")
    
    # 4. EVALUACIÓN FINAL
    print("\n4️⃣ EVALUACIÓN FINAL:")
    
    # Modelo con mejores parámetros
    mejor_modelo = grid_search.best_estimator_
    y_pred = mejor_modelo.predict(X_test)
    
    # Métricas en conjunto de prueba
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    print(f"   📊 Test Accuracy: {accuracy:.3f}")
    print(f"   📊 Test Precision: {precision:.3f}")
    print(f"   📊 Test Recall: {recall:.3f}")
    print(f"   📊 Test F1: {f1:.3f}")
    
    # 5. IMPORTANCIA DE CARACTERÍSTICAS
    print("\n5️⃣ IMPORTANCIA DE CARACTERÍSTICAS:")
    
    feature_importance = mejor_modelo.feature_importances_
    indices_importantes = np.argsort(feature_importance)[::-1][:5]
    
    print(f"   📊 Top 5 características más importantes:")
    for i, idx in enumerate(indices_importantes):
        print(f"      {i+1}. Feature {idx}: {feature_importance[idx]:.3f}")

def integracion_con_tax_calculator_pro():
    """Ejemplo de integración con proyecto tax-calculator-pro"""
    
    print("\n" + "=" * 50)
    print("🗂️ INTEGRACIÓN CON NOTESASSISTANT")
    print("=" * 50)
    
    import numpy as np
    import pandas as pd
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.cluster import KMeans
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, classification_report
    
    print("💡 ML aplicado a tu proyecto de notas:")
    
    # 1. CLASIFICACIÓN AUTOMÁTICA DE NOTAS
    print("\n1️⃣ CLASIFICACIÓN AUTOMÁTICA DE NOTAS:")
    
    # Datos simulados de notas
    notas_ejemplo = [
        "Reunión con el equipo mañana a las 10am",
        "Comprar leche, pan y huevos en el supermercado", 
        "Estudiar capítulo 5 de álgebra lineal",
        "Llamar al médico para agendar cita",
        "Idea para nueva funcionalidad en la app",
        "Revisar código del módulo de autenticación",
        "Preparar presentación para el cliente",
        "Lista de compras: manzanas, yogurt, pasta",
        "Ejercicios de matemáticas para el examen",
        "Recordatorio: pagar servicios antes del 15"
    ]
    
    categorias_ejemplo = [
        'trabajo', 'personal', 'estudio', 'personal', 'trabajo',
        'trabajo', 'trabajo', 'personal', 'estudio', 'personal'
    ]
    
    # Vectorizar texto
    vectorizer = TfidfVectorizer(max_features=100, stop_words='english')
    X_text = vectorizer.fit_transform(notas_ejemplo)
    
    # Entrenar clasificador
    X_train, X_test, y_train, y_test = train_test_split(
        X_text, categorias_ejemplo, test_size=0.3, random_state=42
    )
    
    clasificador = MultinomialNB()
    clasificador.fit(X_train, y_train)
    
    # Predecir categorías
    y_pred = clasificador.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"   📊 Accuracy del clasificador: {accuracy:.3f}")
    print(f"   📝 Ejemplo de predicción:")
    
    nueva_nota = ["Terminar informe de ventas del trimestre"]
    nueva_prediccion = clasificador.predict(vectorizer.transform(nueva_nota))
    print(f"      Nota: '{nueva_nota[0]}'")
    print(f"      Categoría predicha: {nueva_prediccion[0]}")
    
    # 2. CLUSTERING DE NOTAS SIMILARES
    print("\n2️⃣ CLUSTERING DE NOTAS SIMILARES:")
    
    # Agrupar notas por similitud
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(X_text.toarray())
    
    print(f"   📊 Notas agrupadas en {len(np.unique(clusters))} clusters:")
    
    for i, cluster in enumerate(np.unique(clusters)):
        notas_cluster = [notas_ejemplo[j] for j in range(len(notas_ejemplo)) if clusters[j] == cluster]
        print(f"   📁 Cluster {cluster + 1}:")
        for nota in notas_cluster:
            print(f"      • {nota}")
    
    # 3. ANÁLISIS DE SENTIMIENTOS
    print("\n3️⃣ ANÁLISIS DE PATRONES EN NOTAS:")
    
    # Simular características de notas
    np.random.seed(42)
    
    datos_notas = {
        'longitud': np.random.normal(100, 30, 50),
        'num_palabras': np.random.normal(20, 8, 50),
        'tiene_fecha': np.random.choice([0, 1], 50, p=[0.7, 0.3]),
        'tiene_numero': np.random.choice([0, 1], 50, p=[0.6, 0.4]),
        'hora_creacion': np.random.randint(0, 24, 50),
        'productividad': np.random.choice(['alta', 'media', 'baja'], 50, p=[0.3, 0.5, 0.2])
    }
    
    df_notas = pd.DataFrame(datos_notas)
    
    # Preparar datos para ML
    X_features = df_notas[['longitud', 'num_palabras', 'tiene_fecha', 'tiene_numero', 'hora_creacion']]
    y_productividad = df_notas['productividad']
    
    # Entrenar modelo para predecir productividad
    from sklearn.ensemble import RandomForestClassifier
    
    X_train, X_test, y_train, y_test = train_test_split(
        X_features, y_productividad, test_size=0.3, random_state=42
    )
    
    modelo_productividad = RandomForestClassifier(random_state=42)
    modelo_productividad.fit(X_train, y_train)
    
    y_pred_prod = modelo_productividad.predict(X_test)
    accuracy_prod = accuracy_score(y_test, y_pred_prod)
    
    print(f"   📊 Accuracy predicción productividad: {accuracy_prod:.3f}")
    
    # Importancia de características
    feature_names = X_features.columns
    importances = modelo_productividad.feature_importances_
    
    print(f"   📊 Características más importantes para productividad:")
    for feature, importance in sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True):
        print(f"      {feature}: {importance:.3f}")
    
    # 4. EJEMPLOS DE FUNCIONES ÚTILES
    print("\n4️⃣ FUNCIONES ÚTILES PARA TU PROYECTO:")
    
    print("""
def classify_note_category(note_text, vectorizer, classifier):
    '''Clasificar automáticamente una nota'''
    text_vector = vectorizer.transform([note_text])
    category = classifier.predict(text_vector)[0]
    confidence = classifier.predict_proba(text_vector).max()
    return category, confidence

def find_similar_notes(new_note, notes_corpus, vectorizer, n_similar=5):
    '''Encontrar notas similares usando TF-IDF'''
    from sklearn.metrics.pairwise import cosine_similarity
    
    # Vectorizar todas las notas
    all_vectors = vectorizer.fit_transform(notes_corpus + [new_note])
    
    # Calcular similitud
    similarities = cosine_similarity(all_vectors[-1:], all_vectors[:-1])
    similar_indices = similarities[0].argsort()[-n_similar:][::-1]
    
    return [(notes_corpus[i], similarities[0][i]) for i in similar_indices]

def predict_note_productivity(note_features, model):
    '''Predecir si una nota será productiva'''
    # note_features: [longitud, num_palabras, tiene_fecha, tiene_numero, hora]
    productivity = model.predict([note_features])[0]
    confidence = model.predict_proba([note_features]).max()
    return productivity, confidence

def cluster_notes_by_topic(notes_text, n_clusters=5):
    '''Agrupar notas por temas similares'''
    vectorizer = TfidfVectorizer(max_features=100, stop_words='english')
    text_vectors = vectorizer.fit_transform(notes_text)
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(text_vectors)
    
    return clusters, vectorizer, kmeans
    """)

def casos_uso_comunes():
    """Casos de uso más comunes de scikit-learn"""
    
    print("\n" + "=" * 50)
    print("🎯 CASOS DE USO COMUNES")
    print("=" * 50)
    
    print("1. Flujo básico de ML:")
    print("   from sklearn.model_selection import train_test_split")
    print("   X_train, X_test, y_train, y_test = train_test_split(X, y)")
    print("   model.fit(X_train, y_train)")
    print("   y_pred = model.predict(X_test)")
    
    print("\n2. Clasificación:")
    print("   from sklearn.ensemble import RandomForestClassifier")
    print("   from sklearn.linear_model import LogisticRegression")
    print("   from sklearn.svm import SVC")
    
    print("\n3. Regresión:")
    print("   from sklearn.linear_model import LinearRegression")
    print("   from sklearn.ensemble import RandomForestRegressor")
    print("   from sklearn.svm import SVR")
    
    print("\n4. Clustering:")
    print("   from sklearn.cluster import KMeans, DBSCAN")
    print("   clusters = KMeans(n_clusters=3).fit_predict(X)")
    
    print("\n5. Preprocessing:")
    print("   from sklearn.preprocessing import StandardScaler")
    print("   scaler = StandardScaler()")
    print("   X_scaled = scaler.fit_transform(X)")
    
    print("\n6. Evaluación:")
    print("   from sklearn.metrics import accuracy_score, classification_report")
    print("   from sklearn.model_selection import cross_val_score")
    
    print("\n7. Pipelines:")
    print("   from sklearn.pipeline import Pipeline")
    print("   pipe = Pipeline([('scaler', StandardScaler()), ('clf', RandomForestClassifier())])")

if __name__ == "__main__":
    # Ejecutar todos los ejemplos
    ejemplo_sklearn_basico()
    ejemplo_sklearn_clasificacion()
    ejemplo_sklearn_preprocessing()
    ejemplo_sklearn_clustering()
    ejemplo_sklearn_validacion()
    casos_uso_comunes()
    integracion_con_tax_calculator_pro()
    
    print("\n" + "=" * 50)
    print("✅ RESUMEN DEL MÓDULO scikit-learn")
    print("=" * 50)
    print("🔧 Usos principales:")
    print("   • Clasificación y regresión")
    print("   • Clustering y reducción dimensional")
    print("   • Preprocessing de datos")
    print("   • Validación y selección de modelos")
    print("   • Métricas de evaluación")
    print("   • Pipelines de ML completos")
    print("\n📚 Documentación oficial:")
    print("   https://scikit-learn.org/")
    print("\n💡 Consejo: scikit-learn es la puerta de entrada al ML")
    print("   API consistente, documentación excelente, comunidad activa.") 