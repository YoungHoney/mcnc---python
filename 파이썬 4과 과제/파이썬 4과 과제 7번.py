f1=open("Q7.txt",'r')

check=f1.read()

f1.close()

check=check.replace('java','python')

f2=open('Q7.txt','w')
f2.write(check)
f2.close()
