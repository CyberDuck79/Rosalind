# Finding a Motif in DNA

with open("data/DNA.txt", "r") as myfile:
    data = myfile.readlines()

s = data[0].strip()
t = data[1].strip()

for i in range(0, len(s)):
    if s[i:i+len(t)] == t:
        print(i+1, end=' ')
