def outer(a, b):
    def plus(c, d):
        return c + d#←が足し算の結果を返す設定
    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)

outer(2,8)