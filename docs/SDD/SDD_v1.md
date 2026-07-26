# Documento de Diseño del Software

**Proyecto:** Aplicación para la gestión de cobranzas en campo  
**Versión:** 1.0  
**Estado:** Candidato a línea base  
**Fecha:** 26 de julio de 2026  

## 1. Objetivo

Describir el diseño inicial y las decisiones técnicas de una aplicación orientada a la consulta, priorización y registro de cobranzas en campo para Dermafreya S. A.

## 2. Arquitectura

Se utilizará una arquitectura simple organizada en tres componentes:

- **Presentación:** permite al usuario visualizar la información de las cobranzas.
- **Lógica de negocio:** procesa los días de mora y el valor pendiente para determinar la prioridad.
- **Datos:** representa la información de clientes, documentos pendientes, gestiones y compromisos de pago.

## 3. Componentes principales

### 3.1 Consulta de cartera

Muestra los clientes y los valores pendientes de cobro.

### 3.2 Priorización de cobranzas

Clasifica las cobranzas según los días de mora y el valor pendiente.

### 3.3 Gestión de cobro

Registra la fecha, el tipo y el resultado de las acciones realizadas.

### 3.4 Compromisos de pago

Registra el valor, la fecha acordada y el estado de cada compromiso.

## 4. Decisiones técnicas

- Se utilizará Python 3.12 para la implementación mínima.
- El código fuente se almacenará en la carpeta `src`.
- Los requisitos y el diseño se documentarán en formato Markdown.
- La configuración de ejemplo se mantendrá separada del código.
- Git permitirá controlar las versiones y establecer la línea base mediante el tag `v1.0`.

## 5. Relación con los requisitos

Los componentes definidos permiten atender los requisitos REQ-001 a REQ-006 establecidos en el documento SRS.

## 6. Estado del diseño

Este diseño será considerado aprobado cuando sea revisado, registrado mediante un commit y asociado con la línea base v1.0.