#EXCEPCIONES#

class ProdNoEncontrado(Exception):
    """Se lanza cuando se busca o actualiza un producto inexistente."""
    pass

class StockInsuficiente(Exception):
    """Se lanza cuando se intenta retirar más stock del disponible"""
    pass

class PrecioInvalido(Exception):
    """Se lanza cuando el precio ingresado es menor o igual a cero"""
    pass

class CodDuplicado(Exception):
    """Se lanza cuando se intenta registrar un producto con un código ya existente"""
    pass

class StockNegativo(Exception):
    """Se lanza cuando se intenta registrar o ingresar un stock menor a cero[cite: 1]."""
    pass

#CLASE PREDUCTO#

class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        self.codigo = codigo.strip().upper()
        self.nombre = nombre.strip()
        self.precio = self._validar_precio(precio)
        self.stock = self._validar_stock(stock)

    def _validar_precio(self, precio: float) -> float:
        """Valida que el precio sea positivo."""
        if precio <= 0:
            raise PrecioInvalido(f"El precio debe ser mayor a 0. Se ingresó: ${precio:.2f}")
        return precio

    def _validar_stock(self, stock: int) -> int:
        """Valida que el stock no sea negativo[cite: 1, 2]."""
        if stock < 0:
            raise StockNegativo(f"El stock no puede ser negativo. Se ingresó: {stock}")
        return stock

    def __str__(self):
        return f"Código: {self.codigo:<8} | Nombre: {self.nombre:<30} | Precio: ${self.precio:>6.2f} | Stock: {self.stock:>3} unids."

#CLASE DE CONTROL DE INVENTARIO#

class InventarioMascotas:
    def __init__(self, nombre_tienda: str):
        self.nombre_tienda = nombre_tienda
        self.__productos = {}  # Diccionario privado {codigo: Objeto Producto}

    def registrar_producto(self, producto: Producto):
        """Registra un nuevo producto en el sistema[cite: 1]."""
        if producto.codigo in self.__productos:
            raise CodDuplicado(f"El código '{producto.codigo}' ya pertenece al producto: '{self.__productos[producto.codigo].nombre}'.")
        
        self.__productos[producto.codigo] = producto
        print(f"\n✅ Producto '{producto.nombre}' registrado correctamente.")

    def actualizar_stock(self, codigo: str, cantidad: int):
        """Actualiza el stock (sumando o restando unidades)[cite: 1]."""
        codigo = codigo.strip().upper()
        if codigo not in self.__productos:
            raise ProdNoEncontrado(f"No existe ningún producto con el código '{codigo}'.")

        prod = self.__productos[codigo]
        nuevo_stock = prod.stock + cantidad

        if nuevo_stock < 0:
            raise StockInsuficiente(
                f"No hay suficiente stock de '{prod.nombre}'. Stock actual: {prod.stock}, intento de retiro: {abs(cantidad)}"
            )

        prod.stock = nuevo_stock
        print(f"\n✅ Stock actualizado para '{prod.nombre}'. Nuevo stock disponible: {prod.stock} unidades.")

    def consultar_disponibilidad(self, codigo: str):
        """Consulta el estado y disponibilidad de un producto[cite: 1]."""
        codigo = codigo.strip().upper()
        if codigo not in self.__productos:
            raise ProdNoEncontrado(f"No existe ningún producto registrado con el código '{codigo}'.")
        
        prod = self.__productos[codigo]
        estado = "🟢 DISPONIBLE" if prod.stock > 0 else "🔴 AGOTADO"
        print("\n" + "=" * 50)
        print("🔎 DETALLE DE DISPONIBILIDAD")
        print("=" * 50)
        print(f"Producto  : {prod.nombre}")
        print(f"Código    : {prod.codigo}")
        print(f"Precio    : ${prod.precio:.2f}")
        print(f"Stock     : {prod.stock} unidades")
        print(f"Estado    : {estado}")
        print("=" * 50)

    def listar_productos(self):
        """Muestra todos los productos registrados."""
        if not self.__productos:
            print("\n⚠️ No hay productos registrados en el sistema.")
            return

        print("\n" + "=" * 70)
        print(f"📦 INVENTARIO GENERAL - {self.nombre_tienda.upper()}")
        print("=" * 70)
        for prod in self.__productos.values():
            print(prod)
        print("=" * 70)

#MENU INTERACTIVO

def ejecutar_menu():
    tienda = InventarioMascotas("Pet Gourmet - Alimentos & Mascotas")

    # Carga opcional de datos iniciales de ejemplo
    try:
        tienda.registrar_producto(Producto("COM-001", "Alimento Perro Adulto 15kg", 130.0, 10))
        tienda.registrar_producto(Producto("GAT-001", "Lata Comida Húmeda Gato", 5.50, 25))
    except Exception:
        pass

    while True:
        print("\n" + "─" * 45)
        print("   🐾 SISTEMA DE CONTROL - PET GOURMET 🐾")
        print("─" * 45)
        print("1. Registrar nuevo producto")
        print("2. Actualizar stock de un producto")
        print("3. Consultar disponibilidad de producto")
        print("4. Ver lista de todos los productos")
        print("5. Salir")
        print("─" * 45)

        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            print("\n--- REGISTRAR NUEVO PRODUCTO ---")
            try:
                codigo = input("Ingrese código del producto (ej. DOG-101): ")
                nombre = input("Ingrese nombre/descripción del producto: ")
                precio = float(input("Ingrese precio ($): "))
                stock = int(input("Ingrese stock inicial: "))

                nuevo_prod = Producto(codigo, nombre, precio, stock)
                tienda.registrar_producto(nuevo_prod)

            except ValueError:
                print("❌ Error de entrada: El precio y el stock deben ser valores numéricos válidos.")
            except (PrecioInvalido, StockNegativo, CodDuplicado) as e:
                print(f"❌ Error al registrar: {e}")

        elif opcion == "2":
            print("\n--- ACTUALIZAR STOCK DE PRODUCTO ---")
            try:
                codigo = input("Ingrese código del producto a actualizar: ")
                print("Nota: Use valores positivos para agregar stock (ej. 10) o negativos para retirar/vender (ej. -5).")
                cantidad = int(input("Ingrese la cantidad a modificar: "))

                tienda.actualizar_stock(codigo, cantidad)

            except ValueError:
                print("❌ Error de entrada: La cantidad debe ser un número entero.")
            except (ProdNoEncontrado, StockInsuficiente) as e:
                print(f"❌ Error de actualización: {e}")

        elif opcion == "3":
            print("\n--- CONSULTAR DISPONIBILIDAD ---")
            try:
                codigo = input("Ingrese el código del producto a consultar: ")
                tienda.consultar_disponibilidad(codigo)

            except ProdNoEncontrado as e:
                print(f"❌ Error de consulta: {e}")

        elif opcion == "4":
            tienda.listar_productos()

        elif opcion == "5":
            print("\n¡Gracias por usar el sistema de control de Pet Gourmet! 👋")
            break

        else:
            print("❌ Opción no válida. Por favor, ingrese un número del 1 al 5.")


if __name__ == "__main__":
    ejecutar_menu()
