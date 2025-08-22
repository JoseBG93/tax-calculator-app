"""
GUÍA COMPLETA DE DECORADORES EN PYTHON - BLOQUE 2
@property - CONVERTIR MÉTODOS EN ATRIBUTOS

"""

# ============================================================================
# 2. @property - CONVERTIR MÉTODOS EN ATRIBUTOS
# ============================================================================
#
# CONCEPTO CLAVE: @property convierte un MÉTODO en un ATRIBUTO
# • Sin @property: calc.calcular_suma()    - con paréntesis (método normal)
# • Con @property: calc.suma               - sin paréntesis (como atributo)
#
# VENTAJA PRINCIPAL: CÁLCULO DINÁMICO Y AUTOMÁTICO
# • Sin @property: Resultado FIJO - se calcula una vez y no se actualiza
#   Problema: Necesitas duplicar código (atributo + método) y mantener sincronizado
#   Ejemplo: self.result = self.sum() en __init__ + def sum(self)
# • Con @property: Resultado DINÁMICO - se recalcula automáticamente cada vez
#   Ventaja: Una sola definición, siempre actualizado, sintaxis limpia
#
# PERFECTO PARA IIVTNU: Los cálculos fiscales deben actualizarse cuando cambian los valores
# ============================================================================


class CalculadoraIIVTNU:
    def __init__(self, valor_actual: float, valor_anterior: float, coeficiente: float):
        self._valor_actual = valor_actual
        self._valor_anterior = valor_anterior
        self._coeficiente = coeficiente
    
    @property
    def incremento_valor(self) -> float:
        """Calcula automáticamente el incremento cuando se accede"""
        return self._valor_actual - self._valor_anterior
    
    @property
    def base_imponible(self) -> float:
        """Calcula automáticamente la base imponible"""
        return self.incremento_valor * (self._coeficiente / 100)
    
    @property
    def valor_actual(self) -> float:
        """Getter para valor actual"""
        return self._valor_actual
    
    @valor_actual.setter # 'Setter' es una función que se utiliza para añadir un valor nuevo a un atributo.
    def valor_actual(self, nuevo_valor: float):
        """Setter con validación"""
        if nuevo_valor <= 0:
            raise ValueError("El valor actual debe ser positivo")
        self._valor_actual = nuevo_valor

# Ejemplo de uso
calc = CalculadoraIIVTNU(100000, 80000, 15.5)
print(f"Incremento: {calc.incremento_valor}")  # Se usa como atributo, no como método.
print(f"Base imponible: {calc.base_imponible}")
calc.valor_actual = 120000  # Usa el setter.
print(f"Nueva base imponible: {calc.base_imponible}")

print("\n🎯 RESUMEN BLOQUE 2:")
print("✅ @property convierte métodos en atributos (sin paréntesis)")
print("✅ Cálculos dinámicos que se actualizan automáticamente")
print("✅ Getters y setters con validación")
print("✅ Perfecto para cálculos IIVTNU que deben actualizarse")