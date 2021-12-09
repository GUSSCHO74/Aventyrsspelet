from _typeshed import Self
import random

#MÅSTE SKAPA EN LISTA FÖR ATT SPARA OCH UPPDATERA DATA KRING STATUS
class Player():
    def __init__(self, lvl, hp, strength, inv):
        self.lvl = lvl
        self.hp = hp
        self.strength = strength
        self.inv = []

    def print_info(self):
        print(f"-----------------\nCurrent Level: {self.lvl}\nYour HP: {self.hp}\nStrength: {self.strength}\n-----------------")


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
    elif door_type == "Trap":
        #MÅSTE FIXA ATT FÖR VARJE TRAP TAR MAN 1 DAMAGE PÅ SITT player.hp
    elif door_type == "Monster":
        monster_strength = random(1,10)
        print("The monster has a strength of {monster.strength}.")
    
        
def start_game():
    player = Player(1,20,4,[])
    while player.hp > 0: #checka om spelaren dött?
        choice = input("What would you like to do?\nA: Check your stats\nB: Pick your door\nC: Check your inventory\nYOUR CHOICE: ")
        if choice == "A":
            print()
            print("YOUR STATS:")  #SKAPA FUNKTION SOM PRINTAR UT STATS (class Player)
            player.print_info()
            print()
        elif choice == "B":
            print()
            door(player)
            if door.type(Player) == "Treasure":
                print("You have found a treasure with a sword of strength {item.strength}")
            elif door.type(Player) == "Trap":
                print("You fell into a trap")
            elif door.type(Player) == "Monster":
                print("You have encountered a monster with the strength of {Monster.strength}")
        elif choice == "C":
            print()
            print("YOUR INVENTORY:\n--------------")  #SKAPA FUNKTION SOM PRINTAR UT INVENTORY (class Item)
            print(player.inv)
            print()
        else:
            print()
            print("Please type either A, B or C\n")

start_game()