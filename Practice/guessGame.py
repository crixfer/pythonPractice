# importar random
import random

# generar número aleatorio entre 1 y 100
number = random.randint(1,10)
# intentos = 0
tries = 0
max_tries = 5
# mientras True:
print("Welcome to Guess the Secret Number!")  
while tries < max_tries:
#     pedir número al usuario
      print("You have ", max_tries - tries, " tries remaining!")  
      try:  
            playerNumber = int(input("\nGuess your number: "))  
#     aumentar intentos  
            tries += 1  
#     si número == secreto:
            if playerNumber == number:  
#     mostrar "ganaste"
                  print(f"Your number is: {playerNumber} and the random number is {number}, too!")  
                  print("You won!")  
#     mostrar intentos
                  print(f"You had {tries} tries.") 
              
#     si número < secreto:
            if playerNumber < number:   
#     mostrar "muy bajo"    
                  print("\nNumber too low.")   

#     si número > secreto:
            if playerNumber > number:  
#     mostrar "muy alto"  
                  print("\nNumber too hight")

      except ValueError:
            print("Debes insertar un número para proceder!")

if tries == 5:
    print("\nYou have already used all your tries.")
    print(f"\nThe number was: {number}.")

