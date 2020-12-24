import re

required_fields = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
}

optional_fields = { 'cid' }

def parse_passport(line, passport):
    key_value_pairs = line.split(' ')
    for pair in key_value_pairs:
        k, v = pair.split(':')
        passport[k] = v

def is_valid_part_one(passport):
    for field in required_fields:
        if field not in passport:
            return False
    return True

def is_valid_num(num_string, minimum, maximum):
    try:
        num = int(num_string)
    except ValueError:
        return False

    if num < minimum or num > maximum:
        return False
    return True

def is_valid_byr(passport):
    """four digits; at least 1920 and at most 2002"""
    return is_valid_num(passport['byr'], 1920, 2002)

def is_valid_iyr(passport):
    """four digits; at least 2010 and at most 2020"""
    return is_valid_num(passport['iyr'], 2010, 2020)

def is_valid_eyr(passport):
    """four digits; at least 2020 and at most 2030"""
    return is_valid_num(passport['eyr'], 2020, 2030)

def is_valid_hgt(passport):
    """a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76"""
    hgt = passport['hgt']
    if hgt.endswith('cm'):
        centimeters = hgt[:-2]
        return is_valid_num(centimeters, 150, 193)
    elif hgt.endswith('in'):
        inches = hgt[:-2]
        return is_valid_num(inches, 59, 76)
    else:
        return False

def is_valid_hcl(passport):
    """a # followed by exactly six characters 0-9 or a-f"""
    hcl = passport['hcl']
    if re.match('^#[\da-f]{6}$', hcl):
        return True
    return False

def is_valid_ecl(passport):
    ecl = passport['ecl']
    if ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        return True
    return False

def is_valid_pid(passport):
    pid = passport['pid']
    if re.match('^\d{9}$', pid):
        return True
    return False

def is_valid_part_two(passport):
    if not is_valid_byr(passport):
        return False
    if not is_valid_iyr(passport):
        return False
    if not is_valid_eyr(passport):
        return False
    if not is_valid_hgt(passport):
        return False
    if not is_valid_hcl(passport):
        return False
    if not is_valid_ecl(passport):
        return False
    if not is_valid_pid(passport):
        return False
    return True

def get_valid_totals(valid_part_one, valid_part_two, passport):
    if not is_valid_part_one(passport):
        return valid_part_one, valid_part_two

    if not is_valid_part_two(passport):
        return valid_part_one + 1, valid_part_two

    return valid_part_one + 1, valid_part_two + 1

with open('input.txt') as file:
    valid_part_one = 0
    valid_part_two = 0
    passport = {}
    for line in file:
        line = line.strip()
        if line:
            parse_passport(line, passport)
            continue

        valid_part_one, valid_part_two = get_valid_totals(
            valid_part_one,
            valid_part_two,
            passport
        )

        passport = {}

    # Catch the last line
    valid_part_one, valid_part_two = get_valid_totals(
        valid_part_one,
        valid_part_two,
        passport
    )

print('Part One: {} valid passports'.format(valid_part_one))
print('Part Two: {} valid passports'.format(valid_part_two))
