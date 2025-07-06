import tarfile #.tar や .tar.gz（gzip圧縮されたtarファイル）などのアーカイブファイルを作成・解凍するためのモジュール

# with tarfile.open('test.tar.gz', 'w:gz') as tr:
#    tr.add('test_dir')

with tarfile.open('test.tar.gz', 'r:gz') as tr:# 'test.tar.gz' という gzip圧縮されたtarファイルを開く
   # tr.extractall(path='test_tar')
    with tr.extractfile('test_dir/test2_dir/test4.txt') as f:
        print(f.read())