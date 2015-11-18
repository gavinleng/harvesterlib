__author__ = 'G'

import pandas as pd

import now
import fpkey
import dataclean as dclean


def save(raw_data, col, keyCol, digitCheckCol, noDigitRemoveFields, dName, logfile):
    # write csv file
    logfile.write(str(now.now()) + ' writing to file\n')
    print('writing to file ' + dName)
    df = pd.DataFrame(raw_data, columns=col)
    df.columns = [x.title() for x in col]
    col = df.columns.tolist()

    # clean data--remove spaces
    logfile.write(str(now.now()) + ' data cleaning\n')
    print('data cleaning------')
    df = dclean.stripcsv(df, col)

    # remove the cell with no digit data
    check_field = [x.title() for x in digitCheckCol]
    remove_field = [x.title() for x in noDigitRemoveFields]
    df = dclean.nodigit(df, check_field, remove_field, logfile)

    # delete the duplicate data
    logfile.write(str(now.now()) + ' check and delete the duplicate data\n')
    print('check and delete the duplicate data------')
    df = df.drop_duplicates(col, take_last=True)

    # create primary key by md5 for each row
    logfile.write(str(now.now()) + ' create primary key\n')
    print('create primary key------')
    col += ['pkey']
    keyCol = [x.title() for x in keyCol]
    df[col[-1]] = fpkey.fpkey(df, keyCol)
    logfile.write(str(now.now()) + ' create primary key end\n')
    print('create primary key end------')

    # save to file
    df.to_csv(dName, index=False)
    logfile.write(str(now.now()) + ' has been extracted and saved as ' + str(dName) + '\n')
    print('Requested data has been extracted and saved as ' + dName)
    logfile.write(str(now.now()) + ' finished\n')
    print("finished")
