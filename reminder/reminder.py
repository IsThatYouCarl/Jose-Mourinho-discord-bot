import time
import re

def get_seconds_and_reason(message):
    word_remove_list = ["in", "every", "at"]
    for word in word_remove_list:
        if word in message:
            request = message.replace(word, "").strip()
            break

    time = request[:request.index("(")]

    reason_parenthesis = request.replace(time, "").strip()
    reason = reason_parenthesis.replace("(", "").replace(")", "")

    hours_match = re.findall(r'(\d+)h', time)
    if hours_match:
        time = time.replace(f'{hours_match[0]}h', "")
        hour = hours_match[0]
    else:
        hour = 0

    minutes_match = re.findall(r'(\d+)m', time) 
    if minutes_match:
        time = time.replace(f'{minutes_match[0]}m', "")
        minute = minutes_match[0]
    else:
        minute = 0

    seconds_match = re.findall(r'(\d+)s', time)

    if seconds_match:
        time = time.replace(f'{seconds_match[0]}', "")
        second = seconds_match[0]
    else:
        second = 0

    seconds = int(hour)*3600 + int(minute)*60 + int(second)*1

    return seconds, reason
