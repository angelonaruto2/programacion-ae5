
import tkinter as tk
from tkinter import messagebox

def mostrar_datos():
    codigo = entrada_codigo.get()
    stock = entrada_stock.get()
    dni = entrada_dni.get()

    if not codigo or not stock or not dni:
        messagebox.showerror("Error", "Completa todos los campos")
        return

    try:
        stock = int(stock)
    except ValueError:
        messagebox.showerror("Error", "El stock debe ser un número")
        return

    resultado.config(
        text=f"Código: {codigo}\nStock: {stock}\nDNI: {dni}"
    )

ventana = tk.Tk()
ventana.title("Registro de productos")
ventana.geometry("300x300")

tk.Label(ventana, text="Código:").pack()
entrada_codigo = tk.Entry(ventana)
entrada_codigo.pack()

tk.Label(ventana, text="Stock:").pack()
entrada_stock = tk.Entry(ventana)
entrada_stock.pack()

tk.Label(ventana, text="DNI:").pack()
entrada_dni = tk.Entry(ventana)
entrada_dni.pack()

tk.Button(
    ventana,
    text="Registrar",
    command=mostrar_datos
).pack(pady=10)

resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()
