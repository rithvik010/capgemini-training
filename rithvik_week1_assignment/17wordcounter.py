#input
def getinput():
    user_input = input("type a sentence: ")
    return user_input
def get_wordslist(user_input):
    list_of_words_with_duplicates = user_input.split()
    list_of_words = set(list_of_words_with_duplicates)
    return (list_of_words, list_of_words_with_duplicates)
#wordcount
def word_count_and_print(list_of_words, list_of_words_with_duplicates):
    for word in list_of_words:
        word_occurrence = list_of_words_with_duplicates.count(word)
        if(word_occurrence > 1):
            print(f"{word} is occurred {word_occurrence} times in the given string")
        else:
            print(f"{word} is occurred {word_occurrence} time in the given string")
def main():
    user_input = getinput()
    (list_of_words, list_of_words_with_duplicates) = get_wordslist(user_input)
    word_count_and_print(list_of_words, list_of_words_with_duplicates)
main()