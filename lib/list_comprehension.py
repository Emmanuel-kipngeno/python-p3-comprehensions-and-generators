#!/usr/bin/env python3

# File: lib/data_structures.py

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]


# File: lib/data_structures.py

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]
