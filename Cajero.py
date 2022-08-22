def clave():
    clave = int(input("Digite su clave de 4 digitos: "))
    if clave == 2485:
        print("Clave correcta, ingresando al sistema...")
    else:
        print("Error fatal, reiniciando sistema...")
        return clave()
clave()
def x():
    saldo = 10000
    print("\t >MENU<")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("Digite una opción del menú: "))
    if opcion == 1:
        extra = float(input("Cuánto dinero desea ingresar -->"))
        saldo += extra
        print(f"Dinero en la cuenta: {saldo}")
        continuar = int(input("Digite 1 si quiere continuar, digite 0 si quiere salir: "))           
        if continuar == 1:
            print("Volviendo a empenzar...")
            return x()
        else:
            print("Cerrando sistema...") 
        while continuar >= 2:
            print("Digite una opcion valida")
            continuar = int(input("Digite 1 si quiere continuar, digite 0 si quiere salir: "))
            if continuar == 1:
                 print("Volviendo a empenzar...")
                 return x()
            elif continuar == 0:
                print("Cerrando sistema...")
    elif opcion == 2:
        retirar = float(input("Cuánto dinero desa retirar -->"))
        if retirar > saldo:
            print("No tiene esa cantidad de dinero")
            print("Reiniciando sistema...")
            return x()
        else:
            saldo -= retirar
            print(f"Dinero en la cuenta: {saldo}")
        continuar = int(input("Digite 1 si quiere continuar, digite 0 si quiere salir: "))           
        if continuar == 1:
            print("Volviendo a empenzar...")
            return x()
        else:
            print("Cerrando sistema...") 
        while continuar >= 2:
            print("Digite una opcion valida")
            continuar = int(input("Digite 1 si quiere continuar, digite 0 si quiere salir: "))
            if continuar == 1:
                 print("Volviendo a empenzar...")
                 return x()
            elif continuar == 0:
                print("Cerrando sistema...")
    elif opcion == 3:
        print(f"Dinero en la cuenta: {saldo}")
        continuar = int(input("Digite 1 si quiere continuar, digite 0 si quiere salir: "))           
        if continuar == 1:
            print("Volviendo a empenzar...")
            return x()
        else:
            print("Cerrando sistema...") 
        while continuar >= 2:
            print("Digite una opcion valida")
            continuar = int(input("Digite 1 si quiere continuar, digite 0 si quiere salir: "))
            if continuar == 1:
                 print("Volviendo a empenzar...")
                 return x()
            elif continuar == 0:
                 print("Cerrando sistema...")
    elif opcion == 4:
        print("Gracias por utilizar este cajero automático") 
        continuar = int(input("Digite 1 si quiere continuar, digite 0 si quiere salir: "))
        continuar = int(input("Digite 1 si quiere continuar, digite 0 si quiere salir: "))           
        if continuar == 1:
            print("Volviendo a empenzar...")
            return x()
        else:
            print("Cerrando sistema...") 
        while continuar >= 2:
            print("Digite una opcion valida")
            continuar = int(input("Digite 1 si quiere continuar, digite 0 si quiere salir: "))
            if continuar == 1:
                 print("Volviendo a empenzar...")
                 return x()
            elif continuar == 0:
                print("Cerrando sistema...")
    elif opcion == 0:
        print("Error fatal.. reiniciando sistema..")
        return x()
    while opcion >=5:
        print("Error, elija una opción del menu")
        tecla = int(input("presione un número del 1 - 4: "))
        if 1 >=  tecla or tecla <= 4:
            input("Presione cualquier tecla para volver a empezar: ")
            return x()
x()