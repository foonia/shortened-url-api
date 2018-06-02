import re

def validate(url):
    p = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    m = p.match(url)

    if m:
        return True
    else:
        return False

