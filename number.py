import random 
start = input('請使用者決定開始值')
end = input('請使用者決定結束值')
start = int(start)
end = int(end)
r = random.randint(start, end)
x = 0
while True:
	x += 1
	number = input('請輸入數字')
	number = int(number)
	if number == r:
		print('終於猜對了!')
		print('你已經猜第', x, '次了')
		break
	elif number > r:
		print('比答案大')
	elif number < r:
		print('比答案小')
	print('你已經猜第', x, '次了')
