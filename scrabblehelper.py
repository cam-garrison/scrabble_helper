from sympy.utilities.iterables import multiset_permutations


# This function gives us all the possible permutations of all lengths, no duplicates
def list_anagrams(input_letters):
    len_letters = len(input_letters)
    if len_letters <= 1:
        return input_letters

    else:
        anagrams = [''.join(perm) for perm in multiset_permutations(input_letters)]
        num_letters = len_letters - 1
        while num_letters >= 3:
            anagrams = anagrams + [''.join(perm) for perm in multiset_permutations(input_letters, num_letters)]
            num_letters = num_letters - 1
        anagram = list(dict.fromkeys(anagrams))
        return anagrams


# This function should return a list of the permutations that are actually words, using a big ol txt file
def find_real_words(anagrams):
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    real_words = []

    for word in anagrams:
        if word in valid_words:
            real_words.append(word)

    return real_words


# This function uses the above functions to output a words list from an input of letters.
def scrabble_words(letters):
    anagrams_list = list_anagrams(letters)
    words_list = find_real_words(anagrams_list)
    return words_list


# This function uses the function below to output a list of scrabble word values corresponding to words
def scrabble_scores_list(words_list):
    length = len(words_list)
    score_list = []

    for word in words_list:
        score = scrabble_score_word(word)
        score_list.append(score)

    return score_list


# This function will output the scrabble value of an inputted word
def scrabble_score_word(word):
    value = 0
    for letter in word:
        if letter in ('a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'):
            value = value + 1
        elif letter in ('d', 'g'):
            value = value + 2
        elif letter in ('b', 'c', 'm', 'p'):
            value = value + 3
        elif letter in ('f', 'h', 'v', 'w', 'y'):
            value = value + 4
        elif letter == 'k':
            value = value + 5
        elif letter in ('j', 'x'):
            value = value + 8
        elif letter in ('q', 'z'):
            value = value + 10

    return value


# This function is the big combo, will combine and print the final sorted wordlist + scorelist from an input of letters.
def scrabble_helper(letters):
    word_list = scrabble_words(letters)
    value_list = scrabble_scores_list(word_list)

    bubble_sort(value_list, word_list)

    length = len(word_list)
    final_list = []

    index = 0
    while index<length:
        final_list.append(word_list[index])
        final_list.append(value_list[index])
        index = index + 1

    print(final_list)


# Using a modified bubble sort to sort the lists so that words with high values are displayed first
def bubble_sort(nums, words):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                words[i], words[i + 1] = words[i + 1], words[i]
                # Set the flag to True so we'll loop again
                swapped = True


while True:
    letters = input("Enter letters: ")
    scrabble_helper(letters)