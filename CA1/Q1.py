myString = input()
seen = {}
seen[0] = 1
bitmask = 0
numOfSubstrings = 0
for i in range(len(myString)):
    bitmask ^= (1 << (ord(myString[i]) - ord('a')))
    if bitmask in seen:
        numOfSubstrings += seen[bitmask]
    else:
        numOfSubstrings += 0
    for j in range(26):
        if bitmask ^ (1 << j) in seen:
            numOfSubstrings += seen[bitmask ^ (1 << j)]
        else:
            numOfSubstrings += 0
    if bitmask in seen:
        seen[bitmask] += 1
    else:
        seen[bitmask] = 1
print(numOfSubstrings)