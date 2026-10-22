#CASUÍSTICA 3: Procesamiento de Ventas o Reservas

#La empresa requiere procesar ventas, pedidos o reservas

#exepciones personalizadas

class pagoinsuficiente(Exception):
    pass
class reservaduplicada(Exception):
    pass

#creacion clase que hwereda a las 3 siguientes

class maestra():
    def __init__(self,codigo: str, stock: int, dni: str ,precio: float ):
        self.__codigo = codigo
        self.__stock = stock
        self.__dni = dni
        self.__precio=precio


    def mostrar_datos(self):
        print(f"codigo: {self.__codigo}")
        print(f"stock: {self.__stock}")
        print(f"dni: {self.__dni}")
        print(f"precio: {self.__precio}")

# ventas, pedidos y reservas
class venta(maestra):
    def __init__(self, codigo, stock, dni,precio):
        super().__init__(codigo, stock, dni,precio)

    def mostrar_datos(self):
        super().mostrar_datos()


class pedido(maestra):
    def __init__(self, codigo, stock, dni,estado,precio):
        super().__init__(codigo, stock, dni,precio)
        self.__estado = estado

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"estado: {self.__estado}")




class reserva(maestra):
    def __init__(self, codigo, stock, dni,estado,precio,fecha):
        super().__init__(codigo, stock, dni,precio)


        self.__estado = estado
        self.__fecha = fecha
