# LAGUNAS NORMATIVAS IDENTIFICADAS
## Tax Calculator Pro - Alfafar IIVTNU

---

## 🚨 ESTADO CRÍTICO: ORDENANZAS MUNICIPALES NO ACCESIBLES

### Información Faltante Crítica

#### Ordenanzas Fiscales del Ayuntamiento de Alfafar 2024-2025

**ESTADO**: ❌ **NO ACCESIBLES**

**Fuentes Consultadas sin Éxito**:

1. **Portal Municipal Principal**
   - URL: alfafar.es/normativa-municipal/
   - Estado: **Error 404 - Página no encontrada**
   - Fecha consulta: 2025-01-13
   - Error: Recurso no disponible

2. **Oficina Virtual Tributaria**
   - URL: alfafar.tributoslocales.es
   - Estado: **Portal no accesible**
   - Fecha consulta: 2025-01-13
   - Error: Contenido no cargable (spinner infinito)

3. **Búsquedas Alternativas**
   - Google: "ordenanzas fiscales Alfafar 2024 IIVTNU"
   - BOE: Sin resultados específicos para Alfafar
   - DOGV: No consultado sistemáticamente

---

## 📋 DATOS ESPECÍFICOS PENDIENTES

### 1. Parámetros Fiscales IIVTNU

#### Tipos de Gravamen
- **Pendiente**: Tipo de gravamen específico de Alfafar
- **Límite Legal**: Máximo 30% (LRHL Art. 108)
- **Proyecto**: Usando 30% como referencia por defecto
- **Impacto**: CRÍTICO - afecta directamente al cálculo de cuotas

#### Coeficientes Municipales
- **Pendiente**: Tabla de coeficientes específica de Alfafar
- **Marco Legal**: RD-ley 8/2023 (coeficientes máximos estatales)
- **Proyecto**: Usando coeficientes máximos estatales
- **Impacto**: ALTO - puede diferir de la realidad municipal

### 2. Bonificaciones y Exenciones

#### Bonificaciones Familiares
- **Pendiente**: Porcentaje exacto aplicado en Alfafar
- **Límite Legal**: Máximo 95% (potestativa municipal)
- **Proyecto**: Usando 95% como referencia
- **Impacto**: ALTO - beneficio directo para contribuyentes

#### Requisitos Específicos
- **Pendiente**: Condiciones exactas para bonificaciones
- **Marco Legal**: Vivienda habitual + mantenimiento 3 años
- **Proyecto**: Aplicando requisitos legales mínimos
- **Impacto**: MEDIO - criterios de aplicación

#### Exenciones Locales Adicionales
- **Pendiente**: Exenciones específicas más allá de la ley
- **Marco Legal**: Artículo 105 LRHL (exenciones mínimas)
- **Proyecto**: Solo exenciones legales básicas
- **Impacto**: BAJO - posibles beneficios adicionales

### 3. Procedimientos Administrativos

#### Plazos de Presentación
- **Pendiente**: Plazos específicos de Alfafar
- **Referencia**: Habitualmente 30 días hábiles
- **Proyecto**: Usando plazos estándar
- **Impacto**: MEDIO - gestión de expedientes

#### Recargos por Demora
- **Pendiente**: Porcentajes específicos de recargo
- **Marco Legal**: LGT (recargos generales)
- **Proyecto**: Aplicando LGT estándar
- **Impacto**: MEDIO - penalizaciones

#### Formas de Pago
- **Pendiente**: Métodos de pago aceptados
- **Estándar**: Transferencia, domiciliación, presencial
- **Proyecto**: Configuración genérica
- **Impacto**: BAJO - funcionalidad administrativa

---

## 🛠️ ESTRATEGIA DE MITIGACIÓN ADOPTADA

### Implementación con Parámetros Configurables

#### 1. Valores por Defecto Legalmente Conformes
```python
# config.py - Configuración actual
IIVTNU_DEFAULT_TAX_RATE = 30.0  # Máximo legal
IIVTNU_DEFAULT_FAMILY_BONUS = 95.0  # Máximo legal
MUNICIPALITY_NAME = 'Alfafar'
MUNICIPALITY_CODE = '46009'  # INE
```

#### 2. Arquitectura Escalable
- **Módulo de configuración municipal** independiente
- **Sistema de validación legal** contra límites LRHL
- **Estructura preparada** para integración específica
- **Documentación de fuentes** para trazabilidad

#### 3. Validación Normativa
- **Cumplimiento LRHL** artículos 104-110
- **Coeficientes estatales vigentes** (RD-ley 8/2023)
- **Límites legales respetados** en todos los cálculos
- **Base jurídica sólida** para escalabilidad

---

## 📅 PLAN DE RESOLUCIÓN

### Acciones Inmediatas Requeridas

#### 1. Contacto Directo con Ayuntamiento
- **Objetivo**: Obtener ordenanzas fiscales vigentes 2024-2025
- **Método**: Contacto telefónico + presencial si necesario
- **Responsable**: José (empleado municipal con acceso)
- **Prioridad**: ALTA

#### 2. Búsqueda en Fuentes Oficiales Alternativas
- **DOGV** (Diario Oficial Generalitat Valenciana)
- **BOP Valencia** (Boletín Oficial Provincial)
- **Portal transparencia** municipal
- **Registro municipal** de ordenanzas

#### 3. Consulta a Colegas/Departamento
- **GTT/Gestiona** - compañeros de José
- **Departamento tributario** interno
- **Asesoría jurídica** municipal
- **Otros municipios** de referencia (Valencia, Sagunto)

### Información Específica a Solicitar

#### Documentos Necesarios
1. **Ordenanza Fiscal nº X** - IIVTNU vigente 2024-2025
2. **Tabla de coeficientes** municipal actualizada
3. **Baremos de bonificaciones** familiares
4. **Procedimientos administrativos** específicos
5. **Modelos de liquidación** y autoliquidación

#### Datos Numéricos Críticos
- Tipo de gravamen exacto (≤ 30%)
- Porcentaje bonificación familiar (≤ 95%)
- Coeficientes municipales vs. estatales
- Recargos por presentación tardía
- Plazos administrativos específicos

---

## 🎯 IMPACTO EN EL PROYECTO

### Estado Actual: VIABLE CON LIMITACIONES

#### ✅ Fortalezas Mantenidas
- **Base legal sólida** (LGT + LRHL completo)
- **Cálculos conformes** a normativa estatal
- **Arquitectura escalable** para integración municipal
- **Validación jurídica** implementada

#### ⚠️ Limitaciones Temporales
- **Parámetros de referencia** en lugar de exactos
- **Bonificaciones máximas** como estándar
- **Procedimientos genéricos** vs. específicos municipales

#### 🚀 Potencial de Mejora
- **Integración inmediata** una vez obtenidas ordenanzas
- **Parametrización exacta** con datos reales
- **Validación específica** contra normativa local
- **Funcionalidad completa** sin cambios arquitectónicos

### Valor del Proyecto Actual

#### Para Portfolio/Demostración
- **✅ COMPLETO**: Demuestra dominio técnico y legal
- **✅ ESCALABLE**: Arquitectura profesional preparada
- **✅ REALISTA**: Gestión transparente de limitaciones
- **✅ DOCUMENTADO**: Marco jurídico completo

#### Para Implementación Real
- **⚠️ PENDIENTE**: Requiere ordenanzas específicas
- **✅ PREPARADO**: Base sólida para despliegue rápido
- **✅ CONFORME**: Cumple normativa estatal vigente
- **✅ VALIDADO**: Contra fuentes jurídicas oficiales

---

## 📞 CONTACTOS PARA RESOLUCIÓN

### Ayuntamiento de Alfafar
- **Dirección**: Plaza de la Constitución, 1 - 46910 Alfafar
- **Teléfono**: 96 121 51 00
- **Email**: ayuntamiento@alfafar.es
- **Horario**: L-V 9:00-14:00

### Departamento Tributario
- **Responsable**: José (contacto directo interno)
- **Expedientes**: IIVTNU y tributos locales
- **Software**: GTT/Gestiona (experiencia previa)

### Fuentes Oficiales Alternativas
- **DOGV**: dogv.gva.es
- **BOP Valencia**: bop.dival.es
- **Portal Transparencia**: (verificar disponibilidad)

---

**Documento creado**: 2025-01-13  
**Estado**: ACTIVO - Pendiente resolución  
**Próxima revisión**: Tras obtención ordenanzas municipales  
**Responsable actualización**: José (usuario del proyecto)