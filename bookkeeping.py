import os # operating system (作業系統)
# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f: # 讀取檔案
		for line in f:
			if '商品,價格' in line:
				continue
			name,price = line.strip().split(',')
			products.append([name, price])
	return products
# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		price = int(price)
		products.append([name, price])
	print(products)
	return products
# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])
# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f: # encoing (編碼)
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')
# 收納所有function
def main():
	file = 'products.csv'
	if os.path.isfile(file): # 檢查檔案在不在
		print('讀取舊檔')	
		products = read_file(file)
	else:
		print('創建新檔')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)
# 執行
main()