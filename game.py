#Changed Workspace

import os

#|Workspace|#

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


from random import randint
import time
import winsound
import pickle


game_running = True

game_results = []

def monster_atk(): 
    return randint(monster["attack_min"], monster["attack_max"])

def player_atk():
    return randint(player["attack_min"], player["attack_max"])

def player_heal():
    return randint(player["heal_min"], player["heal_max"])

def player_miss():
    return randint(1, 100)

def player_crit():
    return randint(1,100)

def game_ends(winner_name):
    print(f"{winner_name} won the game")
    time.sleep(2)






while game_running == True:

    counter = 0
    new_round = True
    classc = True
    player = {"name": "Maurice", "attack_min": 10, "attack_max": 15, "heal_min": 16, "heal_max": 25, "health": 100,"armor": 0}
    monster = {"name": "Hendrik", "attack_min": 10, "attack_max": 20, "health": 200}
    miss = 5
    missm = 5
    critp = 6
    critm = 4
    dodgem = 1.5
    healmiss = 5

    #Klassen


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
    



    resetm = missm
    resetheal = healmiss

    coins = 0
    shop = {"atk": 0, "hp": 0, "crit": 0, "heal": 0, "armor": 0, "dodge": 0, "hcompanion": 0, "dcompanion":0}
    shop =  pickle.load(open("Game recode/functions/shopdata/shop.dat", "rb"))
    coins = pickle.load(open("Game recode/functions/shopdata/coins.dat", "rb"))
    shopc = True

    #coins = coins + 1
    #pickle.dump(coins, open("Game recode/functions/shopdata/coins.dat", "wb"))
    #pickle.dump(shop, open("shop.dat", "wb"))
    #print (coins)

    print("Do you want to visit the Shop? You have " + str(coins) + " coins to spend")
    print(" 1) Yes          2) no")

    player_choice = input()

    if player_choice == "1":
        winsound.PlaySound("shopmusic" ,winsound.SND_ASYNC)
        

        while shopc == True:
            print("\n" * 3)
            print("What do you want to buy?                     coins: " + str(coins))
            print("\n")
            print("        Equipment")
            print("\n")
            print("1) (Bloodrush) +2 ATK            ( " + str(shop["atk"]) + "/5 )      3 Coins")
            print("2) (Remnant of the Gods) +5 HP   ( " + str(shop["hp"]) + "/5 )      3 Coins")
            print("3) (Hidden Dagger) +2 Crit%      ( " + str(shop["crit"]) + "/5 )      3 Coins")
            print("4) (Holy Water) +3 Heal          ( " + str(shop["heal"]) + "/5 )      3 Coins")
            print("5) (Iron Plateings) +3 Armor     ( " + str(shop["armor"]) + "/5 )      3 Coins")
            print("6) (Shrink Potion) +2 Dodge%     ( " + str(shop["dodge"]) + "/5 )      3 Coins")
            print("\n")
            print("         Pets")
            print("\n")
            print("7) (Guardian Angel) Restores 5% Of your missing Health after your Turn       ( " + str(shop["hcompanion"]) + "/1 )       20 Coins")
            print("8) (Sekhmet) Deals 12% Of your Attack damage after you attacked an enemy     ( " + str(shop["dcompanion"]) + "/1 )       20 Coins")
            print("\n")
            print("9) Exit")
        
            player_choice = input()

            if player_choice == "1":
                if coins < 3:
                    print("You don't have enough Coins for that, please choose another Item")
                    time.sleep(2)
                    shopc = True
                else:
                    if shop["atk"] == 5:
                        print("You already have the maximum ammount of Bloodrush, please choose another Item")
                        time.sleep(2)
                        shopc = True
                    else:
                        print("Are you sure you want to buy Bloodrush for 3 Coins?")
                        print("1) Yes           2) No")
                        player_choice = input()
                        if player_choice == "1" :
                            coins = coins - 3
                            shop["atk"] = shop["atk"] + 1
                            print("You succesfully bought 1 Bloodrush!")
                            time.sleep(2)
                            shopc = True
                            pickle.dump(coins, open("Game recode/functions/shopdata/coins.dat", "wb"))
                            pickle.dump(shop, open("Game recode/functions/shopdata/shop.dat", "wb"))
                        elif player_choice == "2" :
                            print("Canceled Payment")
                            time.sleep(2)
                        else:
                            print("Invalid Input, retry")
                            time.sleep(2)

            elif player_choice == "2":
                if coins < 3:
                    print("You don't have enough Coins for that, please choose another Item")
                    time.sleep(2)
                    shopc = True
                else:
                    if shop["hp"] == 5:
                        print("You already have the maximum ammount of Remnant of the Gods, please choose another Item")
                        time.sleep(2)
                        shopc = True
                    else:
                        print("Are you sure you want to buy Remnant of the Gods for 3 Coins?")
                        print("1) Yes           2) No")
                        player_choice = input()
                        if player_choice == "1" :
                            coins = coins - 3
                            shop["hp"] = shop["hp"] + 1
                            print("You succesfully bought 1 Remnant of the Gods!")
                            time.sleep(2)
                            shopc = True
                            pickle.dump(coins, open("Game recode/functions/shopdata/coins.dat", "wb"))
                            pickle.dump(shop, open("Game recode/functions/shopdata/shop.dat", "wb"))
                        elif player_choice == "2" :
                            print("Canceled Payment")
                            time.sleep(2)
                        else:
                            print("Invalid Input, retry")
                            time.sleep(2)
            elif player_choice == "3":
                if coins < 3:
                    print("You don't have enough Coins for that, please choose another Item")
                    time.sleep(2)
                    shopc = True
                else:
                    if shop["crit"] == 5:
                        print("You already have the maximum ammount of Hidden Dagger, please choose another Item")
                        time.sleep(2)
                        shopc = True
                    else:
                        print("Are you sure you want to buy Hidden Dagger for 3 Coins?")
                        print("1) Yes           2) No")
                        player_choice = input()
                        if player_choice == "1" :
                            coins = coins - 3
                            shop["crit"] = shop["crit"] + 1
                            print("You succesfully bought 1 Hidden Dagger!")
                            time.sleep(2)
                            shopc = True
                            pickle.dump(coins, open("Game recode/functions/shopdata/coins.dat", "wb"))
                            pickle.dump(shop, open("Game recode/functions/shopdata/shop.dat", "wb"))
                        elif player_choice == "2" :
                            print("Canceled Payment")
                            time.sleep(2)
                        else:
                            print("Invalid Input, retry")
                            time.sleep(2)
            elif player_choice == "4":
                if coins < 3:
                    print("You don't have enough Coins for that, please choose another Item")
                    time.sleep(2)
                    shopc = True
                else:
                    if shop["heal"] == 5:
                        print("You already have the maximum ammount of Holy Water, please choose another Item")
                        time.sleep(2)
                        shopc = True
                    else:
                        print("Are you sure you want to buy Holy Water for 3 Coins?")
                        print("1) Yes           2) No")
                        player_choice = input()
                        if player_choice == "1" :
                            coins = coins - 3
                            shop["heal"] = shop["heal"] + 1
                            print("You succesfully bought 1 Holy Water!")
                            time.sleep(2)
                            shopc = True
                            pickle.dump(coins, open("Game recode/functions/shopdata/coins.dat", "wb"))
                            pickle.dump(shop, open("Game recode/functions/shopdata/shop.dat", "wb"))
                        elif player_choice == "2" :
                            print("Canceled Payment")
                            time.sleep(2)
                        else:
                            print("Invalid Input, retry")
                            time.sleep(2)
            elif player_choice == "5":
                if coins < 3:
                    print("You don't have enough Coins for that, please choose another Item")
                    time.sleep(2)
                    shopc = True
                else:
                    if shop["armor"] == 5:
                        print("You already have the maximum ammount of Iron Plateings, please choose another Item")
                        time.sleep(2)
                        shopc = True
                    else:
                        print("Are you sure you want to buy Iron Plateings for 3 Coins?")
                        print("1) Yes           2) No")
                        player_choice = input()
                        if player_choice == "1" :
                            coins = coins - 3
                            shop["armor"] = shop["armor"] + 1
                            print("You succesfully bought 1 Iron Plateing!")
                            time.sleep(2)
                            shopc = True
                            pickle.dump(coins, open("Game recode/functions/shopdata/coins.dat", "wb"))
                            pickle.dump(shop, open("Game recode/functions/shopdata/shop.dat", "wb"))
                        elif player_choice == "2" :
                            print("Canceled Payment")
                            time.sleep(2)
                        else:
                            print("Invalid Input, retry")
                            time.sleep(2)
            elif player_choice == "6":
                if coins < 3:
                    print("You don't have enough Coins for that, please choose another Item")
                    time.sleep(2)
                    shopc = True
                else:
                    if shop["dodge"] == 5:
                        print("You already have the maximum ammount of Shrink Potions, please choose another Item")
                        time.sleep(2)
                        shopc = True
                    else:
                        print("Are you sure you want to buy Shrink Potion for 3 Coins?")
                        print("1) Yes           2) No")
                        player_choice = input()
                        if player_choice == "1" :
                            coins = coins - 3
                            shop["dodge"] = shop["dodge"] + 1
                            print("You succesfully bought 1 Shrink Potion!")
                            time.sleep(2)
                            shopc = True
                            pickle.dump(coins, open("Game recode/functions/shopdata/coins.dat", "wb"))
                            pickle.dump(shop, open("Game recode/functions/shopdata/shop.dat", "wb"))
                        elif player_choice == "2" :
                            print("Canceled Payment")
                            time.sleep(2)
                        else:
                            print("Invalid Input, retry")
                            time.sleep(2)
            elif player_choice == "7":
                if coins < 20:
                    print("You don't have enough Coins for that, please choose another Item")
                    time.sleep(2)
                    shopc = True
                else:
                    if shop["hcompanion"] == 1:
                        print("You already have the maximum ammount of Guardian Angels, please choose another Item")
                        time.sleep(2)
                        shopc = True
                    else:
                        print("Are you sure you want to buy Guardian Angel for 20 Coins?")
                        print("1) Yes           2) No")
                        player_choice = input()
                        if player_choice == "1" :
                            coins = coins - 20
                            shop["hcompanion"] = shop["hcompanion"] + 1
                            print("You succesfully bought 1 Guardian Angel!")
                            time.sleep(2)
                            shopc = True
                            pickle.dump(coins, open("Game recode/functions/shopdata/coins.dat", "wb"))
                            pickle.dump(shop, open("Game recode/functions/shopdata/shop.dat", "wb"))
                        elif player_choice == "2" :
                            print("Canceled Payment")
                            time.sleep(2)
                        else:
                            print("Invalid Input, retry")
                            time.sleep(2)
            elif player_choice == "8":
                if coins < 20:
                    print("You don't have enough Coins for that, please choose another Item")
                    time.sleep(2)
                    shopc = True
                else:
                    if shop["dcompanion"] == 1:
                        print("You already have the maximum ammount of Sekhmet, please choose another Item")
                        time.sleep(2)
                        shopc = True
                    else:
                        print("Are you sure you want to buy Sekhmet for 20 Coins?")
                        print("1) Yes           2) No")
                        player_choice = input()
                        if player_choice == "1" :
                            coins = coins - 20
                            shop["dcompanion"] = shop["dcompanion"] + 1
                            print("You succesfully bought 1 Sekhmet!")
                            time.sleep(2)
                            shopc = True
                            pickle.dump(coins, open("Game recode/functions/shopdata/coins.dat", "wb"))
                            pickle.dump(shop, open("Game recode/functions/shopdata/shop.dat", "wb"))
                        elif player_choice == "2" :
                            print("Canceled Payment")
                            time.sleep(2)
                        else:
                            print("Invalid Input, retry")
                            time.sleep(2)
            elif player_choice == "9":
                print("Are you sure you want to exit the shop?")
                print("1) Yes           2) No")
                player_choice = input()
                if player_choice == "1":
                    shopc = False
                    pickle.dump(coins, open("Game recode/functions/shopdata/coins.dat", "wb"))
                    pickle.dump(shop, open("Game recode/functions/shopdata/shop.dat", "wb"))

                elif player_choice == "2":
                    shopc = True

            else:
                print("Invalid Input")
                time.sleep(1.5)
                shopc = True

    shop =  pickle.load(open("Game recode/functions/shopdata/shop.dat", "rb"))
    coins = pickle.load(open("Game recode/functions/shopdata/coins.dat", "rb"))

    if shop["atk"] == 1:
        player["attack_min"] = player["attack_min"] + 2
        player["attack_max"] = player["attack_max"] + 2
    elif shop["atk"] == 2:
        player["attack_min"] = player["attack_min"] + 4
        player["attack_max"] = player["attack_max"] + 4
    elif shop["atk"] == 3:
        player["attack_min"] = player["attack_min"] + 6
        player["attack_max"] = player["attack_max"] + 6
    elif shop["atk"] == 4:
        player["attack_min"] = player["attack_min"] + 8
        player["attack_max"] = player["attack_max"] + 8
    elif shop["atk"] == 5:
        player["attack_min"] = player["attack_min"] + 10
        player["attack_max"] = player["attack_max"] + 10

    if shop["hp"] == 1:
        player["health"] = player["health"] + 5
    elif shop["hp"] == 2:
        player["health"] = player["health"] + 10
    elif shop["hp"] == 3:
        player["health"] = player["health"] + 15
    elif shop["hp"] == 4:
        player["health"] = player["health"] + 20
    elif shop["hp"] == 5:
        player["health"] = player["health"] + 25

    if shop["crit"] == 1:
        critp = critp + 2
    elif shop["crit"] == 2:
        critp = critp + 4
    elif shop["crit"] == 3:
        critp = critp + 6
    elif shop["crit"] == 4:
        critp = critp + 8
    elif shop["crit"] == 5:
        critp = critp + 10

    if shop["heal"] == 1:
        player["heal_min"] = player["heal_min"] + 3
        player["heal_max"] = player["heal_max"] + 3
    elif shop["heal"] == 2:
        player["heal_min"] = player["heal_min"] + 6
        player["heal_max"] = player["heal_max"] + 6
    elif shop["heal"] == 3:
        player["heal_min"] = player["heal_min"] + 9
        player["heal_max"] = player["heal_max"] + 9
    elif shop["heal"] == 4:
        player["heal_min"] = player["heal_min"] + 12
        player["heal_max"] = player["heal_max"] + 12
    elif shop["heal"] == 5:
        player["heal_min"] = player["heal_min"] + 15
        player["heal_max"] = player["heal_max"] + 15

    if shop["armor"] == 1:
        player["armor"] = player["armor"] + 0.03
    elif shop["armor"] == 2:
        player["armor"] = player["armor"] + 0.06
    elif shop["armor"] == 3:
        player["armor"] = player["armor"] + 0.09
    elif shop["armor"] == 4:
        player["armor"] = player["armor"] + 0.12
    elif shop["armor"] == 5:
        player["armor"] = player["armor"] + 0.15

    if shop["dodge"] == 1:
        missm = missm + 2
    elif shop["dodge"] == 2:
        missm = missm + 4
    elif shop["dodge"] == 3:
        missm = missm + 6
    elif shop["dodge"] == 4:
        missm = missm + 8
    elif shop["dodge"] == 5:
        missm = missm + 10
    


    print("\n" * 40)
    print("---" * 7)
    print("Enter Player name")
    player["name"] = input()
    winsound.PlaySound("music" ,winsound.SND_ASYNC)
    reset = player["health"]

    print("---" * 7)
    print(player["name"] + " has " + str(player["health"]) + " HP ")
    print(monster["name"] + " has " + str(monster["health"]) + " HP ")

    while new_round == True:

        counter = counter + 1
        player_won = False
        monster_won = False

        print("---" * 7)
        print("Please select your action")
        print("1) Attack")
        print("2) Heal")
        print("3) Exit")
        print("4) Scoreboard")
        print("\n" * 10)

        player_choice = input()

        if player_choice == "1":
            player_dmg = player_atk()
            if player_miss() >= miss :  
                miss = miss * dodgem
                if miss >= 100:
                    miss = 100
                if player_crit() <= critp :
                    player_dmg = player_dmg * 2
                    print(player["name"] + " dealt " + str(player_dmg) + " damage to " + monster["name"] + " (critical hit) ")
                    monster["health"] = monster["health"] - player_dmg
                    time.sleep(1)
                else:
                    monster["health"] = monster["health"] - player_dmg
                    print(player["name"] + " dealt " + str(player_dmg) + " damage to " + monster["name"])
                    time.sleep(1)
               
                
            else:
                print(player["name"] + " missed his attack ")
                miss = 5
                time.sleep(1)
            
            if monster["health"] <= 0 :
                player_won = True
                
            
            else:
                if player_miss() >= missm :
                    monster_dmg = monster_atk() * (1- player["armor"])
                    monster_dmg = int(monster_dmg)
                    missm = missm * dodgem
                    if missm >= 100:
                        miss = 100
                    if player_crit() <= critm :
                     monster_dmg = monster_dmg * 2
                     player["health"] = player["health"] - (monster_dmg)
                     print (monster["name"] + " dealt " + str(monster_dmg) + " damage to " + player["name"] + (" (critical hit) "))
                     time.sleep(1.5)


                    else:
                     player["health"] = player["health"] - (monster_dmg)
                     print (monster["name"] + " dealt " + str(monster_dmg) + " damage to " + player["name"])
                     time.sleep(1.5)
                else:
                    print((monster["name"] + " missed his attack "))
                    missm = resetm
                    time.sleep(1)
            if player["health"] <= 0:
                monster_won = True

            if shop["dcompanion"] == 1:
                dmgh = player_dmg * 0.12
                dmgh = int(dmgh)
                monster["health"] = monster["health"] - dmgh
                print("Sekhmet dealt " + str(dmgh) + " damage to" + monster["name"])
                time.sleep(1.5)
                if monster["health"] <= 0 :
                    player_won = True
            
            if shop["hcompanion"] == 1:
                hheal = (reset - player["health"]) * 0.05
                hheal = int(hheal)
                player["health"] = player["health"] + hheal
                print("Guardian Angel healed you for " + str(hheal) + " HP")
                time.sleep(1.5)



        elif player_choice == "2":
            if player_miss() >= healmiss :
                healmiss = healmiss * 1.5
                if healmiss >= 100:
                    healmiss = 100
                player_h = player_heal()
                player["health"] = player["health"] + player_h
                print(player["name"] + " got healed by " + str(player_h) + " HP ")
                time.sleep(1)
            else :
                print("Healing failed")
                time.sleep(1)
                healmiss = 5

            if player_miss() >= missm :
                    monster_dmg = monster_atk() * (1- player["armor"])
                    monster_dmg = int(monster_dmg)
                    missm = missm * dodgem
                    if missm >= 100:
                        miss = 100
                    if player_crit() <= critm :
                     monster_dmg = monster_dmg * 2
                     player["health"] = player["health"] - monster_dmg
                     print (monster["name"] + " dealt " + str(monster_dmg) + " damage to " + player["name"] + (" (critical hit) "))
                     time.sleep(1.5)


                    else:
                     player["health"] = player["health"] - monster_dmg
                     print (monster["name"] + " dealt " + str(monster_dmg) + " damage to " + player["name"])
                     time.sleep(1.5)
            else:
                print((monster["name"] + " missed his attack "))
                missm = resetm
                time.sleep(1)
            if player["health"] <= 0:
                monster_won = True

            if shop["hcompanion"] == 1:
                hheal = (reset - player["health"]) * 0.05
                hheal = int(hheal)
                player["health"] = player["health"] + hheal
                print("Guardian Angel healed you for " + str(hheal) + " HP")
                time.sleep(1.5)

            

        elif player_choice == "3":
            new_round = False
            game_running = False 

        elif player_choice == "4":
            for score in game_results:
                print(score)
            input("Press any Key to continue")    
            


        else:
            print("Invalid Input")
            time.sleep(1.5)

        if player_won == False and monster_won == False and player_choice!= "3":
            print("\n" * 10)
            print(player["name"] + " has " + str(player["health"]) + " HP left ")
            print(monster["name"] + " has " + str(monster["health"]) + " HP left ")

        elif player_won:
            game_ends(player["name"])
            round_result = {"name": player["name"], "health": player["health"], "rounds": counter, "Stage" : "Stage 1"}
            game_results.append(round_result)
            new_round = False
            level_2 = True
            coins = coins + 1
            pickle.dump(coins, open("Game recode/functions/shopdata/coins.dat", "wb"))

        elif monster_won:
            game_ends(monster["name"])
            round_result = {"name": player["name"], "health": player["health"], "rounds": counter, "stage" : "Stage 2"}
            game_results.append(round_result)
            new_round = False

    while level_2 == True:
        player["health"] = reset
        print("\n" * 30)
        print("You succesfully slayed " + monster["name"] + " !! ")
        time.sleep(1)
        print("Choose a reward!")
        time.sleep(1)
        print("1) +50 HP")
        print("2) +5 ATK")
        print("3) +3% Critical strike chance")
        print("4) +8 Heal")
        print("5) +10 Armor")


        player_choice = input()

        if player_choice == "1":
            player["health"] = player["health"] + 50
            print("HP increased by 50!")
        if player_choice == "2":
            player["attack_min"] = player["attack_min"] + 5
            player["attack_max"] = player["attack_max"] + 5
            print("ATK increased by 5!")
        if player_choice == "3":
            critp = critp + 6
            print("Critical strike chance increased by 3%!")
        if player_choice == "4":
            player["heal_min"] = player["heal_min"] + 8
            player["heal_max"] = player["heal_max"] + 8
            print("Heal increased by 8!")
        if player_choice == "5":
            player["armor"] = player["armor"] + 0.1
            print("Armor increased by 10!")
        time.sleep(2)

        new_round = True
        counter2 = 0
        monster2 = {"name": "Merzimaxi", "attack_min": 15, "attack_max": 25, "health": 250}
        level_2 = False
        reset = player["health"]
        missm = resetm
        healmiss = resetheal

        print("\n" * 40)
        print(" Prepare to face " + monster2["name"] + "!")
        time.sleep(4)

        def monster2_atk(): 
            return randint(monster2["attack_min"], monster2["attack_max"])
        
        print("\n" * 40)
        print(player["name"] + " has " + str(player["health"]) + " HP ")
        print(monster2["name"] + " has " + str(monster2["health"]) + " HP ")

        while new_round == True:
            counter2 = counter2 + 1
            player_won = False
            monster_won = False

            print("---" * 7)
            print("Please select your action")
            print("1) Attack")
            print("2) Heal")
            print("3) Exit")
            print("4) Scoreboard")
            print("\n" * 10)

            player_choice = input()

            if player_choice == "1":
                if player_miss() >= miss :  
                    player_dmg = player_atk()
                    miss = miss * 1.5
                    if miss >= 100:
                        miss = 100
                    if player_crit() <= critp :
                        player_dmg = player_dmg * 2
                        print(player["name"] + " dealt " + str(player_dmg) + " damage to " + monster2["name"] + " (critical hit) ")
                        monster2["health"] = monster2["health"] - player_dmg
                        time.sleep(1)
                    else:
                        monster2["health"] = monster2["health"] - player_dmg
                        print(player["name"] + " dealt " + str(player_dmg) + " damage to " + monster2["name"])
                        time.sleep(1)
                
                    
                else:
                    print(player["name"] + " missed his attack ")
                    miss = 5
                    time.sleep(1)
                
                if monster2["health"] <= 0 :
                    player_won = True
                    
                
                else:
                    if player_miss() >= missm :
                        monster2_dmg = monster2_atk() * (1- player["armor"])
                        monster2_dmg = int(monster2_dmg)
                        missm = missm * 1.5
                        if missm >= 100:
                            miss = 100
                        if player_crit() <= critm :
                            monster2_dmg = monster2_dmg * 2
                            player["health"] = player["health"] - monster2_dmg
                            print (monster2["name"] + " dealt " + str(monster2_dmg) + " damage to " + player["name"] + (" (critical hit) "))
                            time.sleep(1.5)
                        else:
                            player["health"] = player["health"] - monster2_dmg
                            print (monster2["name"] + " dealt " + str(monster2_dmg) + " damage to " + player["name"])
                            time.sleep(1.5)
                    else:
                        print((monster2["name"] + " missed his attack "))
                        missm = resetm
                        time.sleep(1)
                if player["health"] <= 0:
                    monster_won = True

                if shop["dcompanion"] == 1:
                    dmgh = player_dmg * 0.12
                    dmgh = int(dmgh)
                    monster["health"] = monster["health"] - dmgh
                    print("Sekhmet dealt " + str(dmgh) + " damage to" + monster2["name"])
                    time.sleep(1.5)
                    if monster2["health"] <= 0 :
                        player_won = True
            
                if shop["hcompanion"] == 1:
                    hheal = (reset - player["health"]) * 0.05
                    hheal = int(hheal)
                    player["health"] = player["health"] + hheal
                    print("Guardian Angel healed you for " + str(hheal) + " HP")
                    time.sleep(1.5)


            elif player_choice == "2":
                if player_miss() >= healmiss :
                    healmiss = healmiss * 1.5
                    if healmiss >= 100:
                        healmiss = 100
                    player_h = player_heal()
                    player["health"] = player["health"] + player_h
                    print(player["name"] + " got healed by " + str(player_h) + " HP ")
                    time.sleep(1)
                else :
                    print("Healing failed")
                    time.sleep(1)
                    healmiss = 5

                if player_miss() >= missm :
                        monster2_dmg = monster2_atk() * (1 - player["armor"])
                        monster2_dmg = int(monster2_dmg)
                        missm = missm * 1.5
                        if missm >= 100:
                            miss = 100
                        if player_crit() <= critm :
                            monster2_dmg = monster2_dmg * 2
                            player["health"] = player["health"] - monster2_dmg
                            print (monster2["name"] + " dealt " + str(monster2_dmg) + " damage to " + player["name"] + (" (critical hit) "))
                            time.sleep(1.5)
                        else:
                            player["health"] = player["health"] - monster2_dmg
                            print (monster2["name"] + " dealt " + str(monster2_dmg) + " damage to " + player["name"])
                            time.sleep(1.5)
                else:
                    print((monster2["name"] + " missed his attack "))
                    missm = resetm
                    time.sleep(1)
                if player["health"] <= 0:
                    monster_won = True
                    
                if shop["hcompanion"] == 1:
                    hheal = (reset - player["health"]) * 0.05
                    hheal = int(hheal)
                    player["health"] = player["health"] + hheal
                    print("Guardian Angel healed you for " + str(hheal) + " HP")
                    time.sleep(1.5)



            elif player_choice == "3":
                new_round = False
                game_running = False 

            elif player_choice == "4":
                for score in game_results:
                    print(score)
                input("Press any Key to continue")    
                


            else:
                print("Invalid Input")
                time.sleep(1.5)

            if player_won == False and monster_won == False and player_choice!= "3":
                print("\n" * 10)
                print(player["name"] + " has " + str(player["health"]) + " HP left ")
                print(monster2["name"] + " has " + str(monster2["health"]) + " HP left ")

            elif player_won:
                game_ends(player["name"])
                round_result = {"name": player["name"], "health": player["health"], "rounds": counter2, "stage": "Stage 2"}
                game_results.append(round_result)
                new_round = False
                level_3 = True
                coins = coins + 1
                pickle.dump(coins, open("Game recode/functions/shopdata/coins.dat", "wb"))

            elif monster_won:
                game_ends(monster2["name"])
                round_result = {"name": player["name"], "health": player["health"], "rounds": counter2, "stage": "Stage 2"}
                game_results.append(round_result)
                new_round = False
    
    while level_3 == True:
        player["health"] = reset
        print("\n" * 30)
        print("You succesfully slayed " + monster2["name"] + " !! ")
        time.sleep(1)
        print("Choose a reward!")
        time.sleep(1)
        print("1) +50 HP")
        print("2) +5 ATK")
        print("3) +3% Critical strike chance")
        print("4) +8 Heal")
        print("5) +10 Armor")

        


        player_choice = input()

        if player_choice == "1":
            player["health"] = player["health"] + 50
            print("HP increased by 50!")
        if player_choice == "2":
            player["attack_min"] = player["attack_min"] + 5
            player["attack_max"] = player["attack_max"] + 5
            print("ATK increased by 5!")
        if player_choice == "3":
            critp = critp + 6
            print("Critical strike chance increased by 3%!")
        if player_choice == "4":
            player["heal_min"] = player["heal_min"] + 8
            player["heal_max"] = player["heal_max"] + 8
            print("Heal increased by 8!")
        if player_choice == "5":
            player["armor"] = player["armor"] + 0.1
            print("Armor increased by 10!")
        time.sleep(2)

        new_round = True
        counter3 = 0
        monster3 = {"name": "Epicus Maximus", "attack_min": 20, "attack_max": 30, "health": 300}
        level_3 = True
        reset = player["health"]
        missm = resetm
        healmiss = resetheal

        print("\n" * 40)
        print(" Prepare to face " + monster3["name"] + "!")
        time.sleep(4)

        def monster3_atk(): 
            return randint(monster3["attack_min"], monster3["attack_max"])
        
        print("\n" * 40)
        print(player["name"] + " has " + str(player["health"]) + " HP ")
        print(monster3["name"] + " has " + str(monster3["health"]) + " HP ")

        while level_3 == True:
            counter3 = counter3 + 1
            player_won = False
            monster_won = False

            print("---" * 7)
            print("Please select your action")
            print("1) Attack")
            print("2) Heal")
            print("3) Exit")
            print("4) Scoreboard")
            print("\n" * 10)

            player_choice = input()

            if player_choice == "1":
                if player_miss() >= miss :  
                    player_dmg = player_atk()
                    miss = miss * dodgem
                    if miss >= 100:
                        miss = 100
                    if player_crit() <= critp :
                        player_dmg = player_dmg * 2
                        print(player["name"] + " dealt " + str(player_dmg) + " damage to " + monster3["name"] + " (critical hit) ")
                        monster3["health"] = monster3["health"] - player_dmg
                        time.sleep(1)
                    else:
                        monster3["health"] = monster3["health"] - player_dmg
                        print(player["name"] + " dealt " + str(player_dmg) + " damage to " + monster3["name"])
                        time.sleep(1)
                
                    
                else:
                    print(player["name"] + " missed his attack ")
                    miss = 5
                    time.sleep(1)
                
                if monster3["health"] <= 0 :
                    player_won = True
                    
                
                else:
                    if player_miss() >= missm :
                        monster3_dmg = monster3_atk() * (1- player["armor"])
                        monster3_dmg = int(monster3_dmg)
                        missm = missm * dodgem
                        if missm >= 100:
                            miss = 100
                        if player_crit() <= critm :
                            monster3_dmg = monster3_dmg * 2
                            player["health"] = player["health"] - monster2_dmg
                            print (monster3["name"] + " dealt " + str(monster3_dmg) + " damage to " + player["name"] + (" (critical hit) "))
                            time.sleep(1.5)
                        else:
                            player["health"] = player["health"] - monster3_dmg
                            print (monster3["name"] + " dealt " + str(monster3_dmg) + " damage to " + player["name"])
                            time.sleep(1.5)
                    else:
                        print((monster3["name"] + " missed his attack "))
                        missm = resetm
                        time.sleep(1)
                if player["health"] <= 0:
                    monster_won = True

                
                if shop["dcompanion"] == 1:
                    dmgh = player_dmg * 0.12
                    dmgh = int(dmgh)
                    monster["health"] = monster["health"] - dmgh
                    print("Sekhmet dealt " + str(dmgh) + " damage to" + monster3["name"])
                    time.sleep(1.5)
                    if monster3["health"] <= 0 :
                        player_won = True
            
                if shop["hcompanion"] == 1:
                    hheal = (reset - player["health"]) * 0.05
                    hheal = int(hheal)
                    player["health"] = player["health"] + hheal
                    print("Guardian Angel healed you for " + str(hheal) + " HP")
                    time.sleep(1.5)



            elif player_choice == "2":
                if player_miss() >= healmiss :
                    healmiss = healmiss * 1.5
                    if healmiss >= 100:
                        healmiss = 100
                    player_h = player_heal()
                    player["health"] = player["health"] + player_h
                    print(player["name"] + " got healed by " + str(player_h) + " HP ")
                    time.sleep(1)
                else :
                    print("Healing failed")
                    time.sleep(1)
                    healmiss = 5

                if player_miss() >= missm :
                        monster3_dmg = monster3_atk() * (1- player["armor"])
                        monster3_dmg = int(monster3_dmg)
                        missm = missm * dodgem
                        if missm >= 100:
                            miss = 100
                        if player_crit() <= critm :
                            monster3_dmg = monster3_dmg * 2
                            player["health"] = player["health"] - monster3_dmg
                            print (monster3["name"] + " dealt " + str(monster3_dmg) + " damage to " + player["name"] + (" (critical hit) "))
                            time.sleep(1.5)
                        else:
                            player["health"] = player["health"] - monster3_dmg
                            print (monster3["name"] + " dealt " + str(monster3_dmg) + " damage to " + player["name"])
                            time.sleep(1.5)
                else:
                    print((monster3["name"] + " missed his attack "))
                    missm = resetm
                    time.sleep(1)
                if player["health"] <= 0:
                    monster_won = True
                
                if shop["hcompanion"] == 1:
                    hheal = (reset - player["health"]) * 0.05
                    hheal = int(hheal)
                    player["health"] = player["health"] + hheal
                    print("Guardian Angel healed you for " + str(hheal) + " HP")
                    time.sleep(1.5)



            elif player_choice == "3":
                new_round = False
                game_running = False 

            elif player_choice == "4":
                for score in game_results:
                    print(score)
                input("Press any Key to continue")    
                


            else:
                print("Invalid Input")
                time.sleep(1.5)

            if player_won == False and monster_won == False and player_choice!= "3":
                print("\n" * 10)
                print(player["name"] + " has " + str(player["health"]) + " HP left ")
                print(monster3["name"] + " has " + str(monster3["health"]) + " HP left ")

            elif player_won:
                game_ends(player["name"])
                round_result = {"name": player["name"], "health": player["health"], "rounds": counter3, "stage": "Stage 3"}
                game_results.append(round_result)
                level_3 = False
                level_4 = True
                coins = coins + 1
                pickle.dump(coins, open("Game recode/functions/shopdata/coins.dat", "wb"))

            elif monster_won:
                game_ends(monster3["name"])
                round_result = {"name": player["name"], "health": player["health"], "rounds": counter3, "stage": "Stage 3"}
                game_results.append(round_result)
                level_3 = False


    while level_4 == True:
        player["health"] = reset
        print("\n" * 30)
        print("You succesfully slayed " + monster3["name"] + " !! ")
        time.sleep(1)
        print("Choose a reward!")
        time.sleep(1)
        print("1) +50 HP")
        print("2) +5 ATK")
        print("3) +3% Critical strike chance")
        print("4) +8 Heal")
        print("5) +10 Armor")

        


        player_choice = input()

        if player_choice == "1":
            player["health"] = player["health"] + 50
            print("HP increased by 50!")
        if player_choice == "2":
            player["attack_min"] = player["attack_min"] + 5
            player["attack_max"] = player["attack_max"] + 5
            print("ATK increased by 5!")
        if player_choice == "3":
            critp = critp + 6
            print("Critical strike chance increased by 3%!")
        if player_choice == "4":
            player["heal_min"] = player["heal_min"] + 8
            player["heal_max"] = player["heal_max"] + 8
            print("Heal increased by 8!")
        if player_choice == "5":
            player["armor"] = player["armor"] + 0.1
            print("Armor increased by 10!")
        time.sleep(2)

        new_round = True
        counter4 = 0
        monster4 = {"name": "Jasmyn", "attack_min": 20, "attack_max": 30, "health": 200}
        level_4 = True
        reset = player["health"]
        missm = resetm
        healmiss = resetheal

        print("\n" * 40)
        print(" Prepare to face " + monster4["name"] + "!")
        time.sleep(4)

        def monster4_atk(): 
            return randint(monster4["attack_min"], monster4["attack_max"])
        
        print("\n" * 40)
        print(player["name"] + " has " + str(player["health"]) + " HP ")
        print(monster4["name"] + " has " + str(monster4["health"]) + " HP ")

        while level_4 == True:
            counter4 = counter4 + 1
            player_won = False
            monster_won = False

            print("---" * 7)
            print("Please select your action")
            print("1) Attack")
            print("2) Heal")
            print("3) Exit")
            print("4) Scoreboard")
            print("\n" * 10)

            player_choice = input()

            if player_choice == "1":
                if player_miss() >= miss :  
                    player_dmg = player_atk()
                    miss = miss * dodgem
                    if miss >= 100:
                        miss = 100
                    if player_crit() <= critp :
                        player_dmg = player_dmg * 2
                        print(player["name"] + " dealt " + str(player_dmg) + " damage to " + monster4["name"] + " (critical hit) ")
                        monster4["health"] = monster4["health"] - player_dmg
                        time.sleep(1)
                    else:
                        monster4["health"] = monster4["health"] - player_dmg
                        print(player["name"] + " dealt " + str(player_dmg) + " damage to " + monster4["name"])
                        time.sleep(1)
                
                    
                else:
                    print(player["name"] + " missed his attack ")
                    miss = 5
                    time.sleep(1)
                
                if monster4["health"] <= 0 :
                    player_won = True
                    
                
                else:
                    if player_miss() >= missm :
                        monster4_dmg = monster4_atk() * (1- player["armor"])
                        monster4_dmg = int(monster4_dmg)
                        missm = missm * dodgem
                        if missm >= 100:
                            miss = 100
                        if player_crit() <= critm :
                            monster4_dmg = monster4_dmg * 2
                            player["health"] = player["health"] - monster4_dmg
                            print (monster4["name"] + " dealt " + str(monster4_dmg) + " damage to " + player["name"] + (" (critical hit) "))
                            time.sleep(1.5)
                        else:
                            player["health"] = player["health"] - monster4_dmg
                            print (monster4["name"] + " dealt " + str(monster4_dmg) + " damage to " + player["name"])
                            time.sleep(1.5)
                            jasmynh = player_dmg * 0.25
                            jasmynh = int(jasmynh)
                            print (monster4["name"] + " used black magic to restore " + str(jasmynh) + " HP!")
                            monster4["health"] = monster4["health"] + jasmynh
                            time.sleep (1.5)

                    else:
                        print((monster4["name"] + " missed his attack "))
                        missm = resetm
                        time.sleep(1)
                if player["health"] <= 0:
                    monster_won = True

                
                if shop["dcompanion"] == 1:
                    dmgh = player_dmg * 0.12
                    dmgh = int(dmgh)
                    monster["health"] = monster["health"] - dmgh
                    print("Sekhmet dealt " + str(dmgh) + " damage to" + monster4["name"])
                    time.sleep(1.5)
                    if monster4["health"] <= 0 :
                        player_won = True
            
                if shop["hcompanion"] == 1:
                    hheal = (reset - player["health"]) * 0.05
                    hheal = int(hheal)
                    player["health"] = player["health"] + hheal
                    print("Guardian Angel healed you for " + str(hheal) + " HP")
                    time.sleep(1.5)



            elif player_choice == "2":
                if player_miss() >= healmiss :
                    healmiss = healmiss * 1.5
                    if healmiss >= 100:
                        healmiss = 100
                    player_h = player_heal()
                    player["health"] = player["health"] + player_h
                    print(player["name"] + " got healed by " + str(player_h) + " HP ")
                    time.sleep(1)
                else :
                    print("Healing failed")
                    time.sleep(1)
                    healmiss = 5

                if player_miss() >= missm :
                        monster4_dmg = monster4_atk() * (1- player["armor"])
                        monster4_dmg = int(monster4_dmg)
                        missm = missm * dodgem
                        if missm >= 100:
                            miss = 100
                        if player_crit() <= critm :
                            monster4_dmg = monster4_dmg * 2
                            player["health"] = player["health"] - monster4_dmg
                            print (monster4["name"] + " dealt " + str(monster4_dmg) + " damage to " + player["name"] + (" (critical hit) "))
                            time.sleep(1.5)
                        else:
                            player["health"] = player["health"] - monster4_dmg
                            print (monster4["name"] + " dealt " + str(monster4_dmg) + " damage to " + player["name"])
                            time.sleep(1.5)
                else:
                    print((monster4["name"] + " missed his attack "))
                    missm = resetm
                    time.sleep(1)
                if player["health"] <= 0:
                    monster_won = True

                if shop["hcompanion"] == 1:
                    hheal = (reset - player["health"]) * 0.05
                    hheal = int(hheal)
                    player["health"] = player["health"] + hheal
                    print("Guardian Angel healed you for " + str(hheal) + " HP")
                    time.sleep(1.5)



            elif player_choice == "3":
                new_round = False
                game_running = False 

            elif player_choice == "4":
                for score in game_results:
                    print(score)
                input("Press any Key to continue")    
                


            else:
                print("Invalid Input")
                time.sleep(1.5)

            if player_won == False and monster_won == False and player_choice!= "3":
                print("\n" * 10)
                print(player["name"] + " has " + str(player["health"]) + " HP left ")
                print(monster4["name"] + " has " + str(monster4["health"]) + " HP left ")

            elif player_won:
                game_ends(player["name"])
                round_result = {"name": player["name"], "health": player["health"], "rounds": counter3, "stage": "Stage 3"}
                game_results.append(round_result)
                level_4 = False
                level_5 = True
                coins = coins + 1
                pickle.dump(coins, open("Game recode/functions/shopdata/coins.dat", "wb"))

            elif monster_won:
                game_ends(monster4["name"])
                round_result = {"name": player["name"], "health": player["health"], "rounds": counter3, "stage": "Stage 3"}
                game_results.append(round_result)
                level_4 = False   
    

        
