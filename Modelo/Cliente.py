class Cliente:
    def __init__(self, nombre,apellido,dni) :
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.cuentas= []
    
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getDni(self):
        return self.dni
    
    def agregarCuenta(self,cuenta):
        self.cuentas.append(cuenta)