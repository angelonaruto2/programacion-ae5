import registro 
import random
registro.registrar()
numero = random.randint(1, 10)

class persona:
    def __init__(self,nombre,apellido,dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

class empleado(persona):
    def __init__(self,salario):
        self.salario = salario

class gerente(empleado):
    def __init__(self, salario):
        super().__init__(salario)


class marketing(empleado):
    def __init__(self, salario):
        super().__init__(salario)

    def hacer_tiktok(self,):
        print(f"hace un tiktok : genera {numero} mil visitas")


angelo = marketing(2323)

angelo.hacer_tiktok()







class cliente(persona):
    def __init__(self):
        
        pass


class clilente_vip(persona):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)
        pass