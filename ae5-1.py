
# ==========================================
# EXCEPCIONES PERSONALIZADAS
# ==========================================

class DatosInvalidosException(Exception):
    pass


class ClienteDuplicadoException(Exception):
    pass


# ==========================================
# CLASE CLIENTE
# ==========================================

class Cliente:
    def __init__(self, nombre, apellido, edad, dni, correo):
        # Validar campos vacíos
        if not nombre or not apellido or not dni or not correo:
            raise DatosInvalidosException(
                "Todos los campos son obligatorios"
            )

        # Validar nombre y apellido
        if (len(nombre) < 2 or len(apellido) < 2
                or nombre.isdigit() or apellido.isdigit()):
            raise DatosInvalidosException(
                "Nombre o apellido inválido"
            )

        # Validar edad
        if edad < 18:
            raise DatosInvalidosException(
                "El cliente debe ser mayor de edad"
            )

        # Validar DNI
        if not dni.isdigit() or len(dni) != 8:
            raise DatosInvalidosException(
                "El DNI debe tener 8 dígitos"
            )

        # Validar correo
        if "@" not in correo or "." not in correo.split("@")[-1]:
            raise DatosInvalidosException(
                "El formato del correo no es válido"
            )

        # Atributos privados: encapsulamiento
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__dni = dni
        self.__correo = correo

    # Métodos para consultar los atributos
    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni

    @property
    def correo(self):
        return self.__correo

    def mostrar_datos(self):
        print(f"Nombre: {self.__nombre} {self.__apellido}")
        print(f"Edad: {self.__edad}")
        print(f"DNI: {self.__dni}")
        print(f"Correo: {self.__correo}")


# ==========================================
# CLASE REGISTRO DE CLIENTES
# ==========================================

class RegistroClientes:
    def __init__(self):
        self.__lista_clientes = []

    def registrar_cliente(self, cliente):
        # Evitar DNI duplicados
        for usuario in self.__lista_clientes:
            if usuario.dni == cliente.dni:
                raise ClienteDuplicadoException(
                    "Este DNI ya está registrado"
                )

        self.__lista_clientes.append(cliente)

    def mostrar_clientes(self):
        if not self.__lista_clientes:
            print("No hay clientes registrados")
            return

        for cliente in self.__lista_clientes:
            print("\n--------------------")
            cliente.mostrar_datos()

    def buscar_cliente(self, dni):
        for cliente in self.__lista_clientes:
            if cliente.dni == dni:
                return cliente

        raise DatosInvalidosException(
            "No se encontró el cliente"
        )


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

registro = RegistroClientes()

while True:
    print("\n=== REGISTRO DE CLIENTES ===")
    print("1. Registrar cliente")
    print("2. Mostrar clientes")
    print("3. Buscar cliente por DNI")
    print("4. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        try:
            nombre = input("Ingrese nombre: ").strip()
            apellido = input("Ingrese apellido: ").strip()
            edad = int(input("Ingrese edad: ").strip())
            dni = input("Ingrese DNI: ").strip()
            correo = input("Ingrese correo: ").strip()

            nuevo_cliente = Cliente(
                nombre, apellido, edad, dni, correo
            )

            registro.registrar_cliente(nuevo_cliente)

            print("Cliente registrado correctamente")

        except ValueError:
            print("Error: la edad debe ser un número entero")

        except (DatosInvalidosException,
                ClienteDuplicadoException) as e:
            print(f"Error al registrar: {e}")

        finally:
            print("Fin del intento de registro")

    elif opcion == "2":
        registro.mostrar_clientes()

    elif opcion == "3":
        dni_buscar = input("Ingrese el DNI: ").strip()

        try:
            cliente = registro.buscar_cliente(dni_buscar)
            cliente.mostrar_datos()

        except DatosInvalidosException as e:
            print(f"Error: {e}")

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")
