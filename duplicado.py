#modulo para registrar nuevos usuarios
lista_usuarios = []
def registrar():

    dni = int(input("ingrese numero de dni:"))


        
    for i in lista_usuarios:
        if i["dni"] == dni:
            print("este usuario ya se registro...")
        break


    lista_usuarios.append(
        {

        "dni":  dni

        }
    )


        

registrar()
registrar()

