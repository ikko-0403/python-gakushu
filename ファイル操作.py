import os #ファイル操作やディレクトリ操作 存在確認・作成・削除など
import pathlib #オブジェクト指向なファイル操作モジュール
import glob #パターンマッチでファイル検索
import shutil #コピーや移動の専門

# print(os.path.exists('test.txt'))#このファイルありますか？
# print(os.path.isfile('symlink.txt'))#ファイルですか？
# print(os.path.isdir('test.txt'))#ディレクトリですか？

# os.rename('rename.txt', 'renamed.txt')#rename
# os.symlink('renamed.txt', 'symlink.txt')
# print(os.path.exists('symlink.txt'))#symlink

# os.mkdir('test_dir')#ディレクトリ作成
# s.rmdir('test_dir')#中身からなら削除

# pathlib.Path('empty.txt').touch()　#空のファイル作成
# os.remove('empty.txt')

# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')#ディレクトリの中にディレクトリ作成
# print(os.listdir('test_dir'))

# pathlib.Path('test_dir/test_dir2/empty.txt').touch()
# shutil.copy('test_dir/test_dir2/empty.txt',
#            'test_dir/test_dir2/empty2.txt')#コピー作成

#print(glob.glob('test_dir/test_dir2/*'))#中身検索

shutil.rmtree('test_dir')#全削除

