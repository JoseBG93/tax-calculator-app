# MARCO JURÍDICO IIVTNU - Tax Calculator Pro

## FUNDAMENTOS NORMATIVOS

### Normativa Estatal Básica

#### 1. Ley General Tributaria (LGT)
- **Norma**: Ley 58/2003, de 17 de diciembre, General Tributaria
- **BOE**: BOE-A-2003-23186
- **Ámbito**: Principios y normas jurídicas generales del sistema tributario español
- **Aplicación**: Todas las administraciones tributarias (estatal, autonómica, local)

#### 2. Ley Reguladora de las Haciendas Locales (LRHL)
- **Norma**: Real Decreto Legislativo 2/2004, de 5 de marzo
- **BOE**: BOE-A-2004-4214
- **Ámbito**: Texto refundido de la Ley Reguladora de las Haciendas Locales
- **Aplicación**: Marco regulatorio de los tributos locales

## ARTICULADO ESPECÍFICO IIVTNU

### Artículo 104 - Naturaleza y Hecho Imponible
**Texto Legal**: "Constituye el hecho imponible el incremento de valor que experimenten los terrenos de naturaleza urbana..."

**Elementos del Hecho Imponible**:
- Incremento de valor de terrenos urbanos
- Transmisión de la propiedad por cualquier título
- Constitución o transmisión de derechos reales de goce limitativos del dominio

**Supuestos de No Sujeción**:
- Transmisiones mortis causa a favor de cónyuge, descendientes y adoptados
- Transmisiones lucrativas por causa de muerte a favor de ascendientes, descendientes, cónyuge y hermanos

### Artículo 105 - Exenciones
**Exenciones Objetivas**:
- Estado, Comunidades Autónomas y Entidades Locales
- Organismos autónomos del Estado y entidades de derecho público
- Instituciones que tengan reconocida exención en otros tributos

**Exenciones Subjetivas**:
- Entidades sin fines lucrativos (Ley 49/2002)
- Cooperativas protegidas por legislación de cooperativas

### Artículo 106 - Sujetos Pasivos
**Sujeto Pasivo**:
- **Transmisiones onerosas**: Transmitente (vendedor)
- **Transmisiones gratuitas**: Adquirente (comprador/donatario/heredero)
- **Constitución/transmisión derechos reales**: Titular del derecho real

**Responsabilidad Solidaria**:
- En transmisiones onerosas: Adquirente responde solidariamente
- Límite: Valor real del terreno

### Artículo 107 - Base Imponible
**Métodos de Cálculo**:

#### Método Objetivo (Valores Catastrales)
1. **Valor del suelo en momento de transmisión** (valor catastral actual)
2. **Valor del suelo en momento de adquisición** (valor catastral histórico)
3. **Incremento = Valor actual - Valor anterior**
4. **Aplicación de coeficientes** según período de generación

#### Método Subjetivo (Valores Reales)
- Cuando el contribuyente demuestre que incremento es inferior al resultante de aplicación objetiva
- Requiere prueba del valor real de adquisición y transmisión

**Coeficientes Máximos Vigentes 2025** (RD-ley 8/2023):
- Hasta 1 año: 14%
- Hasta 2 años: 13%
- Hasta 3 años: 12%
- Hasta 4 años: 11%
- Hasta 5 años: 10%
- [Continúa escala descendente hasta máximo legal]

### Artículo 108 - Tipo de Gravamen
**Límites**:
- **Máximo legal**: 30%
- **Determinación**: Ordenanza fiscal municipal
- **Diferenciación**: Posible por categorías de terrenos

**Cuota Íntegra**: Base imponible × Tipo de gravamen
**Cuota Líquida**: Cuota íntegra - Bonificaciones + Recargos

**Bonificaciones Potestativas**:
- **Transmisiones mortis causa familiares**: Hasta 95%
  - Requisitos: Cónyuge, descendientes, adoptados, ascendientes
  - Condición: Vivienda habitual del causante
  - Plazo mantenimiento: Mínimo 3 años

### Artículo 109 - Devengo
**Momento del Devengo**:
- **Transmisiones inter vivos**: Fecha del documento público
- **Transmisiones mortis causa**: Fecha del fallecimiento
- **Subasta judicial**: Fecha de adjudicación

**Período de Imposición**:
- Desde adquisición anterior hasta transmisión actual
- Cómputo: Años completos + meses + días

### Artículo 110 - Gestión
**Competencia**: Ayuntamiento del término municipal donde radique el terreno

**Procedimiento**:
- **Autoliquidación**: Sujeto pasivo calcula e ingresa
- **Liquidación municipal**: Ayuntamiento liquida y notifica
- **Plazos**: Según ordenanza municipal (generalmente 30 días hábiles)

## NORMATIVA RECIENTE RELEVANTE

### Real Decreto-ley 26/2021 (8 noviembre)
**Objeto**: Adaptación a jurisprudencia del Tribunal Constitucional
**Sentencia TC 182/2021**: Declaró inconstitucional el anterior sistema de cálculo
**Cambios**:
- Introducción del método subjetivo alternativo
- Posibilidad de demostrar inexistencia de incremento real
- Nueva configuración de coeficientes máximos

### Real Decreto-ley 8/2023 (27 diciembre)
**Objeto**: Establecimiento de coeficientes máximos para 2024
**Vigencia**: Aplicable a devengos desde 1 enero 2024
**Estado**: VIGENTE para 2025 (tras derogación RD-ley 9/2024)

### Real Decreto-ley 9/2024 (23 diciembre) - DEROGADO
**Objeto**: Actualización coeficientes para 2025
**Estado**: NO CONVALIDADO por Congreso (22 enero 2025)
**Efecto**: Continúan vigentes coeficientes RD-ley 8/2023

## LAGUNAS NORMATIVAS IDENTIFICADAS

### Ordenanzas Municipales Alfafar 2024-2025
**ESTADO**: NO ACCESIBLES

**Fuentes Consultadas**:
- ❌ alfafar.es/normativa-municipal/ (Error 404)
- ❌ alfafar.tributoslocales.es (Portal no accesible)

**Información Pendiente**:
1. **Tipo de gravamen exacto** (hasta 30% máximo legal)
2. **Coeficientes municipales específicos**
3. **Bonificaciones familiares** (porcentaje exacto hasta 95%)
4. **Exenciones locales adicionales**
5. **Procedimientos administrativos**
6. **Plazos de presentación y pago**
7. **Recargos por presentación tardía**

### Impacto en el Proyecto
**ESTRATEGIA ADOPTADA**:
- Implementación según normativa estatal (LRHL)
- Valores de referencia configurables
- Arquitectura preparada para integración municipal específica
- Validación legal contra artículos 104-110 LRHL

**ESCALABILIDAD**:
- Módulo de configuración municipal flexible
- Sistema de actualización normativa
- Validación automática contra límites legales
- Documentación de fuentes jurídicas

## VALIDACIÓN LEGAL DEL PROYECTO

### Cumplimiento Normativo Actual
✅ **Fundamento jurídico sólido** (LGT + LRHL)
✅ **Cálculos conformes** a artículos 104-110
✅ **Coeficientes vigentes** (RD-ley 8/2023)
✅ **Límites legales respetados** (30% máximo, 95% bonificación)

### Pendiente de Completar
🔄 **Ordenanzas Alfafar específicas**
🔄 **Parametrización municipal exacta**
🔄 **Procedimientos administrativos locales**

---

**Documento actualizado**: {{ fecha_actual }}
**Base normativa**: LGT, LRHL y normativa de desarrollo vigente
**Próxima revisión**: Acceso a ordenanzas municipales Alfafar