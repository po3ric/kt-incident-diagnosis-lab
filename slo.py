def availability(good, total):
    # return good / total as a number between 0 and 1
    return good / total if total > 0 else None

def is_slo_met(avail, target):
    # return True if avail is at least the target
    if avail is None:
        return False
    return avail >= target
