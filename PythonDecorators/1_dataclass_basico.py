"""
GUÍA COMPLETA DE DECORADORES EN PYTHON - BLOQUE 1
@dataclass - EL MÁS IMPORTANTE PARA NUESTRO PROYECTO
Tax Calculator Pro - Referencia para José

Un decorador es una función que modifica o extiende el comportamiento
de otra función o clase SIN cambiar su código interno.

Sintaxis: @nombre_decorador se coloca justo ANTES de la función/clase
"""

from dataclasses import dataclass

print("="*80)
print("BLOQUE 1: @dataclass - DECORADOR FUNDAMENTAL")
print("="*80)

# ============================================================================
# 1. @dataclass - EL MÁS IMPORTANTE PARA NUESTRO PROYECTO
# ============================================================================
#
# MÉTODOS QUE ENGLOBA @dataclass:
# • __init__()     - Constructor de la clase                    → ACTIVADO por defecto (init=True)
# • __repr__()     - Representación legible del objeto         → ACTIVADO por defecto (repr=True)
# • __eq__()       - Comparación de igualdad por contenido     → ACTIVADO por defecto (eq=True)
# • __hash__()     - Identificador numérico para diccionarios  → DESACTIVADO por defecto (unsafe_hash=False)
# • __lt__()       - Comparación "menor que" (<)               → DESACTIVADO por defecto (order=False)
# • __le__()       - Comparación "menor o igual" (<=)          → DESACTIVADO por defecto (order=False)
# • __gt__()       - Comparación "mayor que" (>)               → DESACTIVADO por defecto (order=False)
# • __ge__()       - Comparación "mayor o igual" (>=)          → DESACTIVADO por defecto (order=False)
# • __post_init__()- Método ejecutado después del constructor  → MANUAL (debes definirlo tú)
# • frozen=True    - Hace el objeto inmutable                  → DESACTIVADO por defecto (frozen=False)
#
# EJEMPLO DE USO CON PARÁMETROS:
# @dataclass(init=True, repr=True, eq=True, order=True, frozen=True, unsafe_hash=True)
# ============================================================================

print("\n1. @dataclass - Para crear clases de datos automáticamente")
print("-" * 60)

# SIN @dataclass (tedioso)
class PersonaSinDecorador:
    def __init__(self, nombre: str, edad: int, ciudad: str): # 'init' es un método especial que se ejecuta cuando se crea una instancia de una clase. Se le pasa el nombre, la edad y la ciudad como parámetros.
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    
    def __repr__(self): # 'repr' significa 'representación'. Es un método especial que se ejecuta cuando se imprime un objeto, y sirve para mostrar el objeto de una forma legible, en formato de cadena de texto.
        # Si no se define este método, se imprimiría algo como <__main__.PersonaSinDecorador object at 0x7f8160123456>.
        return f"PersonaSinDecorador(nombre='{self.nombre}', edad={self.edad}, ciudad='{self.ciudad}')"
    
    def __eq__(self, other): # 'eq' significa 'igualdad'. Es un método especial que se ejecuta cuando se comparan dos objetos en cuanto a su contenido, y devuelve un valor booleano. 
        # Si no se invoca este método, se compararán, por defecto, en cuanto a su dirección en espacio físico de memoria, por lo que, aunque tengan mismo contenido, serán diferentes, devolviendo False.
        if not isinstance(other, PersonaSinDecorador):
            return False
        return self.nombre == other.nombre and self.edad == other.edad and self.ciudad == other.ciudad
    
    def __hash__(self): # Un 'hash' es un número único, valor entero, generado por Python, que identifica un objeto en concreto.
        # En este caso, 'hash' es un método especial dentro del decorador 'dataclass' que habilita a Python para realizar el cálculo del hash de cada objeto.
        # Cada objeto tiene sus propios atributos. En este caso, el objeto PersonaSinDecorador tiene los atributos 'nombre', 'edad' y 'ciudad'. 
        # El hash se calcula a partir del valor de esos atributos. Si se añade un nuevo atributo o se modifica alguno de los ya existentes, Python recalculará el hash.
        # Entre dos objetos 'Persona' que tengan los mismos atributos, y estos atributos los mismos valores, sendos hashes serán identicos.
        # Pero si se añade un nuevo atributo a uno de los objetos, o se modifica alguno de los atributos ya existentes, el hash del objeto 'Persona' que haya cambiado
        # se recalculará, por lo que sendos hashes serán diferentes.
        # Si no se declara este método (en caso de no invocar el decorador) o si no se le pasa este parámetro al decorador dentro de paréntesis, con valor 'True',
        # el hash se referirá, por defecto, a una dirección del espacio físico de memoria, por lo que, aunque dos objetos tengan exactaemente el mismo contenido, tanto en
        # atributos como en valores de éstos, sendos hashes serán diferentes, por apuntar a espacios de memoria distintos.
        # En resumen: 
        #       - Sin __hash__(): Objetos idénticos → hashes diferentes (usa memoria). 
        #       - Con __hash__(): Objetos idénticos → hashes iguales (usa contenido).
        

        return hash((self.nombre, self.edad, self.ciudad))

# CON @dataclass (automático)
@dataclass
class PersonaConDecorador:
    nombre: str
    edad: int
    ciudad: str = "Valencia"  # Valor por defecto

# Ejemplo de uso
p1 = PersonaConDecorador("José", 30, "Alfafar")
p2 = PersonaConDecorador("María", 25)  # Usa valor por defecto
print(f"Con @dataclass: {p1}")
print(f"Con valor por defecto: {p2}")
print(f"¿Son iguales? {p1 == p2}")

# @dataclass con configuraciones avanzadas
@dataclass(frozen=True)  # Inmutable - no se puede modificar después de crear
class ConfiguracionImpuesto:
    tipo_gravamen: float
    bonificacion_familiar: float
    municipio: str = "Alfafar"

config = ConfiguracionImpuesto(29.0, 50.0)
print(f"Configuración inmutable: {config}")
# config.tipo_gravamen = 30.0  # ¡ERROR! No se puede cambiar

print("\n🎯 RESUMEN BLOQUE 1:")
print("✅ @dataclass automatiza la creación de clases de datos")
print("✅ Genera automáticamente __init__, __repr__, __eq__ y más")
print("✅ Perfecto para modelos de datos del Tax Calculator Pro")
print("✅ Opciones frozen=True para inmutabilidad")