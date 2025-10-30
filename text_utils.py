# Text processing utilities with bugs

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words.reverse()  # reverse() returns None
    return " ".join(reversed_words)

def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count  # Doesn't handle uppercase vowels

def truncate_string(text, max_length):
    if len(text) > max_length
        return text[:max_length] + "..."  # Missing colon
    return text

def find_longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest  # Doesn't handle empty sentence

def capitalize_first_letter(text):
    return text[0].upper() + text[1:]  # Crashes on empty string

def replace_spaces(text, replacement):
    return text.replace(" ", replacement)

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned = cleaned[::-1]  # Wrong operator, should be ==

def extract_numbers(text):
    result = []
    for char in text:
        if char.isdigit():
            result.append(int(char))
    return result  # Doesn't handle multi-digit numbers

# Unused imports
import re
import string
import datetime

def word_frequency(text):
    words = text.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq  # Doesn't handle punctuation or case sensitivity
