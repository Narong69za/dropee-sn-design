# =====================================================
# MODULE  : token_parser.py
# VERSION : 1.0.0
# PURPOSE : Parse Telegram WebApp initData tokens
# =====================================================

import urllib.parse
import json


def parse_token(token_string):

    parsed = urllib.parse.parse_qs(token_string)

    result = {}

    for key, value in parsed.items():
        result[key] = value[0]

    if "user" in result:
        try:
            user_data = urllib.parse.unquote(result["user"])
            result["user"] = json.loads(user_data)
        except Exception:
            pass

    return result
