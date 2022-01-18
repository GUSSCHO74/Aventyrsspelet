import random

#MÅSTE SKAPA EN LISTA FÖR ATT SPARA OCH UPPDATERA DATA KRING STATUS
class Player():
    def __init__(self, lvl, hp, strength, inv):
        self.lvl = lvl
        self.hp =  hp
        self.strength = strength
        self.inv = []

    def stats(self):
        print(f"-----------------\nCurrent Level: {self.lvl}\nYour HP: {self.hp}\nStrength: {self.strength}\n-----------------")
   
class Item():
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength


diamond_sword = Item("Diamond sword", 25)
iron_sword = Item("Iron sword", 20)
gold_sword = Item("Gold sword", 15)
stone_sword = Item("Stone sword", 10)
wooden_sword = Item("Wooden sword", 5)

list_of_items = [diamond_sword, iron_sword, gold_sword, stone_sword, wooden_sword]

def door(player):
    door_type = random.choice(["Treasure", "Trap", "Monster"]) 
    if door_type == "Treasure":
        random_treasure = random.choice(list_of_items)
        print("You received a" + random_treasure)
        print(f"This item has a strength of {random_treasure.strength}.")
        if player.inv < 5:
            player.inv.append(random_treasure)
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
        trap_damage = random.randint(1,3)
        player.hp = player.hp - trap_damage
        print("You encountered a trap")
        print("The trap dealt" + trap_damage + "damage")
    elif door_type == "Monster":
        monster_strength = random.randint(20, 40)
        print("The monster has a strength of {monster_strength}.")
        if monster_strength > player.strength:
            player.hp = player.hp - 1
            print("The monster won the battle and you lost 1 hp")
        if monster_strength < player.strength:
            player.lvl = player.lvl + 1
            print("You won the battle against the monster")
            print("Your level went up by one point")

                
def start_game():
    player = Player(1,20,4,[])
    while player.hp > 0: #checka om spelaren dött?
        choice = input("What would you like to do?\nA: Check your stats\nB: Pick your door\nC: Check your inventory\nYOUR CHOICE: ")
        if choice == "A":
            print()
            print("YOUR STATS:")  #SKAPA FUNKTION SOM PRINTAR UT STATS (class Player)
            player.stats()
            print()
        elif choice == "B":
            print()
            door(player)
            if door.type(Player) == "Treasure":
                print("You have found a treasure with a sword of strength {item.strength}")
            elif door.type(Player) == "Trap":
                print("You fell into a trap")
            elif door.type(Player) == "Monster":
                print("You have encountered a monster with the strength of {monster.strength}")
        elif choice == "C":
            print()
            print("YOUR INVENTORY:\n--------------")  #SKAPA FUNKTION SOM PRINTAR UT INVENTORY (class Item)
            print(player.inv)
            print()
        else:
            print()
            print("Please type either A, B or C\n")

start_game()