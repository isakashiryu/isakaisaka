# 練習1
def max_value_key(d):
    return max(d,key=lambda k:d[k])

# 練習2
def max_abs(ln):
    return max(map(abs,ln))

# 練習3
def number_of_big_numbers(ln,n):
    def pas(x):
        if x>n:
            return True
        else:
            return False
    return len(list(filter(pas,ln)))

# 練習4
# ファイルだるいので飛ばしま〜す
   
        
