# 學習創作變數暫時儲存需要用的東西

# 讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: # 若編碼出現\ufeff 在 utf-8 後面加上 -sig
		for line in f:
			lines.append(line.strip())
	return lines


# 轉換格式
def convert(lines):
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	allen_figure_count = 0
	viki_sticker_count = 0
	viki_figure_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_figure_count += 1
			else:
				for text in s[2:]:
					allen_word_count += len(text)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_figure_count += 1
			else:
				for text in s[2:]:
					viki_word_count += len(text)
	print('Allen said', allen_word_count, 'words')
	print('Viki said', viki_word_count, 'words')
	print('Allen sent', allen_sticker_count, 'stickers')
	print('Viki sent', viki_sticker_count, 'stickers')
	print('Allen sent', allen_figure_count, 'figures')
	print('Viki sent', viki_figure_count, 'figures')


# 寫入檔案
def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')


# 主要功能    
def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	# write_file('LINEoutput.txt', lines)


# 執行檔案
if __name__ == '__main__':
	main()