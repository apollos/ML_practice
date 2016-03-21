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

n = np.shape(trainDataList[0])[1]
for DataSet in trainDataList:
    for DataInf in DataSet:        
        tmpX = DataInf[0]
        tmpX2 = DataInf[n - 3]
        tmpY1 = DataInf[n - 2]
        tmpY2 = DataInf[n - 1]
        xAx.append(tmpX)
        yAx.append((tmpY1, tmpY2))
        cAx.append(color[tmpX2%len(color)])

minX = min(xAx)
xAx = np.array(xAx, dtype = float)/float(minX)
yAx = np.array(yAx, dtype = float)

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

predictRst = [[40, 2597.830278286669, 425.45709459592126], [60, 1956.9806100969738, 341.41863967466986], [80, 1769.6031552438997, 334.3584049290738], [100, 1582.774764434862, 327.34261468424233], [120, 1290.7981749303044, 282.628799805835], [140, 999.5067647049106, 238.04967842889587], [160, 708.9170008359923, 193.60826488923186], [180, 898.7342293851916, 241.1769292665435], [200, 129.90770186170653, 105.15053170104943], [220, 261.1569766623129, 133.05092390127527], [240, 912.8140551215411, 269.8884150851281], [260, 509.71787214750884, 186.87912904652597], [280, 627.1076172235653, 212.81790610168346], [300, 739.9572485347107, 238.1139978468075], [320, 848.3080692558149, 262.7731971310951], [340, 952.2020846857124, 286.80139472716013], [360, 1051.6819007782506, 310.2045655533328], [380, 1146.7906269160803, 332.9887554770869], [400, 1237.5717829640048, 355.1600687045989], [420, 1271.243628017301, 357.89932621247453]]

predictRst = [[40, 2333.956685510723, 570.7974205790968], [60, 1809.1211228086306, 504.27526689152637], [80, 1625.5404857575522, 512.027589411613], [100, 1444.8124203778111, 520.1912816989559], [120, 1170.3601137067537, 465.28176101430324], [140, 897.0131174695352, 410.59331949101306], [160, 624.7982425799344, 356.131728337879], [180, 708.9582063223186, 401.5606281447811], [200, 83.87267851721117, 247.91227056725714], [220, 113.73742403203664, 260.4098951678974], [240, 533.1284708518649, 401.8947514411697], [260, 157.19421795949108, 282.5000920282916], [280, 171.01581952393428, 292.1338430210797], [300, 179.71248779211953, 300.85295307842244], [320, 183.38887469629833, 308.67622867904834], [340, 182.14564501954442, 315.62177866329114], [360, 176.07953423639287, 321.70702656673103], [380, 165.28341853757308, 326.948724893198], [400, 149.84639538098293, 331.36297104588044], [420, 80.77065676078985, 302.85937230793695]]


subplots[2] = plt.subplot(2,2,3)
plt.ylabel('Consumed Time(s)')
plt.xlabel('Task Num')
plt.title('Total Time Trend')
subplots[2].scatter(xAx, yAx[:, 0]+yAx[:, 1],c=cAx, s=25,alpha=0.4,marker='o')
predictMat = np.array(predictRst, dtype = float)

xAx = predictMat[:, 0]/float(minX)
'''
yAx = predictMat[:, 1]
subplots[2].scatter(xAx, yAx, c='r',s=25,marker='o')
'''
yAx1 = predictMat[:, 1]
yAx2 = predictMat[:, 2]
yAx3 = yAx1+yAx2
'''
subplots[0].scatter(xAx, yAx1, c='r',s=25,marker='o')
subplots[1].scatter(xAx, yAx2, c='r',s=25,marker='o')
subplots[2].scatter(xAx, yAx3, c='r',s=25,marker='o')
'''
subplots[0].plot(xAx, yAx1, c='r')
subplots[1].plot(xAx, yAx2, c='r')
subplots[2].plot(xAx, yAx3, c='r')

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

