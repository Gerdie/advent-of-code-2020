
num_valid = 0
num_valid_by_index = 0

def is_valid(letter, password, min_constraint, max_constraint):
    appearances = 0
    for char in password:
        if char == letter:
            appearances += 1
            if appearances > max_constraint:
                return False

    if appearances < min_constraint:
        return False

    return True

def is_valid_by_index(letter, password, index_1, index_2):
    # normalize for 0 index
    index_1 -= 1
    index_2 -= 1
    characters = set([password[index_1], password[index_2]])
    if len(characters) == 2 and letter in characters:
        return True
    return False

with open('input.txt') as file:
    for line in file:
        line = line.strip()
        constraint, letter, password = line.split(' ')
        min_constraint, max_constraint = map(int, constraint.split('-'))
        letter = letter[:-1]
        if is_valid(letter, password, min_constraint, max_constraint):
            num_valid += 1
        if is_valid_by_index(letter, password, min_constraint, max_constraint):
            num_valid_by_index += 1

    print('Part One: {} valid passwords'.format(num_valid))
    print('Part Two: {} valid passwords'.format(num_valid_by_index))
