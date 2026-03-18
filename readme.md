# 🏥 Sistema de Registro de Pacientes

Este proyecto consiste en un módulo en etapa temprana para abordar el esxpediente médico electrónico para una plataforma de salud del SECEN.
Está diseñado bajo el paradigma de **Programación Funcional**, aplicando una estructura **modular** que garantiza la legibilidad del código y facilita su escalabilidad futura.

## 🚀 Características Principales

- **Paradigma Funcional:** Se hizo uso de una función principal para el registro de pacientes, la cual se encarga de solicitar y validar los datos del paciente.
- **Modularización:** La estructura se dividió en bloques lógicos de validación, lo que permite extraer componentes fácilmente en el futuro.
- **Robustez:** Implementación de bloques `try-except-finally` para el manejo de excepciones (como `KeyboardInterrupt` o errores inesperados).
- **Validación con Match-Case:** Aprovecha el _Structural Pattern Matching_ (Python 3.10+) para un control de flujo más claro y moderno mediante "guardas".

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
    python registro_pacientes.py
    ```

## 🛡️ Manejo de Errores

El código está protegido contra:

- **Cierres inesperados:** Captura de `Ctrl+C`.
- **Entradas vacías:** No permite el avance si los campos se encuentran vacíos.
- **Tipado incorrecto:** Se filtran caracteres no numéricos en campos que requieren cifras.

---

_Desarrollado como parte de una práctica de desarrollo estructuras de datos mediante la creación de una función en Python que permita ingresar y almacenar información básica de pacientes en una lista o diccionario, con el fin de comprender la importancia de organizar datos de manera eficiente en sistemas digitales._

_Con el objetivo de modernizar los servicios de salud por parte del Gobierno de México mediante la plataforma del SECEN, proyecto que busca unificar y digitalizar el expediente médico electrónico para mejorar la atención a los derechohabientes._
