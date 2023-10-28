class Persona:

    def __init__(self, cedula, nombre, apellido, ciudad):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.ciudad = ciudad


class Cliente(Persona):

    def __init__(self, cedula, nombre, apellido, ciudad, type_cuenta, number_card):
        Persona.__init__(self, cedula, nombre, apellido, ciudad)
        self.type_cuenta = type_cuenta
        self.number_card = number_card

    def __str__(self):
        table_format = (
            "----------------------------------------------------------------------------------\n"
            "{:<10} {:<10} {:<10} {:<15} {:<15} {:<15}\n"

            "{:<10} {:<10} {:<10} {:<15} {:<15} {:<15}\n"
            "----------------------------------------------------------------------------------\n"
        )
        return table_format.format(
            "Cédula", "Nombre", "Apellido", "Ciudad", "Tipo de cuenta", "Numero de cuenta",
            self.cedula, self.nombre, self.apellido, self.ciudad, self.type_cuenta, self.number_card
        )
