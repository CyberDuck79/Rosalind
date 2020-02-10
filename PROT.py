# Translating RNA into Protein

with open("data/RNA.txt", "r") as myfile:
    data = myfile.readlines()

trans = {
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H",
    "AUU": "I", "AUC": "I", "AUA": "I",
    "AAA": "K", "AAG": "K",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "UUA": "L", "UUG": "L",
    "AUG": "M",
    "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGA": "R", "AGG": "R",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "AGU": "S", "AGC": "S",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAG": "STOP", "UAA": "STOP", "UGA": "STOP"
}

RNA = data[0].strip("\n")
start = RNA.find("AUG")
protein = ""
for i in range(start, len(RNA), 3):
    codon = RNA[i:i+3]
    if trans[codon] == "STOP":
        break
    protein += trans[codon]
    # print(f"RNA codon: {codon}")
    # print(f"Translation: {trans[codon]}")
print(f"\nProtein code: {protein}")
