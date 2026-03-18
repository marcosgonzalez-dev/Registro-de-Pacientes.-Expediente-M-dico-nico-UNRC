#creamos un diccionario para simular una base de datos
base_datos_pacientes = {}

#definimos la función principal
def registrar_paciente():
    try:
        # pedimos al usuario que ingrese los datos del paciente
        print("\nIngrese los datos del paciente: ")

        # solicitar y validar Número de Seguridad Social con match-case
        while True:
            numero_seguridad_social = input("Ingrese el Número de Seguridad Social (mínimo 10 caracteres): ").strip()
        
            match numero_seguridad_social:
                # validamos que el campo no esté vacío
                case "":
                    print("El Número de Seguridad Social no puede estar vacío.")
                
                # tiene menos de 10 caracteres (usamos una guarda de seguridad'if')
                case nss if len(nss) < 10:
                    print(f"El NSS debe tener al menos 10 caracteres. Solo ingresaste {len(nss)}.")
                
                # verificamos que el NSS contenga solo números
                case nss if not nss.isdigit():
                    print("El NSS debe contener solo números.")
                
                # el número ya existe en nuestro diccionario principal
                case nss if nss in base_datos_pacientes:
                    print("El NSS ya existe en la base de datos.")
                
                # si no cae en ninguno de los errores anteriores, es válido
                case _:
                    # salimos el ciclo while y avanzamos al siguiente dato
                    break 

    # solicitar Nombre Completo
        while True:
            nombre_completo = input("Ingrese el nombre completo del paciente: ").strip()
        
            match nombre_completo:
                # validamos que el campo no esté vacío
                case "":
                    print("El nombre completo no puede estar vacío.")
                
                # validamos que el nombre tenga al menos 8 caracteres
                case name if len(name) < 8:
                    print(f"El nombre debe tener al menos 8 caracteres. Solo ingresaste {len(name)}.")
                
                # si no cae en ninguno de los errores anteriores, es válido
                case _:
                # salimos el ciclo while y avanzamos al siguiente dato
                    break

    # solicitamos la edad del paciente
        while True:
            edad = input("Ingrese la edad del paciente: ").strip()
        
            match edad:
                # validamos que el campo no esté vacío
                case "":
                    print("Error: La edad no puede estar vacía.")
                
                # validamos que la edad sea un número
                case age if not age.isdigit():
                    print("Error: La edad debe ser un número.")
                
                # si no cae en ninguno de los errores anteriores, es válido
                case _:
                # salimos el ciclo while y avanzamos al siguiente dato
                    break
    
   # solicitamos el consultorio asignado al paciente
        while True:
            consultorio = input("Ingrese el consultorio asignado al paciente (1-9): ").strip()
        
            match consultorio:
                # validamos que el campo no esté vacío
                case "":
                    print("El consultorio no puede estar vacío.")
                
                # validamos que el consultorio sea un número
                case consultorio if not consultorio.isdigit():
                    print("Error: El consultorio debe ser un número.")
                
                # validamos que el consultorio sea un número entre 1 y 9
                case consultorio if int(consultorio) < 1 or int(consultorio) > 9:
                    print("Error: El consultorio debe ser un número entre 1 y 9.")
                
                # si no cae en ninguno de los errores anteriores, es válido
                case _:
                # salimos el ciclo while y avanzamos al siguiente dato
                    break
    
    # agregamos los datos del paciente al diccionario
        datos_paciente = {
            "numero_seguridad_social": numero_seguridad_social,
            "nombre_completo": nombre_completo,
            "edad": edad,
            "consultorio": consultorio
        }

    #agregamos el diccionario de datos del paciente a la base de datos
        base_datos_pacientes[numero_seguridad_social] = datos_paciente

        #imprimimos los datos del paciente
        print("\nDatos del paciente:")
        print(f"Número de Seguridad Social: {numero_seguridad_social}")
        print(f"Nombre Completo: {nombre_completo}")
        print(f"Edad: {edad}")
        print(f"Consultorio: {consultorio}")

    #imprimimos un mensaje de confirmación
        print("\nPaciente registrado exitosamente.")

    except KeyboardInterrupt:
        # se activa si el usuario presiona Ctrl+C
        print("\n\nSaliendo... Registro cancelado por el usuario.")
    except Exception as e:
        # capturamos cualquier otro error inesperado (disco lleno, error de memoria, etc.)
        print(f"\n Ocurrió un error inesperado: {e}")
    finally:
        # termina la ejecución de la función
        print("Finalizando proceso de registro.")

#ejecutamos la función principal
registrar_paciente()