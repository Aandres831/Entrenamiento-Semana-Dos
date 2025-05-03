# Entrada de datos:
# Solicita al usuario ingresar una calificación numérica y valida la entrada
# Permite al usuario ingresar una lista de calificaciones y un valor específico para comparar

# Se inicializa la variable de decisión que controlará la ejecución del bucle
decision = "S"

# Se inicia un bucle que continuará ejecutándose mientras la decisión sea "S"
while decision == "S":

    # Mensaje de bienvenida para el usuario
    print("Bienvenido al sistema de calificaciones de RIWI.\nA continuación ingresaras las notas finales de los estudiantes de tu curso.")

    # Solicita al usuario que ingrese las calificaciones separadas por comas
    calificaciones = input("Ingresa las calificaciones finales de tus estudiantes entre (0-100), recuerda separarlas por ',': ")

    # Separa las calificaciones ingresadas y las almacena en una lista
    cal = calificaciones.split(",")
    lista_calificaciones = []
    mayo = 0  # Contador para notas mayores a una comparación
    iguales = 0  # Contador para notas iguales a una comparación

    try:
        # Se recorre la lista de calificaciones para validar y convertir cada valor a flotante
        for values in cal:
            entrada = float(values.strip())  # Convierte la entrada a número y elimina espacios

            # Se verifica que la calificación esté dentro del rango válido (1-100)
            if 1 <= entrada <= 100:
                lista_calificaciones.append(entrada)
            else:
                print(f"Tu nota {entrada} ingresada no es válida")

        # Se muestran las calificaciones finales procesadas
        print(f"Las notas finales ingresadas son: {lista_calificaciones}")

        i = 1
        # Se recorre la lista de calificaciones para determinar si los estudiantes aprobaron o reprobaron
        for index in lista_calificaciones:
            if index >= 60:
                print(f"El estudiante {i} con la nota {index} aprobó el curso.")
            elif index > 0 and index < 60:
                print(f"El estudiante {i} con la nota {index} reprobó el curso.")
            else:
                print("No perteneces a este curso")
            i += 1

        # Se calcula el promedio de las calificaciones ingresadas
        suma_notas = sum(lista_calificaciones)
        promedio = suma_notas / len(lista_calificaciones)
        print(f"El promedio de las notas {lista_calificaciones} es {promedio}") 

        # Solicita al usuario que ingrese una nota para comparar
        comparacion = float(input("Ingresa una nota para comparar si hay notas mayores y menores en las notas existentes "
                                "(Recuerda que las notas están comprendidas entre (0-100)): "))

        # Se cuentan las calificaciones mayores a la comparación
        for calificaciones in lista_calificaciones:
            if calificaciones > comparacion:
                mayo += 1
        print(f"Hay {mayo} notas mayores que {comparacion} en la lista de calificaciones finales.")

        # Se cuentan las calificaciones iguales a la comparación
        for calificaciones in lista_calificaciones:
            if calificaciones == comparacion:
                iguales += 1
        print(f"Hay {iguales} notas igual que {comparacion} en la lista de calificaciones finales.")

        # Se solicita al usuario si desea continuar ingresando nuevas listas de calificaciones
        decision = input("Ingresa 'S' si deseas ingresar una nueva lista de calificaciones o ingresa 'N' si deseas salir: ").upper()

    except ValueError:
        # Se captura el error en caso de que la entrada no sea válida
        print("Ingresa una calificación verdadera, recuerda que las calificaciones están comprendidas entre (0-100).") 

    # Se verifica la decisión del usuario para finalizar el programa
    if decision != "S":
        print("Gracias por ingresar tus notas.")
