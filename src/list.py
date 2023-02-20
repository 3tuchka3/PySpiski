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
    print(stringListSpisok)