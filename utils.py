def equals_headers(headers1, headers2, ignore_keys=[]):
    for key in headers1:
        if key in ignore_keys:
            continue
        if key not in headers2 or not equals_value(headers1[key], headers2[key], ignore_keys):
            return False
    return True

def equals_bodies(body1, body2, ignore_keys=[]):
    return equals_value(body1, body2, ignore_keys)

def equals_dict(dic1, dic2, ignore_keys=[]):
    for key in dic1:
        if key in ignore_keys:
            continue
        if key not in dic2 or not equals_value(dic1[key], dic2[key], ignore_keys):
            return False
    return True


def equals_list(lis1, lis2, ignore_keys=[]):
    if len(lis1) != len(lis2):
        return False
    for idx in range(len(lis1)):
        return equals_value(lis1[idx], lis2[idx], ignore_keys)
    return True


def equals_value(val1, val2, ignore_keys=[]):
    if type(val1) != type(val1):
        return False
    if type(val1) == dict:
        return equals_dict(val1, val2, ignore_keys)
    elif type(val1) == list:
        return equals_list(val1, val2, ignore_keys)
    else:
        if val1 != val2:
            return False
    return True