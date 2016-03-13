from __future__ import division
import shapeFile as sF
import random
import numpy as np
import math
import matplotlib.pyplot as plt
import writeTrainingResult as wTR


files = sF.listAllFiles("/home/yu/workspace/Data/train")
ComputeDict = sF.shapeWrfComputingfile(files)

