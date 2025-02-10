#4Q.Write a Python program to count and display the vowels of a given text
vowels = 'aeiou'
vowel_cnt = {}
for char in vowels:
    if char.lower() in vowel_cnt:
        vowel_cnt[char.lower()] += 1
    elif char.lower() in vowels:
        vowel_cnt[char.lower()] = 1

print(vowel_cnt)
