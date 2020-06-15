# print numbers from 1 "To" 5 (it doesn't print 5)
for value in range(1,5):
    print(value)

# print numbers from 1 ends at 5
for value in range(1, 6):
    print(value)

# using range to make a list
numbers = list(range(1,6))

# list of even numbers between 1 to 10
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# list of first 10 square numbers
squares = []
for value in range(1, 11):
    square  = value**2
    squares.append(square)
    # Or we can write the last two lines in just one line more concisely
    #squares.append(value**2)
print(squares)

# Simple statistics with lists
digits = [1,2,3,4,5,6,7,8,9,0]

print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehenstion
squares = [value**2 for value in range(1, 11)]
print(squares)
