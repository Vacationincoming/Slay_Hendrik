from random import randint
import time
import winsound    #pygame?
import pickle
import os

#|Workspace|#

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

import functions.character as character_choice
import functions.shop as shop
import functions.shopdata.shopdata as shopdata

game_running = True
game_results = []

while game_running == True :
    
    character_choice  #Char Auswahl

    shop #shop

    shopdata #stats Anpassung

    







 
