a = int(input('Введите время в секундах: '))
hh = a // 3600
mm = (a - hh * 3600) // 60
ss = a % 60
print('%d:%d:%d' % (hh,mm,ss))