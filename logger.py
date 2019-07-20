#coding:utf-8
#########################################################################
# File Name: logger.py
# Author: kangshaoshun
# mail: kangshaoshun@rong360.com
# Created Time: Fri 30 Nov 2018 06:44:33 PM CST
#########################################################################
import sys
import logging
reload(sys)
sys.setdefaultencoding('utf-8')

def get_logger(logger_name, log_file, level=logging.INFO):
	formatter = logging.Formatter('%(asctime)s : %(message)s', "%Y-%m-%d %H:%M:%S")
	fileHandler = logging.FileHandler(log_file, mode='a')
	fileHandler.setFormatter(formatter)
	vlog = logging.getLogger(logger_name)
	vlog.setLevel(level)
	vlog.addHandler(fileHandler)
	return vlog
						
						
if __name__ == '__main__':
	log_file1='logger_test1.log'
	logger1 = get_logger(__name__, log_file1)
	logger1.info('>>> test1 log msg: %s', "111111111111111111111")
