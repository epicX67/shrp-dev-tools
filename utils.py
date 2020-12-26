def extractFileName(path):
        return path[path.rfind('\\') + 1:]

def removeDublicate(list):
    flag = True
    while flag:
        flag = False
        for item in list:
            if list.count(item) > 1 :
                list.remove(item)
                flag = True
                break
    
    return list


def getFileLines(data):
    return data.split('\n')
    