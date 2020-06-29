import json

fromBoolean = lambda x: x
fromNumber = lambda x: x
fromString = lambda x: x
fromArray = lambda x: x
fromObject = lambda x: x
jsonNone = None

stringify = json.dumps


def isArray(a):
    return type(a) == list


def _caseJson(isNone, isBool, isNum, isStr, isArr, isObj, j):
    if j == None:
        return isNone()
    elif type(j) == bool:
        return isBool(j)
    elif (type(j) == int) or (type(j) == float):
        return isNum(j)
    elif type(j) == str:
        return isStr(j)
    elif isArray(j):
        return isArr(j)
    else:
        return isObj(j)

def _compare(EQ, GT, LT, a, b):
    if a == None:
        if b == None:
            return EQ
        else:
            return LT
    elif type(a) == bool:
        if type(b) == bool:
            # boolean / boolean
            if a == b:
                return EQ
            elif a == False:
                return LT
            else:
                return GT
        elif b == None:
            return GT
        else:
            return LT
    elif (type(a) == int) or (type(a) == float):
        if (type(b) == int) or (type(b) == float):
            if a == b:
                return EQ
            elif a < b:
                return LT
            else:
                return GT
        elif b == None:
            return GT
        elif type(b) == bool:
            return GT
        else:
            return LT
    elif type(a) == str:
        if type(b) == str:
            if a == b:
                return EQ
            elif a < b:
                return LT
            else:
                return GT
        elif b == None:
            return GT
        elif type(b) == bool:
            return GT
        elif (type(b) == int) or (type(b) == float):
            return GT
        else:
            return LT
    elif isArray(a):
        if isArray(b):
            for i in range(min(len(a), len(b))):
                ca = _compare(EQ, GT, LT, a[i], b[i])
                if ca != EQ:
                    return ca
            if len(a) == len(b):
                return EQ
            elif len(a) < len(b):
                return LT
            else:
                return GT
        elif b == None:
            return GT
        elif type(b) == bool:
            return GT
        elif (type(b) == int) or (type(b) == float):
            return GT
        elif type(b) == str:
            return GT
        else:
            return LT
    else:
        if b == None:
            return GT
        elif type(b) == bool:
            return GT
        elif (type(b) == int) or (type(b) == float):
            return GT
        elif type(b) == str:
            return GT
        elif isArray(b):
            return GT
        else:
            akeys = a.keys()
            bkeys = b.keys()
            if akeys.length < bkeys.length:
                return LT
            elif akeys.length > bkeys.length:
                return GT
            keys = akeys.concat(bkeys).sort()
            for k in keys:
                if k not in a:
                    return LT
                elif k not in b:
                    return GT
                ck = _compare(EQ, GT, LT, a[k], b[k])
                if ck != EQ:
                    return ck
            return EQ

