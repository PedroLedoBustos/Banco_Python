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

    def bajaCuenta(self):
        numeroCuenta= Utilidades.leerInteger("Introduce el número de cuenta que quieres dar de baja: ")
        cuentaEncontrada= None

        for cuenta in self.cuentas:
            if cuenta.getNumero() == numeroCuenta:
                cuentaEncontrada= cuenta
        
        if cuentaEncontrada == None:
            print(f"La cuenta con numero: {numeroCuenta} no esta registrada")
        else:
            self.cuentas.remove(cuentaEncontrada)
            print(f"La cuenta con numero: {cuentaEncontrada.getNumero()} ha sido dada de baja")
            

    def ingresoDinero(self):
        numeroCuenta= Utilidades.leerInteger("Introduce el número de cuenta: ")

        cuentaEncontrada=None
        for cuenta in self.cuentas:
            if cuenta.getNumero()== numeroCuenta:
                cuentaEncontrada= cuenta
        
        if cuentaEncontrada == None:
            print("Lo siento, esta cuenta no esta registrada")
        else:
            cantidadIngresar= Utilidades.leerFloat("Introduce la cantidad a ingresar: ")
            cuentaEncontrada.ingreso(cantidadIngresar)
    
    def sacarDinero(self):
        numeroCuenta= Utilidades.leerInteger("Introduce el número de cuenta: ")

        cuentaEncontrada=None
        for cuenta in self.cuentas:
            if cuenta.getNumero()== numeroCuenta:
                cuentaEncontrada= cuenta
        
        if cuentaEncontrada == None:
            print("Lo siento, esta cuenta no esta registrada")
        else:
            cantidadSacar= Utilidades.leerFloat("Introduce la cantidad que quieres retirar: ")
            cuentaEncontrada.sacar(cantidadSacar)
    
    def dineroCuenta(self):
        numeroCuenta= Utilidades.leerInteger("Introduce el número de cuenta: ")

        cuentaEncontrada=None
        for cuenta in self.cuentas:
            if cuenta.getNumero()== numeroCuenta:
                cuentaEncontrada= cuenta
        
        if cuentaEncontrada == None:
            print("Lo siento, esta cuenta no esta registrada")
        else:
            print(f"La cuenta con número: {cuentaEncontrada.getNumero()} tiene {cuentaEncontrada.getCantidad()}€")


    def dineroTotal(self):
        total=0
        for cuenta in self.cuentas:
            total += cuenta.getCantidad()
        
        print(f"El total de todas tus cuentas es de: {total}€")
    
    def menu(self):
        salir=False
        while salir==False:
            print("###################################")
            print(f"######## MENU {self.nombre} {self.apellido} ##################")
            print("###################################")
            print("1 Alta cuenta")
            print("2 Baja cuenta")
            print("3 Ingresar dinero")
            print("4 Sacar dinero")
            print("5 Dinero en cuenta")
            print("6 Dinero total")
            print("9 Salir")
            opcion= Utilidades.leerString("Escoge una opción: ")

            if opcion== "1":
                self.altaCuenta()
            elif opcion== "2":
                self.bajaCuenta()
            elif opcion== "3":
                self.ingresoDinero()
            elif opcion== "4":
                self.sacarDinero()
            elif opcion== "5":
                self.dineroCuenta()
            elif opcion== "6":
                self.dineroTotal()
            elif opcion== "9":
                print("Saliendo...")
                salir=True
            else:
                print("Escoge una opción válida")

