#list

n = [3,3,3,3,5,6,7,8,]
m = [1,2,3,4,1]


n.append(100)



print(list(n + m))
print(m.index(2))
print(n.index(3,3))
print(m.count(1))
print(n[2])
#このリストに８があったらexistと出力して
if 8 in n:
    print("exist")


print("###########################################")

#リストの並び替え
n.sort()
print(n)
n.reverse()
print(n)

print("###########################################")

#名前を""を使って分割してりすとにいれる
s = "My name is IKKO"
ss = s.split( )
print(ss)
#リストの中身を""を使ってつないでください
t = " ".join(ss)
print(t)