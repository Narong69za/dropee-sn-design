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
            log(f"Processing account: {token[:8]}...", "info")

            try:
                run_tasks(token)
                tap_action(token)
                collect_rewards(token)

                time.sleep(3)

            except Exception as e:
                log(f"Error processing account: {e}", "error")