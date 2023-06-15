class Alumno:
    facultad = "FES Aragón"

    def __init__(self, nom, ed, carr):
        self.__nombre = nom
        self.__edad = ed
        self.__carrera = carr

    def set_nombre(self, nom):
        self.__nombre = nom

    def get_nombre(self):
            return self.__nombre

    def set_edad(self, ed):
        return self.__ed

    def get_edad(self):
        return self.__edad

    def set_carrera(self, car):
        self.__carrera = car

    def get_carrera(self):
        return self.__carrera

    def __str__(self):
        cadena = "nombre:" + self.__nombre
        cadena = cadena + "\n edad:" + str(self.__edad)
        cadena = cadena + "\n Carrera: " + self.__carrera
        return cadena

    def estudiar(self, horas=1):
        print(f"el alumno {self.__nombre} esta estudiando por {horas} horas")

class Perro:
    reino = "Canino"

    def __init__(self, raza, edad, estatura):
        self.__raza= raza
        self.__edad = edad
        self.__estatura = estatura

    #metodo de acceso get

    @property
    def raza(self):
        return self.__ raza


    #metodo de acceso set

    @raza.setter
    def raza(self, la_raza):
        self.__raza= la_raza

   @property
    def edad(self)
return self.__edad

@edad.setter
def edad(self, la_edad);



@property
def estatura(self):
return self.__estatura

@estarura.setter
def estatura(self, la_estatura):
 if la_estatura > 0.1 and la_estatura <1.1
self.__estatura = la_estatura

else:
print("No way")
self._ estatura = 0.1


def __str__(self):
return f"""
------------------
"""


@staticmethod
def es_cachorro(edad):
return edad < 3

@staticmethod
def dormir(veces = 5):
for n in range(veces):
print(f"danfo vuelta {n +1}")
print("zzzzzz")
