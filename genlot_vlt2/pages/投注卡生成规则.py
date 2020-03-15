
str1 = '1106060000000550'

list = []

for i in str1:
    list.append(i)

list.remove(list[4])
list.remove(list[4])
temp = int(list[0])^int(list[1])^int(list[2])^int(list[3])^int(list[4])^int(list[5])^int(list[6])^int(list[7])\
       ^int(list[8])^int(list[9])^int(list[10])^int(list[11])^int(list[12])^int(list[13])

aa = int('0xff', 16)
#print aa
print temp%aa
