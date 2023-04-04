# 練習１
def reverse_lookup2(dic1):
    dic2 = {}
    for key,value in dic1.items():
        dic2[value] = key
    return dic2    

# 練習２
def sum_n(x,y):
    s = 0
    for n in range(x,y+1):
        s = s + n
    return s    

# 練習３
def construct_list(int_size):
    list1 = []
    for list_value in range(int_size):
        list1 = list1 + [list_value]
    return list1    

# 練習4
def sum_lists(list1):
    sum = 0
    for list2 in list1:
        for n in list2:
            sum = sum + n
    return sum        
         
# 練習5
def sum_matrix(list1,list2):
    list3 = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            list3[i][j] += list1[i][j] + list2[i][j]
    return list3       

# 練習6
def simple_match(str1, str2):
    for i in range(len(str1)-len(str2)+1):
        j = 0
        while j < len(str2) and str1[i+j] == str2[j]:  #str1とstr2が一致している限りループ（ただし、jがstr2の長さ以上にならないようにする）#この条件がないと…？
            j += 1
        if j == len(str2):  #str2の最後まで一致しているとこの条件が成立
            return i
    return -1
    
#練習７
# from time import sleep
# x = 0
# while True:
#     if x >= 10:
#         break
#     print('Yeah!')
#     sleep(1)
#     x += 1

# 練習8
def collect_engwords(str_engsentences):
    list_punctuation = ['.', ',', ':', ';', '!', '?']
    for j in range(len(list_punctuation)):  #list_punctuationの中の文字列（この場合、句読点）を空文字列に置換する
        str_engsentences = str_engsentences.replace(list_punctuation[j], '')
    list_str1 = str_engsentences.split(' ')
    list_str2 = []
    for str_engwords in list_str1:
        if len(str_engwords) >= 3:
            list_str2 += str_engwords
    return list_str2

      

# 練習9
def swap_lists(ln1,ln2):
    for odd_number in range(1,len(ln1),2):
        ln2[odd_number],ln1[odd_number] = ln1[odd_number],ln2[odd_number]
    tuple1 = (ln1,ln2)
    return tuple1 

# 練習10
def count_capitalletters(str1):
    count = 0
    for letter in str1:
        if letter.isupper():
            count += 1
    return count   

# 練習11
def identify_codons(str_augc):
    str_codons = []
    for i in range(0,len(str_augc),3):
        str_codons.append(str_augc[i*3: i*3+3])
    return str_codons  

# 練習12
def add_commas(int1):
    