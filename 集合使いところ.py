#共通点の友達見つける

my_frends = {"a", "b", "c", "d"}
a_frends = {"b", "d"}
print(my_frends & a_frends)
#"b"と"d"が　私と"a"さんの共通の友達

#listからsetに型変換

f = ["apple", "banana", "orange", "banana"] #買い物したもの
kind = set(f)                               #listからsetに置き換え
print(kind)                                 #集合にしたからジャンルごとにまとまる