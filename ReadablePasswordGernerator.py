import random

wordList = []
specialChar = ['@', '!', '#', '%', '^', '&', '*', '_', '-']

with open("paragraphForPassword.txt", 'r') as file:
    data = file.readlines()
    for line in data:
        words = line.split()

    for item in words:
        if len(item) > 5:
            wordList.append(item.capitalize())
    word = random.choice(wordList)
    specialCharRandom = random.choice(specialChar)
    num = str(random.randint(10, 99))
    password = word + specialCharRandom + num
    print(password)
