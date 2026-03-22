# Write a function called find_max that takes a list of numbers and returns the largest one. 
# No using Python's built-in max() — use a loop.

# In this type of problems the pattern is "Running best or the Running result"

def find_max(numbers):
    current_max = numbers[0]        # Initially assuming numbers[0] as max 
    for number in numbers[1:]:
        if number > current_max:
            current_max = number
    return current_max
    
print(find_max([1,45,67,23,75,12,2,0]))