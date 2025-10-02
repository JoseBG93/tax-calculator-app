#!/usr/bin/env python3
"""
MÓDULO EXTERNO: beautifulsoup4
==============================

¿QUÉ ES?
Beautiful Soup es la librería más popular para parsing HTML y XML.
Permite extraer datos de páginas web de forma simple y efectiva.

INSTALACIÓN:
pip install beautifulsoup4

¿PARA QUÉ SIRVE?
- Parsear HTML y XML
- Extraer datos de páginas web
- Web scraping
- Navegar por estructura DOM
- Buscar elementos específicos
- Modificar contenido HTML

IMPORTANCIA: ⭐⭐⭐⭐⭐ (Esencial para scraping)
"""

def verificar_instalacion():
    """Verificar si beautifulsoup4 está instalado"""
    try:
        from bs4 import BeautifulSoup
        print("✅ Módulo 'beautifulsoup4' instalado correctamente")
        print(f"📦 Beautiful Soup disponible")
        return True
    except ImportError:
        print("❌ Módulo 'beautifulsoup4' no encontrado")
        print("💡 Para instalar: pip install beautifulsoup4")
        return False

def ejemplo_beautifulsoup_basico():
    """Ejemplo básico de Beautiful Soup"""
    
    print("=" * 50)
    print("🔍 MÓDULO BEAUTIFULSOUP4 - WEB SCRAPING")
    print("=" * 50)
    
    if not verificar_instalacion():
        return
    
    from bs4 import BeautifulSoup
    
    # HTML de ejemplo
    html_ejemplo = """
    <html>
        <head>
            <title>Mi página de notas</title>
        </head>
        <body>
            <h1>Mis Notas</h1>
            <div class="nota" id="nota1">
                <h2>Nota importante</h2>
                <p>Esta es una nota muy importante</p>
                <span class="fecha">2024-01-15</span>
            </div>
            <div class="nota" id="nota2">
                <h2>Otra nota</h2>
                <p>Otra nota interesante</p>
                <span class="fecha">2024-01-16</span>
            </div>
        </body>
    </html>
    """
    
    # Parsear HTML
    soup = BeautifulSoup(html_ejemplo, 'html.parser')
    
    print("\n📝 Ejemplo básico de Beautiful Soup:")
    print("   # Crear soup object")
    print("   soup = BeautifulSoup(html_content, 'html.parser')")
    
    print("\n✅ Operaciones básicas:")
    print(f"   • Título: {soup.title.string}")
    print(f"   • H1: {soup.h1.string}")
    print(f"   • Primer párrafo: {soup.p.string}")
    
    # Encontrar elementos
    notas = soup.find_all('div', class_='nota')
    print(f"   • Total notas encontradas: {len(notas)}")
    
    for nota in notas:
        titulo = nota.find('h2').string
        contenido = nota.find('p').string
        fecha = nota.find('span', class_='fecha').string
        print(f"     - {titulo}: {contenido} ({fecha})")

def ejemplo_beautifulsoup_selectors():
    """Ejemplo de selectores en Beautiful Soup"""
    
    print("\n" + "=" * 50)
    print("🎯 SELECTORES EN BEAUTIFUL SOUP")
    print("=" * 50)
    
    from bs4 import BeautifulSoup
    
    html = """
    <html>
        <body>
            <div class="container">
                <article class="post" data-id="1">
                    <h2>Título del post</h2>
                    <p class="content">Contenido del post</p>
                    <a href="https://example.com">Enlace</a>
                </article>
                <article class="post" data-id="2">
                    <h2>Otro título</h2>
                    <p class="content">Otro contenido</p>
                </article>
            </div>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html, 'html.parser')
    
    print("\n📝 Métodos de búsqueda:")
    print("""
# Buscar por tag
soup.find('h2')                    # Primer h2
soup.find_all('h2')                # Todos los h2

# Buscar por clase
soup.find('div', class_='container')
soup.find_all('p', class_='content')

# Buscar por ID
soup.find('div', id='mi-id')

# Buscar por atributo
soup.find('article', {'data-id': '1'})

# Selectores CSS
soup.select('.post')               # Por clase
soup.select('#mi-id')              # Por ID
soup.select('div.container')       # Tag + clase
soup.select('article h2')          # Descendientes
soup.select('article > h2')        # Hijos directos
    """)
    
    print("\n✅ Ejemplos prácticos:")
    
    # Todos los artículos
    posts = soup.find_all('article', class_='post')
    print(f"   • Artículos encontrados: {len(posts)}")
    
    # Selectores CSS
    titulos = soup.select('article h2')
    print(f"   • Títulos con CSS selector: {len(titulos)}")
    
    # Buscar por atributo
    post_especifico = soup.find('article', {'data-id': '1'})
    if post_especifico:
        print(f"   • Post específico encontrado: {post_especifico.h2.string}")
    
    # Enlaces
    enlaces = soup.find_all('a')
    for enlace in enlaces:
        print(f"   • Enlace: {enlace.get('href')} - {enlace.string}")

def ejemplo_beautifulsoup_requests():
    """Ejemplo de Beautiful Soup con requests"""
    
    print("\n" + "=" * 50)
    print("🌐 BEAUTIFUL SOUP + REQUESTS")
    print("=" * 50)
    
    print("📝 Ejemplo de web scraping real:")
    print("""
import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    '''Scraping de citas desde httpbin'''
    try:
        # Hacer petición HTTP
        response = requests.get('https://httpbin.org/html')
        response.raise_for_status()
        
        # Parsear HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrar elementos
        title = soup.find('h1')
        if title:
            print(f"Título: {title.string}")
        
        # Encontrar todos los párrafos
        paragraphs = soup.find_all('p')
        for i, p in enumerate(paragraphs):
            print(f"Párrafo {i+1}: {p.get_text()}")
        
    except requests.RequestException as e:
        print(f"Error en petición: {e}")
    except Exception as e:
        print(f"Error en scraping: {e}")

def scrape_github_repos(username):
    '''Scraping de repositorios de GitHub'''
    url = f"https://github.com/{username}"
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Buscar repositorios
        repos = soup.find_all('a', {'itemprop': 'name codeRepository'})
        
        print(f"Repositorios de {username}:")
        for repo in repos[:5]:  # Primeros 5
            print(f"  - {repo.get_text().strip()}")
            
    except Exception as e:
        print(f"Error scraping GitHub: {e}")
    """)
    
    print("\n✅ Mejores prácticas:")
    print("   • Usar requests + BeautifulSoup juntos")
    print("   • Verificar response.status_code")
    print("   • Manejar excepciones")
    print("   • Respetar robots.txt")
    print("   • Usar delays entre peticiones")
    print("   • Verificar estructura HTML")

def ejemplo_beautifulsoup_scraping_practico():
    """Ejemplo práctico de scraping"""
    
    print("\n" + "=" * 50)
    print("🛠️ SCRAPING PRÁCTICO")
    print("=" * 50)
    
    from bs4 import BeautifulSoup
    
    # HTML simulado de una página de noticias
    html_noticias = """
    <html>
        <body>
            <div class="news-container">
                <article class="news-item">
                    <h3 class="title">Python 3.12 Released</h3>
                    <p class="summary">Nueva versión de Python con mejoras</p>
                    <span class="date">2024-01-15</span>
                    <a class="read-more" href="/news/python-3-12">Leer más</a>
                </article>
                <article class="news-item">
                    <h3 class="title">Django 5.0 Features</h3>
                    <p class="summary">Nuevas características en Django</p>
                    <span class="date">2024-01-14</span>
                    <a class="read-more" href="/news/django-5">Leer más</a>
                </article>
            </div>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html_noticias, 'html.parser')
    
    print("\n📝 Función de scraping:")
    print("""
def scrape_news(html_content):
    '''Extraer noticias de HTML'''
    soup = BeautifulSoup(html_content, 'html.parser')
    
    noticias = []
    articles = soup.find_all('article', class_='news-item')
    
    for article in articles:
        noticia = {
            'titulo': article.find('h3', class_='title').get_text().strip(),
            'resumen': article.find('p', class_='summary').get_text().strip(),
            'fecha': article.find('span', class_='date').get_text().strip(),
            'enlace': article.find('a', class_='read-more').get('href')
        }
        noticias.append(noticia)
    
    return noticias
    """)
    
    # Ejecutar scraping
    noticias = []
    articles = soup.find_all('article', class_='news-item')
    
    for article in articles:
        noticia = {
            'titulo': article.find('h3', class_='title').get_text().strip(),
            'resumen': article.find('p', class_='summary').get_text().strip(),
            'fecha': article.find('span', class_='date').get_text().strip(),
            'enlace': article.find('a', class_='read-more').get('href')
        }
        noticias.append(noticia)
    
    print("\n✅ Noticias extraídas:")
    for i, noticia in enumerate(noticias, 1):
        print(f"   {i}. {noticia['titulo']}")
        print(f"      Resumen: {noticia['resumen']}")
        print(f"      Fecha: {noticia['fecha']}")
        print(f"      Enlace: {noticia['enlace']}")
        print()

def integracion_con_tax_calculator_pro():
    """Ejemplo de integración con proyecto tax-calculator-pro"""
    
    print("\n" + "=" * 50)
    print("🗂️ INTEGRACIÓN CON NOTESASSISTANT")
    print("=" * 50)
    
    print("💡 Posibles usos en tu proyecto:")
    
    print("\n📝 1. Importar notas desde web:")
    print("""
def import_notes_from_web(url):
    '''Importar notas desde página web'''
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Buscar elementos que parezcan notas
        note_elements = soup.find_all(['article', 'div'], 
                                     class_=['note', 'post', 'entry'])
        
        imported_notes = []
        for element in note_elements:
            title = element.find(['h1', 'h2', 'h3'])
            content = element.find(['p', 'div'])
            
            if title and content:
                note = {
                    'title': title.get_text().strip(),
                    'content': content.get_text().strip(),
                    'source': url
                }
                imported_notes.append(note)
        
        return imported_notes
    
    except Exception as e:
        print(f"Error importando notas: {e}")
        return []
    """)
    
    print("\n📝 2. Monitorear sitios web:")
    print("""
def monitor_website_changes(url, selector):
    '''Monitorear cambios en sitio web'''
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrar contenido específico
        content = soup.select(selector)
        current_content = [elem.get_text().strip() for elem in content]
        
        # Comparar con contenido anterior (guardado en archivo)
        # Si hay cambios, crear nota automáticamente
        
        return current_content
    
    except Exception as e:
        print(f"Error monitoreando: {e}")
        return []
    """)
    
    print("\n📝 3. Extraer información de documentos:")
    print("""
def extract_info_from_html(html_content):
    '''Extraer información estructurada de HTML'''
    soup = BeautifulSoup(html_content, 'html.parser')
    
    info = {
        'title': '',
        'headings': [],
        'links': [],
        'text_content': ''
    }
    
    # Título
    title = soup.find('title')
    if title:
        info['title'] = title.string
    
    # Encabezados
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    info['headings'] = [h.get_text().strip() for h in headings]
    
    # Enlaces
    links = soup.find_all('a')
    info['links'] = [{'text': a.get_text().strip(), 'href': a.get('href')} 
                     for a in links if a.get('href')]
    
    # Texto completo
    info['text_content'] = soup.get_text().strip()
    
    return info
    """)
    
    print("\n🎯 Casos de uso:")
    print("   • Importar notas desde blogs")
    print("   • Monitorear cambios en sitios")
    print("   • Extraer información de documentos")
    print("   • Crear resúmenes automáticos")
    print("   • Generar notas desde noticias")
    print("   • Parsear emails HTML")

def casos_uso_comunes():
    """Casos de uso más comunes de Beautiful Soup"""
    
    print("\n" + "=" * 50)
    print("🎯 CASOS DE USO COMUNES")
    print("=" * 50)
    
    print("1. Parsear HTML:")
    print("   soup = BeautifulSoup(html_content, 'html.parser')")
    
    print("\n2. Encontrar elementos:")
    print("   soup.find('div', class_='container')")
    print("   soup.find_all('p')")
    print("   soup.select('.class-name')")
    
    print("\n3. Extraer texto:")
    print("   element.get_text()")
    print("   element.string")
    
    print("\n4. Obtener atributos:")
    print("   link.get('href')")
    print("   img.get('src')")
    
    print("\n5. Navegar por DOM:")
    print("   element.parent")
    print("   element.find_next('p')")
    print("   element.find_previous('h2')")
    
    print("\n6. Modificar HTML:")
    print("   element.string = 'Nuevo texto'")
    print("   element.decompose()  # Eliminar")

if __name__ == "__main__":
    # Ejecutar todos los ejemplos
    ejemplo_beautifulsoup_basico()
    ejemplo_beautifulsoup_selectors()
    ejemplo_beautifulsoup_requests()
    ejemplo_beautifulsoup_scraping_practico()
    casos_uso_comunes()
    integracion_con_tax_calculator_pro()
    
    print("\n" + "=" * 50)
    print("✅ RESUMEN DEL MÓDULO beautifulsoup4")
    print("=" * 50)
    print("🔧 Usos principales:")
    print("   • Parsear HTML y XML")
    print("   • Web scraping")
    print("   • Extraer datos estructurados")
    print("   • Navegar por DOM")
    print("   • Modificar contenido HTML")
    print("   • Buscar elementos específicos")
    print("\n📚 Documentación oficial:")
    print("   https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
    print("\n💡 Consejo: Combina con requests para scraping")
    print("   Beautiful Soup + requests = poder total.") 