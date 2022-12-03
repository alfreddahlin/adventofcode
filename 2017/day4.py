import re

input_data = open("inputs/day4.in", "r").read().strip().split("\n")

valid_word = 0
valid_anagram = 0
for phrase in input_data:
    words = re.findall(r"\w+", phrase)
    words_order = ["".join(sorted(word)) for word in words]
    words_set = set(words)
    words_order_set = set(words_order)
    if len(words_set) == len(words):
        valid_word += 1
    if len(words_order_set) == len(words_order):
        valid_anagram += 1

print(valid_word, valid_anagram)
