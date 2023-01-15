import random  

r = random.randint(1, 100)
count = 0  #計數用

while True:
	count += 1  # count  = count + 1
	ans = input ('請猜出1~100中任意數字:')
	ans = int(ans)
	if ans == r:
		print ('答對了!')
		print ('這是您猜的第', count, '次')
		break
	elif ans > r:
		print ('小一點~')
	elif ans < r:
		print ('大一點~')
	print ('這是您猜的第', count, '次')