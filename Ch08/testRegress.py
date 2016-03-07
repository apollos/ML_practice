import regression
from numpy import *
import matplotlib.pyplot as plt

#xArr, yArr = regression.loadDataSet('ex0.txt')

xArr, yArr = regression.loadDataSet('abalone.txt')
'''
ws = regression.standRegres(xArr, yArr)
xMat = mat(xArr)
yMat = mat(yArr)
yHat = xMat*ws
'''
#Retry by lwlr to get best k

corrcoefMin=100
bestK=1
keysets = [0.1,1,10,0.02,0.3]

for step in keysets:   
    print(step) 
    yHat = regression.lwlrTest(xArr[4000:],xArr[0:4000],yArr[0:4000],step)
    if(sum(yHat) != 0):
        if(corrcoefMin >= linalg.det(corrcoef(yHat.T, yArr[4000:]))):
            corrcoefMin = linalg.det(corrcoef(yHat.T, yArr[4000:]))
            bestK=step
        print(regression.rssError(yArr[4000:], yHat.T))
print("=======================")
print(bestK)
print(corrcoefMin)

'''
fig = plt.figure()
ax = fig.add_subplot(111)

ax.scatter(xMat[:,1], yMat.T[:,0])

xCopy = xMat.copy()
xCopy.sort(0)
yHat = xCopy*ws
ax.plot(xCopy[:, 1], yHat)
plt.show()
'''
