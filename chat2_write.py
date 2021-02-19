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
    new = []
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
    allen_word = ('Allen said ' + str(allen_word_count) + ' words')
    viki_word = ('Viki said ' + str(viki_word_count) + ' words')
    allen_sticker = ('Allen sent ' + str(allen_sticker_count) + ' stickers')
    viki_sticker = ('Viki sent ' + str(viki_sticker_count) + ' stickers')
    allen_figure = ('Allen sent ' + str(allen_figure_count) + ' figures')
    viki_figure = ('Viki sent ' + str(viki_figure_count) + ' figures')

    new.append(allen_word)
    new.append(viki_word)
    new.append(allen_sticker)
    new.append(viki_sticker)
    new.append(allen_figure)
    new.append(viki_figure)
    print(new)
    return new
    

# 寫入檔案
def write_file(filename, new):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
            for line in new:
                f.write(line + '\n')


# 主要功能    
def main():
    lines = read_file('LINE-Viki.txt')
    new = convert(lines)
    write_file('LINEoutput.txt', new)


# 執行檔案
if __name__ == '__main__':
    main()