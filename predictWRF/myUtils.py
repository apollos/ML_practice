import numpy as np

constantValue = 1.23
def getConstantValue():
    return constantValue

def getXandYMatfromList(infoList):
    m = len(infoList)
    n = len(infoList[0])

    taskMat = np.mat(infoList)

    #generate a X matrix and first feature is constant, and set to constantValue
    xMat = np.ones((m, n-2+1)) #
    xMat[:, 0] = constantValue
    xMat[:,1:n-2+1] = taskMat[:, 0:n-2]
    yMat = taskMat[:, n-2:n]
    return xMat, yMat
