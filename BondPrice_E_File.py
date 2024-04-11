def getBondPrice_E(face, couponRate, m, yc):
    bondPrice = 0
    for t, rate in enumerate(yc, start=1):
        if t == m:
            couponPayment = face * couponRate
            bondPrice += couponPayment / ((1 + rate) ** t)
            bondPrice += face / ((1 + rate) ** t)
        else:
            couponPayment = face * couponRate
            bondPrice += couponPayment / ((1 + rate) ** t)
    return bondPrice

