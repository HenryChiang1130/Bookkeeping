import os # operating system (作業系統)

products = []
# 檢查檔案在不在
if os.path.isfile('products.csv'):
	print('讀取舊檔')
	with open('products.csv', 'r', encoding='utf-8') as f: # 讀取檔案
		for line in f:
			if '商品,價格' in line:
				continue
			name,price = line.strip().split(',')
			products.append([name, price])
else:
	print('創建新檔')

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price])
print(products)

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: # encoing (編碼)
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')