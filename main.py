from cosas import *

def main():
    per1 = Persona("Jose", 19)
    print(per1)
    print(Persona.descripcion)

    print("........Herencia alumno-------")
    al1 = Alumno("Jose", 19, "2344543", "ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre ="Juan"
    print(al2)
    al2.dormir()

    print("---------Herencia profe-------")
    profe1= Profesor("Jesus", 30 + 16, 577656, "Ingenieria de software")
    print(profe1)
    profe1.dormir()

    print("----------Herencia Ayudante profe-----------")
    ayudante = AyudanteProfesor("Adrian", 20, "6587268", "ICO", 4867, "Ing. software", 4)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = "Leslie"
    ayudante.dar_clase("POO")

main()