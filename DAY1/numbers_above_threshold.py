#Part B: Write a function called count_above that takes a list and a threshold, 
# and returns how many numbers are above the threshold.

def count_above(numbers, threshold):
    count = 0                             # A pattern of Running result or Running best
    for number in numbers:
        if number > threshold:
            count += 1
    return count

print(count_above([10, 55, 30, 80, 45], 40))
