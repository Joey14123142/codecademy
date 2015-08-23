__author__ = 'zxy'
def count(sequence, item):
    time = 0
    for i in item.split():
        if i == sequence.split():
            time += 1
    return time