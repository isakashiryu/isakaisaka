def reverse_lookup(list1):
    result = {}
    for index, value in enumerate(list1):  #enumerate:The enumerate(list1) function is used to simultaneously get the elements of list list1 and corresponding indices accordingly
        result[value] = index
    return result

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
result = reverse_lookup(list1)
print(result)