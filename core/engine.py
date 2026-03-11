# =====================================================
# PROJECT : DROPEE SN DESIGN
# MODULE  : core/engine.py
# VERSION : 1.1.1
# AUTHOR  : SN DESIGN STUDIO
# UPDATED : 2026-03-11
# PURPOSE : Main automation engine for Dropee bot
# CHANGELOG:
# 1.1.1 - Improve logging and account handling
# =====================================================

import time
from modules.tasks import run_tasks
from modules.reward import collect_rewards
from modules.tap import tap_action
from utils.logger import log


class DropeeEngine:

    def __init__(self, accounts):
        self.accounts = accounts


    def run_cycle(self):

        for token in self.accounts:

            try:

                account_preview = str(token)[:12]

                log(f"Processing account: {account_preview}...", "info")

                log("Running tasks...", "info")
                run_tasks(token)

                log("Executing tap action...", "info")
                tap_action(token)

                log("Collecting rewards...", "info")
                collect_rewards(token)

                time.sleep(3)

            except Exception as e:

                log(f"Error processing account: {e}", "error")


    def run(self):

        log("Dropee Engine Started", "info")

        while True:

            self.run_cycle()

            log("Cycle complete - sleeping 60s", "info")

            time.sleep(60)
