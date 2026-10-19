#modulo para registrar nuevos usuarios
lista_usuarios = []
def registrar():
    nombre = input("Ingrese nombre: ").strip() #strip para evitar espacios 
    apellido = input("Ingrese apellido: ").strip()
    edad = input("Ingrese edad: ").strip()
    dni = input("Ingrese numero de DNI: ").strip()

    if not dni.isdigit() or len(dni) != 8: #evitar digitos menor a 8
        print("Error: El DNI debe tener 8 digitos.")
        return


    
    for i in lista_usuarios:
            if i["dni"] == dni: #evitar duplicados
                print("este usuario ya se registro...")
                return
            
    correo = input("ingrese correo")


    lista_usuarios.append(
        {
        "nombre" : nombre,
        "apellido " : apellido ,
        "edad" : edad,
        "dni":  dni,
        "correo" : correo
        }
    )


        

registrar()
registrar()

