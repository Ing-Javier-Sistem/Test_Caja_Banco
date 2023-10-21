class Cuenta:
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo
        self.historial = []

    def depositar(self, monto):
        self.saldo += monto
        self.historial.append(f'Depósito de ${monto}')

    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            self.historial.append(f'Retiro de ${monto}')
        else:
            self.historial.append('Fondos insuficientes')
