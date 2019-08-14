f1=open("test1.txt",'a')

insert=input("내용을 입력하세요")

f1.write(insert)

f1.close()

f2=open("test1.txt",'r')

check=f2.read()

print(check)
f2.close()
