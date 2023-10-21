from caja_banco.cliente import Cliente
from cuenta import Cuenta

class Caja:
    def __init__(self):
        self.cuentas = []

    def registrar_cliente(self, nombre, identificacion):
        for cuenta in self.cuentas:
            if cuenta.cliente.identificacion == identificacion:
                return "El cliente ya existe"
        cliente = Cliente(nombre, identificacion)
        cuenta = Cuenta(cliente, 0)
        self.cuentas.append(cuenta)
        return "Cliente registrado exitosamente"

    def obtener_cuenta(self, identificacion):
        for cuenta in self.cuentas:
            if cuenta.cliente.identificacion == identificacion:
                return cuenta
        return None
