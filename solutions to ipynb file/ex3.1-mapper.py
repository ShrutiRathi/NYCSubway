#ex3.1
import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():
    
    keys = []

    for line in sys.stdin:
        data = line.split(',')
        if data[0] == "":
            keys = data
        else:
            data_point = dict(zip(keys,data))
            logging.info(str(data_point['UNIT']) + '\t' + str(data_point['ENTRIESn_hourly']))

mapper()
sys.stdin=open('turnstile_data_master_with_weather.csv')
sys.stdout=open('mapper_result.txt','w')
