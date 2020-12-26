import os
from fnmatch import fnmatch
from pathlib import Path
from resources import Resources
from resources import FontResource
from resources import StyleFile
from resources import Xmlres
import xmls
import pages
import utils


#FF = FontResource('./files/base/fonts.xml')
#Langs = xmls.Language('./files/languages/en.xml')


def getUnusedLangStrings():
    lang = xmls.Language('./files/languages/en.xml')
    pageData = pages.Pages('./files/pages/')
    pageData.loadXML('./files/base/styles.xml')
    pageData.loadXML('./files/base/c_page.xml')
    pageData.loadXML('./files/base/powerPanel.xml')
    pageData.loadXML('./files/ui.xml')
    pageData.loadXML('./files/portrait.xml')
    pageLang = utils.removeDublicate(pageData.langStrings)
    

    uncommonList = []
    flag = 0

    for item in lang.langStrings:
        for mItem in pageLang:
            #print(f'comparing {item.get("langString")} with {mItem}')
            if item.get('langString') == mItem:
                #print(f'matched {item.get("langString")} with {mItem}')
                flag = 1
                break
            else:
                flag = 0

        if flag == 0:

            uncommonList.append(item)

    for item in uncommonList:
        print(f'Line {item.get("lineNo")} : {item.get("langString")}')
    print(len(uncommonList))



def getUnusedStyles():
    styleFile = StyleFile('./files/base/styles.xml')
    p = pages.Pages('./files/pages/')
    p.loadXML('./files/base/styles.xml')
    p.loadXML('./files/base/c_page.xml')
    p.loadXML('./files/base/powerPanel.xml')
    p.loadXML('./files/ui.xml')
    p.loadXML('./files/portrait.xml')
    RAW = ""
    result = []

    for page in p.pageData:
        rawTexts = page.get("lines")
        for line in rawTexts:
            RAW+=line

    
    for style in styleFile.styles:
        if style not in RAW:
            result.append(style)

    print("Unused Styles - ")
    for unused in result:
        print(unused)


def getUnusedFonts():
    styleFile = StyleFile('./files/base/styles.xml')
    p = pages.Pages('./files/pages/')
    p.loadXML('./files/base/styles.xml')
    p.loadXML('./files/base/c_page.xml')
    p.loadXML('./files/base/powerPanel.xml')
    p.loadXML('./files/ui.xml')
    p.loadXML('./files/portrait.xml')
    RAW = ""
    result = []

    for page in p.pageData:
        rawTexts = page.get("lines")
        for line in rawTexts:
            RAW+=line

    fonts = utils.removeDublicate(styleFile.usedFont)

    for font in fonts:
        if font not in RAW:
            result.append(font)

    print("Unused Fonts - ")
    for unused in result:
        print(unused)



def getUnusedVariables():
    x = Xmlres('./files/base/variables.xml')
    
    for var in x.xmlVars:
        print(var.get('varName'))







def getMissingMainImages():
    x = Xmlres('./files/base/images.xml')
    imageName = []
    images = Path('./files/images/').glob('*.png')

    result = []

    for image in images:
        tmp = str(image)
        imageName.append(tmp[tmp.rfind('\\')+1:tmp.rfind('.')])

    for var in x.fileVars:
        if var.get('varName') not in imageName:
            result.append(var.get('varName'))


    for missing in result:
        print(missing)
        



def getUnusedImages():
    x = Xmlres('./files/base/images.xml')
    p = pages.Pages('./files/pages/')
    p.loadXML('./files/base/styles.xml')
    p.loadXML('./files/base/c_page.xml')
    p.loadXML('./files/base/powerPanel.xml')
    p.loadXML('./files/ui.xml')
    p.loadXML('./files/portrait.xml')

    result = []

    RAW = p.getRAW()
    
    for var in x.fileVars:
        if var.get('varName') not in RAW:
            result.append(var.get('varName'))

    return result



def removeUnunsedImages(images):
    root = '.\\files\\themeResources'
    pattern = "*.png"

    pngs = []

    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                os.path.join(path, name)
                pngs.append(path + '\\' + name)

    
    for image in images:
        for themePng in pngs:
            if image in themePng:
                os.remove(themePng)
                print("Removed - " + themePng)

    i = Path('.\\files\\images\\').glob('*.png')
    mainPngs = []
    for x in i:
        mainPngs.append(str(x))

    for image in images:
        for sImage in mainPngs:
            if image in sImage:
                if Path('.\\' + sImage).exists():
                    os.remove('.\\' + sImage)
                    print("removed -" + sImage)



    
    
    

def getPosValue(line):
    value = line[line.find('", "')+4 : line.rfind('");')]
    return int(value)

def setPosValue(line, value):
    f_str = line[0 : line.find('", "') + 4]
    return f_str + str(value) + '");'


def posInc(arr, value):
    tmp = []
    for item in arr:
        val = getPosValue(item)
        tmp.append(setPosValue(item, val + value))
    
    return tmp


#x = Xmlres('./files/base/images.xml')
#print(len(x.fileVars))



x = Path('./WorkSpace/SHRPVARS.cpp')
y = utils.getFileLines(x.read_text())
b = []
for item in y:
    if item.find("//") == -1 and item.find('mConst->SetValue("r') != -1:
        b.append(item)

rPos = []
rndPos = []
revPos = []


for item in b:
    if 'mConst->SetValue("rndPos' in item:
        rndPos.append(item)
    if 'mConst->SetValue("rPos' in item:
        rPos.append(item)
    if 'mConst->SetValue("revPos' in item:
        revPos.append(item)


rPos = posInc(rPos, -10)
for item in rPos:
    print(item)
