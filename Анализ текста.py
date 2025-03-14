import string


def clean_punctuation():
    no_punctuation = str.maketrans("", "", string.punctuation)
    new_text = user_entering.translate(no_punctuation)
    return new_text


def find_longest_word(words_separate):
    longest_word = ""
    for words in words_separate:
        if len(words) > len(longest_word):
            longest_word = words
    return longest_word


def find_all_vowels():
    vowels_list = "аеёиоуыэюя"
    vowel_quantity = 0
    for vowels in user_entering:
        if vowels in vowels_list:
            vowel_quantity += 1
    return vowel_quantity


def words_found(words_separate):
    word_list = {}
    for words in words_separate:
        if words in word_list:
            word_list[words] += 1
        else:
            word_list[words] = 1
    return word_list


def show_all():
    user_text = clean_punctuation()
    words_separate = user_text.split()
    longest_word = find_longest_word(words_separate)
    all_vowels = find_all_vowels()
    word_list = words_found(words_separate)
    print(f"Всего слов в тексте: {len(words_separate)}")
    print(f"Самое длинное слово: {longest_word}")
    print(f"Гласных букв в тексте: {all_vowels}")

    for word, number in word_list.items():
        print(f"Слово \"{word}\" использовалось {number} раз(а)")


user_entering = input("Введите ваш текст: ").lower()
show_all()
