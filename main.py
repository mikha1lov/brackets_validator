import re


def brackets_cutter_regex(raw: str) -> str:
    pattern = re.compile(r'\([^\)]+$|[\(]$')
    result = pattern.sub('', raw)
    if result:
        return result
    return ''


def brackets_cutter_python(raw: str) -> str:
    if raw == '':
        return raw

    is_inside = False
    checkpoint = 0

    for position, s in enumerate(raw):
        if s == ')':
            new_checkpoint = position + 1
            if is_inside:
                is_inside = False
            checkpoint = new_checkpoint
        elif s == '(':
            is_inside = True

    if is_inside:
        raw = raw[:checkpoint]

    return raw
