from caja import Caja

caja = Caja()

while True:
    print("1. Registrar Cliente")
    print("2. Realizar Depósito")
    print("3. Realizar Retiro")
    print("4. Consultar Saldo")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del cliente: ")
        identificacion = input("Identificación del cliente: ")
        resultado = caja.registrar_cliente(nombre, identificacion)
        print(resultado)
    elif opcion == "2":
        identificacion = input("Identificación del cliente: ")
        cuenta = caja.obtener_cuenta(identificacion)
        if cuenta:
            monto = float(input("Monto a depositar: $"))
            cuenta.depositar(monto)
            print(f"Depósito realizado. Nuevo saldo: ${cuenta.saldo}")
        else:
            print("Cliente no encontrado.")
    elif opcion == "3":
        identificacion = input("Identificación del cliente: ")
        cuenta = caja.obtener_cuenta(identificacion)
        if cuenta:
            monto = float(input("Monto a retirar: $"))
            cuenta.retirar(monto)
            print(f"Retiro realizado. Nuevo saldo: ${cuenta.saldo}")
        else:
            print("Cliente no encontrado.")
    elif opcion == "4":
        identificacion = input("Identificación del cliente: ")
        cuenta = caja.obtener_cuenta(identificacion)
        if cuenta:
            print(f"Saldo actual: ${cuenta.saldo}")
        else:
            print("Cliente no encontrado.")
    elif opcion == "5":
        break
    else:
        print("Opción no válida.")
