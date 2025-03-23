import datetime as dt
import os

def get_player_names():
    players = []
    for i in range(4):
        name = input(f"Enter the name of Player {i+1}: ")
        players.append(name)
    return players

def select_player(prompt, players, extra_options=None):
    print(prompt)
    for i, player in enumerate(players, 1):
        print(f"{i}: {player}")
    if extra_options:
        for key, label in extra_options.items():
            print(f"{key}: {label}")
    return input("Option: ")

def update_scores(scores, winner_idx, loser_idx, points, is_zimo=False):
    if is_zimo:
        for i in range(4):
            if i != winner_idx:
                scores[i] -= points * 2
        scores[winner_idx] += points * 6
    else:
        scores[loser_idx] -= points * 2
        for i in range(4):
            if i != loser_idx and i != winner_idx:
                scores[i] -= points
        scores[winner_idx] += points * 4

def handle_kang_flower(scores, players):
    while True:
        choice = select_player("\nWhich player had kang(s), or flower pair(s)?", players, {'5': 'None', '6': 'No more'})
        if choice in ['5', '6']:
            break
        idx = int(choice) - 1
        count = int(input("How many did they have?: "))
        for i in range(4):
            if i == idx:
                scores[i] += count * 6
            else:
                scores[i] -= count * 2

def display_scores(players, scores, taino):
    print("\nEach player has gained/lost this amount of money:")
    for player, score in zip(players, scores):
        print(f"{player}: ${score * taino:.2f}.")

# Main program
print("Mahjong Calculator \ny: start a new game \nn: quit\n")
game = input("Option: ")
if game == 'n':
    exit()
elif game == 'y':
    print()
    stime = dt.datetime.now()
    players = get_player_names()
    scores = [0, 0, 0, 0]
    taino = float(input("\nHow much is one tai?: "))

    for roundno in range(1, 10001):
        print(f"\n\nRound: {roundno}")
        winner = select_player("Who won?", players)
        loser = select_player("Who threw the losing tile?", players, {'5': 'zimo'})

        if winner == loser:
            print("\nWinner and loser cannot be the same. Try again.")
            continue

        points = int(input("\nHow many tai were won?: "))
        winner_idx = int(winner) - 1

        if loser == '5':
            update_scores(scores, winner_idx, None, points, is_zimo=True)
        else:
            loser_idx = int(loser) - 1
            update_scores(scores, winner_idx, loser_idx, points)

        handle_kang_flower(scores, players)

        end = input("\nEnd Game? \ny: Yes \nn: No\nOption: ")
        if end == 'y':
            break

    display_scores(players, scores, taino)

    now = dt.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    duration = dt.datetime.now() - stime
    summary = f"Game finished at: {dt_string}! This mahjong session was completed in {roundno} round(s), taking {duration}."
    print(summary)

    with open("mahjong.txt", "a") as mof:
        mof.write(f"{scores} {players} {dt_string}\n")

    os.system("pause")
