
def is_tree_at_index(row_pattern, index):
    if index >= len(row_pattern):
        index_modulo = index % len(row_pattern)
    else:
        index_modulo = index
    if row_pattern[index_modulo] == '#':
        return True
    return False


def count_trees_at_slope(right_slope, down_slope):
    tree_count = 0
    position = 0
    skip_rows = 0
    with open('input.txt') as file:
        for line in file:
            if skip_rows:
                skip_rows -= 1
                continue
            line = line.strip()
            if is_tree_at_index(line, position):
                tree_count += 1
            position += right_slope
            skip_rows = down_slope - 1
    return tree_count

part_one = count_trees_at_slope(3,1)
print('Part One: {} trees'.format(part_one))

part_two = count_trees_at_slope(1,1) * \
    count_trees_at_slope(3,1) * \
    count_trees_at_slope(5,1) * \
    count_trees_at_slope(7,1) * \
    count_trees_at_slope(1,2)

print('Part Two: {} trees'.format(part_two))
