def median(numbers):
    numbers = sorted(numbers)
    length = len(numbers)
    if len(numbers) % 2 == 0:
        length = length-1
        return (numbers[(length//2)] + numbers[length//2 + 1])//2
    else:
        if length(numbers) == 1:
            return numbers[0]
        else:
            return numbers[length//2 + 1]

numberlist = [4]
print median(numberlist)
