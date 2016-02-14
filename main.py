#!/opt/pro/python279/bin/python2.7
#encoding = utf-8

import time, log_helper, sys

dir = sys.path[0]

global __log__path, iphone
__log__path = "%s/createfile.log" %(dir)

iphone = "15721282565,18917637631"

def message(mobile,mes):
    mobiles = mobile.split(',')
    for m in mobiles:
    	sms_alarm(m,mes)
    	time.sleep(5)

def logger(mes):
    log_helper.get_logger(__log__path).info(mes)


def create_file(path, size):
    file = open(path, 'w')
    file.seek(1024*size)
    file.write('\x00')
    file.close()

if __name__ == "__main__":
    a = 0
    while 1:
        time_start = time.time()
        file_dir = '/data/NLTPStore/tvmCloud/live2/ts/iotest/'
        file_name = file_dir+"file"+str(int(time.time()))
        create_file(file_name, 500)
        time_end = time.time()
        elapsedtime = time_end - time_start
        print elapsedtime
        logger("%s-%fs" %(file_name, elapsedtime))
        if elapsedtime > 1.5:
            a+=1 
        if a>60:
            mes = "A total of 100 files time generate 60s" 
            message(iphone, mes)
            a = 0
        time.sleep(1)
