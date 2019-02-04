import re


def brackets_cutter_regex(raw: str) -> str:
    pattern = re.compile(r'\([^\)]+$|[\(]$')
    result = pattern.sub('', raw)
    if result:
        return result
    return ''


def brackets_cutter_python(raw: str) -> str:
    last_closed_bracket = raw.rfind(')')
    start = last_closed_bracket if last_closed_bracket != -1 else 0
    end = raw.rfind('(', start)
    if end != -1:
        return raw[:end]
    return raw

