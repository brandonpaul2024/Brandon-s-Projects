from math import e
global score
score = 0
playerzone = int
north = 4
south = 3
west = 2
east = 1
finalscore = 0
playing = True

print ("You are a wizard setting out to defeat the hag!")
print ("You must collect all your equipment before confronting her, otherwise she will eat you and wear your bones for a cool hat.")
print ("Follow the prompts to collect all your gear.")
print ("Avoid going to the same place twice!")

def end_game():
    playing = False
    quit()

def starting_zone():
    global score
    print ("You are in the starting zone and can go East to the Cluster of trees, to get your wizard staff.")
    print ("You can go South to the trail, to get your pipe.")
    print ("East = 1, West = 2, South = 3, North = 4")
    direction = int(input())
    if direction == 1:
        print ("Player goes east and arrives at Cluster of trees, you gain your wizard staff.\n")
        score = score + 5
        Cluster_of_trees()
    elif direction == 3:
        print ("Player goes south and arrives at the Trail, you gain your pipe.\n")
        score = score + 5
        Trail()
    else:
       print ("Cannont go that way, try again.\n")
       starting_zone()

def Cluster_of_trees():
    global score
    print ("You are at the cluster of trees. Now you can go north to the Crows Nest, south to the Bile Pool, west to the Starting Zone, or east to the Abandoned Inn.\n")
    print ("Player must choose East = 1, West = 2, South = 3, North = 4\n")
    direction = int(input())
    if direction == 3:
        print ("Player goes south and arrives at the Bile Pool, you gain you wizard hat.\n")
        score = score + 5
        Bile_Pool()
    elif direction == 4:
        print ("Player goes north and arrives at the Crows Nest, you gain your spell book.\n")
        score = score + 5
        Crows_nest()
    elif direction == 2:
        print ("Player goes back to starting zone.\n")
        starting_zone()
    elif direction == 1:
        print ("Player goes east and arrives at the Abandoned Inn, you gain your beard lotion.\n")
        score = score + 5
        Abandoned_Inn()

def Trail():
    global score
    print ("You are now at the Trail. Now you can go south to the Hags treehouse or east to the Bile Pool.\n")
    print ("Player must choose East = 1, West = 2, South = 3, North = 4\n")
    direction = int(input())
    if direction == 1:
        print ("Player goes east and arrives at the Bile Pool, you gain your wizard hat.\n")
        score = score + 5
        Bile_Pool()
    elif direction == 3:
        print ("Player goes south to confront the hag!\n")
        if score >= 30:
            print ("You defeated the hag, hozaahhhhh!!!!")
            playing = False
            end_game()
        else:
            print ("You were eaten due to being unprepared, now your bones are a cool hat.\n")
            playing = False
            end_game()
    elif direction == 4:
        print ("Player goes north to starting zone.\n")
        starting_zone()
    else:
        print ("Cannot go that way, try again.\n")
        Trail()

def Bile_Pool():
    global score
    print ("You are now at the Bile Pool. You can go north to the Cluster of trees, west to the Trail, or east to the Abandoned church.\n")
    print ("Player must choose East = 1, West = 2, South = 3, North = 4\n")
    direction = int(input())
    if direction == 1:
        print ("Player goes east and arrives at the Abandoned Church, you gain your prune juice.\n")
        score = score + 5
        Abandoned_Church()
    elif direction == 4:
        print ("Player goes north and arrives at the Cluster of trees, you gain your wizard staff.\n")
        score = score + 5
        Cluster_of_trees()
    elif direction == 2:
        print ("Player goes west and arrives at the Trail, you gain your pipe.\n")
        score = score + 5
        Trail()
    else:
        print ("Cannot go that way, try again.\n")
        Bile_Pool()

def Crows_nest():
    global score
    print ("You are now at the Crows Nest. You can go south to the Cluster of trees, or east to the Abandoned Inn.\n")
    print ("Player must choose East = 1, West = 2, South = 3, North = 4\n")
    direction = int(input())
    if direction == 1:
        print ("Player goes east and arrives at the Abandoned Inn, you gain your beard lotion.\n")
        score = score + 5
        Abandoned_Inn()
    elif direction == 3:
        print ("Player goes south and arrives at the Cluster of tree, you gain your wizard staff.\n")
        score = score + 5
        Cluster_of_trees()
    else:
        print ("Cannot go that way, try again.\n")
        Crows_nest()

def Abandoned_Inn():
    global score
    print ("You are now at the Abandoned Inn. You can go south to the Cluster of trees, west to the Crows nest, or north to the Abandoned Church.\n")
    print ("Player must choose East = 1, West = 2, South = 3, North = 4\n")
    direction = int(input())
    if direction == 4:
        print ("Player goes north to the Abandoned Church, you gain your prune juice.\n")
        score = score + 5
        Abandoned_Church()
    elif direction == 2:
        print ("Player goes west to the Crows nest, you gain your spell book.\n")
        score = score + 5
        Crows_nest()
    elif direction == 3:
        print ("Player goes south to the Cluster of trees, you gain your wizard staff.\n")
        score = score + 5
        Cluster_of_trees()
    else:
        print ("Cannont go that way, try again.\n")
        Abandoned_Inn()

def Abandoned_Church():
    global score
    print ("You are now at the Abandoned Church. You can go south to the Abandoned Inn, or east to the Bile Pool.\n")
    print ("Player must choose East = 1, West = 2, South = 3, North = 4\n")
    direction = int(input())
    if direction == 3:
        print ("Player goes south to the Abandoned Inn, you gain beard lotion.\n")
        score = score + 5
        Abandoned_Inn()
    elif direction == 1:
        print ("Player goes east to the Bile Pool, you gain your wizard hat.\n")
        score = score + 5
        Bile_Pool()
    else:
        print ("Cannot go that way, try again.\n")
        Abandoned_Church()


while (playing): 
    starting_zone()
    


