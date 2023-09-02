import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]

user_choice = int(input("Qué quieres elegir? Escribe (0) para Piedra, (1) para Papel o (2) para Tijera.\n"))
print(images[user_choice])

computer_choice = random.randint(0,2)
print(images[computer_choice])

if user_choice >= 3 or user_choice < 0:
  print("Escribe un numero entre 0 y 2. Prueba nuevamente 🧐")
else:
  if computer_choice == 0 and user_choice == 2:
    print("You lose")

  if user_choice == 0 and computer_choice == 2:
    print("Ganaste")
  elif user_choice > computer_choice:
    print("¡Ganaste! 😁")
  elif computer_choice == user_choice:
    print("Es un empate 🤨")
  elif user_choice < computer_choice:
    print("Perdiste 😢") 