import re
fileBuf= open("regex_sum_357360.txt")
numList = list()
for line in fileBuf:
    numsinLine=re.findall('[0-9]+',line)
    numList.extend(map(int,numsinLine))
print sum(numList)
