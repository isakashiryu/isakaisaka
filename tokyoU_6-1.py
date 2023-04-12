# 練習1
strings = ['The','quick','brown']
list_strings  = [len(strings[i]) for i in range(len(strings))]

# 練習2
str1 = '123,45,-3'
list1 = [int(x) for x in str1.split(',')]

# 練習3
def var(lst):
    n = sum(lst)/len(lst)
    lst2 = [(x - n)**2 for x in lst]
    return sum(lst2)/len(lst2)

# 練習4
def sum_lists(list1):
    return sum([sum(list_int) for list_int in list1])

# 練習5
def sum_matrix(list1,list2):
    list3 = []
    list3 = [[list1[x][y] + list2[x][y] for y in range(3)] for x in range(3)]
    return list3