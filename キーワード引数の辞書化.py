def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)
menu(entree='beef', drink='beer')



d = {    #辞書型
    'entree': 'beef', 
    'drink': 'wine',
    'dessert': 'ice'
}
menu(**d)#タプル