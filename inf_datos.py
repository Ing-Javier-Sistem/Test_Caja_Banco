import csv
from modelo.clases_objetos import Cliente

ARCHIVO_CLIENTES = 'clientes.csv'


def cargar_clientes():
    clientes = []
    try:
        with open(ARCHIVO_CLIENTES, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            next(lector_csv)
            for row in lector_csv:
                cedula, nombre, apellido, ciudad, type_cuenta, number_card = row
                cliente = Cliente(cedula, nombre, apellido, ciudad, type_cuenta, float(number_card))
                clientes.append(cliente)
    except FileNotFoundError:
        pass
    return clientes


class ManejadorClientes:
    def __init__(self):
        self.clientes = cargar_clientes()

    def guardar_clientes(self):
        with open(ARCHIVO_CLIENTES, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(["Cedula", "Nombre", "Apellido", "Ciudad", "Tipo de cuenta", "Numero de cuenta"])
            for cliente in self.clientes:
                escritor_csv.writerow(
                    [cliente.cedula, cliente.nombre, cliente.apellido, cliente.ciudad, cliente.type_cuenta,
                     cliente.number_card])

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        self.guardar_clientes()

    def editar_cliente(self, nombre, nuevo_cliente):
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                cliente.cedula = nuevo_cliente.cedula
                cliente.nombre = nuevo_cliente.nombre
                cliente.apellido = nuevo_cliente.apellido
                cliente.ciudad = nuevo_cliente.ciudad
                cliente.type_cuenta = nuevo_cliente.type_cuenta
                cliente.number_card = nuevo_cliente.number_card
                self.guardar_clientes()

    def eliminar_todos_los_clientes(self):
        self.clientes = []
        self.guardar_clientes()

    def eliminar_cliente(self, nombre):
        self.clientes = [cliente for cliente in self.clientes if cliente.nombre != nombre]
        self.guardar_clientes()
