__author__ = 'G'

import pandas as pd

import openurl
import now
import naturalkeys as nkeys


def getapi(date, colFields, logfile, errfile):
    url = "https://www.nomisweb.co.uk/api/v01/dataset/NM_18_1.data.csv?date=latest&select=date"
    minusDate = []

    # open url
    socket = openurl.openurl(url, logfile, errfile)

    # load this csv file
    df = pd.read_csv(socket, dtype='unicode')

    # get the latest date
    latestDate = df.iloc[0, 0].split('-')
    logfile.write(str(now.now()) + ' get the latest date\n')
    print('get the latest date------')

    # get the required date string
    for i in date:
        if i.lower() == "latest":
            minusDate.append('latest')
            continue

        nYear = int(latestDate[0]) - int(i.split('-')[0])
        nMonth = int(latestDate[1]) - int(i.split('-')[1])

        if nYear == 0:
            nDate = nMonth
            if nDate == 0:
                minusDate.append('latest')
            else:
                minusDate.append('latestMINUS' + str(nDate))
        else:
            nDate = nMonth + 12 * nYear
            minusDate.append('latestMINUS' + str(nDate))
    minusDate = list(set(minusDate))
    minusDate.sort(key=nkeys.natural_keys)
    dateString = ','.join(minusDate)

    # get the required selection string
    colFields = [x.lower() for x in colFields]
    colSelect = ','.join(colFields)

    # get the required API
    urlBase = 'https://www.nomisweb.co.uk/api/v01/dataset/'
    urlAPI = urlBase + 'NM_18_1.data.csv?'
    urlAPI += 'geography=1946157199...1946157245&'
    urlAPI += 'date=' + dateString + '&'
    urlAPI += 'age=MAKE|Aged%2016-24|1;2&duration=MAKE|Up%20to%206%20months|1...7,MAKE|Over%206%20months%20and%20up%20to%20a%20year|8;9,MAKE|Over%201%20year|10...16&sex=5,6&measures=20100,20206'
    urlAPI += '&select=' + colSelect

    return urlAPI
