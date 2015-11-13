__author__ = 'G'

import pandas as pd

import now
import openurl
import datasave as dsave

def download(url, outPath, keyCol, digitCheckCol, noDigitRemoveFields, logfile, errfile):
    dName = outPath

    # open url
    socket = openurl.openurl(url, logfile, errfile)

    # load this csv file
    logfile.write(str(now.now()) + ' csv file loading\n')
    print('csv file loading------')
    df = pd.read_csv(socket, dtype='unicode')
    col = df.columns.tolist()

    # save csv file
    dsave.save(df, col, keyCol, digitCheckCol, noDigitRemoveFields, dName, logfile)
