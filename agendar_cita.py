# libreria para asignar consultorio aleatorio
import random

# base de datos con pacientes registrados
base_datos_pacientes = {
    "1234567890": {"nombre": "Juan Perez", "edad": 30},
    "0987654321": {"nombre": "Maria Lopez", "edad": 25},
    "1122334455": {"nombre": "Carlos Ruiz", "edad": 45},
    "2233445566": {"nombre": "Ana Garcia", "edad": 28},
    "3344556677": {"nombre": "Pedro Ramirez", "edad": 35},
}

# diccionario para rastrear citas y evitar conflictos
citas_programadas = {}


def agendar_cita():
    try:
        print("\n--- Gestión de Agendamiento de Citas ---")

        # solicitar y validar NSS
        nss = input("Ingrese el Número de Seguridad Social del paciente: ").strip()

        if nss not in base_datos_pacientes:
            print("Paciente no se encuentra registrado.")
            print("Por favor, registre el paciente antes de agendar una cita.")
            print("\n--- Fin del proceso ---")
            return

        paciente = base_datos_pacientes[nss]

        # se asigna un consultorio aleatorio
        consultorio = random.randint(1, 9)
        print(f"Paciente: {paciente['nombre']} | Consultorio asignado: {consultorio}")

        # verificar si el paciente ya tiene una cita, validamos comparando el NSS ingresado con el diccionario de citas programadas
        tiene_cita = any(cita["nss"] == nss for cita in citas_programadas.values())

        if tiene_cita:
            print("El paciente ya cuenta con una cita agendada.")
            return

        # se solicita hora y fecha en caso de no tener cita con validacion de conflicto
        while True:
            fecha = input("Ingrese la fecha (DD/MM/AAAA): ").strip()
            hora_input = input("Ingrese la hora (HH:MM): ").strip()

            # validación de horario de atención
            try:
                hora_entera = int(hora_input.split(":")[0])
                if not (8 <= hora_entera < 16):
                    print(
                        "Error: El horario laboral es de 08:00 a 16:00. Intente de nuevo."
                    )
                    continue
            except (ValueError, IndexError):
                print("Error: Formato de hora inválido.")
                continue

            # crear una clave única para el consultorio en ese horario
            id_horario = f"C{consultorio}-{fecha}-{hora_input}"

            if id_horario in citas_programadas:
                print(
                    f"Conflicto: El consultorio {consultorio} ya está ocupado en ese horario."
                )
            else:
                citas_programadas[id_horario] = {
                    "nss": nss,
                    "fecha": fecha,
                    "hora": hora_input,
                    "consultorio": consultorio,
                }
                print(f"\n Cita confirmada para {paciente['nombre']}.")
                print(
                    f"Fecha: {fecha} | Hora: {hora_input} | Consultorio: {consultorio}"
                )
                break

    except KeyboardInterrupt:
        print("\n\nSaliendo... Proceso cancelado.")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")
    finally:
        print("--- Fin del proceso, cita agendada exitosamente ---")


# llamada a la función principal
agendar_cita()

# segunda llamada a la función principal para verificar si un paciente tiene cita previa
agendar_cita()
