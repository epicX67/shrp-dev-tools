def getVarStrings(line):
    if line.find('="') != -1 and line.find('value') != -1:
        line = line[0 : line.find('value')]
        string = line[line.find('="')+2 : line.rfind('"')]

    return string


def getFileVar(line):
    string = None
    if line.find('="') != -1 and line.find('filename') != -1:
        line = line[0 : line.find('filename')]
        string = line[line.find('="')+2 : line.rfind('"')]
        
    return string


def getVarFromCPP(line):
    string = None
    if "//" in line:
        return string
        
    if line.find('"') != -1 and line.rfind('"') != -1 and line.find('"') != line.rfind('"'):
        string = line[line.find('"')+1 : line.rfind('"')]
        
    return string


def getFontResourceVar(line):
    string = None
    if line.find('<font resource="') != -1:
        line = line[line.find('<font resource="') + len('<font resource="') :]
        string = line[0 : line.find('"')]
            
    return string


print(getFontResourceVar('<font resource="largeBold" color="%backgroundColor%"/>'))