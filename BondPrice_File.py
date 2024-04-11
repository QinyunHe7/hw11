def getBondPrice(y, face, couponRate, m, ppy=1):
    pvcfsum = 0
    cf = couponRate * face/ppy
    for i in range(1, m*ppy+1):
        pvf = (1 + y/ppy) ** -i
        pvcf = pvf * cf
        pvcfsum += pvcf
    pvcfsum += face * (1 + y/ppy) ** -(m * ppy)
    return pvcfsum
