s = """\
AAA
XXX
CCC
DDD
"""
with open('test.txt', 'w') as f:
    f.write(s)

with open('test.txt', 'r') as f:
#     #print(f.read())
#     while True:
#         chunk = 2
#         line = f.read(chunk)
#         print(line)
#         if not line:
#             break
      print(f.tell())#今いる場所は０のところですよ
      print(f.read(1))
      f.seek(5)
      print(f.read(1))
      f.seek(7)
      print(f.read(1))