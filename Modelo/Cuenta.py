class Cuenta:
    def __init__(self, numero,cliente):
        self.numero=numero
        self.cliente= cliente
        self.cantidad=0

    def getNumero(self):
        return self.numero
    
    def getCliente(self):
        return self.cliente
    
    def getCantidad(self):
        return self.cantidad
    
    def ingreso(self, cantidadIngreso):
        self.cantidad += cantidadIngreso
        print(f"El dinero ha sido ingresdo con éxito, total de la cuenta: {self.cantidad}")
    
    def sacar(self, cantidadSacar):
        if cantidadSacar> self.cantidad:
            print(f"Lo siento, no tienes fondos suficientes. FONDOS: {self.cantidad}")
        else:
            self.cantidad -= cantidadSacar
            print(f"Dinero retirado con éxito, dinero total de la cuenta: {self.cantidad}")