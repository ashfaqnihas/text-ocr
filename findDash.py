import re
lineList = [line.rstrip('\n') for line in open('notStartWithsSymbolList4.txt',encoding='utf8')]
print(len(lineList))
# for line in lineList:
#     match1=re.match(r'^(\W+)$',line)
#     if match1 is not None:
#         lineText=match1.group(1)
#         print(lineText)


containDashSymbolList=list(filter(lambda x:re.match(r'.*-+.*',x)!=None,lineList))
# StartWithsSymbolList=list(filter(lambda x:re.match(r'^(\W+)$',x)!=None,lineList))
print(len(containDashSymbolList))
# print(len(StartWithsSymbolList))
with open('containDashSymbolList1.txt', 'w',encoding='utf8') as f:
    # f.writelines(notStartWithsSymbolList)
    for item in containDashSymbolList:
        f.write(item)
        f.write('\n')

# with open('StartWithsSymbolList3.txt', 'w',encoding='utf8') as f:
#     # f.writelines(notStartWithsSymbolList)
#     for item in StartWithsSymbolList:
#         f.write(item)
#         f.write('\n')
