#ex3.2
import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    register = {}
    for line in sys.stdin:
        data = line.split('\t')
        if len(data) != 2:
            continue
        else:
            unit, entries = data[0], data[1]
            if unit in register:
                register[unit] += float(entries)
            else:
                register[unit] = float(entries)

    for key in register:
        msg = str(key) + '\t' + str(register[key])
        logging.info(msg)
        print msg

    

reducer()
