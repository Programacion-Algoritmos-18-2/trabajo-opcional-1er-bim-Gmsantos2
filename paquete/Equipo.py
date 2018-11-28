# Creando la clase padre Equipo
class Equipo(object):

    # Creando constructor
    def __init__(self, equ, p):
        self.equipo = equ
        self.pais = p

    #metodos agregar
    def agregar_Equipo(self, equ):
        self.equipo = equ

    def agregar_Pais(self, p):
        self.pais = p


    # Metodos obtener
    def obtener_Equip(self):
        return self.equipo

    def obtener_Pais(self):
        return self.pais

    #Metodo para presentar los datos
    def presentarD(self):
    
        cadena =("\nPertenece al Equipo: %s de %s" % (self.obtener_Equip(),self.obtener_Pais()))
        return cadena
    

    

class Futbolista(Equipo):
    # Constructor
    def __init__(self, n = "", a = "", equipo = None, pos = "",d = 0):
        
        self.nombre = n
        self.apellido = a
        self.equipo = equipo
        self.posicion = pos
        self.dorsal = d

    # Metodos agregar
    def agregar_nombre(self, n):
        self.nombre = n

    def agregar_apellido(self, a):
        self.apellido = a

    def agregar_equipo(self, equipo ):
        self.equipo = equipo

    def agregar_posicion(self, pos):
        self.posicion = pos

    def agregar_dorsal(self, d):
        self.dorsal = d

    # Metodos obtener
    def obtener_nombre(self):
        return self.nombre

    def obtener_apellido(self):
        return self.apellido

    def obtener_equipo(self):
        return self.equipo

    def obtener_posicion(self):
        return self.posicion

    def obtener_dorsal(self):
        return self.dorsal

    # Metodo para presentar los datos
    def presentarD(self):
        cadena = ("Jugador:\n%s %s  %s\nPosicion %s\nDorsal %d\n"%(self.obtener_nombre(),self.obtener_apellido(),self.obtener_equipo().presentarD(),self.obtener_posicion(), self.obtener_dorsal()))
        return cadena

#funcion main donde creo objetos y presento datos
def main():
    f = Futbolista("Antonio","Valencia")
    e = Equipo("Manchester United","Inglaterra")
    f.agregar_equipo(e)
    f.agregar_dorsal(25)
    f.agregar_posicion("LATERAL")
    print(f.presentarD())
    nexaca = Equipo("nexaca","Mexico")
    f2 = Futbolista("Alex", "Aguinaga",nexaca, "MEDIOCENTRO")
    f2.agregar_dorsal(7)
    print(f2.presentarD())
    lazio = Equipo("lazio","Italia")
    f3 = Futbolista("Felipe", "Caicedo",lazio)
    f3.agregar_dorsal(32)
    f.agregar_posicion("LATERAL")
    print(f3.presentarD())
main()