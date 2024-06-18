class Cuenta:
    def __init__(self, numero,cliente):
        self.numero=numero
        self.cliente= cliente

    def getNumero(self):
        return self.numero
    
    def getCliente(self):
        return self.cliente