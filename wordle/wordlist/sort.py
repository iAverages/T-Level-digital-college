# Basic insertion sort across words.txt
# Only sorts alphebetically by the
# first character of the words
# why? why not
file = open("words.txt", "r")
tmp = file.read().splitlines()
file.close()
i = 0

for i in range(1, len(tmp)):
    currItem = tmp[i]
    prevIdx = i - 1
    while prevIdx >= 0 and tmp[prevIdx][0] > currItem[0]:
        tmp[prevIdx + 1] = tmp[prevIdx]
        prevIdx -= 1
    tmp[prevIdx + 1] = currItem

print(tmp)
file2 = open("words-sorted.txt", "w")
file2.write("\n".join(tmp))
file2.close()