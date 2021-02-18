# 學習變數取代的感覺

# 讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: # 若編碼出現\ufeff 在 utf-8 後面加上 -sig
		for line in f:
			lines.append(line.strip())
	return lines

# 轉換格式
def convert(lines):
	new = []
	person = None # 預設值設定成'無'
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue # 跳到下一個迴圈
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: # 如果 person 有值
			new.append(person + '：' + line)
	return new

# 寫入檔案
def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')

# 主要功能    
def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output1.txt', lines)

# 執行檔案
if __name__ == '__main__':
	main()