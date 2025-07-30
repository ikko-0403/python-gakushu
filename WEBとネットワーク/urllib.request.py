"""
REst

HTTPメソッド　クライアントが行いたい処理をサーバに伝える

GET     データの参照
POST    データの新規登録
PUT     データの更新
DELETE  データの削除
"""

import urllib.request
import json

#GET
payload = {'key1': 'value1', 'key2': 'value2'}#欲しいパラメータ指定

# url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)#urlに書き加える

# with urllib.request.urlopen(url) as f:
#     r = json.loads(f.read().decode('utf-8'))
#     print(type(r))

#POST

payload = json.dumps(payload).encode('utf-8')#辞書をJSON文字列に変換し、さらにバイト列に変換（POST用）
req = urllib.request.Request('http://httpbin.org/post', data=payload, method='POST')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))


#PUT
req = urllib.request.Request('http://httpbin.org/put', data=payload, method='PUT')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

#DELETE
req = urllib.request.Request('http://httpbin.org/delete', data=payload, method='DELETE')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))