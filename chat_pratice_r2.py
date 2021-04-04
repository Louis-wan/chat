def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f :
			lines.append(line.strip())
	return lines  

def convert(lines):
	person = None
	allen_word_count = 0
	viki_word_count = 0 
	allen_stiker_count = 0
	viki_stiker_count = 0
	AIC = 0 
	VIC = 0
	for line in lines: 
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] =='貼圖' :
				allen_stiker_count += 1
			elif s[2] == '圖片' :
				AIC += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			for m in s[2:]:
				if s[2] == '貼圖':
					viki_stiker_count += 1
				elif s[2] == '圖片':
					VIC += 1
				else:
					for m in s[2:]:
						viki_word_count += len(m)
		#print(s)
	print('allen say', allen_word_count, '個字')
	print('傳了貼圖' , allen_stiker_count, '個貼圖')
	print('傳了貼圖' , AIC, '圖片')
	print('viki say', viki_word_count, '個字')
	print('傳了貼圖' , allen_stiker_count, '個貼圖')
	print('傳了貼圖' , VIC, '圖片')


def write_file(filename, lines ):
	with open(filename, 'w', encoding='utf-8-sig') as f :
		for line in lines:
			f.write(line + '\n')
def main():	
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)

main()

