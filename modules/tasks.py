from utils.http import api_post
from utils.logger import log

def run_tasks(token):
    log("Running tasks...", "info")
    api_post("/tasks", token)