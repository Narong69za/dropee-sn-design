# =====================================================
# PROJECT : DROPEE SN DESIGN
# MODULE  : modules/tasks.py
# VERSION : 1.1.1
# AUTHOR  : SN DESIGN STUDIO
# UPDATED : 2026-03-11
# PURPOSE : Execute task requests
# =====================================================

from utils.http import api_post
from utils.logger import log


def run_tasks(token):

    log("Running tasks...", "info")

    api_post("/tasks", token)
