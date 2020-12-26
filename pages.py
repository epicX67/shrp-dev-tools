from pathlib import Path
from utils import getFileLines


class Pages:
    langStrings = []
    pageData = []
    pageLine = []

    #page{
    #   file:""
    #   lines:[]
    #}
    #
    #
    #


    def __init__(self, path):
        xmls = Path(path).glob('*.xml')
        for xmlFile in xmls:
            self.loadXML(str(xmlFile))

        self.loadXML('./files/base/c_page.xml')
        self.loadXML('./files/base/powerPanel.xml')
        self.loadXML('./files/base/c_page.xml')
        self.loadXML('./files/ui.xml')



    def __init__(self, path, dummy):
        self.loadXML(path, dummy)



    
    def loadXML(self, path):
        xmlFile = Path(path)
        data = getFileLines(xmlFile.read_text())
        
        self.gatherLangStrings(data)

        

        pageDataItem = {}
        pageDataItem.__setitem__('file', xmlFile.__str__())
        lines = []
        for line in data:
            lines.append(line)

        pageDataItem.__setitem__('lines', lines)

        self.pageData.append(pageDataItem)




    def loadXML(self, path, dummy):
        xmlFile = Path(path)
        self.pageLine = getFileLines(xmlFile.read_text())
        



    def gatherLangStrings(self, data):
        for line in data:
            langTmp = self.getLangStrings(line)
            for langstring in langTmp:
                if langstring != None and  langstring != '':
                    self.langStrings.append(langstring)



    def getLangStrings(self, line):
        strings = []
        if line.find("{@") == -1:
            strings.append(None)
            return strings
        else:
            strings.append(None)
            while line.find("{@") != -1 :
                strings.append(line[line.find("{@")+2 : line.find("=")])
                line = line[line.find("}") + 1 : ]

            return strings


    def getRAW(self):
        RAW = ""
        for eachPageData in self.pageData:
            lines = eachPageData.get('lines')
            for line in lines:
                RAW +=line

        return RAW

    
    


            

    






