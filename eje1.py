class Mago:
    def hechizos(self):
        print("El mago lanza un hechizo")

class Guerrero:
    def defensa(self):
        print("El guerrero se defiende con su escudo")

class Elfo:
    def aura(self):
        print("El elfo emite un aura mágica")

class DarkLord(Guerrero, Elfo, Mago):
    pass

oscuro = DarkLord()
oscuro.defensa()
oscuro.aura()
oscuro.hechizos()

print("\nMRO con el orden Guerrero, Elfo, Mago:")
print(DarkLord.__mro__)
for clase in DarkLord.__mro__:
    print(clase.__name__)

class DarkLord2(Elfo, Guerrero, Mago):
    pass

print("\nMRO con el orden Elfo, Guerrero, Mago:")
print(DarkLord2.__mro__)
for clase in DarkLord2.__mro__:
    print(clase.__name__)
    
