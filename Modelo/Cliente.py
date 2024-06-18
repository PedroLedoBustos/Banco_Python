from Modelo.Cuenta import Cuenta
from Utilidades.Utilidades import Utilidades


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
    
    def altaCuenta(self):
        numeroCuenta= Utilidades.leerInteger("Introduce el número de cuenta que quieres dar de alta: ")
        if any(cuenta.getNumero()== numeroCuenta for cuenta in self.cuentas):
            print("Lo siento este numero de cuenta ya esta registrado para este usuario")
        else:
            cuentaNueva= Cuenta(numeroCuenta,self)
            self.cuentas.append(cuentaNueva)
            print("Cuenta dada de alta")
