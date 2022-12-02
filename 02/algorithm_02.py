# f = open("sample.txt", "r")
f = open("input.txt", "r")

input = f.read().split("\n")
matrix = list(map(lambda line: line.split(), input))

# If elf puts a letter, which one I should play to lose
lose_map = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

# If elf puts a letter, which one I should play to win
win_map = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}

score_map = {
    'A': 1,
    'B': 2,
    'C': 3
}

score_map_result = {
    'X': (0, False),
    'Y': (3, None),
    'Z': (6, True),
    
}
total = 0
for entry in matrix:
    total += score_map_result[entry[1]][0]
    result = score_map_result[entry[1]][1]
    should_play = ''
    if result == True:
        should_play = win_map[entry[0]]
    elif result == False:
        should_play = lose_map[entry[0]]
    else:
        should_play = entry[0]
    total += score_map[should_play]


print(total)