import json

j = {
    'employee':
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
}

print(j)
print("#########################")
print(json.dumps(j))

with open('test,json', 'w') as f:#ファイルに書き込む
    json.dump(j, f)

print("#########################")
print("#########################")


with open('test,json', 'r') as f:#ファイルから読み取る
    print(json.load(f))