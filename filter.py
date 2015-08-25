__author__ = 'zxy'
squares = [n**2 for n in range(1,11)]
print filter(lambda x: x in range(30,71), squares)