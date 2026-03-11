# =====================================================
# PROJECT : DROPEE SN DESIGN
# MODULE  : modules/reward.py
# VERSION : 1.1.1
# AUTHOR  : SN DESIGN STUDIO
# UPDATED : 2026-03-11
# PURPOSE : Claim reward system
# =====================================================

from utils.http import api_post
from utils.logger import log


def collect_rewards(token):

    log("Collecting rewards...", "info")

    api_post("/rewards", token)
