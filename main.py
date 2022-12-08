def main():
    opponent = {
        "A": "rock",
        "B": "paper",
        "C": "scissors"
    }

    player = {
        "Y": "paper",
        "X": "rock",
        "Z": "scissors"
    }

    player_score = 0

    with open("input.txt") as file:
        for line in file:
            if player[line[2]] == "rock":
                player_score += 1
            elif player[line[2]] == "paper":
                player_score += 2
            else:
                player_score += 3

            if opponent[line[0]] == player[line[2]]:
                player_score += 3

            if opponent[line[0]] == "rock" and player[line[2]] == "paper":
                player_score += 6
                
            if opponent[line[0]] == "scissors" and player[line[2]] == "rock":
                player_score += 6
                
            if opponent[line[0]] == "paper" and player[line[2]] == "scissors":                
                player_score += 6
               
    print(player_score)


if __name__ == '__main__':
    main()
