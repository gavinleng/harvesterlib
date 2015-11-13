__author__ = 'G'

import hashlib


def fpkey(data, keyCol):
    pkey = []
    for i in range(data.shape[0]):
        mystring = ''
        for j in keyCol:
            mystring += str(data[j][i])

        mystring = mystring.replace(" ", "").replace("-", "").lower()

        mymd5 = hashlib.md5(mystring.encode()).hexdigest()

        pkey.append(mymd5)

    return pkey
