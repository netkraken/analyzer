def myAssertDictEqual(a, b):
    dictAInB(a, b)
    dictAInB(b, a)

def dictAInB(a, b):
    for akey, avalue in a.items():
        bvalue = b.get(akey)
        if akey in b:
            if avalue == bvalue:
                continue
        raise Exception("%s[%s] != [%s]" % (akey, avalue, bvalue))
