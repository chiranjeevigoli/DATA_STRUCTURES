#Part C: Write a function called reverse_list that takes a list and returns a new list 
#with the items in reverse order. No using Python's built-in reverse() or slicing tricks — use a loop.

def reverse_list(some_list):
    new_list = []
    for item in range(len(some_list)-1, -1, -1):
        new_list.append(some_list[item])
    return new_list
        
        
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["a","b","c"]))