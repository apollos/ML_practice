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
bestKList = [0.07, 0.3, 0.1, 0.7, 3, 10, 28, 40, 60, 80, 100]#[100, 80, 60, 40, 28, 10, 3, 0.7, 0.3, 0.07, 0.01]    
predictHourList = [6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 180, 200]
predictHours = predictHourList[0]
predictList = []
for tTSize in range(40, 440, 20):
    xCheckMat = mat([myUtils.getConstantValue(), tTSize, predictHours], dtype = float)
    preDictPerTask = []
    for taskIdx in range(0,2):
        xMat, yMat = myUtils.getXandYMatfromList(trainDataList[taskIdx])
        xMat = mat(xMat, dtype = float)
        #Regularize the matrix 
        xMean = mean(xMat[:, 1:], 0)
        xVar = var(xMat[:, 1:], 0)
        yMean = mean(yMat, 0)
        xMat[:, 1:] = (xMat[:, 1:] - xMean)/xVar #regression.regularize(xMat[:, 1:])
        yMat = yMat - mean(yMat, 0)
       
        xCheckMat[:, 1:] = (xCheckMat[:, 1:] - xMean)/xVar
        #print "Start compute taskIdx %d:" % (taskIdx)
        #print  xMean, xVar
        
        preDictPerComponent = []
        for yIdx in range(0, 2): #caculate computing result and then communication result
            yMatTmp = list(zip(*yMat)[yIdx])       
            
            taskPredict = 0
            for kElement in bestKList:
                taskPredict = 0
                #get the result for cared data
                #xCheckMat = mat([myUtils.getConstantValue(), 200, 10, 20, 180], dtype = float)            
                #print xCheckMat
                wr = regression.lwlr(xCheckMat, xMat,yMatTmp,kElement)
                if (wr != None):
                    #print wr
                    taskPredict = xCheckMat * wr + yMean[yIdx]
                    #print taskPredict
                    print "Task Size: %d, Predict Hours: %d Result[%d] is %f with k %f" % (tTSize, predictHours, yIdx, taskPredict, kElement)
                    #print wr
                    break                       
            if taskPredict != 0:
                preDictPerComponent.append(taskPredict)
            else:
                print "Error! Task Size: %d, Predict Hours: %d Task %d can not get predict value" % (tTSize, predictHours, yIdx)
        
        preDictPerTask.append(sum(preDictPerComponent))
    predictList.append([tTSize, max(preDictPerTask)])

print predictList
