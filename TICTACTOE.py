a = input(str())
print("---------")
print("| " + a[0] + " " + a[1] + " " + a[2] + " |")
print("| " + a[3] + " " + a[4] + " " + a[5] + " |")
print("| " + a[6] + " " + a[7] + " " + a[8] + " |")
print("---------")

x_wins = False
o_wins = False
empty = "_" in a
for i in range(0, 8, 3):
    if a[i] == a[i + 1] == a[i + 2] == "X":
        x_wins = True
    elif a[i] == a[i + 1] == a[i + 2] == "O":
        o_wins = True
for i in range(3):
    if a[i] == a[i + 3] == a[i + 6] == "X":
        x_wins = True
    elif a[i] == a[i + 3] == a[i + 6] == "O":
        o_wins = True
if a[0] == a[4] == a[8] == "X" or a[2] == a[4] == a[6] == "X":
    x_wins = True
if a[0] == a[4] == a[8] == "O" or a[2] == a[4] == a[6] == "O":
    o_winx = True
if a.count("X") - a.count("O") >= 2 or a.count("O") - a.count("X") >= 2:
    print("Impossible")
elif x_wins == True and o_wins == True:
    print("Impossible")
elif x_wins == False and o_wins == False and empty == False:
    print("Draw")
elif x_wins == True:
    print("X wins")
elif o_wins == True:
    print("O wins")
else:
    print("Game not finished")