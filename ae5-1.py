
class ClienteExistente(Exception):
    pass

class DNIInvalido(Exception):
    pass

class EdadInvalida(Exception):
    pass

class NombreApellidoInvalido(Exception):
    pass


lista_usuarios = []

# 1. Validar nombre y apellido
while True:
    try:
        nombre = input("Ingrese nombre: ").strip()
        apellido = input("Ingrese apellido: ").strip()

        if (len(nombre) < 2 or len(apellido) < 2
                or nombre.isdigit() or apellido.isdigit()):
            raise NombreApellidoInvalido(
                "Nombre o apellido inválido"
            )

        break

    except NombreApellidoInvalido as e:
        print(f"Error: {e}")


# 2. Validar edad
while True:
    try:
        edad = int(input("Ingrese edad: ").strip())

        if edad < 18:
            raise EdadInvalida("Debe ser mayor de edad")

        break

    except ValueError:
        print("Error: debe ingresar una edad numérica")

    except EdadInvalida as e:
        print(f"Error: {e}")


# 3. Validar DNI
while True:
    try:
        dni = input("Ingrese número de DNI: ").strip()

        if not dni.isdigit() or len(dni) != 8:
            raise DNIInvalido("El DNI debe tener 8 dígitos")

        for usuario in lista_usuarios:
            if usuario["dni"] == dni:
                raise ClienteExistente(
                    "Este DNI ya está registrado"
                )

        break

    except DNIInvalido as e:
        print(f"Error: {e}")

    except ClienteExistente as e:
        print(f"Error: {e}")


# 4. Guardar todos los datos del mismo usuario
nuevo_usuario = {
    "nombre": nombre,
    "apellido": apellido,
    "edad": edad,
    "dni": dni
}

lista_usuarios.append(nuevo_usuario)

print("Usuario registrado correctamente")
print(lista_usuarios)
