import requests

r = requests.post(
    'http://127.0.0.1:5000/post', data={'username': "Mike"}
)
print("ステータスコード：", r.status_code)
print("レスポンス：", r.text)