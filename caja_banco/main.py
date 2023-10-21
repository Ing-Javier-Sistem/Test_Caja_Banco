from caja import Caja

caja = Caja()

while True:
    print("1. Registrar Cliente")
    print("2. Realizar Depósito")
    print("3. Realizar Retiro")
    print("4. Consultar Saldo")
    print("5. Última Persona Atendida")
    print("6. Ver Todos los Clientes")
    print("7. Eliminar Cliente")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del cliente: ")
        identificacion = input("Identificación del cliente: ")
        resultado = caja.registrar_cliente(identificacion, nombre)
        print(resultado)
    elif opcion == "2":
        identificacion = input("Identificación del cliente: ")
        monto = float(input("Monto a depositar: $"))
        resultado = caja.depositar(identificacion, monto)
        print(resultado)
    elif opcion == "3":
        identificacion = input("Identificación del cliente: ")
        monto = float(input("Monto a retirar: $"))
        resultado = caja.retirar(identificacion, monto)
        print(resultado)
    elif opcion == "4":
        identificacion = input("Identificación del cliente: ")
        saldo = caja.consultar_saldo(identificacion)
        print(saldo)
    elif opcion == "5":
        ultima_persona_atendida = caja.obtener_ultima_persona_atendida()
        print(f"Última persona atendida: {ultima_persona_atendida}")
    elif opcion == "6":
        print("Clientes registrados:")
        for cliente in caja.obtener_clientes():
            print(cliente)
    elif opcion == "7":
        identificacion = input("Identificación del cliente a eliminar: ")
        resultado = caja.eliminar_cliente(identificacion)
        print(resultado)
    elif opcion == "8":
        break
    else:
        print("Opción no válida.")
