import random 
r = random.randint(1, 100)
x = 0
while True:
	x = x + 1
	number = input('請輸入數字')
	number = int(number)
	if number == r:
		print('終於猜對了!')
		break
	elif number > r:
		print('比答案大')
	elif number < r:
		print('比答案小')
	print('你已經猜第', x, '次了')
