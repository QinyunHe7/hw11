def getBondPrice_Z(face, couponRate, times, yc):
    pvfsum = 0
    cf = couponRate * face
    for t, i in zip(times, yc):
        pvf = (1 + i) ** - t
        pvfsum += pvf
    pvcfsum = pvfsum * cf + face * (1 + yc[-1]) ** -times[-1]
    return(pvcfsum)