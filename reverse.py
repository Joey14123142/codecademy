__author__ = 'zxy'
def reverse(text):
    final = []
    for i in range(len(str(text))):
        final.insert(0,str(text)[i])
    return ''.join(final)