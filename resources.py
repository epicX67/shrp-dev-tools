from pathlib import Path
from utils import extractFileName
from utils import removeDublicate
from utils import getFileLines


class Resources:
    mainImages = []
    mainPath = ''

    accentImages = []
    accPath = ''

    backgroundImages = []
    bgPath = ''

    dashboardImages = []
    dashPath = ''

    navImages = []
    navPath = ''


    accType = ( 'blue', 'brown', 'cyan', 'dark', 'green', 'indigo', 'lred', 'orange', 'pink', 'purple', 'red', 'rpink', 'teal', 'white', 'yellow')
    backgroundType = ('black', 'dark', 'darkViolate', 'deepBlue', 'white')
    navType = ('c_custom', 'c_default', 'c_nxtbit', 'c_samsung')
    dashboardType = ('aex', 'black', 'default', 'stock', 'white')

    def __init__(self,basePath,resourcePath):
        self.mainPath = basePath + '/'
        self.accPath = resourcePath + '/accentResources/'
        self.bgPath = resourcePath + '/backgroundResources/'
        self.dashPath = resourcePath + '/dashboardResources/'
        self.navPath = resourcePath + '/navigationResources/'
        self.load_Images()



    def load_Images(self):
        tmp = Path(self.mainPath).glob('*.png')
        
        #loading MainImages
        for item in tmp:
            self.mainImages.append(extractFileName(item.__str__()))
        
        #Loading Accent Images
        for color in self.accType:
            tmp = Path(f'{self.accPath}/{color}/').glob('*.png')
            for item in tmp:
                self.accentImages.append(extractFileName(item.__str__()))
        
        #loading BG
        for color in self.backgroundType:
            tmp = Path(f'{self.bgPath}/{color}/').glob('*.png')
            for item in tmp:
                self.backgroundImages.append(extractFileName(item.__str__()))

        #loading BG
        for color in self.dashboardType:
            tmp = Path(f'{self.dashPath}/{color}/').glob('*.png')
            for item in tmp:
                self.dashboardImages.append(extractFileName(item.__str__()))

        for tpe in self.navType:
            for color in self.accType:
                tmp = Path(f'{self.navPath}/{tpe}/c_{color}/').glob('*.png')
                for item in tmp:
                    self.navImages.append(extractFileName(item.__str__()))


    def getCommonImages(self):
        bigList = removeDublicate(self.navImages)
        

        return bigList



class Xmlres:
    fileVars = []
    xmlVars = []
    cppVars = []

    def __init__(self, path):
        self.path = path
        self.loadXML(path)


    def loadXML(self, path):
        xml = Path(path)
        data = getFileLines(xml.read_text())
        count = 1
        for line in data:

            tmp = self.getVarStrings(line)
            if tmp != None : 
                info = { }
                info.__setitem__('lineNo', count)
                info.__setitem__('line', line)
                info.__setitem__('varName', tmp)
                self.xmlVars.append(info)

            tmp = self.getFileVar(line)
            if tmp != None:
                info = {}
                info.__setitem__('lineNo', count)
                info.__setitem__('line', line)
                info.__setitem__('varName', tmp)
                self.fileVars.append(info)

            count += 1


        
    def loadCPP(self, path):
        xml = Path(path)
        data = getFileLines(xml.read_text())
        count = 1
        for line in data:
            tmp = self.getVarFromCPP(line)
            if tmp != None : 
                info = { }
                info.__setitem__('lineNo', count)
                info.__setitem__('line', line)
                info.__setitem__('varName', tmp)
                self.cppVars.append(info)

            count += 1



    def getVarStrings(self, line):
        string = None
        if line.find('="') != -1 and line.find('value') != -1:
            line = line[0 : line.find('value')]
            string = line[line.find('="')+2 : line.rfind('"')]

        return string


    def getFileVar(self, line):
        string = None
        if line.find('="') != -1 and line.find('filename') != -1:
            line = line[0 : line.find('filename')]
            string = line[line.find('="')+2 : line.rfind('"')]
            
        return string

    
    def getVarFromCPP(self, line):
        string = None
        if "//" in line:
            return string

        if "mConst" or "mData" or "mPersist" not in line:
            return string
            
        if line.find('"') != -1 and line.rfind('"') != -1 and line.find('"') != line.rfind('"'):
            string = line[line.find('"')+1 : line.rfind('"')]
            
        return string




class FontResource:
    availableFont = []

    def __init__(self, path):
        xml = Path(path)
        data = getFileLines(xml.read_text())
        for line in data:
            tmp = self.getFileVar(line)
            if tmp != None:
                self.availableFont.append(tmp)


            


    def getFileVar(self, line):
        string = None
        if line.find('="') != -1 and line.find('filename') != -1:
            line = line[0 : line.find('filename')]
            string = line[line.find('="')+2 : line.rfind('"')]
            
        return string




class StyleFile:
    usedFont = []
    styles = []

    def __init__(self, path):
        xml = Path(path)
        data = getFileLines(xml.read_text())
        for line in data:
            tmp = self.getStyleVar(line)
            if tmp != None:
                self.styles.append(tmp)

            tmp = self.getFontResourceVar(line)
            if tmp != None:
                self.usedFont.append(tmp)


    def getStyleVar(self, line):
        string = None
        if line.find('<style name=') != -1:
            string = line[line.find('"') + 1 : line.rfind('">')]
        
        return string

    def getFontResourceVar(self, line):
        string = None
        if line.find('<font resource="') != -1:
            line = line[line.find('<font resource="') + len('<font resource="') :]
            string = line[0 : line.find('"')]
            
        return string







    

        
            









