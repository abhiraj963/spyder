s = input()

def count_words(s):
    lst = s.split()
    return str(len(lst))

def count_spaces(s):
    counter = 0
    for char in s:
        if char == ' ':
            counter = counter + 1
    return str(counter)

def count_characters(s):
    counter = 0
    lst = s.split()
    for word in lst:
        for char in word:
            counter = counter + 1
    return str(counter)

def count_vowels(s):
    counter = 0
    vowels = 'a e i o u'.split()
    for word in s.split():
        for char in word:
            if char in vowels:
                counter = counter + 1
    return str(counter)

print('C:'+count_characters(s)+'S:'+count_spaces(s)+'W:'+count_words(s)+'V:'+count_vowels(s))

