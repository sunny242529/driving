country = input('請問你的國籍:')
age = input('請問你的年齡:')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你不可以考駕照')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你不可以考駕照')
else:
	print('國籍請輸入 台灣/美國')
