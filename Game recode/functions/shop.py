import pickle
import time
import winsound

coins = 0
shop = {"atk": 0, "hp": 0, "crit": 0, "heal": 0, "armor": 0, "dodge": 0, "hcompanion": 0, "dcompanion":0}
shop =  pickle.load(open("Game recode/functions/shopdata/shop.dat", "rb"))
coins = pickle.load(open("Game recode/functions/shopdata/coins.dat", "rb"))
shopc = True

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