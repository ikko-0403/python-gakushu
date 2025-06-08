l = [1, 2, 3]
i = 5
#del l

try:
    l[i]
    #l[0]
except IndexError as ex:#このエラー出た時に
    print("Don'tworry: {}".format(ex))
except NameError as ex:
    print(ex)
else:
    print('done')
finally:
    print("finish!!!!!!!!!")