# Computing GC Content


class GC:
    def __init__(self, title):
        self.title = title.strip("\n")
        self.data = ""
        self.content = 0


GC_lst = []
with open("rosalind.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        if line[0] == ">":
            GC_lst.append(GC(line.strip(">")))
        else:
            GC_lst[-1].data += line.strip("\n")

highest = GC_lst[0]
for GC in GC_lst:
    count = 0
    for DNA in GC.data:
        if DNA == "C" or DNA == "G":
            count += 1
    GC.content = count / len(GC.data) * 100
    if GC.content > highest.content:
        highest = GC

print(highest.title)
print(highest.content)

