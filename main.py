
from cosas import Alumno

def main():

    al1 = Alumno("jose", 19, "ICO")
    print(vars(al1))
    al1.__nombre="Diego"
    print(vars(al1))
    al1.set_nombre("Maria")
    print(vars(al1))
    print("-----To string-----")
    print(al1)
    al1.set_edad(999)
    al1.estudiar(4)
    print("----PERRO----")
    perro1= Perro("Poddle", 2, 0.35)
    print(vars(perro1))
    perro1.raza = "De la calle" #set de notacion pythonic
    print(vars(perro1))
    perro1.__raza = "otra"
    print(vars(perro1))
    perro1.edad = 12
    perro1.estatura = 0.45
    print(perro1)
    cachorro = Perro.es_cachorro(perro1.edad)
    print(cachorro)
perro2 =Perro()

    main()