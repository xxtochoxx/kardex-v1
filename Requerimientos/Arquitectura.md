# Autor

<img src="jenkins_cholo.png" alt="Humberto Melendez" width="100" height="100" align="left"/>

<br>

> Humberto Melendez

<br>


# Introducción

Este documento describe la arquitectura del sistema, incluyendo diagramas, componentes, flujos principales y lineamientos técnicos. Está orientado a ofrecer una visión clara y estructurada del funcionamiento interno del proyecto.

# 🏗️ Arquitectura General

La arquitectura está basada en microservicios, permitiendo escalabilidad y fácil integración con servicios externos [por aahora desestimado]

🔧 Componentes Principales

```bash

[first] crear funciones python que se puedan ejecutar ebn vsc

[En una siguiente etapa]API Gateway / API Bus: [Descripción]

Backend / Microservicios: [Descripción]

Base de Datos: [Descripción]

Sistema de Logs y Trazabilidad: [Descripción]

Servicios Externos: [Descripción]
```

# 🗂️ Diagrama de Arquitectura TO-BE

Incluye aquí el archivo correspondiente:

![Architecture Diagram](./docs/architecture.png)
📘 Descripción del Flujo

El usuario inicia una petición desde el Frontend.

El API Gateway enruta y controla el tráfico.

El Backend procesa la lógica del negocio.

Los logs se registran en el sistema de trazabilidad.[proponer solución a nivel capa free]


# 🔁 Diagramas de Secuencia

Se utilizarán diagramas UML para representar interacciones actor–sistema.

![Sequence Diagram](./docs/sequence-main.png)
Tipos de diagramas recomendados


```bash

Diagrama de componentes

Diagrama de secuencia

Diagrama arquitectura de componentes

```