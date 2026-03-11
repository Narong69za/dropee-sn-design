from colorama import Fore, Style, init
init(autoreset=True)

def log(message, level="info"):
    if level == "info":
        print(Fore.CYAN + "[INFO] " + message)
    elif level == "success":
        print(Fore.GREEN + "[SUCCESS] " + message)
    elif level == "warning":
        print(Fore.YELLOW + "[WARNING] " + message)
    elif level == "error":
        print(Fore.RED + "[ERROR] " + message)
    else:
        print(message)