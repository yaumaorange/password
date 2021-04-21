password = '123456'
i = 3
print('總共六位數密碼,你有', i, '次機會')

while True:
	guesst = input('請輸入密碼:')
	if i > 1:
		if guesst == password:
			print('登入成功!')
			break
		i = i - 1
		print('密碼錯誤!還有', i, '次機會')
	else:
		if guesst == password:
			print('登入成功!')
		else:
			print('請999年後再重新登入')
		break
	