def create_card(start_number):

  list = []

  for i in start_number:
      list.append(i)

  # list.remove(list[4])
  del list[4]
  # list.remove(list[4])
  del list[4]
  temp = int(list[0])^int(list[1])^int(list[2])^int(list[3])^int(list[4])^int(list[5])^int(list[6])^int(list[7])\
         ^int(list[8])^int(list[9])^int(list[10])^int(list[11])^int(list[12])^int(list[13])

  aa = int('0xff', 16)
  #print aa
  result = str(temp%aa)
  if len(result) == 1:
      result = '0' + result

  return list[0]+list[1]+list[2]+list[3]+result+list[4]+list[5]+list[6]+list[7]+list[8]+list[9]+list[10]+list[11]+list[12]+list[13]

print   create_card('1106990000000550')





