"""
GUÍA COMPLETA DE DECORADORES EN PYTHON - BLOQUE 3
@staticmethod y @classmethod - MÉTODOS ESPECIALES
Tax Calculator Pro - Referencia para José
"""

print("="*80)
print("BLOQUE 3: @staticmethod y @classmethod - MÉTODOS ESPECIALES")
print("="*80)

# ============================================================================
# 3. @staticmethod y @classmethod - MÉTODOS ESPECIALES
# ============================================================================
#
# CONCEPTO CLAVE: @staticmethod crea métodos INDEPENDIENTES de la clase e instancia
# • Método normal:    def validar(self, nif): ...     - Necesita instancia (self)
# • Método estático:  @staticmethod def validar(nif): - NO necesita nada
# • Método de clase:  @classmethod def crear(cls):    - Necesita clase (cls)
#
# ¿QUÉ ES @staticmethod?
# • Un método que pertenece a la clase pero funciona INDEPENDIENTEMENTE
# • NO recibe 'self' (instancia) ni 'cls' (clase) como primer parámetro
# • Se puede llamar desde la CLASE directamente: ValidadorTributario.validar_nif("12345678A")
# • Es como una función normal, pero organizada dentro de una clase
#
# ¿CUÁNDO USAR @staticmethod?
# • Funciones de utilidad relacionadas con la clase
# • Validaciones que no dependen de datos específicos de instancia
# • Operaciones que lógicamente pertenecen a la clase pero son independientes
#
# VENTAJAS DE @staticmethod:
# • Organización: Agrupa funciones relacionadas dentro de la clase
# • No necesita crear instancia para usarlo
# • Claridad: Indica que la función no modifica el estado de la clase
# • Eficiencia: Python no necesita pasar 'self' o 'cls'
#
# PERFECTO PARA IIVTNU: Validaciones de NIF, cálculos generales, conversiones
#
# ¿QUÉ ES @classmethod?
# • Un método que recibe la CLASE (cls) como primer parámetro automáticamente
# • cls = la clase misma (ValidadorTributario), NO una instancia específica
# • Se puede llamar desde la CLASE: ValidadorTributario.crear_validador_alfafar()
# • Útil para crear instancias o acceder a datos compartidos de la clase
#
# DIFERENCIA cls vs self:
# • self = UNA instancia específica (objeto individual con sus propios datos)
# • cls = LA clase completa (plantilla compartida por todas las instancias)
#
# ¿CUÁNDO USAR @classmethod?
# • Constructores alternativos: crear instancias de formas específicas
# • Acceder a DATOS DE CLASE: atributos compartidos por todas las instancias
# • Factory methods: métodos que crean y configuran objetos
#
# DATOS DE CLASE vs DATOS DE INSTANCIA:
# • CLASE: MAX_TAX_RATE = 30.0 - mismo valor para TODAS las instancias
# • INSTANCIA: self.municipio = "Alfafar" - valor específico de CADA objeto
#
# ÚTIL PARA IIVTNU: Crear validadores específicos, acceder a límites legales, configuraciones
# ============================================================================

print("\n3. @staticmethod y @classmethod - Métodos especiales")
print("-" * 60)

class ValidadorTributario:
    MAX_TAX_RATE = 30.0  # Constante de clase
    
    def __init__(self, municipio: str):
        self.municipio = municipio
    
    @staticmethod
    def validar_nif(nif: str) -> bool:
        """Método estático - no necesita instancia de la clase"""
        # Validación simple del NIF
        if len(nif) != 9:
            return False
        return nif[:-1].isdigit() and nif[-1].isalpha()
    
    @classmethod
    def crear_validador_alfafar(cls):
        """Método de clase - crea una instancia específica"""
        return cls("Alfafar")
    
    @classmethod
    def obtener_limite_legal(cls) -> float:
        """Accede a constantes de clase"""
        return cls.MAX_TAX_RATE

# Ejemplos de uso
# @staticmethod - se puede usar sin crear instancia
print(f"¿NIF válido? {ValidadorTributario.validar_nif('12345678A')}")

# @classmethod - crea instancias de forma específica
validador = ValidadorTributario.crear_validador_alfafar()
print(f"Validador creado para: {validador.municipio}")
print(f"Límite legal: {ValidadorTributario.obtener_limite_legal()}%")

print("\n🎯 RESUMEN BLOQUE 3:")
print("✅ @staticmethod: Métodos independientes que no necesitan instancia")
print("✅ @classmethod: Métodos que trabajan con la clase, reciben 'cls'")
print("✅ Perfecto para validaciones, constructores alternativos")
print("✅ Organiza funciones relacionadas dentro de la clase")