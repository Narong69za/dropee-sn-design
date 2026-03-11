from utils.http import api_post
from utils.logger import log

def collect_rewards(token):
    log("Collecting rewards...", "info")
    api_post("/rewards", token)