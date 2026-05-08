#   practica de clases creando personajes.

###   ABSTRACCION   ###

class Character:
    # atributos del personaje
    def __init__(self, name, strength, intelligence, defense, life):
        self.name = name # self.__name: encapsulado
        self.strength = strength # self.__strength: encapsulado
        self.intelligence = intelligence
        self.defense = defense
        self.life = life

    # informacion de los atributos
    def attributes(self):
        print(self.name, ":", sep="")
        print("•Strength:", self.strength)
        print("•Intelligence:", self.intelligence)
        print("•Defense:", self.defense)
        print("•Life:", self.life)

    # informacion de aumento de niveles
    def level_up(self, strength, intelligence, defense, life):
        self.strength = self.strength + strength
        self.intelligence = self.intelligence + intelligence
        self.defense = self.defense + defense
        self.life = self.life + life

    # funcion de personaje con vida
    def alive(self):
        return self.life > 0
    
    # funcion de personaje muerto
    def dead(self):
        self.life = 0
        print(self.name, "has died")

    # funcion de daño a personaje
    def damage(self, enemy):
        return self.strength - enemy.defense
    
    # funcion de ataque a personaje
    def attack(self, enemy):
        damage = self.damage(enemy)
        enemy.life = enemy.life - damage
        print(self.name, "Has done", damage, "damage points to", enemy.name)
        if enemy.alive():
            print("The life of", enemy.name, "is", enemy.life)
        else:
            enemy.dead()

    # getters = consigue el atributo para ser cambiado en caso de encapsulamiento.
    def get_strength(self):
        return self.strength
    
    # setter =  permite o no cambiar el estado del atrubuto en caso de encapsulamiento.
    def set_strength(self, strength):
        if strength < 0:
            print("Error, negative numbers are not allowed!")
        else:
            self.strength = strength



# warrior = Character("Goku", 10, 7, 8, 100)
# enemy = Character("Boo", 5, 1, 3, 50)

# print(warrior.get_strength())
# warrior.set_strength(12)
# warrior.attributes()

###  HERENCIA  ###

# Guerrero
class Sayan(Character):

    def __init__(self, name, strength, intelligence, defense, life, sayan):
        # al usar super().__init__ no es necesario escribir self dentro del constructor.
        super().__init__(name, strength, intelligence, defense, life)
        self.sayan = sayan

    # Option para cambiar el poder del personaje
    def transformar(self):
        option = int(input("Transform into:\n •1. Super Sayan \n •2. Super Sayan Two \n •3. Super Sayan Three \n •4. Super Sayan Four \n Option: "))
        
        match option:
            case 1:
                self.sayan, self.life = 15, 1000
            case 2:
                self.sayan, self.life = 20, 1500
            case 3:
                self.sayan, self.life = 25, 1800
            case 4:
                self.sayan, self.life = 40, 2000
            case _:
                print("Not an option")

    def attributes(self):
        super().attributes()
        print("•Sayan:", self.sayan)
    
    def damage(self, enemy):
        return self.strength * self.sayan - enemy.defense
    
# Enemigo
class Majin_bu(Character):
    
    def __init__(self, name, strength, intelligence, defense, life, magic):
        super().__init__(name, strength, intelligence, defense, life)
        self.magic = magic

    def attributes(self):
        super().attributes()
        print("•Magic:", self.magic)

    def damage(self, enemy):
        return self.intelligence * self.magic - enemy.defense
    

# Characters with attributes:
player_1 = Sayan("Goku", 20, 10, 15, 700, 10)
player_2 = Majin_bu("Bu", 30, 20, 25, 1000, 15)

# Fight:

def combat(player1, player2, turn=0):

    while player1.alive() and player2.alive():

        print("\nTurn", turn)

        print(">>> Action of ", player1.name, ":", sep="")
        player1.attack(player2)

        # Check if player2 is still alive before their turn
        if not player2.alive():
            break
            
        print(">>> Action of ", player2.name, ":", sep="")
        player2.attack(player1)

        turn = turn + 1
        
        # Check for transformation and continue with same combat instance
        if player1.life < 200 and player1.life > 0:
            player1.transformar()
            print(f"\n{player1.name} has transformed! Combat continues...")

    # Declare winner only once
    if player1.alive():
        print(f"\n🎉 {player1.name} has won the battle!")
    elif player2.alive():
        print(f"\n🎉 {player2.name} has won the battle!")
    else:
        print("\n⚔️ It's a draw!")


combat(player_1, player_2)