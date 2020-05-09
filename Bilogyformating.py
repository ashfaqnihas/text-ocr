import re


lineList = [line.rstrip('\n') for line in open('biotamil2018to2015.txt',encoding='utf8')]
print(len(lineList))
# for line in lineList:
#     match1=re.match(r'^(\W+)$',line)
#     if match1 is not None:
#         lineText=match1.group(1)
#         print(lineText)


notStartWithsSymbolList=list(filter(lambda x:re.match(r'^(\W+)$',x)==None,lineList))
StartWithsSymbolList=list(filter(lambda x:re.match(r'^(\W+)$',x)!=None,lineList))
print(len(notStartWithsSymbolList))
print(len(StartWithsSymbolList))
with open('notStartWithsSymbolListbiotamil2018to2015.txt', 'w',encoding='utf8') as f:
    # f.writelines(notStartWithsSymbolList)
    for item in notStartWithsSymbolList:
        f.write(item)
        f.write('\n')

with open('StartWithsSymbolListbiotamil2018to2015.txt', 'w',encoding='utf8') as f:
    # f.writelines(notStartWithsSymbolList)
    for item in StartWithsSymbolList:
        f.write(item)
        f.write('\n')

