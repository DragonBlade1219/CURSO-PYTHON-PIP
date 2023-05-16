'''
print("Hola Mundo, esto es Python")

print("Hola, Soy Andrés y Tengo 31 años")
#Esto es un comentario
print(12+5)
'''
import random

options = ("piedra", "papel", "tijera")
rounds = 1
computer_wins = 0
user_wins = 0
print("Hola Bienvenido al primer juego en Python aprendido en Platzi!")

while True:

  print("*" * 10)
  print("ROUND", rounds)
  print("*" * 10)
  print("Elije!")
  
  user_option = input( "Piedra, Papel o Tijera? => ")
  user_option = user_option.lower()
  rounds += 1
  
  if not user_option in options:
    print("Esa opción no es válida!")
    continue
    
  computer_option = random.choice(options) 
  
  print("Users option => ", user_option)
  print("Computer option => ", computer_option)
  
  if user_option == computer_option:
    print("Empate!")
    
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("piedra gana a tijera")
      print("User gana!")
      user_wins += 1
    else:
      print("Papel gana a piedra")
      print("Computer gana!")
      computer_wins += 1
      
  elif user_option == "tijera":
    if computer_option == "papel":
      print("tijera gana a papel")
      print("User gana!")
      user_wins += 1
    else:
      print("piedra gana a tijera")
      print("Computer gana!")
      computer_wins += 1
  
  elif user_option == "papel":
    if computer_option == "piedra":
      print("papel gana a piedra")
      print("User gana!")
      user_wins += 1
    else:
      print("tijera gana a papel")
      print("Computer gana!")
      computer_wins += 1
  
  print("Computer Wins => ", computer_wins)
  print("User Wins => ", user_wins)  
  
  if computer_wins == 2:
    print("El ganador es la computadora!!!")
    break
  if user_wins == 2:
    print("El ganador es la usuario!!!")
    break
  
  