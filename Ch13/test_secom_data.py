'''
Created on Jun 14, 2011

@author: Song Yu
'''
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import pca


def replaceNanWithMean():
    datMat = pca.loadDataSet('secom.data', ' ')
    numFeat = shape(datMat)[1]
    for i in range(numFeat):
        meanVal = mean(datMat[nonzero(~isnan(datMat[:,i].A))[0],i]) #values that are not NaN (a number)
        datMat[nonzero(isnan(datMat[:,i].A))[0],i] = meanVal  #set NaN values to mean
    return datMat


dataMat = replaceNanWithMean()

lowDDataMat, reconMat, total, varPercentage = pca.pca(dataMat, topNfeat=9999999)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(1, 51), varPercentage[:50], marker='^')
plt.xlabel('Principal Component Number')
plt.ylabel('Percentage of Variance')
plt.show()

