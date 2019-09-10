import time
import pickle
import winsound

classc = True

player = {"name": "Maurice", "attack_min": 10, "attack_max": 15, "heal_min": 16, "heal_max": 25, "health": 100,"armor": 0}
monster = {"name": "Hendrik", "attack_min": 10, "attack_max": 20, "health": 200}
miss = 5
missm = 5
critp = 6
critm = 4
dodgem = 1.5
healmiss = 5


# Klassen

print("Choose one of the following classes:")
time.sleep(1)
print("        1) Priest         2) Rogue        3) Warrior")
print(" ATK :      7-13             10-15            12-18 ")
print("Heal :      24-35            12-20            16-25 ")
print("Health:     150               75              175   ")
print("Armor :     15                10              30    ")
print("Crit% :     6                 20              10    ")
print("Dodge :     5                 20              10    ")

while classc == True:
    player_choice = input()
    #Priest
    if player_choice == "1" :
        player["attack_min"] = 7
        player["attack_max"] = 13
        player["health"] = 150
        player["heal_min"] = 24
        player["heal_max"] = 35
        player["armor"] = 0.15
        critp = 6
        missm = 5
        dodgem = 1.5
        classc = False

        #Rogue
    elif player_choice == "2" :
        player["attack_min"] = 17
        player["attack_max"] = 22
        player["health"] = 100
        player["heal_min"] = 12
        player["heal_max"] = 20
        player["armor"] = 0.1
        critp = 20
        missm = 20
        dodgem = 2
        classc = False
        #Warrior
    elif player_choice == "3" :
        player["attack_min"] = 12
        player["attack_max"] = 18
        player["health"] = 175
        player["heal_min"] = 16
        player["heal_max"] = 25
        player["armor"] = 0.3
        critp = 10
        missm = 10
        dodgem = 1.5
        classc = False

    elif player_choice == "cheat376" :
        player["attack_min"] = 100
        player["attack_max"] = 150
        player["health"] = 10000
        player["heal_min"] = 16
        player["heal_max"] = 25
        player["armor"] = 0.3
        critp = 10
        missm = 10
        dodgem = 1.5
        classc = False

    else:
        print("Invalid Input")
        time.sleep(1.5)

#Resets

resetm = missm
resetheal = healmiss
reset = player["health"]


print("\n" * 40)
print("---" * 7)
print("Enter Player name")
player["name"] = input()
winsound.PlaySound("music" ,winsound.SND_ASYNC)






