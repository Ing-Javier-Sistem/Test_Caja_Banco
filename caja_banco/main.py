from inf_datos import ManejadorClientes
from cuenta import Cliente

manejador = ManejadorClientes()

while True:
    print("1. Agregar Cliente")
    print("2. Mostrar Clientes")
    print("3. Editar Cliente")
    print("4. Eliminar Cliente")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        cedula = input("Cedula: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        ciudad = input("Ciudad: ")
        monto = float(input("Monto: "))
        efectivo = float(input("Efectivo: "))
        tarjeta = float(input("Tarjeta: "))

        cliente = Cliente(cedula, nombre, apellido, ciudad, monto, efectivo, tarjeta)
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
            float(input("Nuevo Monto: ")),
            float(input("Nuevo Efectivo: ")),
            float(input("Nueva Tarjeta: "))
        )
        manejador.editar_cliente(nombre_buscar, nuevo_cliente)
        print("Cliente editado con éxito.")

    elif opcion == "4":
        nombre_buscar = input("Nombre del cliente a eliminar: ")
        manejador.eliminar_cliente(nombre_buscar)
        print("Cliente eliminado con éxito.")

    elif opcion == "5":
        break
