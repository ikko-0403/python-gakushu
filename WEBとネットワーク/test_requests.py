import requests

payload = {'key1': 'value1', 'key2': 'value2'}

#r = requests.get('http://httpbin.org/get', params=payload)
#r = requests.post('http://httpbin.org/post', data=payload)
#r = requests.put('http://httpbin.org/put', params=payload)
#r = requests.delete('http://httpbin.org/delete', params=payload)

r = requests.get('http://httpbin.org/get', params=payload, timeout=1)#応答にタイムアウト設定


print(r.status_code)
print(r.text)
print(r.json())