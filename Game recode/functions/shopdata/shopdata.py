import pickle
import os

from ...functions.character import player, monster, miss, missm, critp, critm, dodgem, healmiss
shop =  pickle.load(open("Game recode/functions/shopdata/shop.dat", "rb"))



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
