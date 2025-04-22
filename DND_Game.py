from itertools import filterfalse
from math import e
import random
player = 0
global health
health = 100
playing = True
no = 0
yes = 1
global gold
goblins = 50
manticore = 100
minotour = 150
enemy_army = 1000
ally_army = 500
global damage
damage = 10
inventory = {1: 'Sword',
             2: 'Shield',
             3: 'Healing tonic',
             4: '50x Gold'}

tavernlist = {1: 'Ale = 2 Gold',
              2: 'Big Ale = 4 Gold',
              3: 'Da biggest Ale = 6 Gold',
              4: 'Loaf of Bread = 2 Gold',
              5: 'Wheel of Cheese = 10 Gold',
              6: 'You change your mind and want nothing.'}

tradingpost = {1: 'Healing Tonic = 25 Gold',
               2: 'Bomb = 50 Gold',
               3: 'Big Sword = 100 Gold',
               4: 'Spoon = 1 Gold',
               5: 'Holy Water = 25 Gold',
               6: 'Flaming Sword = 75 Gold',
               7: 'You change your mind and want nothing.'}

hellsgate_trader = {1: 'Flimsy sword = 80 Gold',
                    2: 'Off colored Tonic = 35 Gold',
                    3: 'Plastic spoon = 20 Gold'}

human_inventory = {}

print("You are an adventurer who just arrived in Clurosant (A large walled city).")
print("You are starting by yourself, and have 100 health points for the adventure.")
print("You will have the option to recruit more members as the adventure goes on.")
print("Party members will increase your overall health, and add new items to inventory for use.")
print("Your inventory is listed below.")
print(inventory)
del inventory [1]
del inventory [2]

def broke_money():
    global gold
    if gold < 0:
        print ("You shift through your pockets to find some money and realize you dont have anymore. Your broke.")

def modify_health():
    global health
    health += 50
    print("Your health is now at", health, "points.")
    return

def damage_output():
    global damage
    if "Flaming Sword" in inventory.values():
        if "Blade" in human_inventory.values():
            damage = 50
            return damage
        else:
            damage = 30
            return damage
    elif "Big Sword" in inventory.values():
        if "Blade" in human_inventory.values():
            damage = 40
            return damage
        else:
            damage = 20
            return damage
    else:
        if "Blade" in human_inventory.values():
            damage = 30
            return damage
        else:
            damage = 10
            return damage
    return damage
    

def combat_tutorial():
    print ("This is a combat tutorial.")
    print ("You will have the option to attack, defend, parry, or use an item.")
    print ("The enemy will have the same options.")
    print ("Your enemy will have a certain amount of health points, and you will have to reduce them to zero to win.")
    print ("If your health points reach zero, you lose.")
    print ("Attacking will do damage to the enemy, defending will block all of the damage the enemy does, parry will reduce the damage the enemy can do but not all of it. It will also inflict some damage back at the enemy.")
    print ("You can also use an item from your inventory to help you in combat. These items will have a variety of effects.\n")
    return

def end_Game():
    global playing
    playing = False
    quit()

def starting_zone():
    global gold
    gold = 50
    print("You are a handsome warrior relaxing in a tavern, enjoying a large beer and a big fried bug wing for breakfast.")
    print("When suddently a large hairy tavern keeper wanders over to you asking if your up for a job?!")
    print("He goes on to explain that a town in the blue mountains has not been heard from for some time.") 
    print("And he would like you to investigate what has happened. However he never directly mentions pay.")
    print("Do you accept? 0 = No, 1 = Yes")
    player_choice = int(input())
    if player_choice == 0:
        print ("Player chose to deny the request of the tavern owner.")
        print ("Tavern owner looks sad, sighs then says 'No worries chap, I dont blame you'. It would take a hero to take the quest on.")
        cowards_end()
    elif player_choice == 1:
        print ("Player chose to accept the request of the tavern owner.")
        print ("Tavern owner looks happy, and says 'Great! Here is 50 gold to help you on your way.'")
        gold += 50
        print ("You now have ", gold, "gold.\n")
        print ("Tavern owner starts to break down the mission details. The town you are looking for is called Journeys End, and is located in the blue mountains.") 
        print ("Head north east to Hells Gate Castle then continue following the dirt road.") 
        print ("That path should take you straight there, just keep an eye out for trolls or dragons.")
        print ("The tavern owner informs you that you will be payed upon return with news of the towns fate and the seal of the mayor that resides there.", "The pay promised will be an additional 500 Gold.")
        print ("Tavern owner says: ", "Would you like to purchcase some supplies for the jounrey my lad?\n")
        player_choice = int(input("0 = No, 1 = Yes\n"))
        if player_choice == 0:
            print ("Then have a nice day lad!\n Player heads outside.\n")
            road_ahead ()
        elif player_choice == 1:
            tavern_food ()
        else:
            print ("Invalid input, please try again.\n")
            starting_zone ()

def cowards_end():
    print ("You leave the tavern ready for whatever lay ahead.")
    print ("There is a loud crash and boom, and the tavern explodes into a million pieces.")
    print ("You go flying into the air and land on a pile of rubble.")
    print ("As you look up you see Squeeks the Destroyer, a 60 foot tall squirrel.")
    print ("Squeeks squeaks in a mocking tone, and then proceeds to eat you.")
    print ("If only you had accepted the tavern owners request, you could have been a hero.")
    print ("Game Over!!!\n")
    print("Would you like to play again? 0 = No, 1 = Yes\n")
    player_choice = int(input())
    if player_choice == 0:
        end_Game()
    elif player_choice == 1:
        starting_zone()


def tavern_food():
    global gold
    print ("What would you like to eat or drink?") 
    print("The seller has a limited supply, you can only buy each thing once.\n")
    print(tavernlist)
    player_choice = int(input())
    if gold <= 0:
        broke_money ()
        print ("Tavern owner says: ", "Sorry lad your out of money, and my shop isnt for poor people.")
        print("Tavern owner kicks you out.\n")
        gold == 0
        print ("You have ", gold, "gold left.\n")
        road_ahead ()
        return
    if player_choice == 1:
            gold -= 2
            inventory [5] = "Ale"
            del tavernlist [1]
    elif player_choice == 2:
            gold -= 4
            inventory [6] = "Big Ale"
            del tavernlist [2]
    elif player_choice == 3:
            gold -= 6
            inventory [7] = "Da biggest Ale"
            del tavernlist [3]
    elif player_choice == 4:
            gold -= 2
            inventory [8] = "Loaf of Bread"
            del tavernlist [4]
    elif player_choice == 5:
            gold -= 10
            inventory [9] = "Wheel of Cheese"
            del tavernlist [5]
    elif player_choice == 6:
            print ("You chose not to buy anything and headed outside.\n")
            road_ahead ()
            return
    else:
        print ("Invalid input, please try again.\n")
        tavern_food ()
    print ("You have ", gold, "gold left.\n")
    print ("Tavern owner says: ", "Would you like anything else my lad?\n")
    player_choice = int(input("0 = No, 1 = Yes\n"))
    if player_choice == 0:
        print ("Then have a nice day lad!\n Player heads outside.\n")
        road_ahead ()
    elif player_choice == 1:
        tavern_food ()
    else:
        print ("Invalid input, please try again.\n")
        tavern_food ()
    

def road_ahead():
    global gold
    print ("You are outside the tavern and have the option of going to the trading post for supplies/equipment. Or heading out on your journey right away\n")
    print ("Press 1 to go to the trading post, or 2 to head out on your journey.\n")
    player_choice = int(input())
    if player_choice == 1:
        trading_post ()
    elif player_choice == 2:
        print ("You head out on your journey.\n")
        journeyend()

def trading_post():
    global gold
    print ("You arrive at the trading post and a young lass asks if you need any help. The seller has a limited supply, you can only buy each thing once.\n")
    print("Do you want to shop?")
    print ("0 = no, 1 = yes")
    player_choice = int(input())
    if player_choice == 0:
        print ("You tell the young lass you are just browsing and eventually head outside.\n")
        road_ahead ()
    elif player_choice == 1:
        print ("You tell the young lass you are looking for supplies for your journey.")
        print ("The young lass says: ", "I have a few things you might be interested in.")
        print ("You have ", gold, "gold to spend.\n")
        if gold <= 0:
            broke_money ()
            print ("Young lass says: ", "Sorry mister your out of money, comeback when you have some to spend.\n", "Young lass kicks you out.\n")
            gold == 0
            print ("You have ", gold, "gold left.\n")
            road_ahead ()
            return
        print(tradingpost)
        player_choice = int(input())
        if player_choice == 1:
            gold -= 25
            inventory [10] = "Healing Tonic"
            del tradingpost [1]
        elif player_choice == 2:
            gold -= 50
            inventory [11] = "Bomb"
            del tradingpost [2]
        elif player_choice == 3:
            gold -= 100
            inventory [12] = "Big Sword"
            del tradingpost [3]
        elif player_choice == 4:
            gold -= 1
            inventory [13] = "Spoon"
            del tradingpost [4]
        elif player_choice == 5:
            gold -= 25
            inventory [14] = "Holy Water"
            del tradingpost [5]
        elif player_choice == 6:
            gold -= 75
            inventory [15] = "Flaming Sword"
            del tradingpost [6]
        elif player_choice == 7:
            print ("You chose not to buy anything and headed outside.\n")
            road_ahead ()
            return
        else:
            print ("Invalid input, please try again.\n")
            trading_post ()
        print ("You have ", gold, "gold left.\n")
        print ("Young lass says: ", "Would you like anything else my lad?")
        player_choice = int(input("0 = No, 1 = Yes\n"))
        if player_choice == 0:
            print ("Young lass says: Then have a nice day Mister! Player heads outside.\n")
            road_ahead ()
        elif player_choice == 1:
            trading_post ()
        else:
            print ("Invalid input, please try again.\n")
            trading_post ()

def journeyend():
    global gold
    print ("You Start your jounrey to Journeys End, and head north east to Hells Gate Castle.")
    print ("On your way you see a group of goblins in the distance, they have not seen you yet.")
    print ("The goblins seem to be fighting over a wounded traveraler, who is laying on the ground.")
    print ("Do you want to help the wounded traveraler? 0 = No, 1 = Yes\n")
    player_choice = int(input())
    if player_choice == 0:
        print ("You decide to ignore the wounded traveraler and continue on your way to Hellsgate.\n")
        hellsgate ()
    if player_choice == 1:
        print ("You decided to help the traveler and engage the gobblins.\n")
        combat_tutorial()
        goblin_combat(goblins, inventory)
        print("The traveler who is a younger redhead woman looks up and thanks you for your assistance.")
        print("She says her name is Kate and is a skilled healer, she offers to join you on your journey, as payment for saving her.")
        print("Do you accept her offer? 0 = No, 1 = Yes\n")
    player_choice = int(input())
    if player_choice == 0:
        print("You receive 150 gold for your assistance and Kate heads off towards Clurosant.")
        print("You continue on the road towards Hells Gate.")
        gold += 150
        hellsgate ()
    elif player_choice == 1:
        inventory ['15'] = "Large Healing Tonic"
        print("You join forces with Kate (Healer class), and she shares her inventory with you.")
        print("You now have a Large Healing Tonic and + 50 extra health points.")
        modify_health ()
        human_inventory [1] = "Kate"
        print("You both continue on the dirt road towards Hells Gate Castle.\n")
        hellsgate ()


def goblin_combat(goblins, inventory):
    global health
    global damage
    damage = damage_output()
    print ("Will you attack, defend, parry, or use an item?")
    print ("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
    while goblins > 0 and health > 0:
        player_choice = int(input())
        enemy_action = random.randint(0, 2)
        if player_choice == 0:
            if enemy_action == 0:
                print ("You attack the enemy and deal damage.")
                goblins -= damage
                print ("The goblins have ", goblins, "health left.")
                print ("The enemy attacks you and deals 5 damage.")
                health -= 5
                print ("You have ", health, "health left.\n")
                if goblins <= 0:
                    print("You defeated the goblins.\n")
                    return
                if health <= 0:
                    print("You have died.\n", "Game Over!!!\n")
                    print("Would you like to play again? 0 = No, 1 = Yes\n")
                    player_choice = int(input())
                    if player_choice == 0:
                        end_Game()
                    elif player_choice == 1:
                        starting_zone()
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 0:
            if enemy_action == 1:
                print ("You leap forward to attack but the enemy defends.")
                print ("No damage is dealt.\n")
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 0:
            if enemy_action == 2:
                print ("You attack the enemy but they parry!")
                goblins -= (damage - 10)
                print ("The goblins have ", goblins, "health left.")
                print ("The enemy parrys your attack and deals 5 damage back to you.")
                health -= 5
                print ("You have ", health, "health left.\n")
                if goblins <= 0:
                    print("You defeated the goblins.\n")
                    return health
                if health <= 0:
                    print("You have died.\n", "Game Over!!!\n")
                    print("Would you like to play again? 0 = No, 1 = Yes\n")
                    player_choice = int(input())
                    if player_choice == 0:
                        end_Game()
                    elif player_choice == 1:
                        starting_zone()
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 1:
            if enemy_action == 1:
                print("You defend against an attack that isnt coming.")
                print("The goblin chooses to defend as well.\n")
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 1:
            if enemy_action == 0:
                print("You raise your shield to defend against a mighty attack just in time.")
                print("No damage is dealt to you.\n")
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 1:
            if enemy_action == 2:
                print("You raise your shield to defend but the enemy was ready to parry, no attack comes.")
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 2:
            if enemy_action == 2:
                print("You are ready to parry but no attack comes.")
                print("The goblins were ready to parry as well.\n")
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 2:
            if enemy_action == 0:
                print("You are ready to parry when the enemy attacks, you reduce the damage taken and deal some back.")
                goblins -= 5
                print("The goblins have", goblins, "health left.")
                print("You take 1 point of damage in the exchange.")
                print("You have", health, "health left.\n")
                if goblins <= 0:
                    print("You defeated the goblins.\n")
                    return health
                if health <= 0:
                    print("You have died.\n", "Game Over!!!\n")
                    print("Would you like to play again? 0 = No, 1 = Yes\n")
                    player_choice = int(input())
                    if player_choice == 0:
                        end_Game()
                    elif player_choice == 1:
                        starting_zone()
                return
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 2:
            if enemy_action == 1:
                print("You are ready to parry, but the enemy has their shield up ready to block.")
                print("No attack comes.\n")
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 3:
            print("What item would you like to use?") 
            print (inventory)
            inventory_choice = int(input())
            if inventory_choice == 3:
                health += 25
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                del inventory [3]
            elif inventory_choice == 5:
                health += 5
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                del inventory [5]
            elif inventory_choice == 6:
                health += 6
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                del inventory [6]
            elif inventory_choice == 7:
                health += 7
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                del inventory [7]
            elif inventory_choice == 8:
                health += 5
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                del inventory [8]
            elif inventory_choice == 9:
                health += 25
                print ("Your health is now", health)
                del inventory [9]
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
            elif inventory_choice == 10:
                health += 25
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                del inventory [10]
            elif inventory_choice == 11:
                print ("You throw and hit the enemy with your bomb. Dealing 100 damage!")
                goblins -= 100
                print ("The goblins are not in small pieces scattered everywhere, you won!\n")
                del inventory [11]
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
            elif inventory_choice == 13:
                print ("You whip out a spoon and throw it at the enemy.")
                print ("In confusion at the sheer randomness the enemy bolts out of there!")
                goblins -= 100
                print ("You have defeated the goblins.\n")
                del inventory [13]
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
            elif inventory_choice == 14:
                print ("You toss holy water at the enemy.")
                print ("The goblins shreek as you just gave them a bath, their mortal foe.")
                print ("The goblins gain health due to the rage you put them in.")
                goblins += 15
                del inventory [14]
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")

def hellsgate():
    print("You arrive at Hells Gate Castle.")
    print("The castle is well armed, you see high walls and many guards.")
    print("You approach the gate and request entry. The guard informs you that the castle is closed to vistors due to many enemy patrols.")
    print("You are directed to a nearby market instead, consisting of tents and wagoons.")
    trader_options()
    
def trader_options():
    global gold
    global damage
    print("You see a trader and a mercenary, which would you like to talk to?")
    print("1 = trader, 2 = mercenary, 3 = neither continue adventure.")
    player_choice = int(input())
    if player_choice == 1:
        print("You find a traded who goes by Dance. He is rude and sizing you up the entire conversation. They offer to trade.")
        print("Do you wish to trade?")
        player_choice = int(input("0 = No, 1 = Yes\n"))
        if player_choice == 0:
            print("Dance says: Figured you were to poor to afford my valuable goods. Get out of here you peasant.")
            trader_options ()
        elif player_choice == 1:
            print("Dance shows you his wares, but they seem a bit more expensive than usual.")
            print("Dance has a evil smurk on his face.")
            hellsgatetrader ()
            player_choice = int(input("Would you like anything else?, 0 = No, 1 = Yes"))
            if player_choice == 1:
                hellsgatetrader ()
            elif player_choice == 0:
                trader_options()
    elif player_choice == 2:
        if "Blade" in human_inventory.values():
            print("You cannot hire blade twice, he is already in your party.")
            trader_options()
        print("You meet a mercenary who goes by Blade, he offers to join you on your quest for a fee.")
        print("Would you like him to join you for a fee of 100 gold?")
        player_choice = int(input("0 = No, 1 = Yes\n"))
        if player_choice == 0:
            print("You tell Blade you dont have the money and he leaves.")
            print("You setup a tent and catch a nights sleep. From there you continue on your path to Journeysend.\n")
            journeysend ()
        if player_choice == 1:
            print("You tell Blade you wish for him to join the party and pay him.")
            if gold < 100:
                broke_money ()
                print ("Blade says: You dont have the money, come back when you do.")
                trader_options()
            elif gold >= 100:
                gold -= 100
                human_inventory [2] = "Blade"
                print("You have ", gold, "gold left.\n")
                print("Blade says: Lead the way, I will follow you.")
                print ("Blade buffs your damage output and increases your health max.")
                modify_health ()
                trader_options()
    elif player_choice == 3:
        print("You setup a tent and catch a nights sleep. From there you continue on your path to Journeysend.\n")
        journeysend ()
        

def hellsgatetrader ():
    global gold
    print ("You have ", gold, "gold to spend.")
    print ("Dance: What would you like?")
    print (hellsgate_trader)
    player_choice = int(input())
    if gold <= 0:
        broke_money ()
        print ("Dance: You dont have any money, get out of here.")
        print ("You have ", gold, "gold left.\n")
        trader_options()
    if player_choice == 1:
        gold -= 80
        inventory ['16'] = "Flimsy sword"
        print ("Your inventory is now", inventory)
        del hellsgate_trader [1]
    if player_choice == 2:
        gold -= 35
        inventory ['17'] = "Off colored Tonic"
        print ("Your inventory is now", inventory)
        del hellsgate_trader [2]
    if player_choice == 3:
        gold -= 20
        inventory ['18'] = "Plastic spoon"
        print ("Your inventory is now", inventory)
        del hellsgate_trader [3]


def manticorefight(manticore, inventory):
    global health
    global damage
    damage = damage_output()
    print ("Will you attack, defend, parry, or use an item?")
    print ("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
    while manticore > 0 and health > 0:
        player_choice = int(input())
        enemy_action = random.randint(0, 2)
        if player_choice == 0:
            if enemy_action == 0:
                print ("You attack the enemy and deal damage.")
                manticore -= damage
                print ("The manticore has ", manticore, "health left.")
                print ("The enemy attacks you and deals 25 damage.")
                health -= 25
                print ("You have ", health, "health left.\n")
                if manticore <= 0:
                    print("You defeated the manticore.\n")
                    return health
                if health <= 0:
                    print("You have died.\n", "Game Over!!!\n")
                    print("Would you like to play again? 0 = No, 1 = Yes\n")
                    player_choice = int(input())
                    if player_choice == 0:
                        end_Game()
                    elif player_choice == 1:
                        starting_zone()
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 0:
            if enemy_action == 1:
                print ("You leap forward to attack but the enemy defends.")
                print ("No damage is dealt.\n")
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 0:
            if enemy_action == 2:
                print ("You attack the enemy but they parry!")
                manticore -= (damage - 10)
                print ("The manticore has ", manticore, "health left.")
                print ("The enemy parrys your attack and deals 10 damage back to you.")
                health -= 10
                print ("You have ", health, "health left.\n")
                print ("Will you attack, defend, parry, or use an item?")
                print ("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                if manticore <= 0:
                    print("You defeated the manticore.\n")
                    return health
                if health <= 0:
                    print("You have died.\n", "Game Over!!!\n")
                    print("Would you like to play again? 0 = No, 1 = Yes\n")
                    player_choice = int(input())
                    if player_choice == 0:
                        end_Game()
                    elif player_choice == 1:
                        starting_zone()
        if player_choice == 1:
            if enemy_action == 1:
                print("You defend against an attack that isnt coming.")
                print("The manticore chooses to defend as well.\n")
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 1:
            if enemy_action == 0:
                print("You raise your shield to defend against a mighty attack just in time.")
                print("No damage is dealt to you.\n")
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 1:
            if enemy_action == 2:
                print("You raise your shield to defend but the enemy was ready to parry, no attack comes.")
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 2:
            if enemy_action == 2:
                print("You are ready to parry but no attack comes.")
                print("The manticore was ready to parry as well.\n")
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 2:
            if enemy_action == 0:
                print("You are ready to parry when the enemy attacks, you reduce the damage taken and deal some back.")
                manticore -= 10
                health -= 10
                print("The manticore has", manticore, "health left.")
                print("You take 10 points of damage in the exchange.")
                print("You have", health, "health left.\n")
                if manticore <= 0:
                    print("You defeated the manticore.\n")
                    return health
                if health <= 0:
                    print("You have died.\n", "Game Over!!!\n")
                    print("Would you like to play again? 0 = No, 1 = Yes\n")
                    player_choice = int(input())
                    if player_choice == 0:
                        end_Game()
                    elif player_choice == 1:
                        starting_zone()
                return
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 2:
            if enemy_action == 1:
                print("You are ready to parry, but the enemy has their shield up ready to block.")
                print("No attack comes.\n")
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 3:
            print("What item would you like to use?") 
            print (inventory)
            inventory_choice = int(input())
            if inventory_choice == 3:
                health += 25
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                del inventory [3]
            elif inventory_choice == 5:
                health += 5
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                del inventory [5]
            elif inventory_choice == 6:
                health += 6
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                del inventory [6]
            elif inventory_choice == 7:
                health += 7
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                del inventory [7]
            elif inventory_choice == 8:
                health += 5
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                del inventory [8]
            elif inventory_choice == 9:
                health += 25
                print ("Your health is now", health)
                del inventory [9]
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
            elif inventory_choice == 10:
                health += 25
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                del inventory [10]
            elif inventory_choice == 11:
                print ("You throw and hit the enemy with your bomb. Dealing 100 damage!")
                manticore -= 100
                print ("The manticore is now in small pieces scattered everywhere, you won!\n")
                del inventory [11]
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
            elif inventory_choice == 13:
                print ("You whip out a spoon and throw it at the enemy.")
                print ("In confusion at the sheer randomness the enemy bolts out of there!")
                manticore -= 100
                print ("You have defeated the manticore.\n")
                del inventory [13]
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
            elif inventory_choice == 14:
                print ("You toss holy water at the enemy.")
                print ("The manticore shreeks as you just gave them a bath, their mortal foe.")
                print ("The manticore gain health due to the rage you put them in.")
                manticore += 20
                del inventory [14]
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
            elif inventory_choice == 15:
                health += 50
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
            elif inventory_choice == 16:
                print ("You attack with the Flimsy sword and it shatters on impact.")
                print ("The manticore is not impressed and attacks you.")
                health -= 20
                print ("You have ", health, "health left.\n")
                del inventory [16]
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
            elif inventory_choice == 17:
                print ("You drink the off colored tonic, and a moment later you feel your guts shift.")
                print ("Then bam, you shit yourself. You loose pride.\n")
                del inventory [17]
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
            elif inventory_choice == 18:
                print ("You go to use your might spoon, however this spoon is cheaply made.")
                print ("The spoon flys out of your hand when you go to strike.")
                print ("Manticore bites you in retaliation.")
                health -= 20
                print ("You have ", health, "health left.\n")
                del inventory [18]
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")

def journeysend ():
    print ("You set off on your adventure down a dusty path towards the mountains.")
    print ("After 6 days travel that goes on without event you reach the mountain entrance.")
    print ("It is quiet a little to quiet. You hear some flapping and quickly look up to see a maticore coming down in your direction screeching.\n")
    manticorefight (manticore, inventory)
    print ("Congrats you defeated the manticore and go through the mountain entrance.")
    print ("After a further day of two of traveling you reach Journeysend.")
    print ("The town sits in a thick pine forest. It is small and surrounded by a wooden wall.")
    print ("The front gate looks damaged. The buildings and walls have major damaged in the form of gashes and claw marks")
    print ("Toward the front gate you see an over turned cart and a dead horse.")
    print ("Do you want to go through the front gate or camp and stake out the area?")
    if human_inventory [1] == "Kate":
        player_choice = int(input("0 = Camp, 1 = Front gate\n"))
        if player_choice == 0:
            print ("You setup a small hiding spot on cliff over looking the town.")
            print ("After a couple hours waiting you hear some crashing and heavy movement in the town.")
            print ("The sound is very loud and you see the top of some creature over the top of the wall.")
            print ("After waiting a bit longer you see a massive minotaur bust through a section of the wall and head into the forest.")
            print ("You decide to follow the minotaur and see where it is going.")
            print ("You follow the minotaur for a couple hours and see it enter a cave.")
            print ("You approach the entrance and see the minotaur is sitting down and seems to be resting.")
            print ("You decide that now is the best time to attack!\n")
            minotaur_fight ()
            print ("You defeated the foe that destroyed Journeysend. The town is now safe.")
            print ("Though it seems you were to late to save anyone.")
            print ("You start your long journey back home, knowing that you have avenged the fallen.")
            hellsgate_2()
        if player_choice == 1:
            print ("You decide to go through the front gate.")
            print ("As you enter the town you see that it is in ruins, and there are no signs of life.")
            print ("Bodies are scattered around, and the buildings are heavily damaged.")
            print ("Suddenly you hear a loud roar and see the minotaur charging towards you from around a building.")
            print ("You brace yourself for battle!\n")
            minotaur_fight (inventory, minotour)
            print ("You defeated the foe that destroyed Journeysend. The town is now safe.")
            print ("Though it seems you were to late to save anyone.")
            print ("You start your long journey back home, knowing that you have avenged the fallen.\n")
            hellsgate_2()
    elif 1 not in human_inventory:
        player_choice = int(input("0 = Camp, 1 = Front gate\n"))
        if player_choice == 0:
            print ("You setup a small hiding spot on the nearby cliff. As you sit there you hear the screams of people being eaten.")
            print ("If only you had gone inside right away you might have been able to save them.")
            print ("After a couple hours waiting you hear some crashing and heavy movement in the town.")
            print ("The sound is very loud and you see the top of some creature over the top of the wall.")
            print ("After waiting a bit longer you see a massive minotaur bust through a section of the wall and head into the forest.")
            print ("You decide to follow the minotaur and see where it is going.")
            print ("You follow the minotaur for a couple hours and see it enter a cave.")
            print ("You approach the entrance and see the minotaur is sitting down and seems to be resting.")
            print ("You decide that now is the best time to attack!\n")
            minotaur_fight ()
            print ("You defeated the foe that destroyed Journeysend. The town is now safe.")
            print ("Though it seems you were to late to save anyone.")
            print ("You start your long journey back home, knowing that you have avenged the fallen.\n")
        if player_choice == 1:
            print ("You charge into the town after hearing some screams.")
            print ("You are greeted by carnage, as a large minotaur is rampaging through the streets.")
            print ("You see the minotaur charging towards you from around a building.")
            minotaur_fight ()
            print ("You defeated the large beast, and as the smoke settles from the epic battle people start to gather around.")
            print ("The towns people cheer as you saved most of them. They offer you a large amount of coin as payment for your herioc deed.")
            gold += 500
            print ("You received 500 gold.", "You now have", gold, "gold.")
            print ("You head off back towards Hells Gate Castle knowing you saved the town.\n")
            hellsgate_2 ()


def hellsgate_2():
    print ("You arrive at hellsgate and rest for the night in the horse stable.")
    print ("The next morning you wake up to the sound of guards shouting and a commotion outside.")
    print ("You quickly get dressed and head outside to see what is going on.")
    print ("Seems a massive battle is raging between the guards and a horde of goblins!")
    print ("The great goblin tide has come!!!!")
    print ("You see that the goblins are attacking the castle and the guards are struggling to hold them back.")
    print ("The officers are dead strown about the field. All of the men look to you as the slayer of the mighty minotaur.")
    print ("You will be taking command of the legion forces at Hells Gate Castle.\n")
    armycommandtutorial ()
    army_fight ()

def armycommandtutorial():
    print ("For this battle sequence you can choose to have the men charge, hold the line, or fire arrows.")
    print ("You will have to read the enemies movements correctly and choose the right counter to their plan.")
    print ("The percentage of your forces will decrease with every incorrect guess.")
    print ("The percentage of the enemy forces will decrease with every correct gyess.")
    print ("Whichever side hits 0 first, looses.\n")

def army_fight():
    enemy_army = 1000
    ally_army = 1000
    enemy_choice = random.randint(0, 2)
    if enemy_choice == 0:
        print ("The goblin army looks like they are ready for blood with sword in hand, they seem getting ready to do something.")
        print ("What will you order your men to do?\n")
    if enemy_choice == 1:
        print ("The goblin army looks like they are fortifying, getting ready for an aggressive foe.")
        print ("What will you order your men to do?\n")
    if enemy_choice == 2:
        print("The goblin army looks like they are getting their bows ready.")
        print ("What will you order your men to do?\n")
    player_choice = int(input("0 = Charge, 1 = Hold the line, 2 = Fire arrows\n"))
    if enemy_choice == 0:
        if player_choice == 0:
            print ("You scream CHARGEEEE, as your men charge forth.")
            print ("The goblins were ready for this and counter charge.")
            print ("Both teams take heavy damage.", "Your forces take 100 damage.", "The enemy forces take 200 damage")
            ally_army -= 100
            enemy_army -= 200
            print ("You have", ally_army, "men left.", "The enemy army has", enemy_army, "goblins left.\n")
            if ally_army <= 0:
                print("You and your army were destroyed.\n", "Game Over!!!\n")
                print("Would you like to play again? 0 = No, 1 = Yes\n")
                player_choice = int(input())
                if player_choice == 0:
                    end_Game()
                elif player_choice == 1:
                    starting_zone()
            if enemy_army <= 0:
                victory_fields ()
        if player_choice == 1:
            print ("You see the aggressive stance of the enemy. You order your men to brace for a charge.")
            print ("The goblin army charges but your men were ready for it and repelled the enemy.")
            print ("The goblin army takes heavy losses and your army only suffered minor damage.")
            ally_army -= 25
            enemy_army -= 150
            print ("You have", ally_army, "men left.", "The enemy army has", enemy_army, "goblins left.\n")
            if ally_army <= 0:
              print("You and your army were destroyed.\n", "Game Over!!!\n")
              print("Would you like to play again? 0 = No, 1 = Yes\n")
              player_choice = int(input())
              if player_choice == 0:
                end_Game()
              elif player_choice == 1:
                starting_zone()
            if enemy_army <= 0:
              victory_fields ()
        if player_choice == 2:
            print ("You see the goblins getting ready to charge, and order your men to shoot their range weapons.")
            print ("The goblins charge into a hail of arrows and bolts, the take heavy losses.")
            print ("You inflicted heavy damage but your men werent braced for the charge and took medium losses as a result.")
            ally_army -= 50
            enemy_army -= 200
            print ("You have", ally_army, "men left.", "The enemy army has", enemy_army, "goblins left.\n")
            if ally_army <= 0:
              print("You and your army were destroyed.\n", "Game Over!!!\n")
              print("Would you like to play again? 0 = No, 1 = Yes\n")
              player_choice = int(input())
              if player_choice == 0:
               end_Game()
              elif player_choice == 1:
                starting_zone()
            if enemy_army <= 0:
              victory_fields ()
    if enemy_choice == 1:
        if player_choice == 0:
            print ("The goblin army looks like they are reading defences.")
            print ("You scream for your men to charge, but the goblins were ready for it because of the defences.")
            print ("Your forces take heavy damage. And the goblin forces take minor damage.")
            ally_army -= 100
            enemy_army -= 50
            print ("You have", ally_army, "men left.", "The enemy army has", enemy_army, "goblins left.\n")
            if ally_army <= 0:
              print("You and your army were destroyed.\n", "Game Over!!!\n")
              print("Would you like to play again? 0 = No, 1 = Yes\n")
              player_choice = int(input())
              if player_choice == 0:
                end_Game()
              elif player_choice == 1:
                starting_zone()
            if enemy_army <= 0:
              victory_fields ()
        if player_choice == 1:
            print ("The goblin army looks like they are reading defences.")
            print ("You see the shoddy defences they are putting up and order your men to make bigger better ones.")
            print ("Both sides take no damage as neither side made any kind of attack.")
        if player_choice == 2:
            print ("You see the goblins setting up fortifications. You order your men to fire any and all range weapons.")
            print ("The goblins had fortifications built as a result the loses were minimal.")
            print ("Your forces take no damage as the goblins didnt attack.")
            enemy_army -= 50
            print ("You have", ally_army, "men left.", "The enemy army has", enemy_army, "goblins left.\n")
            if ally_army <= 0:
              print("You and your army were destroyed.\n", "Game Over!!!\n")
              print("Would you like to play again? 0 = No, 1 = Yes\n")
              player_choice = int(input())
              if player_choice == 0:
                end_Game()
              elif player_choice == 1:
                starting_zone()
            if enemy_army <= 0:
                victory_fields ()
    if enemy_choice == 2:
        if player_choice == 0:
            print ("The goblin army looks like they are getting their bows ready.")
            print ("You order your men to charge!!!!")
            print ("The wethering arrow fire riddles your men causing heavy losses.")
            print ("However the goblins were not ready for the charge and took heavy losses as well.")
            enemy_army -= 100
            ally_army -= 100
            print ("You have", ally_army, "men left.", "The enemy army has", enemy_army, "goblins left.\n")
            if ally_army <= 0:
              print("You and your army were destroyed.\n", "Game Over!!!\n")
              print("Would you like to play again? 0 = No, 1 = Yes\n")
              player_choice = int(input())
              if player_choice == 0:
                end_Game()
              elif player_choice == 1:
                starting_zone()
            if enemy_army <= 0:
                victory_fields ()
        if player_choice == 1:
            print ("The goblin army looks like they are getting their bows ready.")
            print ("You order your men to hold the line and build fortifications.")
            print ("When the enemy releases there ranged attacks your forces were ready and take minimal damage.")
            print ("Your forces take minimal damage, and no damage is dealt to the goblin army as you did not attack.")
            ally_army -= 25
            print ("You have", ally_army, "men left.", "The enemy army has", enemy_army, "goblins left.\n")
            if ally_army <= 0:
              print("You and your army were destroyed.\n", "Game Over!!!\n")
              print("Would you like to play again? 0 = No, 1 = Yes\n")
              player_choice = int(input())
              if player_choice == 0:
                end_Game()
              elif player_choice == 1:
                starting_zone()
            if enemy_army <= 0:
                victory_fields ()
        if player_choice == 2:
            print ("The goblin army looks like they are getting their bows ready.")
            print ("You order your men to get their bows ready as well.")
            print ("Both sides take heavy losses as the arrows fly.")
            enemy_army -= 200
            ally_army -= 100
            print ("You have", ally_army, "men left.", "The enemy army has", enemy_army, "goblins left.\n")
            if ally_army <= 0:
              print("You and your army were destroyed.\n", "Game Over!!!\n")
              print("Would you like to play again? 0 = No, 1 = Yes\n")
              player_choice = int(input())
              if player_choice == 0:
                end_Game()
              elif player_choice == 1:
                starting_zone()
            if enemy_army <= 0:
                victory_fields ()

def minotaur_fight(inventory, minotaur):
    global health
    global damage
    minotaur = 150
    damage = damage_output()
    print ("Will you attack, defend, parry, or use an item?")
    print ("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
    while minotaur > 0 and health > 0:
        player_choice = int(input())
        enemy_action = random.randint(0, 2)
        if player_choice == 0:
            if enemy_action == 0:
                print ("You attack the enemy and deal damage.")
                minotaur -= damage
                print ("The minotaur has ", minotaur, "health left.")
                print ("The enemy attacks you and deals 25 damage.")
                health -= 25
                print ("You have ", health, "health left.\n")
                if minotaur <= 0:
                    print("You defeated the minotaur.\n")
                    return health
                if health <= 0:
                    print("You have died.\n", "Game Over!!!\n")
                    print("Would you like to play again? 0 = No, 1 = Yes\n")
                    player_choice = int(input())
                    if player_choice == 0:
                        end_Game()
                    elif player_choice == 1:
                        starting_zone()
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 0:
            if enemy_action == 1:
                print ("You leap forward to attack but the enemy defends.")
                print ("No damage is dealt.\n")
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 0:
            if enemy_action == 2:
                print ("You attack the enemy but they parry!")
                minotaur -= (damage - 10)
                print ("The minotaur has ", minotaur, "health left.")
                print ("The enemy parrys your attack and deals 10 damage back to you.")
                health -= 10
                print ("You have ", health, "health left.\n")
                print ("Will you attack, defend, parry, or use an item?")
                print ("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                if minotaur <= 0:
                    print("You defeated the minotaur.\n")
                    return health
                if health <= 0:
                    print("You have died.\n", "Game Over!!!\n")
                    print("Would you like to play again? 0 = No, 1 = Yes\n")
                    player_choice = int(input())
                    if player_choice == 0:
                        end_Game()
                    elif player_choice == 1:
                        starting_zone()
        if player_choice == 1:
            if enemy_action == 1:
                print("You defend against an attack that isnt coming.")
                print("The minotaur chooses to defend as well.\n")
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 1:
            if enemy_action == 0:
                print("You raise your shield to defend against a mighty attack just in time.")
                print("No damage is dealt to you.\n")
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 1:
            if enemy_action == 2:
                print("You raise your shield to defend but the enemy was ready to parry, no attack comes.")
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 2:
            if enemy_action == 2:
                print("You are ready to parry but no attack comes.")
                print("The minotaur was ready to parry as well.\n")
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 2:
            if enemy_action == 0:
                print("You are ready to parry when the enemy attacks, you reduce the damage taken and deal some back.")
                minotaur -= 10
                health -= 10
                print("The minotaur has", minotaur, "health left.")
                print("You take 10 points of damage in the exchange.")
                print("You have", health, "health left.\n")
                if minotaur <= 0:
                    print("You defeated the minotaur.\n")
                    return health
                if health <= 0:
                    print("You have died.\n", "Game Over!!!\n")
                    print("Would you like to play again? 0 = No, 1 = Yes\n")
                    player_choice = int(input())
                    if player_choice == 0:
                        end_Game()
                    elif player_choice == 1:
                        starting_zone()
                return
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 2:
            if enemy_action == 1:
                print("You are ready to parry, but the enemy has their shield up ready to block.")
                print("No attack comes.\n")
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
        if player_choice == 3:
            print("What item would you like to use?") 
            print (inventory)
            inventory_choice = int(input())
            if inventory_choice == 3:
                health += 25
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                del inventory [3]
            elif inventory_choice == 5:
                health += 5
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                del inventory [5]
            elif inventory_choice == 6:
                health += 6
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                del inventory [6]
            elif inventory_choice == 7:
                health += 7
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                del inventory [7]
            elif inventory_choice == 8:
                health += 5
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                del inventory [8]
            elif inventory_choice == 9:
                health += 25
                print ("Your health is now", health)
                del inventory [9]
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
            elif inventory_choice == 10:
                health += 25
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
                del inventory [10]
            elif inventory_choice == 11:
                print ("You throw and hit the enemy with your bomb. Dealing 100 damage!")
                minotaur -= 100
                print ("The minotaur is now in small pieces scattered everywhere, you won!\n")
                del inventory [11]
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
            elif inventory_choice == 13:
                print ("You whip out a spoon and throw it at the enemy.")
                print ("In confusion at the sheer randomness the enemy bolts out of there!")
                minotaur -= 100
                print ("You have defeated the minotaur.\n")
                del inventory [13]
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
            elif inventory_choice == 14:
                print ("You toss holy water at the enemy.")
                print ("The minotaur shreeks as you just gave them a bath, their mortal foe.")
                print ("The minotaur gain health due to the rage you put them in.")
                minotaur += 20
                del inventory [14]
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
            elif inventory_choice == 15:
                health += 50
                print ("Your health is now", health)
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
            elif inventory_choice == 16:
                print ("You attack with the Flimsy sword and it shatters on impact.")
                print ("The minotaur is not impressed and attacks you.")
                health -= 20
                print ("You have ", health, "health left.\n")
                del inventory [16]
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
            elif inventory_choice == 17:
                print ("You drink the off colored tonic, and a moment later you feel your guts shift.")
                print ("Then bam, you shit yourself. You loose pride.\n")
                del inventory [17]
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")
            elif inventory_choice == 18:
                print ("You go to use your might spoon, however this spoon is cheaply made.")
                print ("The spoon flys out of your hand when you go to strike.")
                print ("minotaur bites you in retaliation.")
                health -= 20
                print ("You have ", health, "health left.\n")
                del inventory [18]
                print("Will you attack, defend, parry, or use an item?")
                print("0 = Attack, 1 = Defend, 2 = Parry, 3 = Use item\n")

def victory_fields():
   global gold
   print ("You have won!")
   print ("The field around you is littered with bodies of enemies and allies.")
   print ("Everyone looks to you with admiration and respect. The towns folk and remaining soldiers gather around you in awe.")
   print ("You won the battle of Hellsgate castle. And thus are named the Hells Gate Hero!")
   print ("You continue your journey back to the tavern that started your long journey.")
   print ("The tavern is in ruins and the owner is dead.")
   print ("You scrounge around the tavern and find a small stash of gold.")
   print ("You found 250 of the promised 500 gold.")
   gold += 250
   print ("You now have", gold, "gold.")
   print (" You head back to Hells Gate Castle and tell the guards what happened.")
   print ("They inform you that the tavern was more than likely destroyed by the goblin army.")
   print ("You are given a small reward of 500 gold for your efforts.")
   gold += 500
   print ("You now have", gold, "gold.")
   print ("As you lookout over the field of battle you see a small group of goblins running away.")
   print ("And you know that this tale is not over yet.")
   print ("Story to be continued...\n")






while (playing):
    starting_zone()
