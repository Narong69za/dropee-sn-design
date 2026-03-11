# =====================================================
# PROJECT : DROPEE SN DESIGN
# MODULE  : modules/tap.py
# VERSION : 1.1.1
# AUTHOR  : SN DESIGN STUDIO
# UPDATED : 2026-03-11
# PURPOSE : Execute tap action
# =====================================================

from utils.http import api_post
from utils.logger import log


def tap_action(token):

    log("Executing tap action...", "info")

    api_post("/tap", token)
