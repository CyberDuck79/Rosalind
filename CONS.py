# Consensus and Profile

size = 0
DNA_list = []
with open("rosalind.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        if line[0] == ">":
            DNA_list.append("")
        else:
            DNA_list[-1] += line.strip("\n")
    size = len(DNA_list[-1])

count = []
for i in range(4):
    count.append([0] * size)
for DNA in DNA_list:
    for i, symbol in enumerate(DNA):
        if symbol == 'A':
            count[0][i] += 1
        if symbol == 'C':
            count[1][i] += 1
        if symbol == 'G':
            count[2][i] += 1
        if symbol == 'T':
            count[3][i] += 1

concensus_str = ""
for i in range(size):
    temp_nb = 0
    temp_symbol = ""
    for j, symbol in enumerate(("A", "C", "G", "T")):
        if count[j][i] > temp_nb:
            temp_nb = count[j][i]
            temp_symbol = symbol
    concensus_str += temp_symbol

print(concensus_str)
print("A:", *count[0], sep=' ')
print("C:", *count[1], sep=' ')
print("G:", *count[2], sep=' ')
print("T:", *count[3], sep=' ')

