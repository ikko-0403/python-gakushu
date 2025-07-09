import datetime#Python 標準の日時操作ライブラリを読み込む

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y-%H%M%S%f'))

today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%y'))

t = datetime.time(hour=1, minute=10, second=5, microsecond=9999)
print(t) 
print(t.isoformat())
print(t.strftime('%H-%M-%S-%f'))

print(now)
d = datetime.timedelta(weeks=1)#日時の計算今から何週後とか
print(now - d)

import time#シンプルに「待つ」「時間を測る」処理
print('####################')
time.sleep(5)
print('###################')

import os
import shutil

file_name = 'test.txt'#バックアップ作成

if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(
        file_name, now.strftime('%Y_%m_%d_%H_%H_%M_%S')))
    
with open(file_name, 'w') as f:
    f.write('ttttest')