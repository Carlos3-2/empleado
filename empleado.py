from persona import Persona


class Empleado(Persona):

    def __int__(self, id_empleado, sueldo, nombre, apellido, cedula):
        super().__init__(nombre=nombre, apellido=apellido, cedula=cedula)
        self._ide_empleado= id_empleado
        self._sueldo= sueldo
        self._nombre = nombre
        self._apellido = apellido
        self._cedula  = cedula


    @property
    def id_empleado(self):
        return self ._ide_empleado

    @id_empleado.setter
    def id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo (self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado {self.__dict__.__str__()}'

    e1 = id_Empleado(nombre='pedro', apellido='Gonzalez', sueldo='500', cedula= '0950361296', id_empleado='1')
    print(e1)




























