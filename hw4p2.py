def ListAvg(list):
    if (len(list) == 0):
        return 0
    for item in list:
        if (isinstance(item, int) or isinstance(item, float)):
            continue
        else:
            return 0
    avg = sum(list) / len(list)
    return avg
