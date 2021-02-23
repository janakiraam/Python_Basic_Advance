import logging

logging.basicConfig(filename= "Logging.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')

for i in range(0,15):
    if(i%2==0):
        logging.warning('Logging warning message')
    if(i%3==0):
        logging.critical('Logging critical message')
    else:
        logging.error('Logging error message')