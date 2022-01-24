import random

DICE_ASCII_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
HEIGHT = len(DICE_ASCII_ART[1])
WIDTH = len(DICE_ASCII_ART[1][0])
FACE_SEPARATOR = " "


def parse_input(string):
    """
    Check if the user input is an integer b/w 1-6.
    Else quit the program with a message.
    :param string:
    :return: int of the string passed, if valid, exit otherwise
    """
    if string.strip() in ["1", "2", "3", "4", "5", "6"]:
        return int(string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)


def roll_dice(num):
    """
    :param num: # of dice cast
    :return: list of results
    """
    results = []
    for _ in range(num):
        roll = random.randint(1, 6)
        results.append(roll)
    return results


def generate_art(dice_values):
    # Get a list of faces from the ASCII Art
    faces = []
    for value in dice_values:
        faces.append(DICE_ASCII_ART[value])

    # List of dice face rows
    dice_faces_rows = []
    for row_id in range(HEIGHT):
        row_components = []
        for die in faces:
            row_components.append(die[row_id])
        row_string = FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

    # Get header
    width = len(dice_faces_rows[0])
    header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([header] + dice_faces_rows)
    return dice_faces_diagram


# Getting user input

num_dice = input("How many dice would you like to roll? [1-6]")

num_dice = parse_input(num_dice)

# Rolling the die
results = roll_dice(num_dice)

# Generating the ASCII Diagram
dice_face_diagram = generate_art(results)

# Display
print(f"\n{dice_face_diagram}")
