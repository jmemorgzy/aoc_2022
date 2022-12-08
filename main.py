import random

# goes first
opponent = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

# goes second
player = {
    "Y": "paper",
    "X": "rock",
    "Z": "scissors"
}

scores = {
    "win": 6,
    "draw": 3,
    "lose": 0,
}


def main():
    player_score = 0
    opponent_score = 0
    print("Rock paper scissors")

    with open("input.txt") as file:
        for line in file:
            print(line[2])
            if player[line[2]] == "rock":
                player_score += 1
            elif player[line[2]] == "paper":
                player_score += 2
            elif player[line[2]] == "scissors":
                player_score += 3
            
            # print(f"Opponent chooses: {opponent[line[0]]}")
            # print(f"Opponent chooses: {player[line[2]]}\n")
            if opponent[line[0]] == player[line[2]]:
                player_score += 3

            elif opponent[line[0]] == "rock":
                if player[line[2]] == "paper":
                    print(f"Player wins and awarded 6 points")
                    player_score += 6
                else:
                    print(f"Opponent wins. Opponent awared 6 points")
                    opponent_score += 6
            elif opponent[line[0]] == "scissors":
                if player[line[2]] == "rock":
                    print(f"Player wins and awarded 6 points")
                    player_score += 6
                else:
                    print(f"Opponent wins. Opponent awared 6 points")
                    opponent_score += 6
            elif opponent[line[0]] == "paper":
                if player[line[2]] == "scissors":
                    print(f"Player wins and awarded 6 points")
                    player_score += 6
                else:
                    print(f"Opponent wins. Opponent awared 6 points")
                    opponent_score += 6


    print(player_score)


if __name__ == '__main__':
    main()