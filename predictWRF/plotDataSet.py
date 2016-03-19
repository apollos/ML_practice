from __future__ import division
import shapeFile as sF
import matplotlib  
import matplotlib.pyplot as plt
import numpy as np

files = sF.listAllFiles("/home/yu/workspace/Data/sameCompute/")
trainDataList = sF.shapeWrfComputingfile(files)

#trainDataList[0] - task 0 info
#trainDataList[1] - other task info
#trainDataList structure [task size, computing size, computing time, communication time]

xAx = []
yAx = []
cAx = []
color = ['g', 'r', 'b', 'y', 'c', 'k', 'g', 'r', 'b', 'y', 'c', 'k', 'g', 'r', 'b', 'y', 'c', 'k', 'g', 'r', 'b', 'y', 'c', 'k', 'g', 'r', 'b', 'y', 'c', 'k', 'g']
for DataSet in trainDataList:
    for DataInf in DataSet:        
        tmpX = DataInf[0]
        tmpX2 = DataInf[1]
        tmpY1 = DataInf[2]
        tmpY2 = DataInf[3]
        xAx.append(tmpX)
        yAx.append((tmpY1, tmpY2))
        cAx.append(color[tmpX2%len(color)])

minX = min(xAx)
xAx = np.array(xAx, dtype = float)/float(minX)
yAx = np.array(yAx, dtype = float)/float(500)

fig = plt.figure(0, figsize=(16,12))
fig.suptitle("Same Computing Hours")   

subplots = range(0, 4)
subplots[0] = plt.subplot(2,2,1)
plt.ylabel('Consumed Time(s)')
plt.xlabel('Task Num')
plt.title('Computing Trend')

subplots[0].scatter(xAx, yAx[:,0],c=cAx, s=25,alpha=0.4,marker='o')


subplots[1] = plt.subplot(2,2,2)
plt.ylabel('Consumed Time(s)')
plt.xlabel('Task Num')
plt.title('Communication Trend')
subplots[1].scatter(xAx, yAx[:,1],c=cAx, s=25,alpha=0.4,marker='o')
print 
predictRst = [[40, 2616.4746303365951], [60, 2352.4019628965975], [80, 2097.0211084258826], [100, 1850.0306293020044], [120, 1822.132462672354], [140, 1821.9692164020839], [160, 1821.8059760415217], [180, 1821.6427415894918], [200, 1821.479513046138], [220, 1821.316290411321], [240, 1821.1530736846419], [260, 1820.9898628657993], [280, 1820.826657955105], [300, 1820.6634589515224], [320, 1820.5002658554693], [340, 1820.337078666309], [360, 1820.173897384333], [380, 1820.0107220086938], [400, 1819.847552539854], [420, 1819.6843889768086]]

subplots[2] = plt.subplot(2,2,3)
plt.ylabel('Consumed Time(s)')
plt.xlabel('Task Num')
plt.title('Total Time Trend')
subplots[2].scatter(xAx, yAx[:, 0]+yAx[:, 1],c=cAx, s=25,alpha=0.4,marker='o')
predictMat = np.array(predictRst, dtype = float)
xAx = predictMat[:, 0]/float(minX)
yAx = predictMat[:, 1]/float(500)
subplots[2].scatter(xAx, yAx, c='r',s=25,marker='o')

'''
###################################################3
files = sF.listAllFiles("/home/yu/workspace/Data/sameTask/")
trainDataList = sF.shapeWrfComputingfile(files)

xAx = []
yAx = []
cAx = []

for DataSet in trainDataList:
    for DataInf in DataSet:        
        tmpX = DataInf[1]
        tmpY1 = DataInf[2]
        tmpY2 = DataInf[3]
        tmpX2 = DataInf[0]
        xAx.append(tmpX)
        yAx.append((tmpY1, tmpY2))
        cAx.append(color[tmpX2%len(color)])

minX = min(xAx)
xAx = np.array(xAx, dtype = float)/float(minX)
yAx = np.array(yAx, dtype = float)/float(500)

fig = plt.figure(1, figsize=(16,12))
fig.suptitle("Same Task Size")   

subplots = range(0, 2)
subplots[0] = plt.subplot(1,2,1)
plt.ylabel('Consumed Time(500s)')
plt.xlabel('Compute Data Size')
plt.title('Computing Trend')

subplots[0].scatter(xAx, yAx[:,0],s=25,alpha=0.4,marker='o', c=cAx)


subplots[1] = plt.subplot(1,2,2)
plt.ylabel('Consumed Time(500s)')
plt.xlabel('Task Num')
plt.title('Communication Trend')
subplots[1].scatter(xAx, yAx[:,1],s=25,alpha=0.4,marker='o', c=cAx)
'''
plt.show()

