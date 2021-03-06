import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def RMSStartPoint(data, mask):
    def rms_function(data, window):
        rms = np.array(data)

        halfMask = round(window)
        for index in range(len(data)):
            # lower upper setting
            if index < halfMask:
                lower = 1
            else:
                lower = index - halfMask

            if index > len(data) - halfMask:
                upper = len(data)
            else:
                upper = index + halfMask

            current = data[lower:upper]
            power2 = current * current
            mean = power2.mean()
            sqrt = np.sqrt(mean)
            rms[index] = sqrt

        return rms


    threshold_start = 250
    threshold_end = 200
    getStart = False
    rms = rms_function(data, mask)

    data = np.array(data)
    mask = float(mask)
    plt.figure(1)
    plt.plot(data)
    plt.plot(rms, '--')
    plt.title('Raw Data && RMS Line && Start Point', fontsize=15, color='Black')


    # plt.figure(data)
    # plt.show()
    # Threshold setting start
    start = 0
    for index in range(len(data)):
        if rms[index] < threshold_start and getStart == False:
            start = start + 1
        else:
            getStart = True
            break
    # Threshold setting end
    end = start
    for index in range(start, len(data)):
        if rms[index] > threshold_end:
            end = end + 1
        else:
            break

    ##duration times
    # timer_start = float(start) / 2000
    # timer_end = float(end)/2000
    # duration = timer_end - timer_start
    # print(start) # startPointIndex
    plt.plot(start, rms[start], marker="o", color="black")
    plt.plot(end, rms[end], marker="o", color="RED")
    # plt.hlines(rms[start], start-1000, start, colors="r", linestyles='solid')
    # plt.text(end, rms[end] + 600, "start point time = " + str(round(timer_start, 4)) + "(s)")
    # plt.text(end, rms[end] + 400, "end point time = " + str(round(timer_end, 4)) + "(s)")
    # plt.text(end, rms[end] + 300, "muscle duration = " + str(round(duration, 4)) + "(s)")
    plt.grid(True)
    plt.show()

##test function 20210111
# if __name__ == '__main__':
#     path = r"C:\Users\angus\Desktop\Python\GUIFunction\swingtest1.csv"
#     data = pd.read_csv(path,
#                        skiprows=3,
#                        usecols=[3])
#     RMSStartPoint(data, 25)