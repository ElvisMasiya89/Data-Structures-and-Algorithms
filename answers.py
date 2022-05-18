s = 'banana'

q = 'banana'


def split(s):
    return [char for char in s]


s = split(s)
print(s)


def get_unique_char(char):
    list_of_unique_numbers = []

    unique_numbers = set(char)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers


s = get_unique_char(s)

s.sort()

uni = s.copy()

print(uni)

print(q.index('a'))
arr = []
word = []

c = ''
for c in uni:
    l = len(q)
    index = q.index(c)
    sub_q = q[index: l]
    p = len(sub_q)
    for i in range(0, p + 1):
        word = sub_q[0: i]
        if word not in arr:
            arr.append(word)

print(arr)