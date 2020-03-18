#readlines02.py

fname = input("파일명을 입력하세요 : ")
f = open(fname, 'r')

lines = f.readlines()
for line in lines:
     print(line)

f.close()
