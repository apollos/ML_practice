import os
import os.path

def listAllFiles(fullPath):

    fullPath=fullPath.strip()
    if fullPath[-1] != '/':
        fullPath += '/'
    fileList = []
    try:
        for parentPath,dirNames,fileNames in os.walk(fullPath):

            for dirName in dirNames:
                fileList.extend(listAllFiles(fullPath+dirName))
            for fileName in fileNames:
                fileList.insert(len(fileList), fullPath+fileName)

    except IOError as err:
        print("IO Error: "+str(err))
    
    return fileList



