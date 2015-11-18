__author__ = 'G'

import now


def checkdigit(data, field, logfile):
    inrow = {}
    for j in field:
        inrow[j] = []

    for j in field:
        for i in data.index.tolist():
            if str(data[j][i]).strip().isdigit() != True:
                cData = str(data[j][i]).strip().split('.')
                if not ((len(cData) == 2)and(cData[0].isdigit())and(cData[1].isdigit())):
                    inrow[j].append(i)
                    print('------------------------------------')
                    logfile.write(str(now.now()) + ' the value is not a digit number at: row ' + str(i+2) + ', col ' + j + '\n')
                    print('the value is not a digit number at: row ' + str(i+2) + ', col ' + j)

    return inrow
