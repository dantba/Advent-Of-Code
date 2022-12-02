# f = open("sample.txt", "r")
f = open("input.txt", "r")

input = f.read().split("\n")
matrix = list(map(lambda line: line.split(), input))
score_map = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

#If I put a letter, which letter played by elf will give me a win
win_map = {
    'X': 'C',
    'Y': 'A',
    'Z': 'B'
}
total = 0
for entry in matrix:
    total += score_map[entry[1]][1]
    elf_play = entry[0]
    my_play = entry[1]
    if my_play == elf_play:
        total += 3
    elif win_map[my_play] == elf_play:
        total += 6

print(total)
