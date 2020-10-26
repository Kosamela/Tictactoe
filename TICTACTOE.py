
b = [' ']

map = [ 
        [b[0], b[0], b[0]],
        [b[0], b[0], b[0]],
        [b[0], b[0], b[0]],
    ]



def play_map():
    print("-" * 9)
    print("| " + map[0][2] + " " + map[1][2] + " " + map[2][2] + " |")
    print("| " + map[0][1] + " " + map[1][1] + " " + map[2][1] + " |")
    print("| " + map[0][0] + " " + map[1][0] + " " + map[2][0] + " |")
    print("-" * 9)

play_map()

def playing():
    game_checker = True
    number = 1

    while game_checker == True:
        ask = input("Enter the coordinates:")
        move = ask.split(" ")
        counter = number % 2

        if move[0].isalpha() or move[1].isalpha():
            print("You should enter numbers!")
        elif int(move[0]) >= 4 or int(move[0]) <= 0 or int(move[1]) >= 4 or int(move[1]) <= 0:
            print("Coordinates should be from 1 to 3!")
        elif map[int(move[0]) - 1][int(move[1])- 1] == "X" or map[int(move[0]) - 1][int(move[1]) - 1] == "O":
            print("This cell is occupied! Choose another one!")
        else:
            for x in range(1, 4):
                for k in range(1, 4):
                    if int(move[0]) == x and int(move[1]) == k and counter == 1:
                        map[x - 1][k - 1] = "X"
                        number += 1
                        play_map()
                    elif int(move[0]) == x and int(move[1]) == k and counter == 0:  
                        map[x - 1][k - 1] = "O"
                        number += 1
                        play_map()                 
                    if (map[x - 1][0] == map[x - 1][1] == map[x - 1][2] == 'X') or (map[2][k - 1] == map[1][k - 1] == map[0][k - 1] == "X"):
                        print("X wins")
                        game_checker = False
                        break
                    elif (map[x - 1][0] == map[x - 1][1] == map[x - 1][2] == 'O') or (map[2][k - 1] == map[1][k - 1] == map[0][k - 1] == "O"):
                        print("O wins")
                        game_checker = False
                        break
                    elif (map[0][0] == map[1][1] == map[2][2] == 'X') or (map[2][0] == map[1][1] == map[0][2] == "X"):
                        print("X wins")
                        game_checker = False
                        break
                    elif (map[0][0] == map[1][1] == map[2][2] == 'O') or (map[2][0] == map[1][1] == map[0][2] == "O"):
                        print("O wins")
                        game_checker = False
                        break
                    if number == 10 and game_checker == True:
                        print("Draw")
                        game_checker = False
                        break
playing()
