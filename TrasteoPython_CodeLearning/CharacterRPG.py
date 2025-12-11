full_dot = "●"
empty_dot = "○"


def create_character(name, strength, inteligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    if not (
        isinstance(strength, int)
        and isinstance(inteligence, int)
        and isinstance(charisma, int)
    ):
        return "All stats should be integers"
    if strength * inteligence * charisma <= 0:
        return "All stats should be no less than 1"
    if not (strength <= 4 and inteligence <= 4 and charisma <= 4):
        return "All stats should be no more than 4"
    if strength + inteligence + charisma != 7:
        return "The character should start with 7 points"

    return f"{name}\nSTR {full_dot*strength}{empty_dot*(10-strength)}\nINT {full_dot*inteligence}{empty_dot*(10-inteligence)}\nCHA {full_dot*charisma}{empty_dot*(10-charisma)}"


print(create_character("ren", 4, 2, 1))