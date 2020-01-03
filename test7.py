#二进制求和
#思路：字符串转化成整型再转化成二进制 相加后二进制输出

A='11'
B='1'

a=int(A,2)#二进制转化
b=int(B,2)#二进制转化
c=bin(a+b)#二进制相加减后二进制显示
print(a)#十进制显示
print(b)#十进制显示
print(c)#二进制显示


 



























 #   def addBinary(self, a: str, b: str) -> str:
 #       return bin(int(a, 2) + int(b, 2))[2:]
