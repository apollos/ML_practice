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

for taskIdx in range(0,1):
    xMat, yMatArray = myUtils.getMatfromList(trainDataList[taskIdx])
    xTMat, yTMatArray = myUtils.getMatfromList(testDataList[taskIdx])
    print "Start compute taskIdx %d:" % taskIdx

    for yIdx in range(0, 2): #caculate computing result and then communication result
        bestKList = []#we may meet sigular case while we predict, so we save 10 good k and try 10 times. [lowestError, bestK]
        invalidKNum = 0
        invalidKMin = inf
        invalidKMax = 0.009
        #aliveCount = 0
        for k in arange(30, 5, -0.01):##find best k  
        #for k in arange(27, 26, -2):##find best k  
        #    if aliveCount % 1000 == 0:
        #        print "I am alive!"
        #    aliveCount += 1
            yAssume = regression.lwlrTest(xTMat,xMat,yMatArray[yIdx].T,k)
            if yAssume.all() == 0:
                #print("%s  %d: regression.lwlr failed by k = %f." %(myDebug.file(), myDebug.line(), k))
                invalidKNum += 1
                if k > invalidKMax:
                    invalidKMax = k
                if k < invalidKMin:
                    invalidKMin = k
                continue
            rssE = regression.rssError(myUtils.transMat2List(yTMatArray[yIdx]), yAssume)
            if len(bestKList) == 0:
                bestKList.insert(0, [rssE, k])
            else:
                for idx in range(0, len(bestKList)):
                    if rssE < bestKList[idx][0]:
                        bestKList.insert(idx, [rssE, k])
                        if len(bestKList) > 10: #save 10 top k
                            bestKList.pop()
                        break
        print bestKList
        for kElement in bestKList:
            taskPredict = 0
            #get the result for cared data
            xCheckMat = mat([myUtils.getConstantValue(), 200, 180])
            wr = regression.lwlr(xCheckMat,xMat,yMatArray[yIdx].T,kElement[1])
            if (wr != None):
                #print wr
                taskPredict = xCheckMat * wr
                #print taskPredict
                print "Result is %f with k %f" % (taskPredict, kElement[1])
                break
        #taskPredict = regression.lwlrTest(xCheckMat,xMat,yCommMat.T,bestK)
        #print taskCoeff




