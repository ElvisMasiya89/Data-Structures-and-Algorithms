class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        """ For something to be iterable it needs to  hate a __iter__ method that return an iterator which has a
        __next__ method in this case it just returns itself as it has the __next__ method """
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


# for num in MyRange(1, 10):
#     print(num)

nums = MyRange(1, 10)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))


# We can create the same iterator  with a generator function

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


nums2 = my_range(1, 10)
print(next(nums2))
print(next(nums2))
print(next(nums2))
print(next(nums2))
