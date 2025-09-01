"""
IIVTNU Legal Validation Framework

This module deploys a complete legal validation system to calculate IIVTNU tax properly, based on the current regulations (LGT, LRHL) and the specific municipal ordinance of Alfafar.

Legal basis:
- LGT: Law 58/2003, of December 17, General Taxation Law
- LRHL: Royal Legislative Decree 2/2004, of March 5 (Arts. 104-110)
- Royal Decree-Law 8/2023: Maximum coefficients in force for 2025
"""

from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime, date
from dataclasses import dataclass
from enum import Enum
import json


class TransmissionType(Enum): # TIPO DE TRANSMISION
    """Transmission types according to LRHL Art. 104"""
    FOR_CONSIDERATION = "FOR_CONSIDERATION" # A título oneroso (sales)
    DONATION = "DONATION"           # Donación (gifts)
    INHERITANCE = "INHERITANCE"     # Herencia (inheritances)

    @property
    def spanish_translation(self):
        """Returns Spanish legal term"""
        mapping = { 
            self.FOR_CONSIDERATION: "A título oneroso",
            self.DONATION: "Donación",
            self.INHERITANCE: "Herencia"
        }
        return mapping[self]
    
class DegreeOfKinship(Enum): # GRADO DE PARENTESCO
    """Family discounts/reductions according to LRHL Art. 104"""    
    HUSBAND_WIFE = 1
    CHILDREN = 2    # Children, grandchildren
    PARENTS = 3     # Parents, grandparents
    BROTHER = 4
    OTHER = 99


@dataclass
class ValidationResult: # RESULTADO DE LA VALIDACION LEGAL
    """Legal validation result"""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    legal_references: List[str]
    calculated_values: Dict[str, Any]


@dataclass
class IIVTNUCalculationParams: # PARAMETROS DE CÁLCULO DE IIVTNU
    """IIVTNU calculation parameters"""
    
    # Basic data
    transmission_type: TransmissionType
    acquisition_date: date
    transmission_date: date
    
    # Cadastral values
    current_cadastral_value: float
    previous_cadastral_value: float
    
    # Municipal configuration
    tax_rate: float
    family_bonus: Optional[float] = None
    
    # Data for family discounts/reductions
    degree_of_kinship: Optional[DegreeOfKinship] = None
    habitual_residence: bool = False
    maintenance_of_residence: bool = False


class IIVTNULegalValidator: 
    """
    Legal validator for IIVTNU calculations according to current regulations.
    It's not recommended to use @dataclass for this class, because this one does not just keep the data, but also contains a complex business logic which performs legal validations.

    Implements:
    - Validation against LRHL articles 104-110
    - Application of coefficients from Royal Decree-Law 8/2023
    - Maximum legal limits
    - Family bonuses in accordance with the law
    """
    
  
   # Python conventions are the following:
   # 1. We use capital letters for constants.
   # 2. We use lowercase for variables, attributes, parameters, modules, and packages.
   # 3. We use snake_case for functions and methods.
   # 4. We use PascalCase for classes.


    # CONSTANTS
    MAX_TAX_RATE = 30.0  # Art. 108 LRHL
    MAX_FAMILY_BONUS = 95.0  # Bonificación máxima potestativa
    ALFAFAR_TAX_RATE = 29.0  # Art. 11 Ordenanza Alfafar 2022
    ALFAFAR_FAMILY_BONUS_FULL = 95.0  # Art. 12 - Vivienda habitual causante + sujeto pasivo (2022)
    ALFAFAR_FAMILY_BONUS_PARTIAL = 50.0  # Art. 12 - Solo vivienda habitual sujeto pasivo (2022)
    STATE_MAX_COEFFICIENTS = {  # Estos son los coeficientes máximos que pueden aplicar los ayuntamientos en 2025, en virtud del RD-ley 8/2023.
        1: 14.0,   # Hasta 1 año
        2: 13.0,   # Hasta 2 años
        3: 12.0,   # Hasta 3 años
        4: 11.0,   # Hasta 4 años
        5: 10.0,   # Hasta 5 años
        6: 9.5,    # Hasta 6 años
        7: 9.0,    # Hasta 7 años
        8: 8.5,    # Hasta 8 años
        9: 8.0,    # Hasta 9 años
        10: 7.5,   # Hasta 10 años
        11: 7.0,   # Hasta 11 años
        12: 6.5,   # Hasta 12 años
        13: 6.0,   # Hasta 13 años
        14: 5.5,   # Hasta 14 años
        15: 5.0,   # Hasta 15 años
        16: 4.5,   # Hasta 16 años
        17: 4.0,   # Hasta 17 años
        18: 3.5,   # Hasta 18 años
        19: 3.0,   # Hasta 19 años
        20: 2.5,   # 20 años o más
    }
    # NOTA: La Ordenanza 2022 (Art. 5.3) elimina los coeficientes específicos de Alfafar
    # Ahora se aplican directamente los coeficientes máximos estatales vigentes del RD-ley 8/2023
    # con actualización automática según las Leyes de Presupuestos Generales del Estado
    
    def __init__(self, use_alfafar_config: bool = True):
        """
        Inicializa el validador con configuración legal vigente
        
        Args:
            use_alfafar_config: Si True, usa parámetros específicos Alfafar (por defecto)
                              Si False, usa solo normativa estatal
        """
        self.use_alfafar_config = use_alfafar_config
        
        if use_alfafar_config:
            self.legal_references = [
                "LGT: Ley 58/2003, de 17 de diciembre, General Tributaria",
                "LRHL: Real Decreto Legislativo 2/2004, de 5 de marzo",
                "RD-ley 8/2023: Coeficientes máximos IIVTNU 2025",
                "Ordenanza Fiscal IIVTNU Alfafar 2022 (BOP 154 - 17/06/2022)"
            ]
        else:
            self.legal_references = [
                "LGT: Ley 58/2003, de 17 de diciembre, General Tributaria",
                "LRHL: Real Decreto Legislativo 2/2004, de 5 de marzo",
                "RD-ley 8/2023: Coeficientes máximos IIVTNU 2025"
            ]
    
    def validate_calculation(self, params: IIVTNUCalculationParams) -> ValidationResult:
        """
        Valida un cálculo IIVTNU completo contra normativa vigente
        
        Args:
            params: Parámetros del cálculo a validar
            
        Returns:
            ValidationResult con validación completa y valores calculados
        """
        errors = []
        warnings = []
        calculated_values = {}
        
        # 1. Validar parámetros básicos
        basic_validation = self._validate_basic_params(params)
        errors.extend(basic_validation.errors)
        warnings.extend(basic_validation.warnings)
        
        # 2. Calcular período de imposición
        period_result = self._calculate_imposition_period(
            params.fecha_adquisicion, 
            params.fecha_transmision
        )
        calculated_values['periodo_imposicion'] = period_result
        
        # 3. Validar y aplicar coeficientes
        coefficient_result = self._validate_and_calculate_coefficient(period_result['años_completos'])
        if coefficient_result['errors']:
            errors.extend(coefficient_result['errors'])
        calculated_values['coeficiente'] = coefficient_result
        
        # 4. Calcular base imponible
        base_result = self._calculate_base_imponible(
            params.valor_suelo_actual,
            params.valor_suelo_anterior,
            coefficient_result['coeficiente_aplicado']
        )
        calculated_values['base_imponible'] = base_result
        
        # 5. Validar tipo de gravamen
        tax_rate_validation = self._validate_tax_rate(params.tipo_gravamen)
        if tax_rate_validation['errors']:
            errors.extend(tax_rate_validation['errors'])
        calculated_values['tipo_gravamen'] = tax_rate_validation
        
        # 6. Calcular cuota íntegra
        gross_quota = base_result['base_imponible'] * (params.tipo_gravamen / 100)
        calculated_values['cuota_integra'] = gross_quota
        
        # 7. Validar y aplicar bonificaciones
        bonus_result = self._validate_family_bonus(params)
        if bonus_result['errors']:
            errors.extend(bonus_result['errors'])
        if bonus_result['warnings']:
            warnings.extend(bonus_result['warnings'])
        calculated_values['bonificacion'] = bonus_result
        
        # 8. Calcular cuota líquida final
        final_quota = self._calculate_final_quota(gross_quota, bonus_result)
        calculated_values['cuota_final'] = final_quota
        
        # 9. Validar cumplimiento normativo global
        compliance_validation = self._validate_overall_compliance(calculated_values)
        errors.extend(compliance_validation['errors'])
        warnings.extend(compliance_validation['warnings'])
        
        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            legal_references=self.legal_references,
            calculated_values=calculated_values
        )
    
    def _validate_basic_params(self, params: IIVTNUCalculationParams) -> ValidationResult:
        """Validación básica de parámetros según LRHL Art. 104-110"""
        errors = []
        warnings = []
        
        # Validar fechas (Art. 109 LRHL - Devengo)
        if params.fecha_transmision < params.fecha_adquisicion:
            errors.append("LRHL Art. 109: Fecha transmisión anterior a adquisición")
        
        # Validar que hay incremento de valor
        if params.valor_suelo_actual <= params.valor_suelo_anterior:
            warnings.append("LRHL Art. 104: Sin incremento de valor - Posible no sujeción")
        
        # Validar valores positivos
        if params.valor_suelo_actual <= 0 or params.valor_suelo_anterior <= 0:
            errors.append("LRHL Art. 107: Valores de suelo deben ser positivos")
        
        # Validar tipo de gravamen en rango legal
        if not (0 <= params.tipo_gravamen <= self.MAX_TAX_RATE):
            errors.append(f"LRHL Art. 108: Tipo gravamen debe estar entre 0% y {self.MAX_TAX_RATE}%")
        
        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            legal_references=["LRHL Arts. 104, 107, 108, 109"],
            calculated_values={}
        )
    
    def _calculate_imposition_period(self, fecha_adq: date, fecha_trans: date) -> Dict[str, Any]:
        """
        Calcula período de imposición según LRHL Art. 107
        
        Returns:
            Dict con años completos, meses y días del período
        """
        delta = fecha_trans - fecha_adq
        años = delta.days // 365
        días_restantes = delta.days % 365
        meses = días_restantes // 30
        días = días_restantes % 30
        
        return {
            'fecha_inicio': fecha_adq,
            'fecha_fin': fecha_trans,
            'días_totales': delta.days,
            'años_completos': años,
            'meses_adicionales': meses,
            'días_adicionales': días
        }
    
    def _validate_and_calculate_coefficient(self, años: int) -> Dict[str, Any]:
        """
        Valida y calcula coeficiente según normativa aplicable
        
        Args:
            años: Años completos de tenencia
            
        Returns:
            Dict con coeficiente aplicado y validación
        """
        errors = []
        
        if años <= 0:
            errors.append("Período debe ser superior a 0 años")
            coeficiente = 0.0
            referencia = "Error en período"
        elif self.use_alfafar_config:
            # Usar coeficientes máximos estatales (Ordenanza Alfafar 2022 - Art. 5.3)
            coeficiente, referencia = self._get_alfafar_coefficient(años)
        else:
            # Usar coeficientes estatales máximos
            if años <= 19:
                coeficiente = self.STATE_MAX_COEFFICIENTS.get(años, 3.0)
            else:
                coeficiente = self.STATE_MAX_COEFFICIENTS[20]
            referencia = 'RD-ley 8/2023 - Coeficientes máximos estatales'
        
        return {
            'años_tenencia': años,
            'coeficiente_aplicado': coeficiente,
            'referencia_legal': referencia,
            'errors': errors
        }
    
    def _get_alfafar_coefficient(self, años: int) -> Tuple[float, str]:
        """
        Calcula coeficiente según Ordenanza Alfafar 2022 (Art. 5.3) - Coeficientes máximos estatales
        
        CAMBIO IMPORTANTE 2022: Ya no se usan coeficientes específicos de Alfafar.
        Se aplican directamente los coeficientes máximos estatales vigentes.
        
        Args:
            años: Años completos de tenencia
            
        Returns:
            Tuple con (coeficiente_total, referencia_legal)
        """
        años = min(años, 20)  # Máximo 20 años según LRHL
        
        if años in self.STATE_MAX_COEFFICIENTS:
            coeficiente_total = self.STATE_MAX_COEFFICIENTS[años]
        else:
            coeficiente_total = self.STATE_MAX_COEFFICIENTS[20]  # Usar el de 20+ años
        
        return (
            coeficiente_total,
            f'Ordenanza Alfafar 2022 Art. 5.3 - Coeficiente máximo estatal: {coeficiente_total}% ({años} años)'
        )
    
    def _calculate_base_imponible(self, valor_actual: float, valor_anterior: float, coeficiente: float) -> Dict[str, Any]:
        """
        Calcula base imponible según LRHL Art. 107
        
        Returns:
            Dict con cálculo detallado de base imponible
        """
        incremento_valor = valor_actual - valor_anterior
        base_imponible = incremento_valor * (coeficiente / 100)
        
        return {
            'valor_suelo_actual': valor_actual,
            'valor_suelo_anterior': valor_anterior,
            'incremento_valor': incremento_valor,
            'coeficiente_porcentaje': coeficiente,
            'base_imponible': base_imponible,
            'metodo_calculo': 'Objetivo (valores catastrales)',
            'referencia_legal': 'LRHL Art. 107'
        }
    
    def _validate_tax_rate(self, tipo_gravamen: float) -> Dict[str, Any]:
        """Valida tipo de gravamen según normativa aplicable"""
        errors = []
        warnings = []
        
        # Validación básica
        if tipo_gravamen < 0:
            errors.append("Tipo gravamen no puede ser negativo")
        
        if tipo_gravamen > self.MAX_TAX_RATE:
            errors.append(f"LRHL Art. 108: Tipo gravamen {tipo_gravamen}% excede máximo legal {self.MAX_TAX_RATE}%")
        
        # Validación específica Alfafar
        if self.use_alfafar_config:
            if tipo_gravamen != self.ALFAFAR_TAX_RATE:
                warnings.append(f"Ordenanza Alfafar establece tipo gravamen {self.ALFAFAR_TAX_RATE}% (recibido: {tipo_gravamen}%)")
            referencia = 'Ordenanza Alfafar Art. 11 - Tipo gravamen 29%'
            tipo_recomendado = self.ALFAFAR_TAX_RATE
        else:
            referencia = 'LRHL Art. 108 - Máximo 30%'
            tipo_recomendado = self.MAX_TAX_RATE
        
        return {
            'tipo_gravamen': tipo_gravamen,
            'tipo_recomendado': tipo_recomendado,
            'maximo_legal': self.MAX_TAX_RATE,
            'es_valido': len(errors) == 0,
            'errors': errors,
            'warnings': warnings,
            'referencia_legal': referencia
        }
    
    def _validate_family_bonus(self, params: IIVTNUCalculationParams) -> Dict[str, Any]:
        """
        Valida bonificación familiar según LRHL Art. 108
        
        Las bonificaciones familiares son potestativas para los municipios
        """
        errors = []
        warnings = []
        aplicable = False
        porcentaje_bonificacion = 0.0
        
        # Solo aplicable en transmisiones gratuitas mortis causa
        if params.tipo_transmision == TipoTransmision.GRATUITA_MORTIS_CAUSA:
            
            # Validar parentesco directo
            if params.parentesco in [GradoParentesco.CONYUGE, GradoParentesco.DESCENDIENTE, GradoParentesco.ASCENDIENTE]:
                
                # Validar vivienda habitual
                if params.vivienda_habitual:
                    aplicable = True
                    
                    # Usar bonificación según configuración
                    if params.bonificacion_familiar is not None:
                        # Validar contra límite legal máximo
                        if params.bonificacion_familiar > self.MAX_FAMILY_BONUS:
                            errors.append(f"Bonificación {params.bonificacion_familiar}% excede máximo legal {self.MAX_FAMILY_BONUS}%")
                        else:
                            porcentaje_bonificacion = params.bonificacion_familiar
                    else:
                        # Usar bonificación específica según configuración
                        if self.use_alfafar_config:
                            porcentaje_bonificacion = self.ALFAFAR_FAMILY_BONUS
                            warnings.append(f"Aplicando bonificación Alfafar: {self.ALFAFAR_FAMILY_BONUS}%")
                        else:
                            porcentaje_bonificacion = self.MAX_FAMILY_BONUS
                            warnings.append("Usando bonificación máxima legal - verificar ordenanza municipal")
                    
                    # Validar mantenimiento vivienda
                    if not params.mantenimiento_vivienda:
                        warnings.append("Verificar compromiso mantenimiento vivienda 3 años")
                
                else:
                    warnings.append("Bonificación familiar requiere vivienda habitual del causante")
            else:
                warnings.append("Bonificación familiar solo para parentesco directo")
        
        # Determinar referencia legal según configuración
        if self.use_alfafar_config and aplicable:
            referencia_legal = 'Ordenanza Alfafar Art. 12 - Bonificación 50% herencias familiares'
        else:
            referencia_legal = 'LRHL Art. 108 - Bonificaciones potestativas'
        
        return {
            'aplicable': aplicable,
            'porcentaje': porcentaje_bonificacion,
            'tipo_transmision': params.tipo_transmision.value,
            'parentesco': params.parentesco.value if params.parentesco else None,
            'vivienda_habitual': params.vivienda_habitual,
            'errors': errors,
            'warnings': warnings,
            'referencia_legal': referencia_legal
        }
    
    def _calculate_final_quota(self, cuota_integra: float, bonificacion: Dict[str, Any]) -> Dict[str, Any]:
        """Calcula cuota líquida final aplicando bonificaciones"""
        
        if bonificacion['aplicable']:
            importe_bonificacion = cuota_integra * (bonificacion['porcentaje'] / 100)
            cuota_liquida = cuota_integra - importe_bonificacion
        else:
            importe_bonificacion = 0.0
            cuota_liquida = cuota_integra
        
        return {
            'cuota_integra': cuota_integra,
            'bonificacion_aplicada': bonificacion['aplicable'],
            'porcentaje_bonificacion': bonificacion['porcentaje'],
            'importe_bonificacion': importe_bonificacion,
            'cuota_liquida': cuota_liquida,
            'referencia_legal': 'LRHL Art. 108'
        }
    
    def _validate_overall_compliance(self, calculated_values: Dict[str, Any]) -> Dict[str, List[str]]:
        """Validación final de cumplimiento normativo global"""
        errors = []
        warnings = []
        
        # Verificar coherencia de resultados
        if calculated_values.get('cuota_final', {}).get('cuota_liquida', 0) < 0:
            errors.append("Cuota líquida negativa - revisar cálculo")
        
        # Verificar incremento mínimo
        base_imponible = calculated_values.get('base_imponible', {}).get('base_imponible', 0)
        if base_imponible <= 0:
            warnings.append("Base imponible nula o negativa - posible no sujeción al impuesto")
        
        return {
            'errors': errors,
            'warnings': warnings
        }
    
    def get_legal_summary(self) -> Dict[str, Any]:
        """
        Retorna resumen del marco legal implementado
        
        Returns:
            Dict con resumen normativo completo
        """
        if self.use_alfafar_config:
            return {
                'configuracion_activa': 'ALFAFAR_2006',
                'normativa_primaria': {
                    'LGT': 'Ley 58/2003, de 17 de diciembre, General Tributaria',
                    'LRHL': 'Real Decreto Legislativo 2/2004, de 5 de marzo',
                    'ordenanza_municipal': 'Alfafar IIVTNU (BOP 31/12/2005)'
                },
                'parametros_alfafar': {
                    'tipo_gravamen': f'{self.ALFAFAR_TAX_RATE}%',
                    'bonificacion_familiar': f'{self.ALFAFAR_FAMILY_BONUS}%',
                    'coeficientes': 'Sistema 2006 (3,1% - 2,8% - 2,7%)',
                    'periodo_maximo': '20 años',
                    'plazos_autoliquidacion': '30 días hábiles / 6 meses'
                },
                'validacion_implementada': {
                    'normativa_municipal': True,
                    'calculo_realista': True,
                    'parametros_especificos': True,
                    'simulacion_trabajo_real': True
                }
            }
        else:
            return {
                'configuracion_activa': 'ESTATAL_2023',
                'normativa_primaria': {
                    'LGT': 'Ley 58/2003, de 17 de diciembre, General Tributaria',
                    'LRHL': 'Real Decreto Legislativo 2/2004, de 5 de marzo',
                    'articulado_iivtnu': 'Arts. 104-110'
                },
                'normativa_secundaria': {
                    'coeficientes_2025': 'Real Decreto-ley 8/2023, de 27 de diciembre',
                    'jurisprudencia': 'STC 182/2021 - Inconstitucionalidad sistema anterior'
                },
                'limites_legales': {
                    'tipo_gravamen_maximo': f'{self.MAX_TAX_RATE}%',
                    'bonificacion_familiar_maxima': f'{self.MAX_FAMILY_BONUS}%',
                    'coeficientes_estatales': 'Tabla RD-ley 8/2023'
                },
                'validacion_implementada': {
                    'cumplimiento_lrhl': True,
                    'limites_estatales': True,
                    'bonificaciones_conformes': True,
                    'arquitectura_escalable': True
                }
            }


# Funciones de utilidad para integración con el sistema

def validate_herencia_document(herencia_data: Dict[str, Any]) -> ValidationResult:
    """
    Valida un documento JSON de herencia contra normativa IIVTNU
    
    Args:
        herencia_data: Diccionario con datos del documento de herencia
        
    Returns:
        ValidationResult con validación completa
    """
    validator = IIVTNULegalValidator()
    
    # Extraer datos del JSON
    try:
        calculo_iivtnu = herencia_data.get('calculo_iivtnu', {})
        transmision_anterior = herencia_data.get('transmision_anterior_causante', {})
        heredero = herencia_data.get('heredero', {})
        inmueble = herencia_data.get('inmueble_heredado', {})
        
        # Convertir a parámetros de validación
        params = IIVTNUCalculationParams(
            tipo_transmision=TipoTransmision.GRATUITA_MORTIS_CAUSA,
            fecha_adquisicion=datetime.strptime(transmision_anterior.get('fecha_adquisicion'), '%Y-%m-%d').date(),
            fecha_transmision=datetime.strptime(herencia_data.get('fecha_documento'), '%Y-%m-%d').date(),
            valor_suelo_actual=inmueble.get('valoracion_catastral_actual', {}).get('valor_suelo_actual', 0),
            valor_suelo_anterior=transmision_anterior.get('valor_suelo_anterior', 0),
            tipo_gravamen=calculo_iivtnu.get('liquidacion', {}).get('tipo_gravamen', 30.0),
            bonificacion_familiar=calculo_iivtnu.get('liquidacion', {}).get('porcentaje_bonificacion'),
            parentesco=GradoParentesco.DESCENDIENTE if 'hijo' in heredero.get('parentesco', '') else GradoParentesco.OTROS,
            vivienda_habitual=inmueble.get('uso_actual') == 'vivienda_habitual',
            mantenimiento_vivienda=True  # Asumir cumplimiento para validación
        )
        
        return validator.validate_calculation(params)
        
    except Exception as e:
        return ValidationResult(
            is_valid=False,
            errors=[f"Error procesando documento: {str(e)}"],
            warnings=[],
            legal_references=[],
            calculated_values={}
        )


def get_municipal_config_template() -> Dict[str, Any]:
    """
    Genera plantilla de configuración municipal para Alfafar
    
    Returns:
        Dict con estructura para configuración específica de Alfafar
    """
    return {
        'municipio': {
            'nombre': 'Alfafar',
            'codigo_ine': '46009',
            'provincia': 'Valencia',
            'comunidad_autonoma': 'Comunidad Valenciana'
        },
        'ordenanza_fiscal': {
            'año': '2024-2025',
            'estado': 'PENDIENTE_ACCESO',
            'url_oficial': 'https://alfafar.es/normativa-municipal/',
            'fecha_vigencia': '2024-01-01'
        },
        'parametros_iivtnu': {
            'tipo_gravamen': {
                'vivienda': None,  # PENDIENTE - hasta 30.0
                'local_comercial': None,  # PENDIENTE - hasta 30.0
                'otros': None  # PENDIENTE - hasta 30.0
            },
            'bonificaciones': {
                'herencia_familiar': None,  # PENDIENTE - hasta 95.0
                'vivienda_habitual': None,  # PENDIENTE - hasta 95.0
                'otros': []
            },
            'coeficientes': {
                'usa_estatales': True,  # Por defecto hasta obtener específicos
                'tabla_municipal': None  # PENDIENTE
            }
        },
        'procedimientos': {
            'plazo_presentacion': None,  # PENDIENTE - días hábiles
            'recargos_demora': None,  # PENDIENTE - porcentajes
            'formas_pago': []  # PENDIENTE
        },
        'validacion': {
            'fuente_datos': 'NORMATIVA_ESTATAL',  # Hasta obtener municipal
            'fecha_ultima_actualizacion': None,
            'responsable_actualizacion': 'José - Funcionario Municipal'
        }
    }