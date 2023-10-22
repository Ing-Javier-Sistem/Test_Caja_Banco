class Persona:

    def __init__(self, cedula, nombre, apellido, ciudad):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.ciudad = ciudad


class Cliente(Persona):

    def __init__(self, cedula, nombre, apellido, ciudad, monto, efectivo, tarjeta):
        Persona.__init__(self, cedula, nombre, apellido, ciudad)
        self.monto = monto
        self.efectivo = efectivo
        self.tarjeta = tarjeta

    def __str__(self):
        table_format = (
            "----------------------------------------------------------------------------------\n"
            "{:<10} {:<10} {:<15} {:<15} {:<15} {:<10}\n"

            "{:<10} {:<10} {:<15} {:<15} {:<15} {:<10}\n"
            "----------------------------------------------------------------------------------\n"
        )
        return table_format.format(
            "Cédula", "Nombre", "Apellido", "Ciudad", "Monto", "Efectivo", "Tarjeta",
            self.cedula, self.nombre, self.apellido, self.ciudad, self.monto, self.efectivo, self.tarjeta
        )
