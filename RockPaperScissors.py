from os import system

MOVES = ["ROCK", "PAPER", "SCISSORS"]


def get_player_move():
    return MOVES[0]


def get_computer_move():
    return MOVES[0]


def get_winner(player_move, computer_move):
    if player_move == computer_move:
        return "It's a draw"
    else:
        return "Moves unrecognised"


if __name__ == '__main__':
    while True:
        system("cls")
        print("Welcome to the rock paper scissors game")

        player = get_player_move()
        computer = get_computer_move()

        print("The player picked", player)
        print("The computer picked", computer)
        print(get_winner(player, computer))

        if input("Press (Y) to continue or (N) to quit:\n") == "N":
            break

