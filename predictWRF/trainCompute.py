from __future__ import division
import shapeFile as sF
import random
from numpy import *
import math
import matplotlib.pyplot as plt
import writeTrainingResult as wTR
import regression 
import os.path
import myUtils
import myDebug

files = sF.listAllFiles("/home/yu/workspace/Data/train")
trainDataList = sF.shapeWrfComputingfile(files)
if not trainDataList:
    print("%s  %d: Get profiling information from %s failed." %(myDebug.file(), myDebug.line(), files))
    exit(1)
#Get test data, we need check together
files = sF.listAllFiles("/home/yu/workspace/Data/test")
testDataList = sF.shapeWrfComputingfile(files)
if not testDataList:
    print("%s  %d: Get profiling information from %s failed." %(myDebug.file(), myDebug.line(), testFile))
    exit(1)
#for i in range(0,2):#0 for task 0 and 1 for other tasks
#The list is sperated to two part, [0] save all task 0 job information, task 1 save all other tasks
#generate traing dataset
#task 0 first
'''
print "%d, %d, %d" % (len(trainDataList), len(trainDataList[0]), len(trainDataList[1]))
print trainDataList
print "==========================="
print "%d, %d, %d" % (len(testDataList), len(testDataList[0]), len(testDataList[1]))
print testDataList
exit(1)
'''
xCheckMat = mat([myUtils.getConstantValue(), 400, 180], dtype = float)
for taskIdx in range(0,2):
    xMat, yMat = myUtils.getXandYMatfromList(trainDataList[taskIdx])
    xTMat, yTMat = myUtils.getXandYMatfromList(testDataList[taskIdx])
    xMat = mat(xMat, dtype = float)
    xTMat = mat(xTMat, dtype = float)
    #Regularize the matrix 
    xMean = mean(xMat[:, 1:], 0)
    xVar = var(xMat[:, 1:], 0)
    yMean = mean(yMat, 0)
    xMat[:, 1:] = (xMat[:, 1:] - xMean)/xVar #regression.regularize(xMat[:, 1:])
    xTMat[:, 1:] = (xTMat[:, 1:] - xMean)/xVar #regression.regularize(xTMat[:, 1:])
    yMat = yMat - mean(yMat, 0)
    yTMat = yTMat - mean(yMat, 0)    #note, the mean shall be yMat but not yTMat
    potentialK = [0.07, 0.3, 0.1, 0.7, 3, 10, 28, 40, 60, 80, 100]#[100, 80, 60, 40, 28, 10, 3, 0.7, 0.3, 0.07, 0.01]

    
    xCheckMat[:, 1:] = (xCheckMat[:, 1:] - xMean)/xVar

    print "Start compute taskIdx %d:" % taskIdx
    
    for yIdx in range(0, 2): #caculate computing result and then communication result
        bestKList = []#we may meet sigular case while we predict, so we save 10 good k and try 10 times. [lowestError, bestK]
        invalidKNum = 0
        invalidKMin = inf
        invalidKMax = 0.009
        #aliveCount = 0
        yMatTmp = list(zip(*yMat)[yIdx])
        yTMatTmp = list(zip(*yTMat)[yIdx])
        
        #for k in arange(10, 0.0009, -0.001):##find best k  
        for k in potentialK:##find best k  
        #    if aliveCount % 1000 == 0:
        #        print "I am alive!"
        #    aliveCount += 1
            
            yAssume = regression.lwlrTest(xTMat,xMat,yMatTmp,k)
            #print yAssume, yMean[yIdx], yTMatTmp
            yAssume += yMean[yIdx]
            if yAssume.all() == 0:
                #print("%s  %d: regression.lwlr failed by k = %f." %(myDebug.file(), myDebug.line(), k))
                invalidKNum += 1
                if k > invalidKMax:
                    invalidKMax = k
                if k < invalidKMin:
                    invalidKMin = k
                continue            
            rssE = regression.rssError(yTMatTmp, yAssume)

            if len(bestKList) == 0:
                bestKList.insert(0, [rssE, k])
            else:
                for idx in range(0, len(bestKList)):
                    if rssE < bestKList[idx][0]:
                        bestKList.insert(idx, [rssE, k])
                        if len(bestKList) > 50: #save 50 top k
                            bestKList.pop()
                        break
        print bestKList
        '''
        for kElement in bestKList:
            taskPredict = 0
            #get the result for cared data
            #xCheckMat = mat([myUtils.getConstantValue(), 200, 10, 20, 180], dtype = float)            
            #print xCheckMat
            wr = regression.lwlr(xCheckMat, xMat,yMatTmp,kElement[1])
            if (wr != None):
                #print wr
                taskPredict = xCheckMat * wr + yMean[yIdx]
                #print taskPredict
                print "Result[%d] is %f with k %f" % (yIdx, taskPredict, kElement[1])
                print wr
                break                       
        '''




