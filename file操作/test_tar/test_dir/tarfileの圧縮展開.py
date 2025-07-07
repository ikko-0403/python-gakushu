import tarfile #.tar や .tar.gz（gzip圧縮されたtarファイル）などのアーカイブファイルを作成・解凍するためのモジュール

with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')