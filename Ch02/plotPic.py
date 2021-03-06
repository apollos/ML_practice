#plot the picture

import kNN
import matplotlib
import matplotlib.pyplot as plt
from array import *
from numpy import *

datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15*array(datingLabels),15*array(datingLabels))
plt.show()
