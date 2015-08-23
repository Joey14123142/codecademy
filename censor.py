__author__ = 'zxy'
def censor(text, word):
    if text.split() == word:
        '"*"*len(word)'.join(text)
    return

def censor(text, word):
    for i in text.split():
        result = []
        if i == word:
            i = '*'*len(word)
        else:
            i = i
        result.append(i)
    return ''.join(result)