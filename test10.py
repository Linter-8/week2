'''
给定一个整数数组 A，只有我们可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。

形式上，如果我们可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。

'''

inputanswer=1 #确认是否输入完毕的标志位
list1=[]        #写入数据的列表

sum1=0          #分别记录均分成三部分的数据和
sum2=0
sum3=0



while inputanswer:                                  #输入数据，直至确认输入完毕
    x=int(input('输入数字，需要是整数：'))            #输入
    list1.append(x)                                 #把数据添加到列表
    inputanswer=bool(int(input('您输入完毕了吗？完毕输入 0 继续按1：')))    #确认是否输入完毕

print(len(list1))
listlen=len(list1)                  #确认列表长度

if listlen % 3 == 0:                #判断是否能被3整除
    zz=int(listlen/3)               #确认均分长度
    for i in range(zz):             #算三部分的和
        sum1=sum1+list1[i]
        sum2=sum2+list1[i+zz]
        sum3=sum3+list1[i+(zz*2)]
    if (sum1==sum2)and(sum2==sum3) :    #如果均等，打印和
        print('符合')
        print(sum1)
    else:
        print('不符合条件2')            #不符合条件2

else:
    print('不符合条件1')                #不符合条件1


