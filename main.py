import time
from core.engine import DropeeEngine
from utils.logger import log

def load_accounts(path="accounts/accounts.txt"):
    accounts = []
    try:
        with open(path, "r") as f:
            for line in f:
                token = line.strip()
                if token:
                    accounts.append(token)
    except FileNotFoundError:
        log("accounts/accounts.txt not found. Please add your tokens.", "error")
    return accounts

def main():
    log("Starting Dropee SN Design Automation Engine", "info")
    accounts = load_accounts()

    if not accounts:
        log("No accounts loaded. Exiting.", "error")
        return

    engine = DropeeEngine(accounts)

    while True:
        engine.run_cycle()
        log("Cycle complete. Sleeping...", "info")
        time.sleep(60)

if __name__ == "__main__":
    main()