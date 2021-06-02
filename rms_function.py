import numpy as np

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
