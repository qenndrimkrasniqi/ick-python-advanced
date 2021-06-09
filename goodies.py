from collections import Counter


def is_positive(n):
    return n > 0


def is_greater(n, m):
    return n > m


def is_python(word):
    return 'Yes' if word == 'Python' else 'No'


def is_long(my_list):
    return "Too long" if len(my_list) > 3 else "Okay"


def do_smth(y):
    x = "positive" if y > 0 else "negative"
    return x


def is_dog(a_list):
    a = "Yes" if 'dog' in a_list else "No"
    return a


def capitalize_all(t):
    t2 = []
    for i in t:
        t2.append(i.capitalize())
    return t2


def capitalize_all(t):
    return [s.capitalize() for s in t]


def minus_2(s):
    return [c - 2 for c in s]

def only_upper(my_list):
    t = []
    for i in my_list:
        if i.isupper():
            t.append(i)
    return t

def only_upper(my_list):
    return [i for i in my_list if i.isupper()]


def avoids(word, forbidden):
    for i in forbidden:
        if i in word:
            return False
    return True


def avoids(word, forbidden):
    return not any([i in word for i in forbidden ])


def uses_all(word, required):
    for i in required:
        if i not in word:
            return False
    return True

def uses_all(word, required):
    return all([i in word for i in required])


def subtract(list1, list2):
    list_s = []
    for i in list1:
        if i not in list2:
            list_s.append(i)
    return list_s

def subtract(list1, list2):
    return set(list1) - set(list2)


def has_duplicates(l1):
    l2 = []
    for i in l1:
        if i not in l2:
            l2.append(i)
    l2.sort()
    l1.sort()
    return l1 != l2


def has_duplicates(l1):
    return len(set(l1)) != len(l1)


list1 = ['ani', 'pse', 'pse']
list2 = ['po', 'jo', 'ani']


def uses_only(word, available):
    for i in word:
        if i not in available:
            return False
    return True

def uses_only(word, available):
    return uses_all(available, word)


def avoids(word, forbidden):
    return set(word).isdisjoint(set(forbidden))


def is_anagram(str1, str2):
    my_str1 = list(str1)
    my_str2 = list(str2)
    my_str1.sort()
    my_str2.sort()
    return my_str1 == my_str2


def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)


def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)


print(is_anagram('ani', 'ina'))  # True
print(is_anagram('ani', 'pse'))  # False
