# An Iterator in an object with a state that remembers where it is during iteration
# Can use the __next__  method to get the next value
# a list in not a iterator but it is iterable, it has the __iter__
# method that returns the iterator for us to loop over

nums = [1, 2, 3, 45, 66]
print(dir(nums))


def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


my_nums = square_numbers(nums)
print(my_nums)


# Using a generator instead to generate
# one number at time rather in one gaols to save memory

def square_numbers_gn(nums_gn):
    for i in nums_gn:
        yield i * i


my_nums_gn = square_numbers_gn(nums)
print(my_nums_gn)

# print(next(my_nums_gn))
# print(my_nums_gn.__next__())
# print(next(my_nums_gn))
# print(next(my_nums_gn))
# print(next(my_nums_gn))

# Or do this
for num in my_nums_gn:
    print(num)

# Creating a generator using list comprehension
my_nums_gn2 = (x * x for x in nums)
print(my_nums_gn2)

# for num in my_nums_gn2:
#     print(num)

# How  to convert a generator to a list
print(list(my_nums_gn2))
