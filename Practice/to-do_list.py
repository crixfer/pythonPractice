# crear lista vacía llamada tareas
tareas = []

# mientras True:
#     mostrar menú:
#         1. Agregar tarea
#         2. Ver tareas
#         3. Marcar como completada
#         4. Eliminar tarea
#         5. Salir

while True:
#     pedir opción al usuario
    opcion = int(input("\nBienvenido! Presiona el número de la opción deseada.\n\n1. Agregar tarea \n2. Ver tareas \n3. Marcar como completada \n4. Eliminar tarea \n5. Salir \n\n Opción: "))
   
#     si opción == 1:
    if opcion == 1:
#         pedir descripción de la tarea
        descripcion = input("\nDescribe brevemente la tarea: ")
#         crear diccionario: {"descripcion": texto, "completada": False}
        nueva_tarea = {
            "descripcion": descripcion,
            "completada": False, 
        }    
#         agregar a la lista
        tareas.append(nueva_tarea)

                    

#     si opción == 2:
    if opcion == 2:
#         recorrer lista con for:
#             mostrar índice + descripción + estado
        if tareas:
            for i, tarea in enumerate(tareas):
                if tarea["completada"] == True:
                    estado = "Hecha"
                else:
                    estado = "Pendiente"
                print("********************* LISTA ***********************")
                print("\n", i + 1, "-", tarea["descripcion"], "::", estado, "\n")
                print("***************************************************")
        else:
            print("******************** MENSAJE **********************")
            print("\n 'No hay tareas asignadas por el momento.'")
            print("***************************************************")

#     si opción == 3:
    if opcion == 3:
#         pedir número de tarea
        numTarea = int(input("\nQue número desea cambiar de estado? \n\n Opción: "))-1
#         cambiar "completada" a True
        if numTarea >= 0 and numTarea < len(tareas):
            if tareas[numTarea]["completada"] == False:
                tareas[numTarea]["completada"] = True
                print("******************** MENSAJE **********************")
                print("\nLa tarea ha sido completada!\n")
                print("***************************************************")

            else:
                print("******************** MENSAJE **********************")
                print("\nLa tarea ya estaba completada.\n")
                print("***************************************************")
        else:
            print("******************** MENSAJE **********************")
            print("\nEsta tarea no existe.\n")
            print("***************************************************")

#     si opción == 4:
    if opcion == 4:
#         pedir número de tarea
        numTarea = int(input("\nQue número desea eliminar? \n\n Opción: "))-1
#         eliminar de la lista
        if numTarea >= 0 and numTarea < len(tareas):
            if tareas[numTarea]["completada"]:
                tareas.pop(numTarea)
                print("******************** MENSAJE **********************")
                print("\nTarea eliminada satisfactoriamente.\n")
                print("***************************************************")
            else:
                print("******************** MENSAJE **********************")
                print("\nTarea ya estaba eliminada.\n")
                print("***************************************************")
        else:
            print("******************** MENSAJE **********************")
            print("\nEsta tarea no existe.\n")
            print("***************************************************")

#     si opción == 5:
    if opcion == 5:
#         romper el loop
        print("******************** MENSAJE **********************")
        print("\nGracias por usar nuestros servicios!\n")
        print("***************************************************")
        break