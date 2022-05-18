# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd

n = [1, 2, 6, 4, 5]
i = 1


# n.sort()
# print(n)

def findNumber(arr, k):
    arr.sort()
    if k in arr:
        print('Yes')

    else:
        print('No')


findNumber(n, i)
