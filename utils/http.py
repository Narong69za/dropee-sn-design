import requests
from utils.logger import log

BASE_URL = "https://dropee.clicker-game-api.tropee.com/api/game"

def api_post(endpoint, token):

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        r = requests.post(BASE_URL + endpoint, headers=headers)
        log(f"API {endpoint} -> {r.status_code}", "info")
        return r.json()
    except Exception as e:
        log(f"HTTP Error: {e}", "error")