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

subplots = range(0, 2)
subplots[0] = plt.subplot(1,2,1)
plt.ylabel('Consumed Time(s)')
plt.xlabel('Task Num')
plt.title('Computing Trend')

subplots[0].scatter(xAx, yAx[:,0],c=cAx, s=25,alpha=0.4,marker='o')


subplots[1] = plt.subplot(1,2,2)
plt.ylabel('Consumed Time(s)')
plt.xlabel('Task Num')
plt.title('Communication Trend')
subplots[1].scatter(xAx, yAx[:,1],c=cAx, s=25,alpha=0.4,marker='o')

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

plt.show()

