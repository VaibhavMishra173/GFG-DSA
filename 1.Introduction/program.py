number = 5

func1Output, func2Output, func3Output = 0, 0, 0

def findSum(number):
    global func1Output, func2Output, func3Output
    func1Output = func1(number)
    func2Output = func2(number)
    func3Output = func3(number)

def func1(number):
    # Sum of the first 'number' natural numbers using the formula
    return (number * (number + 1)) / 2

def func2(number):
    # Sum from 1 to 'number' (inclusive)
    sum = 0
    for i in range(1, number + 1):  # start at 1, go up to 'number'
        sum += i
    return sum

def func3(number):
    # Sum of all numbers below each number up to 'number'
    total_sum = 0
    for i in range(1, number + 1):
        for j in range(i):  # sum from 0 to i-1
            total_sum+=1
    return total_sum

findSum(number)

print(f"func1Output: {func1Output}, func2Output: {func2Output}, func3Output: {func3Output}")
