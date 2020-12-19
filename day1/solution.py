# Part One
seen_numbers = set()

with open('input.txt') as file:
    for line in file:
        number = int(line.strip())
        looking_for = 2020 - number
        if looking_for in seen_numbers:
            print('Part 1: {} x {} = {}'.format(looking_for, number, looking_for * number))
            break
        seen_numbers.add(number)

# Part Two
seen_numbers = set()

with open('input.txt') as file:
    for line in file:
        number = int(line.strip())
        sum = 2020 - number
        for seen_num in seen_numbers:
            looking_for = sum - seen_num
            if looking_for in seen_numbers:
                print('Part 2: {} x {} x {} = {}'.format(looking_for,
                                                         seen_num,
                                                         number,
                                                         looking_for * seen_num * number))
                break
        seen_numbers.add(number)
