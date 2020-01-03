#找零钱
'''
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。

顾客排队购买你的产品，一次购买一杯。

每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。

'''


fivenumber=0    #拥有五元零钱的数目
tennumber=0     #拥有十元零钱的数目

while True:
    x=int(input('顾客付你的钱 5/10/20 :'))  #输入客户给的钱
    if x == 5 :                            #五元是不用找零 增加五元储备
        fivenumber+=1
    elif x == 10:                          #十元是找五元，增加十元储备
        if fivenumber:
            fivenumber-=1
            tennumber+=1
        else:                               #如果不够 返回错误
            print('error')
    elif x == 20:                           #二十元是找优先找10+5 其次找五元
        if tennumber and fivenumber:
            tennumber-=1
            fivenumber-=1
        elif fivenumber>2:
            fivenumber-=3
        else:
            print('error')                  #如果不够 返回错误
    else:
        print('输入有误 请重输')            #输入非5、10、20

