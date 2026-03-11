# =====================================================
# PROJECT : DROPEE SN DESIGN
# MODULE  : core/engine.py
# VERSION : 1.1.0
# AUTHOR  : SN DESIGN STUDIO
# UPDATED : 2026-03-11
# PURPOSE : Main automation engine for Dropee bot
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

            log(f"Processing account: {str(token)[:8]}...", "info")

            try:

                run_tasks(token)
                tap_action(token)
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
