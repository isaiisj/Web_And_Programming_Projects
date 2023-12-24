import random
from urllib import response

players = []

print("Welcome to Team/Player Allocator!")

number_of_players = int(input("How many players are there? "))
for i in range(1, number_of_players + 1):
    name = input(f"Introduce name {i}: ")
    players.append(name)

while True:
    random.shuffle(players)
    response = input("Is it a team or individual sport?  \nType team or individual: ")
    if response == "team":

        team1 = players[:len(players)//3]
        print("Team 1 captain: " + random.choice(team1))
        print("Team 1:")
        for player in team1:
            print(player)

        team2 = players[len(players)//3:(len(players)//2)*2]
        print("\nTeam 2 captain: " + random.choice(team2))
        print("Team 2:")
        for player in team2:
            print(player)

        team3 = players[(len(players)//3)*2:]
        print("\nTeam 3 captain: " + random.choice(team3))
        print("Team 3:")
        for player in team3:
            print(player)
        
    else:
        for i in range(0, 20, 2):
            print(players[i] + " vs " + players[i+1])
            start = random.randrange(i, i+2)
            print(players[start] + " starts")

    response = input("Pick teams again? Type y or n: ")
    
    if response == "n":
        break


