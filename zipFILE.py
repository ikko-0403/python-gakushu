import glob# (* や **）を使ってファイルやフォルダを一覧で取得する
import zipfile

with zipfile.ZipFile('test.zip', 'w') as z:
    
    # z.write('test_dir')
    # z.write('test_dir/test3.txt')
    for f in glob.glob('test_dir/**', recursive=True):
        z.write(f)

with zipfile.ZipFile('test.zip', 'r') as z:
   # z.extractall('zzz2')
   with z.open('test_dir/test3.txt') as f:
       print(f.read())