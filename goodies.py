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

print(avoids('anifdfdf', 'bc'))


