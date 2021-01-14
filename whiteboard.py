#Write a function that will remove all vowels from a given string. The function should return a string.
#Example:
#Input: 'Joel'
#Output: 'Jl'

def remove_vowels(word):
    vowels = ["a","e","i","o","u"]
    for letter in word:
        if letter in vowels:
            word = word.replace(letter,"")
    print(word)

remove_vowels("Joel")
remove_vowels("Patrick")