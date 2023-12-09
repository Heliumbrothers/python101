string = ['h', 'e', 'l', 'l', 'o']

input = "I can show you the world, take you wonder by wonder"

def count_vowels(input):
    vowel_set = set(['o', 'e', 'i', 'u', 'a'])
    vowel_count = 0
    for letter in input:
        if letter.lower() in vowel_set:
            vowel_count += 1
    return vowel_count

print(count_vowels(input))