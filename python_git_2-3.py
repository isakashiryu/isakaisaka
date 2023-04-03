#リスト list1 が引数として与えられたとき、list1 の各要素 value をキー、value の list1 におけるインデックスをキーに対応する値とした辞書を返す関数 reverse_lookup を作成してください。
#以下のセルの ... のところを書き換えて reverse_lookup(list1) を作成してください。
def reverse_lookup(list1):
    dictionary1 = {}
    for key in list1:
        dictionary1[key] = list1.index(key) #dict1は[]で括るよ！
    return dictionary1

print(reverse_lookup(['apple', 'pen', 'orange']) == {'apple': 0, 'orange': 2, 'pen': 1})
