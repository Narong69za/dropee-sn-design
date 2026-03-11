# =====================================================
# MODULE  : http.py
# VERSION : 1.1.1
# DATE    : 2026-03-11
# PURPOSE : Central HTTP API handler
#
# UPDATE
# - Fixed JSON parsing crash
# - Added safe response inspection
# - Improved error logging
# =====================================================

import requests
from utils.logger import log

BASE_URL = "https://dropee.clicker-game-api.tropee.com/api/game"


def api_post(endpoint, token):

    url = BASE_URL + endpoint

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:

        r = requests.post(url, headers=headers)

        log(f"API {endpoint} -> {r.status_code}", "info")

        # debug response
        if r.status_code != 200:
            log(f"Response: {r.text[:120]}", "error")
            return None

        try:
            return r.json()

        except Exception:
            log("Invalid JSON response", "error")
            log(r.text[:120], "error")
            return None

    except Exception as e:
        log(f"HTTP Error: {e}", "error")
        return None
