# An Iterator in an object with a state that remembers where it is during iteration
# Can use the __next__  method to get the next value
# a list in not an iterator, but it is iterable, it has the __iter__
# method that returns the iterator for us to loop over
# Iterator only go forward  to start again ,you have to crate a new iterator

nums = [1, 2, 3, 45, 66]
# print(dir(nums))

# Return the iterator by calling __iter__ method

i_nums = nums.__iter__()  # Or iter(nums)
print(dir(i_nums))

# Calling Next to get the next values

print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
# print(next(i_nums)) # causes stop iteration exception as they no more value to print

# The is basically what the for loop does in
# the background including handling the iteration exception


while True:
    try:
        item = next(i_nums)
        print(item)

    except StopIteration:
        break
