from pathlib import Path
from utils import getFileLines

class Language:
    langStrings = []
    def __init__(self,path):
        count = 1
        lang_file = Path(path)
        data = getFileLines(lang_file.read_text())
        for line in data:
            langSet = {
                "line": '',
                "lineNo": 0,
                "langString": ''
            }
            tmp = self.getLangStrings(line)
            if tmp != "NULL":
                langSet.__setitem__('line', line)
                langSet.__setitem__('lineNo', count)
                langSet.__setitem__('langString', tmp)
                self.langStrings.append(langSet)


            count += 1




        
    def getLangStrings(self,line):
        
        if line.find("<string") == -1:
            return 'NULL'
        else:
            return line[line.find('"')+1:line.rfind('"')]



    def printLangString(self):
        for langItem in self.langStrings:
            print(f'Line {langItem.get("lineNo")} : {langItem.get("langString")}')


    def showCommonLangStrings(self, XmlLineDATA):
        pass



class LanguageX:
    langStrings = []
    def __init__(self,path):
        count = 1
        lang_file = Path(path)
        data = getFileLines(lang_file.read_text())
        for line in data:
            langSet = {
                "line": '',
                "lineNo": 0,
                "langString": ''
            }
            tmp = self.getLangStrings(line)
            if tmp != "NULL":
                langSet.__setitem__('line', line)
                langSet.__setitem__('lineNo', count)
                langSet.__setitem__('langString', tmp)
                self.langStrings.append(langSet)


            count += 1




        
    def getLangStrings(self,line):
        
        if line.find("<string") == -1:
            return 'NULL'
        else:
            return line[line.find('"')+1:line.rfind('"')]



    def printLangString(self):
        for langItem in self.langStrings:
            print(f'Line {langItem.get("lineNo")} : {langItem.get("langString")}')


    def showCommonLangStrings(self, XmlLineDATA):
        pass










