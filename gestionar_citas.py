# librerias para gestionar el programa
from dataclasses import dataclass
from typing import Dict


# clases para que paciente y cita sean inmutables
@dataclass(frozen=True)
class Paciente:
    nss: str
    nombre: str
    edad: int


@dataclass(frozen=True)
class Cita:
    nss: str
    fecha: str
    hora: str
    consultorio: int


# base de datos es el dicionario y cada registro es un objeto de la clase Paciente
base_datos_pacientes: Dict[str, Paciente] = {
    "1234567890": Paciente(nss="1234567890", nombre="Juan Perez", edad=30),
    "0987654321": Paciente(nss="0987654321", nombre="Maria Lopez", edad=25),
    "1122334455": Paciente(nss="1122334455", nombre="Carlos Ruiz", edad=45),
    "2233445566": Paciente(nss="2233445566", nombre="Ana Garcia", edad=28),
    "3344556677": Paciente(nss="3344556677", nombre="Pedro Ramirez", edad=35),
}

# base de datos de citas, cada registro es un objeto de la clase Cita
citas_programadas: Dict[str, Cita] = {}


# valilidacion de NSS
def validar_nss() -> str:
    while True:
        nss = input("Ingrese el NSS del paciente (10 dígitos): ").strip()

        if not nss.isdigit():
            print("Error: El NSS debe contener solo números y no puede estar vacío.")
        elif len(nss) != 10:
            print(
                f"Error: El NSS debe tener 10 dígitos. Ingresaste únicamente: {len(nss)}."
            )

        else:
            if nss in base_datos_pacientes:
                nombre_paciente = base_datos_pacientes[nss].nombre
                mensaje = f"El NSS ingresado pertenece a {nombre_paciente}. ¿Es a este paciente a quien desea agendar una cita? (s/n): "
            else:
                mensaje = f"El NSS ingresado es {nss} (Paciente no registrado). ¿El NSS es correcto? (s/n): "

            confirmacion = input(mensaje).strip().lower()
            if confirmacion == "s":
                return nss
            else:
                print("Por favor, ingrese el NSS nuevamente.")


# validacion de nombre
def validar_nombre() -> str:
    while True:
        nombre = input("Ingrese el nombre completo del paciente: ").strip()

        # Quitamos los espacios temporalmente para verificar si el resto son letras
        if nombre.replace(" ", "").isalpha():
            return nombre
        elif len(nombre) == 0:
            print("Error: El nombre no puede estar vacío.")
        else:
            print(
                "Error: El nombre solo debe contener letras (sin números ni símbolos)."
            )


# validacion de edad
def validar_edad() -> int:
    while True:
        try:
            edad = int(input("Ingrese la edad (0-120): ").strip())
            if 0 <= edad <= 120:
                return edad
            print("Error: La edad debe estar entre 0 y 120.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")


# validacion de consultorio
def validar_consultorio() -> int:
    while True:
        try:
            c = int(input("Seleccione número de consultorio (1-9): ").strip())
            if 1 <= c <= 9:
                return c
            print("Error: Consultorio no esta disponible.")
        except ValueError:
            print("Error: Ingrese un número válido para el consultorio.")


# validacion de fecha
def validar_fecha() -> str:
    while True:
        f = input("Fecha (DD/MM/AAAA): ").strip()
        if len(f) == 10 and f[2] == "/" and f[5] == "/":
            return f
        print("Error: Formato de fecha inválido. Use DD/MM/AAAA.")


# validacion de hora
def validar_hora_estricta() -> str:
    while True:
        h_input = input("Ingrese hora (HH:MM): ").strip()
        if len(h_input) == 5 and h_input[2] == ":":
            try:
                hh = int(h_input[0:2])
                mm = int(h_input[3:5])

                # horario de atención 08:00 a 15:59
                if 8 <= hh < 16 and 0 <= mm <= 59:
                    return h_input
                print("Error: Horario fuera de atención (08:00 a 16:00).")
            except ValueError:
                print("Error: Los caracteres de tiempo deben ser numéricos.")
        else:
            print("Error: Use el formato estricto HH:MM (ej. 09:15).")


# función para dar de alta a un paciente no existente
def registrar_nuevo_paciente(nss: str) -> Paciente:
    print(f"\n--- Registro de Nuevo Paciente (NSS: {nss}) ---")
    nombre = validar_nombre()
    edad = validar_edad()

    # se crea el objeto Paciente
    nuevo_paciente = Paciente(nss=nss, nombre=nombre, edad=edad)

    # actualizamos el estado de la base de datos
    base_datos_pacientes[nss] = nuevo_paciente
    print(f"Paciente {nombre} registrado exitosamente.")
    return nuevo_paciente


# función para agendar citas
def agendar_cita():
    try:
        print("\n--- GESTIÓN DE CITAS ---")
        nss = validar_nss()

        # se busca el NSS en la base de datos para verificar si existe
        if nss not in base_datos_pacientes:
            print("NSS no registrado.")
            if input("¿Desea registrarlo? (s/n): ").lower() == "s":
                paciente = registrar_nuevo_paciente(nss)
            else:
                return
        else:
            paciente = base_datos_pacientes[nss]

        if any(c.nss == nss for c in citas_programadas.values()):
            print(f"{paciente.nombre} ya tiene una cita activa.")
            return

        # se valida la fecha de la cita
        fecha = validar_fecha()

        # se valida el consultorio y la hora
        while True:
            consultorio = validar_consultorio()
            hora = validar_hora_estricta()

            # id unico para cada cita
            id_cita = f"C{consultorio}-{fecha}-{hora}"

            if id_horario_en_uso(id_cita):
                print(
                    f"Conflicto: El consultorio {consultorio} está ocupado el {fecha} a las {hora}."
                )
                print("Por favor, seleccione un consultorio o un horario diferente.")
            else:
                # se guarda la cita en el diccionario de citas como un objeto
                citas_programadas[id_cita] = Cita(
                    nss=nss,
                    fecha=fecha,
                    hora=hora,
                    consultorio=consultorio,
                )
                print(
                    f"CITA CONFIRMADA: {paciente.nombre} | {fecha} {hora} | Cons. {consultorio}"
                )
                break

    except Exception as e:
        print(f"Falla crítica: {e}")


# función para verificar si un id de cita ya existe
def id_horario_en_uso(id_cita: str) -> bool:
    return id_cita in citas_programadas


# función para consultar datos de pacientes
def consultar_datos_paciente() -> None:
    print("\n--- Información General de Pacientes ---")

    # recorremos el diccionario de pacientes
    for nss, paciente_obj in base_datos_pacientes.items():
        # buscamos si existe una referencia de cita para este NSS
        info_cita = "Sin cita agendada."

        for cita_obj in citas_programadas.values():
            if cita_obj.nss == nss:
                info_cita = (
                    f"Cita agendada para el {cita_obj.fecha} a las {cita_obj.hora}"
                )
                break

        # se muestra la información del paciente
        print(
            f"\nNSS: {nss} | Nombre: {paciente_obj.nombre} | Edad: {paciente_obj.edad}"
        )
        print(f"Estado: {info_cita}")


# función para consultar citas por consultorio
def consultar_citas_consultorio() -> None:
    print("\n--- Consultar citas por consultorio ---")
    try:
        num_consultorio = int(input("Ingrese el número de consultorio (1-9): "))
        encontradas = 0
        for cita_obj in citas_programadas.values():
            if cita_obj.consultorio == num_consultorio:
                nombre_p = base_datos_pacientes[cita_obj.nss].nombre
                print(
                    f"Paciente: {nombre_p} | Fecha: {cita_obj.fecha} | Hora: {cita_obj.hora}"
                )
                encontradas += 1

        # si no se encontraron citas se ejecuta esta condicion
        if encontradas == 0:
            print(f"No hay citas para el consultorio {num_consultorio}.")
    except ValueError:
        print(
            "No se puede agendar cita: Debe ingresar un número de consultorio válido."
        )


# función principal
def menu_principal() -> None:
    # controla el flujo de ejecución mediante selección múltiple dentro de un bucle while.
    while True:
        print("\n" + "=" * 35)
        print("   Sistema de Gestión de Citas")
        print("=" * 35)
        print("1. Agendar nueva cita")
        print("2. Consultar información de pacientes registrados")
        print("3. Consultar citas por consultorio")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        # estructura match-case: para manejar las opciones del menú
        match opcion:
            case "1":
                agendar_cita()
            case "2":
                consultar_datos_paciente()
            case "3":
                consultar_citas_consultorio()
            case "4":
                print("Finalizando el programa...")
                break
            # opción por defecto si no hay coincidencia
            case _:
                print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":

    # llama a la función principal para iniciar el programa
    menu_principal()
