from pathlib import Path
import utils
import xmls
import pages



lang = xmls.Language('lang.xml')

#for item in lang.langStrings:
#    print(item.get("line"))

collected = []


lang2 = xmls.LanguageX('lang2.xml')



lang1List = []
lang2List = []

found = False
count = 0
for item in lang.langStrings:
    for item2 in lang2.langStrings:
        if item.get('langString') in item2.get('langString'):
            #print(f'{item.get("langString")}   xxx    {item2.get("langString")} \t {count}')
            count += 1
            found = True
            lang2List.append(item2)
            break
        else:
            found = False

    if not found:
        lang1List.append(item)



for item in lang2List:
    print(item.get('line'))

print('<!--Pending Strings-->')
for item in lang1List:
    print(item.get('line'))


print('---------------------------------')
print(len(lang1List))
print(len(lang2List))






#for item in collected:
    #print(item)