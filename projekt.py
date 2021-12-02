import random

#MÅSTE SKAPA EN LISTA FÖR ATT SPARA OCH UPPDATERA DATA KRING STATUSl
class Player():
    def __init__(self, lvl, hp, strength, inv):
        self.lvl = lvl
        self.hp = hp
        self.strength = strength
        self.inv = []

    def print_info(self):
        print(f"-------------------\nCurrent Level: {self.lvl}\nYour HP: {self.hp}\nStrength: {self.strength}\n-------------------""\n\n")


def door(player):
    door_type = random.choice(["Treasure", "Trap", "Monster"])
    print(door_type)    
    if door_type == "Treasure":
        item_strength = random(1,10)
        print("This sword a strength of {item_strength}.")
        if player.inv < 5:
            player.inv.append()
            print("Adding item to your inventory")
        elif player.inv >= 5:
            exchange = print(input("Your inventory is full, would you like to exchange it for one of your weakest sword?\nType: Y/N (Y for Yes, N for No)"))
            if exchange == "Y":
                player.inv.pop([4])
            elif exchange == "N":
                print("You left the treasure and countinued your journey")
            else:
                print("You need to type Y or N (Y for Yes, N for No):")
 
                    
class Choice():
    def __init__(self, options):
        self.options = options

    def print_info(self):
        print(f"What would you like to do?\nCheck player status: {Player}")
        
def start_game():
    player = Player(1,20,4,[])
    while player.hp > 0: #checka om spelaren dött?
        choice = input("What would you like to do?\nA: Check your stats\nB: Move onto next door\nC: Check your inventory\nYOUR CHOICE: ")
        if choice == "A":
            print("You chose to check your stats")  #SKAPA FUNKTION SOM PRINTAR UT STATS (class Player)
            player.print_info()
        elif choice == "B":
            print("You chose to pick a door")  #SKAPA FUNKTION SOM PRINTAR UT VAD MAN FICK BAKOM DÖRREN (class Scenarios)
            door(player)   
        elif choice == "C":
            print("You chose to check your inventory\n")  #SKAPA FUNKTION SOM PRINTAR UT INVENTORY (class Item)
            print(player.inv, "\n")
        else:
            print("Please type either A, B or C")

start_game()