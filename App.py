from Modelo.Banco import Banco
from Utilidades.Utilidades import Utilidades

banco= Banco()

def menu():
    salir=False
    print("####################################")
    print("########## MENU PRINCIPAL ##########")
    print("####################################")
    print("1 Alta cliente")
    print("2 Baja cliente")
    print("3 Login cliente")
    print("4 Lista clientes")
    print("9 Salir")

    opcion= Utilidades.leerString("Escoge una opción: ")

    if opcion == "1":
        banco.altaCliente()
    elif opcion == "2":
        banco.bajaCliente()
    elif opcion == "3":
        banco.login()
    elif opcion == "4":
        banco.listaClientes()
    elif opcion == "9":
        print("Saliendo...")
        salir=True
    else:
        print("Escoge una opción válida")

    return salir
    
def aplicacion():
    salir=False
    while salir == False:
        salir=menu()

aplicacion()

