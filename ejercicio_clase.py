empleados = []

while True:
    print("=== Menú Principal ===")
    print("1. Registrar empleado")
    print("2. Ver empleados")
    print("3. Ver total de la nómina")
    print("4. Eliminar empleado por ID")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("\n--- Registro de Empleado ---")
        empleado = {}
        empleado["id"] = input("ID del empleado: ")
        empleado["nombre"] = input("Nombre: ")
        empleado["correo"] = input("Correo: ")
        empleado["telefono"] = input("Teléfono: ")
        
      
        while True:
            valor = input("Valor hora (dejar vacío para 5400): ")
            if valor == "":
                empleado["valor_hora"] = 6500
                break
            elif valor.isdigit() and int(valor) > 0:
                empleado["valor_hora"] = int(valor)
                break
            else:
                print("Por favor, ingresa un número válido mayor que 0.")
        
        empleado["cargo"] = input("Cargo: ")
        empleados.append(empleado)
        print("Empleado registrado exitosamente.\n")

    elif opcion == "2":
        print("\n--- Lista de Empleados ---")
        if len(empleados) == 0:
            print("No hay empleados registrados.\n")
        else:
            for i in range(len(empleados)):
                e = empleados[i]
                salario = e["valor_hora"] * 8 * 22
                print("ID:", e["id"], 
                      "Nombre:", e["nombre"], 
                      "Correo:", e["correo"], 
                      "Teléfono:", e["telefono"], 
                      "Valor Hora:", e["valor_hora"], 
                      "Cargo:", e["cargo"], 
                      "Salario Mensual:", salario)
            print()

    elif opcion == "3":
        total = 0
        for i in range(len(empleados)):
            total += empleados[i]["valor_hora"] * 8 * 22
        print("\n--- Total de la Nómina ---")
        print("Total a pagar mensual a todos los empleados:", total, "\n")

    elif opcion == "4":
        id_eliminar = input("\nIngrese el ID del empleado a eliminar: ")
        encontrado = False
        for i in range(len(empleados)):
            if empleados[i]["id"] == id_eliminar:
                empleados.pop(i)
                print("Empleado con ID", id_eliminar, "eliminado exitosamente.\n")
                encontrado = True
                break
        if not encontrado:
            print("No se encontró empleado con ese ID.\n")

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.\n")
