import datetime

class Color:
    RED            = '\033[31m'
    GREEN          = '\033[32m'
    YELLOW         = '\033[33m'
    BLUE           = '\033[34m'
    MAGENTA        = '\033[35m'
    CYAN           = '\033[36m'
    RESET          = '\033[0m'

class Log:
    def Info(str):
        print(f"{Color.BLUE}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}] [INFO] {str}{Color.RESET}")

    def Warn(str):
        print(f"{Color.YELLOW}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}] [WARN] {str}{Color.RESET}")

    def Error(str):
        print(f"{Color.RED}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}] [ERROR] {str}{Color.RESET}")

    def Debug(str, mode):
        if mode == True:
            print(f"{Color.CYAN}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}] [DEBUG] {str}{Color.RESET}")