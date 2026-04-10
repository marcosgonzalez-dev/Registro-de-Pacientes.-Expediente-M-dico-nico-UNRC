# 🏥 Sistema de Registro de Pacientes

Este proyecto consiste en un módulo en etapa temprana para abordar el expediente médico electrónico para la plataforma de salud del SECEN.
En particular, el archivo de agendar citas y gestionar citas representan un **primer diseño y un acercamiento preliminar** a la solución hacia un Expediente Médico Único, sentando las bases para una futura **interoperabilidad de sistemas de salud entre el sector público y el sector privado**.

Está diseñado bajo el paradigma de **Programación Funcional**, aplicando una estructura **modular** que garantiza la legibilidad del código y facilita su escalabilidad futura.

## 🚀 Características Principales

- **Paradigma Funcional:** Se hizo uso de una función principal para el registro de pacientes, la cual se encarga de solicitar y validar los datos del paciente.
- **Modularización:** La estructura se dividió en bloques lógicos de validación, lo que permite extraer componentes fácilmente en el futuro.
- **Robustez:** Implementación de bloques `try-except-finally` para el manejo de excepciones (como `KeyboardInterrupt` o errores inesperados).
- **Manejo del flujo de la aplicación con Match-Case:** Se aprovecha el _Structural Pattern Matching_ (Python 3.10+) para un control de flujo más claro y moderno mediante "guardas".

## 📊 Especificación de Variables

En esta etapa del desarrollo, todas las entradas se capturan como `str` para permitir una limpieza de datos eficiente (`.strip()`). Sin embargo, las reglas de negocio exigen formatos específicos:

| Variable                  | Tipo   | Descripción                               | Regla de Validación                    |
| :------------------------ | :----- | :---------------------------------------- | :------------------------------------- |
| `base_datos_pacientes`    | `dict` | Almacenamiento de datos de los pacientes. | Clave: `NSS`, Valor: Objeto Paciente.  |
| `numero_seguridad_social` | `str`  | ID del paciente.                          | Solo números, mínimo 10 dígitos.       |
| `nombre_completo`         | `str`  | Identificación legal.                     | Mínimo 8 caracteres.                   |
| `edad`                    | `str`  | Edad del paciente.                        | Validada como contenido numérico.      |
| `consultorio`             | `str`  | Consultorio asignado al paciente.         | Debe ser un número entero entre 1 y 9. |

## 🛠️ Cómo ejecutar el proyecto

1.  Asegúrate de tener instalado **Python 3.10** o superior.

2.  Clona este repositorio:
    ```bash
    git clone [https://github.com/marcosgonzalez-dev/Registro-de-Pacientes.-Expediente-M-dico-nico-UNRC.git](https://github.com/marcosgonzalez-dev/Registro-de-Pacientes.-Expediente-M-dico-nico-UNRC.git)
    ```
3.  Ejecuta el script principal:
    ```bash
    python gestionar_citas.py
    ```

## 🛡️ Manejo de Errores

El código está protegido contra:

- **Cierres inesperados:** Captura de `Ctrl+C`.
- **Entradas vacías:** No permite el avance si los campos se encuentran vacíos.
- **Tipado incorrecto:** Se filtran caracteres no numéricos en campos que requieren cifras.

---

## ⚙️ Justificación Técnica de Decisiones de Diseño

El diseño de las validaciones y el flujo en `gestionar_citas.py` se fundamenta en principios sólidos de ingeniería de software:

- **Eficiencia y Escalabilidad (Ciclo `while True`):** Se emplean bucles infinitos controlados para retener el flujo de ejecución sincrónico hasta obtener datos íntegros. A diferencia de las funciones recursivas (que generan _stack overflow_ consumiendo memoria tras repetidas fallas en el input), un patrón iterativo es trivial en el uso de memoria RAM (O(1) en complejidad espacial) y garantiza la estabilidad cuando hay tiempos de espera o errores constantes por parte del operador humano.

- **Agilidad en la concurrencia y Sincronización:** Se ha diseñado la validación como un paso de verificación "off-chain" previo. Antes de registrar datos en memoria o bases de datos, exigimos una confirmación manual (ej. _"¿Es a este paciente a quien desea agendar...?"_). Bloquear el proceso localmente es un mecanismo de sincronización que previene interacciones basura (y potenciales condiciones de carrera o inconsistencias masivas) si esto estuviera conectado a una base de datos centralizada concurrente.
- **Seguridad y Robustez:** Mediante el control de tipo y cast estricto en sentencias `try-except`, se previene explícitamente el volcado o caída del programa cuando hay un intento de inyectar variables inválidas. Evitamos cierres abruptos por excepciones del lenguaje, manteniendo la aplicación en un ambiente controlado ("fail-safe").

- **Paradigma:** Se aplica un enfoque fundamentalmente **modular y procedimental**, fraccionando el flujo en tareas atómicas con altísima cohesión (cada validación tiene su función independiente). De igual forma se favorece el uso de paradigma estructural a través de _match-case_, lo cual reduce en tiempo y recursos humanos el mantenimiento del software en el futuro frente a largas cadenas if-else convencionales.

---

_Desarrollado como parte de una práctica de progracicion estructural, mediante la creación de una función en Python que permite gestionar citas médicas, con el fin de comprender la importancia de organizar datos de manera eficiente en sistemas digitales._

_Con el objetivo de modernizar los servicios de salud por parte del Gobierno de México mediante la plataforma del SECEN, proyecto que busca unificar y digitalizar el expediente médico electrónico para mejorar la atención a los derechohabientes._
