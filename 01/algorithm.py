# f = open("sample.txt", "r")
f = open("input.txt", "r")
elf_backpack = f.read().split("\n\n")

total_kcal = []
for line in elf_backpack:
     food = line.split("\n")
     total_kcal.append(sum([int(f) for f in food if f]))


print(max(total_kcal)) 
# ---------------------------
# 02
total_kcal.sort(reverse=True)
total = sum(total_kcal[:3])

print(total)