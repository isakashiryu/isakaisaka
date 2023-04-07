# これファイル系の勉強だから読み込むのだるいし、ノートがわりに使うね💌

for i in range(4):
    pass
print(i)
# パスめっちゃ便利やん！！すげええ

try:
    it = iter([0,1,2])
    while True:
        x = next(it)
        print(x)
except StopIteration:
    pass
# ごっちゃごちゃ書くわりに不便

for i, c in enumerate('ACDB'):
    print(i + 1, '番目の文字 =', c)
# enumerate：数えつつ処理したい時？使う    

# イテラブルとイテレータの形式的な定義をまとめます。

# イテラブル：iter を適用可能。 __iter__ メソッドを持つ。
# イテレータ：next を適用可能。 __next__ メソッドを持つ。
          # iter を適用したとき、引数のオブジェクトをそのまま返す。
# iter(x) は x.__iter__() と等価なので、iter を適用可能であることと、__iter__ メソッドを持つことは同義です。 
# 同様に、next(x) は x.__next__() と等価なので、 next を適用可能であることと、__next__ メソッドを持つことは同義です。