
#５より小さい間進行するコード
count = 0
while count < 5:
    print(count)
    count += 1  #←これ忘れたら無限に０００００００００００ってなる

print("##################")


#ifとセットでbreak使うと　もしこの条件に達したらwhile文を抜けるというコードに
count = 0
while True:
    if count >= 5:
        break
    print(count)
    count += 1

    print("################################3")

    count = 0
    while True:
        if count >= 5:
            break

        if count == 2:
            count += 1
            continue

        print(count)
        count += 1
print("########################################")

count = 1
while count <= 5:
    print(count)
    count += 1
else:
    print("owari")