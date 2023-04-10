def hello():
    print(f"   Hello! "
          f"\n Welcome to the XOXO "
          f"\n input  x y"
          f"\n x - lines, y - columns")


def show():
    print(f"  | 0 | 1 | 2 | ")
    for i in range(3):
        print("---------------")
        print(f"{i} | {field[i][0]} | {field[i][1]} | {field[i][2]} |")

    print("---------------")


def ask():
    while True:
        coordinates = input(" Your move: ").split()

        if len(coordinates) != 2:
            print("Input 2 coordinates")
            continue

        x, y = coordinates

        if not (x.isdigit()) or not (y.isdigit()):
            print("Input numbers")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Incorrect coordinates")
            continue

        if field[x][y] != " ":
            print("The cage is occupied!")
            continue

        return x, y


def chek_win():
    win_coordinates = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                       ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                       ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for coord in win_coordinates:
        symbols = []
        for c in coord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Winner X")
            return True
        if symbols == ["O", "O", "O"]:
            print("Winner O")
            return True
    return False


hello()
field = [[' '] * 3 for i in range(3)]

num = 0
while True:
    num += 1
    show()
    if num % 2 == 1:
        print("Move X")
    else:
        print("Move O")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if chek_win():
        break

    if num == 9:
        print("Nno one won")
        break