#   Practice with classes.

class Personaje:
    # creando el constructor.
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        
    
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("•Fuerza:", self.fuerza)
        print("•Inteligencia:", self.inteligencia)
        print("•Defensa", self.defensa)
        print("•Vida:", self.vida)

    # AUMENTAR NIVEL
    def subir_nivel(self, fuerza, inteligencia, defensa, vida):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        self.vida = self.vida + vida

    # ESTADO
    def vivo(self):
        return self.vida > 0

    def muerto(self):
        self.vida = 0
        print(self.nombre, "ha muerto.")

    # ACCIONES
    def defender(self):
        print(self.nombre, "se defiende")
        return self.defensa * 2
    
    def danio(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):

        danio = self.danio(enemigo)
        enemigo.vida = enemigo.vida - danio

        if danio <= 0:
            print(self.nombre, "ha fallado su ataque")
        else:
            print(self.nombre, "ha hecho", danio, "puntos de daño a", enemigo.nombre)

        if enemigo.vivo():
            print(enemigo.nombre, "tiene", enemigo.vida, "puntos de vida.")
        else:
            enemigo.muerto()

# PERSONAJE JUGADOR
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, experiencia):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.experiencia = experiencia

   
    def atributos(self):
        super().atributos()
        print("•Experiencia:", self.experiencia)

# ENEMIGO
class Enemigo(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, experiencia):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.experiencia = experiencia

    def dar_exp(self, jugador):
        exp = jugador.experiencia + self.experiencia
        print(jugador.nombre, "ha ganado", exp, "puntos de experiencia.")

jugador = Guerrero("Chris", 30, 35, 40, 1000, 0)
npc = Enemigo("Goblin", 43, 2, 5, 100, 50)

npc.atacar(jugador)
# jugador.atributos()