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
                cedula, nombre, apellido, ciudad, monto, efectivo, tarjeta = row
                cliente = Cliente(cedula, nombre, apellido, ciudad, float(monto), float(efectivo), float(tarjeta))
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
            escritor_csv.writerow(["Cedula", "Nombre", "Apellido", "Ciudad", "Monto", "Efectivo", "Tarjeta"])
            for cliente in self.clientes:
                escritor_csv.writerow(
                    [cliente.cedula, cliente.nombre, cliente.apellido, cliente.ciudad, cliente.monto, cliente.efectivo,
                     cliente.tarjeta])

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
                cliente.monto = nuevo_cliente.monto
                cliente.efectivo = nuevo_cliente.efectivo
                cliente.tarjeta = nuevo_cliente.tarjeta
                self.guardar_clientes()

    def eliminar_cliente(self, nombre):
        self.clientes = [cliente for cliente in self.clientes if cliente.nombre != nombre]
        self.guardar_clientes()
        
        
    




