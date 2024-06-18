from Utilidades.Utilidades import Utilidades


def menu():
    salir=False
    print("####################################")
    print("########## MENU PRINCIPAL ##########")
    print("####################################")
    print("1 Alta cliente")
    print("2 Baja cliente")
    print("3 Alta cuenta")
    print("4 Baja cuenta")
    print("5 Login cliente")
    print("6 Lista clientes")
    print("9 Salir")

    opcion= Utilidades.leerString("Escoge una opción: ")

    if opcion == "1":
        banco.altaCliente()
    elif opcion == "2":
        banco.bajaCliente()
    elif opcion == "3":
        banco.altaCuenta()
    elif opcion == "4":
        banco.bajaCuenta()
    elif opcion == "5":
        banco.login()
    elif opcion == "6":
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

