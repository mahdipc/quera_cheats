n = int(input())
words = []
min_len_word = 100
smallest_word = ""

for i in range(n):
    st = input()
    words.append(st)
    if len(st) < min_len_word:
        min_len_word = len(st)
        smallest_word = st


def seprator_stirng_of_word(word, lenght):
    word_seprator = []
    for i in range(len(word)-lenght+1):
        word_seprator.append(word[i:i+lenght])
    return word_seprator


def check_value_in_all_words(word_seprator, words):
    for word in words:
        if (word_seprator not in word) and (word_seprator[::-1] not in word):
            return False
    return True


while min_len_word > 0:
    smallest_word_seprator_list = seprator_stirng_of_word(
        smallest_word, min_len_word)

    for smallest_word_seprator in smallest_word_seprator_list:
        if check_value_in_all_words(smallest_word_seprator, words):
            if smallest_word_seprator in words[0]:
                print(smallest_word_seprator)
            else:
                print(smallest_word_seprator[::-1])

            min_len_word = 0
            break
    min_len_word -= 1
