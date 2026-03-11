# =====================================================
# MODULE  : dropee_api.py
# VERSION : 1.1.0
# PURPOSE : Dropee API handler
# =====================================================

import requests

BASE_URL = "https://dropee.app"

class DropeeAPI:

    def __init__(self, token):
        self.session = requests.Session()
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    def tasks(self):
        url = f"{BASE_URL}/api/tasks"
        r = self.session.get(url, headers=self.headers)
        print("[INFO] API /tasks ->", r.status_code)
        print(r.text)
        return r

    def tap(self):
        url = f"{BASE_URL}/api/tap"
        r = self.session.post(url, headers=self.headers)
        print("[INFO] API /tap ->", r.status_code)
        print(r.text)
        return r

    def rewards(self):
        url = f"{BASE_URL}/api/rewards"
        r = self.session.get(url, headers=self.headers)
        print("[INFO] API /rewards ->", r.status_code)
        print(r.text)
        return r
