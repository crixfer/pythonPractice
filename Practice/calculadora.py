#CALCULADORA

def proceso():

        while True:
            a = int(input("Inserta un número y presiona ENTER: "))

            if a > 0:     
                b = int(input("Inserta otro número y presiona ENTER: "))

            if b > 0:     
                operador = int(input("\n Elige un número para calcular:\n \n 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir \n \n Opcion: "))
            
            if operador != 1 and operador != 2 and operador != 3 and operador != 4:
                continue
            
            else:
                match operador:
                    case 1:
                        print(f"La suma de {a} y {b} es: ", suma(a,b))
                    case 2:
                        print(f"La resta de {a} y {b} es: ", resta(a,b))
                    case 3:
                        print(f"La multiplicación entre {a} y {b} es: ", multiplicacion(a,b))
                    case 4:
                        print(f"La división entre {a} y {b} es: ", division(a,b))
    
                break
#Funciones/ Definiciones

#SUMA
def suma(x,y):
    return x + y

#RESTA
def resta(x,y):
    return x - y

#MULTIPLICACION
def multiplicacion(x,y):
    return x * y

#DIVISION
def division(x,y):
    return x / y

#Calling the app
proceso() 