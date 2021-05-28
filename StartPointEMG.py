import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from RMSDetect import RMSStartPoint
from plotTimeFrequencyDomain import plotTimeFrequencyDomain

filename = r'C:\Users\angus\Desktop\example.csv'
data = pd.read_csv(filename)
# print(data)
LRec = data.iloc[1]     #dataFrame
LRec = np.array(data)  # array to calculate
rangeData = LRec[:1000]
# print(len(rangeData))
# print(rangeData)
# plt.figure()
# plt.plot(rangeData)
# plt.show()
RMSStartPoint(LRec, 25)

# beforeMedianFrequency = plotTimeFrequencyDomain(LRec)
