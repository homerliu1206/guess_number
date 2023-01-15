import random  

r = random.randint(1, 100)

while True:
	ans = input ('請猜出1~100中任意數字:')
	ans = int(ans)
	if ans == r:
		print ('答對了!')
		break
	elif ans > r:
		print ('小一點~')
	elif ans < r:
		print ('大一點~')