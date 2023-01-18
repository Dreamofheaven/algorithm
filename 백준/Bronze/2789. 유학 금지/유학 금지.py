word = input()
new_word = ''
target_word = list('CAMBRIDGE')

for i in word:
    if i not in target_word:
        new_word += i
print(new_word)