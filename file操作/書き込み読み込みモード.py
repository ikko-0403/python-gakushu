s = """\
AAA
XXX
CCC
DDD
"""
with open('test.txt', 'w+') as f:#w+書き込みと読み込みできますよ
    f.write(s)#書き込み
    f.seek(0)#いったん最初に戻って
    print(f.read())#読み込んでいる