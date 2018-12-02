import time

import random


class Character:
    def __init__(self, health):
        
        self.health = health


player = Character(100)

gwampi = Character(100)

print("Welcome to Gwampi's crusade!\nYour mission is to try and defeat the mighty dwarf Gwampi")
print("--------------------------------------------------------------------------------")
time.sleep(3)

print("This game is turn based, where you will stike first. You both start off at 100HP")
print("--------------------------------------------------------------------------------")
time.sleep(3)

print("You have three attacks\nSlash, which does 25HP\nChop, which does 35HP\nBash. which will do 30HP")
print("--------------------------------------------------------------------------------")
time.sleep(4.5)

print("Gwampi also has 3 different attacks that he can use on you")
print("--------------------------------------------------------------------------------")
time.sleep(3)

print("Your attacks, and gwampi's are both random\nSo there is a 50/50 chance you will land your hit\nAnd the same with Gwampi")
print("--------------------------------------------------------------------------------")
time.sleep(5)

print("The game ends when either of you get to 0HP\nGood Luck!")
print("--------------------------------------------------------------------------------")
time.sleep(4)

for x in range(0,20):
    time.sleep(0.1)
    print("\n")


#Player's Attacks#
def slash():
    attack = random.randint(0,1)

    if attack == 1:
        time.sleep(2)
        print("YOU HIT HIM!")
        time.sleep(2)
        gwampi.health = gwampi.health - 25
        print("Gwampi's health is at " + str(gwampi.health) + " hitpoints")
        end()
        gwampi_attack()
    else:
        time.sleep(2)
        print("YOU MISSED!")
        end()
        gwampi_attack()
    time.sleep(2)

def chop():
    attack = random.randint(0,1)

    if attack == 1:
        time.sleep(2)
        print("YOU HIT HIM!")
        time.sleep(2)
        gwampi.health = gwampi.health - 35
        print("Gwampi's health is at " + str(gwampi.health) + " hitpoints")
        end()
        gwampi_attack()
    else:
        time.sleep(2)
        print("YOU MISSED!")
        end()
        gwampi_attack()
    time.sleep(2)

def bash():
    attack = random.randint(0,1)

    if attack == 1:
        time.sleep(2)
        print("YOU HIT HIM!")
        time.sleep(2)
        gwampi.health = gwampi.health - 30
        print("Gwampi's health is at " + str(gwampi.health) + " hitpoints")
        end()
        gwampi_attack()
    else:
        time.sleep(2)
        print("YOU MISSED!")
        end()
        gwampi_attack()
    time.sleep(2)


#Gwampi's Attacks#

def gwampi_attack():
    print('------------------------------------------------------------')
    time.sleep(2)
    print("It's Gwampi's turn and he looks very mad!")
    gwampi_attack = random.randint(0,2)

    if gwampi_attack == 0:
        stomp()
    elif gwampi_attack == 1:
        fire_breath()
    elif gwampi_attack == 2:
        rock()

    print("Your health is at " + str(player.health) + " hitpoints")
    
    main_player()

def rock():
    attack = random.randint(0,1)

    if attack == 1:
        time.sleep(2)
        print("HE HIT YOU!")
        time.sleep(2)
        player.health = player.health - 35
        time.sleep(2)
        print("Your health is at " + str(player.health) + " hitpoints")
        end()
        main_player()
    else:
        time.sleep(2)
        print("HE MISSED!")
        time.sleep(2)
        end()
        main_player()
    time.sleep(2)

def fire_breath():
    attack = random.randint(0,1)

    if attack == 1:
        time.sleep(2)
        print("HE HIT YOU!")
        time.sleep(2)
        player.health = player.health - 30
        time.sleep(2)
        print("Your health is at " + str(player.health) + " hitpoints")
        end()
        main_player()
    else:
        time.sleep(2)
        print("HE MISSED!")
        time.sleep(2)
        end()
        main_player()
    time.sleep(2)

def stomp():
    attack = random.randint(0,1)

    if attack == 1:
        time.sleep(2)
        print("HE HIT YOU!")
        time.sleep(2)
        player.health = player.health - 25
        time.sleep(2)
        print("Your health is at " + str(player.health) + " hitpoints")
        end()
        main_player()
    else:
        time.sleep(2)
        print("HE MISSED!")
        time.sleep(2)
        end()
        main_player()
    time.sleep(2)

        


def main_player():
    print("It's your turn to strike gwampi, make sure it counts!")
    print('------------------------------------------------------------')
    answer = input("Would you like to Slash, Bash, or Chop the evil Gwampi?(s/b/c)")

    if answer == 's':
        slash()
    elif answer == 'b':
        bash()
    elif answer == 'c':
        chop()
    time.sleep(2)
    print("Gwampi's health is at " + str(gwampi.health) + " hitpoints")

    time.sleep(2)

    gwampi_attack()

def end():
    if player.health <= 0:
        player.health == 0
        print("The mighty Gwampi has defeated you, better luck next time.")
        time.sleep(2)
        
        answer = input("Would you like to play again?(y/n)")
        if answer == 'y':
            main_player()
        else:
            quit()
        
    if gwampi.health <= 0:
        gwampi.health == 0
        print("Wow! You were able to defeat the mighty Gwampi!")
        time.sleep(2)

        answer = input("Would you like to play again?(y/n)")
        if answer == 'y':
            main_player()
        else:
            quit()
    
main_player()
end()
    
