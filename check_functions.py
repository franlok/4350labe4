import re

def check_name(name):
    if name.strip() != name:
        return False
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               "]+", flags=re.UNICODE)
    return not emoji_pattern.search(name)

def check_name_len(name):
    return len(name.encode('utf-8')) <= 20



def check_sid_len(sid):
    sid_str = str(sid)
    return sid_str.isdigit() and len(sid_str) == 10 and sid_str.startswith("1155")

