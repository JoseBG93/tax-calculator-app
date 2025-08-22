"""
GUÍA COMPLETA DE DECORADORES EN PYTHON - BLOQUE 6
@dataclass CON VALIDACIÓN - PARA MODELOS DE DATOS COMPLEJOS

"""

from dataclasses import dataclass, field # 'Field' es una función que se utiliza para definir los campos de la clase, es decir, sus atributos.
from typing import List # 'List' es un tipo de dato que se utiliza para definir listas. Si no se le da ningún argumento, se crea una lista vacía.


# ============================================================================
# 6. @dataclass CON VALIDACIÓN - PARA MODELOS DE DATOS COMPLEJOS
# ============================================================================

@dataclass
class TransmisionInmobiliaria:
    """Modelo de datos para transmisiones inmobiliarias con validación"""
    nif_transmitente: str
    nif_adquirente: str
    valor_actual: float
    valor_anterior: float
    fecha_adquisicion: str
    fecha_transmision: str
    tipo_transmision: str = "onerosa" # 'onerosa' es el valor por defecto de la variable 'tipo_transmision'.
    municipio: str = "Alfafar" # 'Alfafar' es el valor por defecto de la variable 'municipio'.
    
    # EXPLICACIÓN: field(default_factory=list) crea una NUEVA lista vacía [] para CADA objeto
    # Sin field(): Todos los objetos compartirían la misma lista (peligroso)
    # Con field(): Cada objeto tiene su propia lista independiente (correcto)
    # default_factory=list ejecuta list() cada vez que se crea una nueva instancia
    errores_validacion: List[str] = field(default_factory=list) # This is also an attribute of the class.
    
    def __post_init__(self):
        """Se ejecuta automáticamente después de crear la instancia."""
        self._validar_datos()
    
    def _validar_datos(self):
        """Validación automática de datos"""
        if self.valor_actual <= 0:
            self.errores_validacion.append("Valor actual debe ser positivo")
        if self.valor_anterior <= 0:
            self.errores_validacion.append("Valor anterior debe ser positivo")
        if self.valor_actual <= self.valor_anterior:
            self.errores_validacion.append("No hay incremento de valor")
        if len(self.nif_transmitente) != 9:
            self.errores_validacion.append("NIF transmitente inválido")
    
    @property
    def es_valida(self) -> bool:
        """Indica si la transmisión es válida"""
        return len(self.errores_validacion) == 0
    
    @property
    def incremento_valor(self) -> float:
        """Calcula el incremento de valor"""
        return self.valor_actual - self.valor_anterior

# Ejemplo de uso
transmision = TransmisionInmobiliaria(
    nif_transmitente="12345678A",
    nif_adquirente="87654321B",
    valor_actual=120000,
    valor_anterior=100000,
    fecha_adquisicion="2020-01-15",
    fecha_transmision="2024-01-15"
)

print(f"Transmisión válida: {transmision.es_valida}")
print(f"Incremento de valor: {transmision.incremento_valor}")
if transmision.errores_validacion:
    print(f"Errores encontrados: {transmision.errores_validacion}")

print("\n🎯 RESUMEN BLOQUE 6:")
print("✅ @dataclass + field(default_factory=list) para listas automáticas")
print("✅ __post_init__() se ejecuta automáticamente después del constructor")
print("✅ Validación automática de datos en la creación")
print("✅ Combinación perfecta con @property para cálculos dinámicos")
print("✅ Modelo completo para entidades del Tax Calculator Pro")