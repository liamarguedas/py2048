import random

BLANK = 0


def newColumnRow():
    return random.randint(0, 3), random.randint(0, 3)


def new_game(starting_value=2):
    TABLE = [
        [BLANK, BLANK, BLANK, BLANK],
        [BLANK, BLANK, BLANK, BLANK],
        [BLANK, BLANK, BLANK, BLANK],
        [BLANK, BLANK, BLANK, BLANK],
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
            if value[column] != BLANK
        ]
    return [(row, value[column]) for row, value in enumerate(matrix)]


def row(matrix, row, drop_blanks=True):
    if drop_blanks:
        return [
            (column, value)
            for column, value in enumerate(matrix[row])
            if value != BLANK
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

    available_spaces = [BLANK] * (4 - len(result_vector))

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
        if BLANK in row:
            available_moves = True

    return available_moves


def AVAILABLE_SPOT(TABLE, row, column):
    return True if TABLE[row][column] == BLANK else False


def SpawnNumber(TABLE, number=2):
    column, row = newColumnRow()

    while not AVAILABLE_SPOT(TABLE, row, column):
        column, row = newColumnRow()

    TABLE[row][column] = number


def ExecuteUserAction(user_input, TABLE):
    moves = {"w": MOVEUP, "s": MOVEDOWN, "d": MOVERIGHT, "a": MOVELEFT}
    moves[user_input](TABLE)
