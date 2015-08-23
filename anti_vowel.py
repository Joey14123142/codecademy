__author__ = 'zxy'
def anti_vowel(text):
    result = []
    vowel = "aeiou"
    for i in text:
        if i.lower() in vowel:
            continue
        else:
            result.append(i)
    result = "".join(result)
    return result