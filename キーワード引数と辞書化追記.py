def menue(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menue('banana', 'apple', 'orange', entree='beef', drink='coffee')