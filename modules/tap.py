from utils.http import api_post
from utils.logger import log

def tap_action(token):
    log("Executing tap action...", "info")
    api_post("/tap", token)