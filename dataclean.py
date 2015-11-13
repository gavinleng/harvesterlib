__author__ = 'G'

import datavalid as dvalid
import now


def strip(data, col):
    for i in col:
        data[i] = [str(x).lstrip().rstrip() for x in data[i]]

    return data


def stripcsv(data, col):
    for i in col:
        data[i] = data[i].map(lambda x: str(x).lstrip().rstrip())

    return data


def nodigit(data, check_field, remove_field, logfile):
    if len(check_field) > 0:
        # check the no digit data
        logfile.write(str(now.now()) + ' check the no digit data\n')
        print('check the no digit data')
        inrow = dvalid.checkdigit(data, check_field, logfile)

        # drop the no digit data
        remove_inrow = []
        for i in remove_field:
            remove_inrow += inrow[i]

        remove_inrow = list(set(remove_inrow))

        if len(remove_inrow) > 0:
            data = data.drop(data.index[remove_inrow])
            droppedRow = ','.join(str(x+2) for x in remove_inrow)
            print('------------------------------------')
            logfile.write(str(now.now()) + ' the dropped rows are: row ' + droppedRow + '\n')
            print('the dropped rows are: row ' + droppedRow)

    return data
