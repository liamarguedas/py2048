import random


def update_table(values: list):
    print()
    print(f"| {values[0][0]} | {values[0][1]} | {values[0][2]} | {values[0][3]} |")
    print(f"| {values[1][0]} | {values[1][1]} | {values[1][2]} | {values[1][3]} |")
    print(f"| {values[2][0]} | {values[2][1]} | {values[2][2]} | {values[2][3]} |")
    print(f"| {values[3][0]} | {values[3][1]} | {values[3][2]} | {values[3][3]} |")


def newColumnRow():
    return random.randint(0, 3), random.randint(0, 3)


def new_game(starting_value=2):
    TABLE = [
        [" ", " ", " ", " "],
        [" ", " ", " ", " "],
        [" ", " ", " ", " "],
        [" ", " ", " ", " "],
    ]

    FSC, FSR = newColumnRow()

    SSC, SSR = newColumnRow()

    while (SSC == FSC) and (SSR == FSR):
        SSC, SSR = newColumnRow()

    TABLE[FSC][FSR] = starting_value
    TABLE[SSC][SSR] = starting_value

    return TABLE


def column(matrix, column, drop_blanks=True):
    if drop_blanks:
        return [
            (row, value[column])
            for row, value in enumerate(matrix)
            if value[column] != " "
        ]
    return [(row, value[column]) for row, value in enumerate(matrix)]


def row(matrix, row, drop_blanks=True):
    if drop_blanks:
        return [
            (column, value) for column, value in enumerate(matrix[row]) if value != " "
        ]
    return [(column, value) for column, value in enumerate(matrix[row])]


def sum_vector(vector, reversed=False):
    result_vector = []

    value = 0

    while value < len(vector):
        if value + 1 < len(vector) and vector[value] == vector[value + 1]:
            result_vector.append(vector[value] * 2)

            value += 2

        else:
            result_vector.append(vector[value])

            value += 1

    available_spaces = [" "] * (4 - len(result_vector))

    if not reversed:
        result_vector.extend(available_spaces)
        return result_vector

    if reversed:
        available_spaces.extend(result_vector)
        return available_spaces


def MOVEUP(TABLE):
    for n_column in range(4):
        new_vector = sum_vector([item[1] for item in column(TABLE, n_column)])

        for row in range(4):
            TABLE[row][n_column] = new_vector[row]


def MOVEDOWN(TABLE):
    for n_column in range(4):
        new_vector = sum_vector(
            [item[1] for item in column(TABLE, n_column)], reversed=True
        )

        for row in range(4):
            TABLE[row][n_column] = new_vector[row]


def MOVERIGHT(TABLE):
    for n_row in range(4):
        TABLE[n_row] = sum_vector(
            [item[1] for item in row(TABLE, n_row)], reversed=True
        )


def MOVELEFT(TABLE):
    for n_row in range(4):
        TABLE[n_row] = sum_vector([item[1] for item in row(TABLE, n_row)])


def VERIFY_GAME(TABLE):
    available_moves = False

    for row in TABLE:
        if " " in row:
            available_moves = True

    return available_moves


def AVAILABLE_SPOT(TABLE, row, column):
    return True if TABLE[row][column] == " " else False


def SpawnNumber(TABLE, number=2):
    column, row = newColumnRow()

    while not AVAILABLE_SPOT(TABLE, row, column):
        column, row = newColumnRow()

    TABLE[row][column] = number


def get_user_input(input, TABLE):
    moves = {"w": MOVEUP, "s": MOVEDOWN, "d": MOVERIGHT, "a": MOVELEFT}
    moves[input](TABLE)
