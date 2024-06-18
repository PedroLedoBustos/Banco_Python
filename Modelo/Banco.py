from Modelo.Cliente import Cliente
from Utilidades.Utilidades import Utilidades


class Banco:
    def __init__(self):
        self.clientes=[]
    
    def altaCliente(self):
        nombre= Utilidades.leerString("Introduce el nombre del cliente: ")
        apellido= Utilidades.leerString("Introduce el apellido del cliente: ")
        dni= Utilidades.leerInteger("Introduce el dni del cliente SIN letra: ")

        cliente= Cliente(nombre,apellido,dni)

        if any(usuario.getDni()==cliente.getDni() for usuario in self.clientes):
            print(f"Lo siento, el cliente con DNI: {cliente.getDni()} ya esta registrado")
        else:
            self.clientes.append(cliente)
            print(f"El cliente: {cliente.getNombre()} {cliente.getApellido()} con DNI: {cliente.getDni()} ha sido dado de alta")
    
    def bajaCliente(self):
        dni= Utilidades.leerInteger("Introduce el dni del cliente que quieres dar de baja SIN letra: ")

        clienteEncontrado=None
        for usuario in self.clientes:
            if usuario.getDni()==dni:
                clienteEncontrado= usuario
        
        if clienteEncontrado == None:
            print(f"Lo siento el cliente con DNI: {dni} no esta registrado")
        else:
            self.clientes.remove(clienteEncontrado)
            print(f"El cliente: {clienteEncontrado.getNombre()} {clienteEncontrado.getApellido()} con DNI: {clienteEncontrado.getDni()} ha sido dado de baja")