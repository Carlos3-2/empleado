class Persona:
    # Variable de clase para contar objetos creados
    contador_personas = 0

    def __init__(self, nombre, edad, genero, direccion):
        self.__nombre = nombre  # Encapsulamiento
        self.__edad = edad
        self.__genero = genero
        self.__direccion = direccion
        Persona.contador_personas += 1

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_genero(self):
        return self.__genero

    def get_direccion(self):
        return self.__direccion

class Empleado(Persona):
    def __init__(self, nombre, edad, genero, direccion, empleado_id, salario):
        super().__init__(nombre, edad, genero, direccion)
        self.__empleado_id = empleado_id
        self.__salario = salario

    def get_empleado_id(self):
        return self.__empleado_id

    def get_salario(self):
        return self.__salario

class Cliente(Persona):
    def __init__(self, nombre, edad, genero, direccion, cliente_id, email):
        super().__init__(nombre, edad, genero, direccion)
        self.__cliente_id = cliente_id
        self.__email = email

    def get_cliente_id(self):
        return self.__cliente_id

    def get_email(self):
        return self.__email

# Ejemplo de uso:
empleado1 = Empleado("Juan", 30, "Masculino", "123 Calle Principal", "E123", 50000)
cliente1 = Cliente("Ana", 25, "Femenino", "456 Calle Secundaria", "C456", "ana@email.com")

print(f"Nombre del empleado: {empleado1.get_nombre()}")
print(f"Salario del empleado: {empleado1.get_salario()}")
print(f"Nombre del cliente: {cliente1.get_nombre()}")
print(f"Email del cliente: {cliente1.get_email()}")
print(f"Total de personas creadas: {Persona.contador_personas}")
