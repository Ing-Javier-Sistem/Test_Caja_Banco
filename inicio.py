from inf_datos import ManejadorClientes
from modelo.clases_objetos import Cliente

manejador = ManejadorClientes()

while True:
    print("1. Agregar Cliente")
    print("2. Mostrar Clientes")
    print("3. Editar Cliente")
    print("4. Eliminar Cliente")
    print("5. Eliminar Todos los Clientes")
    print("6. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        cedula = input("Cedula: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        ciudad = input("Ciudad: ")
        type_cuenta = input("Tipo de cuenta -DEBITO-  -CORREINTE- o -CREDITO-: ")
        number_card = float(input("Numero de cuenta: "))

        cliente = Cliente(cedula, nombre, apellido, ciudad, type_cuenta, number_card)
        manejador.agregar_cliente(cliente)
        print("Cliente agregado con éxito.")

    elif opcion == "2":
        print('------------------------- >> Clientes Registrados << -----------------------------')
        for cliente in manejador.clientes:
            print(cliente)


    elif opcion == "3":
        nombre_buscar = input("Nombre del cliente a editar: ")
        nuevo_cliente = Cliente(
            input("Nueva Cedula: "),
            input("Nuevo Nombre: "),
            input("Nuevo Apellido: "),
            input("Nueva Ciudad: "),
            input("Tipo de cuenta -DEBITO-  -CORREINTE- o -CREDITO-: "),
            float(input("Nuevo numero de cuenta: ")),
        )
        manejador.editar_cliente(nombre_buscar, nuevo_cliente)
        print("Cliente editado con éxito.")

    elif opcion == "4":
        nombre_eliminar = input("Nombre del cliente a eliminar: ")
        manejador.eliminar_cliente(nombre_eliminar)
        print("Cliente eliminado con éxito.")

    elif opcion == "5":
        manejador.eliminar_todos_los_clientes()
        print("Todos los clientes han sido eliminados.")

    elif opcion == "6":
        break
