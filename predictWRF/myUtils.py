import numpy as np

constantValue = 1.23
def getConstantValue():
    return constantValue

def getMatfromList(infoList):
    m = len(infoList)
    n = len(infoList[0])

    taskMat = np.mat(infoList)

    #generate a matrix
    #first is constant, and set to 1??
    xMat = np.ones((m, n-2+1)) #
    xMat[:, 0] = constantValue
    xMat[:,1:n-2+1] = taskMat[:, 0:2]
    yCompMat = taskMat[:, 2]
    yCommMat = taskMat[:, 3]
    return xMat, (yCompMat, yCommMat)

def transMat2List(matV):
    listV = list(np.array(matV).reshape(-1,))
    return listV
    #return [s for i in listV for s in i]
    
