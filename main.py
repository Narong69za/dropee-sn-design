# ==========================================================
# PROJECT : DROPEE SN DESIGN
# MODULE  : main.py
# VERSION : 1.1.0
# AUTHOR  : SN DESIGN STUDIO
# PURPOSE : Entry point for Dropee Automation Engine
# PLATFORM: Termux / Linux
#
# DESCRIPTION
# Main execution file responsible for:
# - displaying system banner
# - loading accounts
# - initializing DropeeEngine
# - running continuous farming cycles
#
# CHANGELOG
# v1.1.0
# - Added startup banner support (utils/banner.py)
# - Added standardized SN DESIGN header format
# - Improved startup logging structure
#
# ==========================================================

import time

from core.engine import DropeeEngine
from utils.logger import log
from utils.banner import show_banner
from utils.token_parser import parse_token


def load_accounts():

    accounts = []

    with open("accounts/accounts.txt") as f:

        for line in f:

            token = line.strip()

            if not token:
                continue

            account = parse_token(token)

            accounts.append(account)

    return accounts


def main():

    show_banner()

    log("Loading accounts...")

    accounts = load_accounts()

    log(f"Loaded {len(accounts)} account(s)")

    engine = DropeeEngine(accounts)

    engine.run()


if __name__ == "__main__":
    main()
