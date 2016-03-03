__author__ = 'G'

import pandas as pd

import sys
sys.path.append('../harvesterlib')

import now
import dataclean as dclean


def save(raw_data, col, keyCol, digitCheckCol, noDigitRemoveFields, dName, logfile):
    # write file
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

    # create json data
    jsonData = []
    pkeyArray = df[keyCol[0].title()].drop_duplicates().tolist()
    #print(len(pkeyArray))
    for ikey in pkeyArray:
        dfSingle = df.loc[df[keyCol[0].title()] == ikey]
        stringSingle = dfSingle.to_json(orient="records")
        stringSingle = '{"pkey":"' + keyCol[1] + ikey + '","data":' + stringSingle + '}'
        jsonData.append(stringSingle)

    stringSingle = ','.join(jsonData)
    jsonString = '[{"jsondata":[' + stringSingle + ']}]'

    myJson = pd.read_json(jsonString)
    myJson.index = ['mydata']

    # save to file
    myJson.to_json(path_or_buf=dName, orient="index")
    logfile.write(str(now.now()) + ' has been extracted and saved as ' + str(dName) + '\n')
    print('Requested data has been extracted and saved as ' + dName)
    logfile.write(str(now.now()) + ' finished\n')
    print("finished")
