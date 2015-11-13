__author__ = 'G'

import sys
import urllib

import now


def openurl(url, logfile, errfile):
    try:
        socket = urllib.request.urlopen(url)
        logfile.write(str(now.now()) + ' open url\n')
        print('open url------')
    except urllib.error.HTTPError as e:
        errfile.write(str(now.now()) + ' file download HTTPError is ' + str(e.code) + ' . End progress\n')
        logfile.write(str(now.now()) + ' error and end progress\n')
        sys.exit('file download HTTPError = ' + str(e.code))
    except urllib.error.URLError as e:
        errfile.write(str(now.now()) + ' file download URLError is ' + str(e.args) + ' . End progress\n')
        logfile.write(str(now.now()) + ' error and end progress\n')
        sys.exit('file download URLError = ' + str(e.args))
    except Exception:
        print('file download error')
        import traceback
        errfile.write(str(now.now()) + ' generic exception: ' + str(traceback.format_exc()) + ' . End progress\n')
        logfile.write(str(now.now()) + ' error and end progress\n')
        sys.exit('generic exception: ' + traceback.format_exc())

    return socket
