# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 0
for letter in word:
    if letter.isalpha():
        if letter.lower() in 'аеёиоуыэюя':
            vowels += 1
print(vowels)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости к нашим друзьям'
print(len(sentence.split(' ')))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split(" "):
    first_letter = word[0]
    print(first_letter)


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости к маме'
words = sentence.split()
world_count = len(words)
sum = 0
for w in words:
    letter = len(w)
    #print(letter)
    sum = sum + letter
    #print(sum)
    avg = float(sum) / float(world_count)
print('усредненная длина слова: ', avg)