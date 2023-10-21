from database import Database
from cliente import Cliente
from cuenta import Cuenta

class Caja:
    def __init__(self):
        self.clientes = {}  # Almacenar clientes en memoria
        self.db = Database()  # Base de datos

    def registrar_cliente(self, identificacion, nombre):
        if self.clientes.get(identificacion):
            return "CLIENTE YA ESTÁ REGISTRADO"

        self.clientes[identificacion] = Cliente(identificacion, nombre)
        self.db.add_client(identificacion, nombre)
        return "Cliente registrado exitosamente"

    def verificar_cliente_existente(self, identificacion):
        return identificacion in self.clientes

    def depositar(self, identificacion, monto):
        if self.verificar_cliente_existente(identificacion):
            cuenta = Cuenta(self.clientes[identificacion])
            cuenta.depositar(monto)
            self.db.update_client(identificacion, self.clientes[identificacion].nombre, cuenta.saldo)
            return f"Depósito de ${monto} realizado. Nuevo saldo: ${cuenta.saldo}"
        else:
            return "Cliente no encontrado."

    def retirar(self, identificacion, monto):
        if self.verificar_cliente_existente(identificacion):
            cuenta = Cuenta(self.clientes[identificacion])
            if cuenta.saldo >= monto:
                cuenta.retirar(monto)
                self.db.update_client(identificacion, self.clientes[identificacion].nombre, cuenta.saldo)
                return f"Retiro de ${monto} realizado. Nuevo saldo: ${cuenta.saldo}"
            else:
                return "Fondos insuficientes"
        else:
            return "Cliente no encontrado."

    def consultar_saldo(self, identificacion):
        if self.verificar_cliente_existente(identificacion):
            return f"Saldo de {self.clientes[identificacion].nombre}: ${self.db.get_client_by_identification(identificacion)[2]}"
        else:
            return "Cliente no encontrado."

    def obtener_ultima_persona_atendida(self):
        return self.db.get_client_by_identification(self.db.cursor.lastrowid)[1]

    def obtener_clientes(self):
        clients = self.db.cursor.execute("SELECT * FROM clientes")
        return clients.fetchall()

    def eliminar_cliente(self, identificacion):
        if self.verificar_cliente_existente(identificacion):
            del self.clientes[identificacion]
            self.db.delete_client(identificacion)
            return "Cliente eliminado exitosamente"
        else:
            return "Cliente no encontrado."
