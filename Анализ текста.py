user_text = input("Введите ваш текст: ").lower()

words_overall = len(user_text.split())

print(f"Всего слов в тексте: {words_overall}")

words_separate = user_text.split()

longest_word = words_separate[0]

for words in words_separate:
    if len(words) > len(longest_word):
        longest_word = words
        print(f"Самое длинное слово: {longest_word}")

vowels_list = "аеёиоуыэюя"

vowel_quantity = 0

for words in words_separate:
    for vowels in words:
        if vowels in vowels_list:
            vowel_quantity +=1
print(f"Гласных в тексте: {vowel_quantity}")

for words in words_separate:
    word_quantity = 0
    for quantity in words_separate:
        if quantity == words:
            word_quantity +=1
    print(f"Слово \"{words}\" встречается {word_quantity} раз(а)")
