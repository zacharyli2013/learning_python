import random

chars = ['a','b','c','d','e','f',
         'g','h','i','j','k','l',
         'm','n','o','p','q','r',
         's','t','u','v','w','x',
         'y','z']

def generateRandomString(length):
    generatedString = []
    for i in range(length):
        generatedString.append(random.choice(chars))
    return ''.join(generatedString)

for i in range(5):
    print(generateRandomString(10))