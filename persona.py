#C.A.R.G
class Persona:
    contador_personas=0

    def __init__(self,  nombre:str = None , apellido:str = None , cedula:str = None , correo:str = None , edad:int = None, vip:bool = False, fecha_nacimiento= None):
        Persona.contador_personas += 1
        #Persona.contador_personas= Persona.contador_personas +1
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._cedula = cedula
        self._correo = correo
        self._vip = vip
        self._fecha_nacimiento = fecha_nacimiento

    #def __str__(self):
    #    return (f'Persona [nombre: {self._nombre}, epellido: {self._apellido}'
    #            f'cedula: {self._cedula}, correo= {self._cedula}, vip?:{self._vip}]')

    def __str__(self):
        return f'Persona {self.__dict__.__str__()}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo= correo

    @property
    def vip(self):
        return self._vip

    @vip.setter
    def vip(self, vip):
        self._vip = vip

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

'''
if __name__ == '__main__':
    objectPersona1 = Persona(nombre='Karla', apellido='Paz', edad='15',cedula='0959361206', correo='kperez@gmail.com')
    print(objectPersona1)
    print(objectPersona1._nombre)
    print(objectPersona1._apellido)
    print(objectPersona1._edad)

    p2 = Persona (nombre='Armando', cedula='0959361296', apellido='Perez', edad='20', correo='aperez@gmail.com')
    print(p2)
    print(p2._nombre)
    print(p2._apellido)
    print(p2._edad)

    p3 = Persona ('luis', 'Perez','0959361296', 'lperez@gmail.com')
'''

if __name__ == '__main__':
    objPersona1 = Persona(nombre='Karla', apellido='Paz', edad=15, cedula='0123456789', correo='kperez@mail.com')
    print(objPersona1.__str__())

    print(objPersona1.nombre)
    objPersona1.nombre = 'Fernanda'
    print(objPersona1.nombre)







