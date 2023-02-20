import glob
import SpisokClass
pach = glob.glob('./data/*.txt')
string = ''
for el in pach:
    string += str(el)

file = open(string)
stringList = file.readlines()


i = 12
m = 0
newList = []
while i < len(stringList) - 3:
    stringListSpisok = stringList[i].split('~')
    newList.append(stringListSpisok)
    i += 1



for stringListSpisok in newList:
    stringListSpisok.pop(0)
    item = stringListSpisok[3].replace('\n', '')
    stringListSpisok.pop(3)
    stringListSpisok.append(item)
    # print(stringListSpisok)

print(newList)
for stringListSpisok in newList:
    spisokClass = SpisokClass(stringListSpisok[0],stringListSpisok[1],stringListSpisok[2],stringListSpisok[3])
    # spisokClass.SpisokClass.set_nch(stringListSpisok[0])
    # spisokClass.SpisokClass.set_name(stringListSpisok[1])
    # spisokClass.SpisokClass.set_nch(stringListSpisok[2])
    # spisokClass.SpisokClass.set_sum(stringListSpisok[3])
    print(spisokClass)